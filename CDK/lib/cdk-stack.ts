import * as cdk from '@aws-cdk/core';
import * as lambda from '@aws-cdk/aws-lambda';
import * as s3 from '@aws-cdk/aws-s3';
import * as dynamodb from '@aws-cdk/aws-dynamodb';
import * as iam from '@aws-cdk/aws-iam';
import * as kms from '@aws-cdk/aws-kms';
import { S3EventSource } from '@aws-cdk/aws-lambda-event-sources';
import { RetentionDays } from '@aws-cdk/aws-logs';

export class CdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // ----- S3 bucket ----- 
    const appointment_concierge_bucket = new s3.Bucket(this, 'appointment-concierge', {
      bucketName: 'cdk-appointmentconcierge035121dc-1jhcoc97i63qb',
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });
    cdk.Tag.add(appointment_concierge_bucket, 'Name', 'appointment-concierge')
    cdk.Tag.add(appointment_concierge_bucket, 'application', 'Appointment Concierge')

    // ----- DynamoDB table to store extracted data ----- 
    // const table = new dynamodb.Table(this, 'Appointment Concierge', {
    //   partitionKey: { name: 'messageTime', type: dynamodb.AttributeType.STRING },
    //   removalPolicy: cdk.RemovalPolicy.DESTROY,
    // })
    // cdk.Tag.add(table, 'Name', 'appointment-concierge')
    // cdk.Tag.add(table, 'application', 'Appointment Concierge')

    // ----- lambda function to convert audio to text ----- 
    const audio_to_text_handler = new lambda.Function(this, 'audio-to-text', {
      runtime: lambda.Runtime.PYTHON_3_8,
      code: lambda.Code.fromAsset('../AppointmentConcierge/AudioToText'),
      handler: 'audio_to_text.lambda_handler',
      timeout: cdk.Duration.seconds(10),
      logRetention: RetentionDays.THREE_MONTHS,
      environment: {
        OUTPUT_BUCKET: appointment_concierge_bucket.bucketName,
      },
    });
    cdk.Tag.add(audio_to_text_handler, 'Name', 'audio-to-text')
    cdk.Tag.add(audio_to_text_handler, 'application', 'Appointment Concierge')
    
    // ----- lambda function to extract the medical entities ----- 
    const extract_entities_handler = new lambda.Function(this, 'extract-medical-entities', {
      runtime: lambda.Runtime.PYTHON_3_8,
      code: lambda.Code.fromAsset('../AppointmentConcierge/ExtractMedicalEntities'),
      handler: 'extract_medical_entities.lambda_handler',
      timeout: cdk.Duration.seconds(10),
      logRetention: RetentionDays.THREE_MONTHS,
      environment: {
        // DB_TABLE_NAME: table.tableName,
        MSG_DOC_S3_BUCKET: appointment_concierge_bucket.bucketName,
        MSG_DOC_S3_PREFIX: 'message-docs/',
        COMPREHEND_RESULTS_S3_PREFIX: 'comprehend-results/'
      },
    });
    cdk.Tag.add(extract_entities_handler, 'Name', 'extract-medical-entities')
    cdk.Tag.add(extract_entities_handler, 'application', 'Appointment Concierge')

    // ----- lambda function to send email with transcribed message  -----
    const send_email_handler = new lambda.Function(this, 'send-email', {
      runtime: lambda.Runtime.PYTHON_3_8,
      code: lambda.Code.fromAsset('../AppointmentConcierge/SendEmail'),
      handler: 'send_email.lambda_handler',
      timeout: cdk.Duration.seconds(10),
      logRetention: RetentionDays.THREE_MONTHS,
      environment: {
        SSM_PS_APPCONFIG_PATH: '/AppointmentConcierge',
        RECEIVER_EMAIL_ADDRESS: 'steditt@amazon.com',
      },
    });
    cdk.Tag.add(send_email_handler, 'Name', 'send-email')
    cdk.Tag.add(send_email_handler, 'application', 'Appointment Concierge')

    // ----- lambda function to load test data ----- 
    const load_test_data_handler = new lambda.Function(this, 'load-test-data', {
      runtime: lambda.Runtime.PYTHON_3_8,
      code: lambda.Code.fromAsset('../AppointmentConcierge/LoadTestData'),
      handler: 'load_test_data.lambda_handler',
      memorySize: 512,
      timeout: cdk.Duration.seconds(900),
      logRetention: RetentionDays.THREE_MONTHS,
      environment: {
        START_DATE: '2020-03-01',
        END_DATE: '2020-09-03',
        NUM_MESSAGES: '1000',
        TEST_DATA_TARGET_S3_BUCKET: appointment_concierge_bucket.bucketName,
        TEST_DATA_TARGET_S3_PREFIX: 'comprehend-results/',
      },
    });
    cdk.Tag.add(load_test_data_handler, 'Name', 'load-test-data')
    cdk.Tag.add(load_test_data_handler, 'application', 'Appointment Concierge')

    // ----- trigger for lambda functions -----
    audio_to_text_handler.addEventSource(new S3EventSource(appointment_concierge_bucket, {
      events: [ s3.EventType.OBJECT_CREATED_POST, s3.EventType.OBJECT_CREATED_PUT ],
      filters: [ { 
        prefix: 'incoming-audio/' } ],
    }));

    extract_entities_handler.addEventSource(new S3EventSource(appointment_concierge_bucket, {
      events: [ s3.EventType.OBJECT_CREATED_POST, s3.EventType.OBJECT_CREATED_PUT ],
      filters: [ { 
        prefix: 'medical/',
        suffix: '.json' } ],
    }));

    send_email_handler.addEventSource(new S3EventSource(appointment_concierge_bucket, {
      events: [ s3.EventType.OBJECT_CREATED_POST, s3.EventType.OBJECT_CREATED_PUT ],
      filters: [ { 
        prefix: 'message-docs/',
        suffix: '.html' } ],
    }));

    // ----- set permissions -----
    audio_to_text_handler.role?.addManagedPolicy(
      iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonTranscribeFullAccess'));

    extract_entities_handler.role?.addManagedPolicy(
      iam.ManagedPolicy.fromAwsManagedPolicyName('ComprehendMedicalFullAccess'));
    extract_entities_handler.role?.addManagedPolicy(
      iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonDynamoDBFullAccess'));
      
    send_email_handler.addToRolePolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      resources: ['arn:aws:ssm:eu-west-1:060337561279:parameter/AppointmentConcierge'],
      actions: ['ssm:GetParametersByPath'],
    }))
    
    appointment_concierge_bucket.grantReadWrite(audio_to_text_handler);
    appointment_concierge_bucket.grantReadWrite(extract_entities_handler);
    appointment_concierge_bucket.grantReadWrite(send_email_handler);
    appointment_concierge_bucket.grantReadWrite(load_test_data_handler);
    
    const policy_statement = new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      resources: [appointment_concierge_bucket.bucketArn + '/incoming-audio/*'],
      actions: ['s3:PutObject'],
    })

    const policy = new iam.ManagedPolicy(this, 'pythonista_s3_access_policy', {
      managedPolicyName: 'AppointmentConciergeS3ReadWrite',
      description: 'Grants write access to Appointment Concierge S3 bucket.',
      statements: [policy_statement],
      users: [iam.User.fromUserName(this, 'pythonista_user', 'Pythonista_Appointment_Concierge')]
    })

    const key = kms.Key.fromKeyArn(
      this,
      'SendEmailParameterStoreKey',
      'arn:aws:kms:me-south-1:060337561279:key/6116ebe4-074a-4a2b-b042-48dc31a18ccb');
    key.grantEncryptDecrypt(send_email_handler);

  }
}
