# Appointment Concierge

Appointment Concierge is a demo application that allows a patient to record and
send a voice message to his healthcare provider and request an appointment. The 
application uses [Amazon Transcribe Medical](https://aws.amazon.com/transcribe/medical/) 
to transform the voice message into text and 
[Amazon Comprehend Medical](https://aws.amazon.com/comprehend/medical/) to derive
meaningful information. The information extracted from the message is used to 
generate an email for an appointment coordinator. Furthermore, message data is 
analyzed and presented in a dashboard using the 
[Amazon QuickSight](https://aws.amazon.com/quicksight/) service.

![architecture](img/architecture.png)

The application is built following an event driven architecture. (1) a patient uses a mobile 
application to record a voice message. The message is then uploaded to an S3 bucket with a prefix
to identify new audio files. (2) any new file triggers a Lambda function. (3) the Lambda
function   
     



