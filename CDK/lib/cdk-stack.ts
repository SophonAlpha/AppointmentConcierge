import * as cdk from '@aws-cdk/core';
import * as lambda from '@aws-cdk/aws-lambda';
import * as s3 from '@aws-cdk/aws-s3';
import * as dynamodb from '@aws-cdk/aws-dynamodb';
import { S3EventSource } from '@aws-cdk/aws-lambda-event-sources';
import { RetentionDays } from '@aws-cdk/aws-logs';

export class CdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // S3 bucket for incoming voice messages
    const appointment_concierge_bucket = new s3.Bucket(this, 'appointment-concierge', {
      bucketName: 'cdkstack-appointmentconcierge-uak8x5wugi8v',
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });
    cdk.Tag.add(appointment_concierge_bucket, 'Name', 'appointment-concierge')

    // S3 bucket for transacription results
    const voice_audio_transcripts_bucket = new s3.Bucket(this, 'voice-audio-transcripts', {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });
    cdk.Tag.add(voice_audio_transcripts_bucket, 'Name', 'voice-audio-transcripts')

    // lambda function to convert audio to text
    const audio_to_text_handler = new lambda.Function(this, 'audio-to-text', {
      runtime: lambda.Runtime.PYTHON_3_8,
      code: lambda.Code.fromAsset('../AppointmentConcierge/AudioToText'),
      handler: 'audio_to_text.lambda_handler',
      logRetention: RetentionDays.THREE_MONTHS,
      environment: {
        OUTPUT_BUCKET: voice_audio_transcripts_bucket.bucketName,
      },
    });
    cdk.Tag.add(audio_to_text_handler, 'Name', 'audio-to-text')
    
    appointment_concierge_bucket.grantRead(audio_to_text_handler);
    
    audio_to_text_handler.addEventSource(new S3EventSource(appointment_concierge_bucket, {
      events: [ s3.EventType.OBJECT_CREATED_POST, s3.EventType.OBJECT_CREATED_PUT ],
      filters: [ { prefix: 'incoming_audio/' } ],
    }));

    // lambda function to extract the medical entities
    const extract_entities_handler = new lambda.Function(this, 'extract_medical_entities', {
      runtime: lambda.Runtime.PYTHON_3_8,
      code: lambda.Code.fromAsset('../AppointmentConcierge/ExtractMedicalEntities'),
      handler: 'extract_medical_entities.lambda_handler',
      logRetention: RetentionDays.THREE_MONTHS,
    });
    cdk.Tag.add(extract_entities_handler, 'Name', 'extract_medical_entities')
    
    voice_audio_transcripts_bucket.grantRead(extract_entities_handler);
    appointment_concierge_bucket.grantReadWrite(extract_entities_handler)
    
    extract_entities_handler.addEventSource(new S3EventSource(voice_audio_transcripts_bucket, {
      events: [ s3.EventType.OBJECT_CREATED_POST, s3.EventType.OBJECT_CREATED_PUT ],
    }));
    
    // DynamoDB table to store extracted data
    const table = new dynamodb.Table(this, 'Appointment Concierge', {
      tableName: 'appointment-concierge',
      partitionKey: { name: 'time', type: dynamodb.AttributeType.NUMBER },
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    })
    cdk.Tag.add(table, 'Name', 'appointment-concierge')
  }
}
