{"changed":true,"filter":false,"title":"cdk-stack.ts","tooltip":"/CDK/lib/cdk-stack.ts","value":"import * as cdk from '@aws-cdk/core';\nimport * as lambda from '@aws-cdk/aws-lambda';\nimport * as s3 from '@aws-cdk/aws-s3';\nimport * as dynamodb from '@aws-cdk/aws-dynamodb';\nimport * as iam from '@aws-cdk/aws-iam';\nimport * as kms from '@aws-cdk/aws-kms';\nimport { S3EventSource } from '@aws-cdk/aws-lambda-event-sources';\nimport { RetentionDays } from '@aws-cdk/aws-logs';\n\nexport class CdkStack extends cdk.Stack {\n  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {\n    super(scope, id, props);\n\n    // ----- S3 bucket ----- \n    const appointment_concierge_bucket = new s3.Bucket(this, 'appointment-concierge', {\n      bucketName: 'cdk-appointmentconcierge035121dc-1mmu9cw6xkv85',\n      \n      removalPolicy: cdk.RemovalPolicy.DESTROY,\n    });\n    cdk.Tag.add(appointment_concierge_bucket, 'Name', 'appointment-concierge')\n    cdk.Tag.add(appointment_concierge_bucket, 'application', 'Appointment Concierge')\n\n    // ----- DynamoDB table to store extracted data ----- \n    // const table = new dynamodb.Table(this, 'Appointment Concierge', {\n    //   partitionKey: { name: 'messageTime', type: dynamodb.AttributeType.STRING },\n    //   removalPolicy: cdk.RemovalPolicy.DESTROY,\n    // })\n    // cdk.Tag.add(table, 'Name', 'appointment-concierge')\n    // cdk.Tag.add(table, 'application', 'Appointment Concierge')\n\n    // ----- lambda function to convert audio to text ----- \n    const audio_to_text_handler = new lambda.Function(this, 'audio-to-text', {\n      runtime: lambda.Runtime.PYTHON_3_8,\n      code: lambda.Code.fromAsset('../AppointmentConcierge/AudioToText'),\n      handler: 'audio_to_text.lambda_handler',\n      timeout: cdk.Duration.seconds(10),\n      logRetention: RetentionDays.THREE_MONTHS,\n      environment: {\n        OUTPUT_BUCKET: appointment_concierge_bucket.bucketName,\n      },\n    });\n    cdk.Tag.add(audio_to_text_handler, 'Name', 'audio-to-text')\n    cdk.Tag.add(audio_to_text_handler, 'application', 'Appointment Concierge')\n    \n    // ----- lambda function to extract the medical entities ----- \n    const extract_entities_handler = new lambda.Function(this, 'extract-medical-entities', {\n      runtime: lambda.Runtime.PYTHON_3_8,\n      code: lambda.Code.fromAsset('../AppointmentConcierge/ExtractMedicalEntities'),\n      handler: 'extract_medical_entities.lambda_handler',\n      timeout: cdk.Duration.seconds(10),\n      logRetention: RetentionDays.THREE_MONTHS,\n      environment: {\n        // DB_TABLE_NAME: table.tableName,\n        MSG_DOC_S3_BUCKET: appointment_concierge_bucket.bucketName,\n        MSG_DOC_S3_PREFIX: 'message-docs/',\n        COMPREHEND_RESULTS_S3_PREFIX: 'comprehend-results/'\n      },\n    });\n    cdk.Tag.add(extract_entities_handler, 'Name', 'extract-medical-entities')\n    cdk.Tag.add(extract_entities_handler, 'application', 'Appointment Concierge')\n\n    // ----- lambda function to send email with transcribed message  -----\n    const send_email_handler = new lambda.Function(this, 'send-email', {\n      runtime: lambda.Runtime.PYTHON_3_8,\n      code: lambda.Code.fromAsset('../AppointmentConcierge/SendEmail'),\n      handler: 'send_email.lambda_handler',\n      timeout: cdk.Duration.seconds(10),\n      logRetention: RetentionDays.THREE_MONTHS,\n      environment: {\n        SSM_PS_APPCONFIG_PATH: '/AppointmentConcierge',\n        RECEIVER_EMAIL_ADDRESS: 'steditt@amazon.com',\n      },\n    });\n    cdk.Tag.add(send_email_handler, 'Name', 'send-email')\n    cdk.Tag.add(send_email_handler, 'application', 'Appointment Concierge')\n\n    // ----- lambda function to load test data ----- \n    const load_test_data_handler = new lambda.Function(this, 'load-test-data', {\n      runtime: lambda.Runtime.PYTHON_3_8,\n      code: lambda.Code.fromAsset('../AppointmentConcierge/LoadTestData'),\n      handler: 'load_test_data.lambda_handler',\n      memorySize: 512,\n      timeout: cdk.Duration.seconds(900),\n      logRetention: RetentionDays.THREE_MONTHS,\n      environment: {\n        START_DATE: '2020-03-01',\n        END_DATE: '2020-09-03',\n        NUM_MESSAGES: '1000',\n        TEST_DATA_TARGET_S3_BUCKET: appointment_concierge_bucket.bucketName,\n        TEST_DATA_TARGET_S3_PREFIX: 'comprehend-results/',\n      },\n    });\n    cdk.Tag.add(load_test_data_handler, 'Name', 'load-test-data')\n    cdk.Tag.add(load_test_data_handler, 'application', 'Appointment Concierge')\n\n    // ----- trigger for lambda functions -----\n    audio_to_text_handler.addEventSource(new S3EventSource(appointment_concierge_bucket, {\n      events: [ s3.EventType.OBJECT_CREATED_POST, s3.EventType.OBJECT_CREATED_PUT ],\n      filters: [ { \n        prefix: 'incoming-audio/' } ],\n    }));\n\n    extract_entities_handler.addEventSource(new S3EventSource(appointment_concierge_bucket, {\n      events: [ s3.EventType.OBJECT_CREATED_POST, s3.EventType.OBJECT_CREATED_PUT ],\n      filters: [ { \n        prefix: 'medical/',\n        suffix: '.json' } ],\n    }));\n\n    send_email_handler.addEventSource(new S3EventSource(appointment_concierge_bucket, {\n      events: [ s3.EventType.OBJECT_CREATED_POST, s3.EventType.OBJECT_CREATED_PUT ],\n      filters: [ { \n        prefix: 'message-docs/',\n        suffix: '.html' } ],\n    }));\n\n    // ----- set permissions -----\n    audio_to_text_handler.role?.addManagedPolicy(\n      iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonTranscribeFullAccess'));\n\n    extract_entities_handler.role?.addManagedPolicy(\n      iam.ManagedPolicy.fromAwsManagedPolicyName('ComprehendMedicalFullAccess'));\n    extract_entities_handler.role?.addManagedPolicy(\n      iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonDynamoDBFullAccess'));\n      \n    send_email_handler.addToRolePolicy(new iam.PolicyStatement({\n      effect: iam.Effect.ALLOW,\n      resources: ['arn:aws:ssm:eu-west-1:060337561279:parameter/AppointmentConcierge'],\n      actions: ['ssm:GetParametersByPath'],\n    }))\n    \n    appointment_concierge_bucket.grantReadWrite(audio_to_text_handler);\n    appointment_concierge_bucket.grantReadWrite(extract_entities_handler);\n    appointment_concierge_bucket.grantReadWrite(send_email_handler);\n    appointment_concierge_bucket.grantReadWrite(load_test_data_handler);\n    \n    const policy_statement = new iam.PolicyStatement({\n      effect: iam.Effect.ALLOW,\n      resources: [appointment_concierge_bucket.bucketArn + '/incoming-audio/*'],\n      actions: ['s3:PutObject'],\n    })\n\n    const policy = new iam.ManagedPolicy(this, 'pythonista_s3_access_policy', {\n      managedPolicyName: 'AppointmentConciergeS3ReadWrite',\n      description: 'Grants write access to Appointment Concierge S3 bucket.',\n      statements: [policy_statement],\n      users: [iam.User.fromUserName(this, 'pythonista_user', 'Pythonista_Appointment_Concierge')]\n    })\n\n    const key = kms.Key.fromKeyArn(\n      this,\n      'SendEmailParameterStoreKey',\n      'arn:aws:kms:me-south-1:060337561279:key/6116ebe4-074a-4a2b-b042-48dc31a18ccb');\n    key.grantEncryptDecrypt(send_email_handler);\n\n  }\n}\n","undoManager":{"mark":67,"position":100,"stack":[[{"start":{"row":61,"column":14},"end":{"row":61,"column":15},"action":"insert","lines":[" "],"id":1325}],[{"start":{"row":61,"column":14},"end":{"row":61,"column":15},"action":"remove","lines":[" "],"id":1326}],[{"start":{"row":61,"column":14},"end":{"row":61,"column":15},"action":"insert","lines":["_"],"id":1327},{"start":{"row":61,"column":15},"end":{"row":61,"column":16},"action":"insert","lines":["t"]},{"start":{"row":61,"column":16},"end":{"row":61,"column":17},"action":"insert","lines":["e"]},{"start":{"row":61,"column":17},"end":{"row":61,"column":18},"action":"insert","lines":["s"]},{"start":{"row":61,"column":18},"end":{"row":61,"column":19},"action":"insert","lines":["t"]},{"start":{"row":61,"column":19},"end":{"row":61,"column":20},"action":"insert","lines":["_"]},{"start":{"row":61,"column":20},"end":{"row":61,"column":21},"action":"insert","lines":["d"]},{"start":{"row":61,"column":21},"end":{"row":61,"column":22},"action":"insert","lines":["f"]},{"start":{"row":61,"column":22},"end":{"row":61,"column":23},"action":"insert","lines":["a"]},{"start":{"row":61,"column":23},"end":{"row":61,"column":24},"action":"insert","lines":["t"]},{"start":{"row":61,"column":24},"end":{"row":61,"column":25},"action":"insert","lines":["a"]}],[{"start":{"row":61,"column":21},"end":{"row":61,"column":22},"action":"remove","lines":["f"],"id":1328}],[{"start":{"row":61,"column":62},"end":{"row":61,"column":86},"action":"remove","lines":["extract-medical-entities"],"id":1329},{"start":{"row":61,"column":62},"end":{"row":61,"column":76},"action":"insert","lines":["load_test_data"]}],[{"start":{"row":61,"column":66},"end":{"row":61,"column":67},"action":"remove","lines":["_"],"id":1330}],[{"start":{"row":61,"column":66},"end":{"row":61,"column":67},"action":"insert","lines":["-"],"id":1331}],[{"start":{"row":61,"column":71},"end":{"row":61,"column":72},"action":"remove","lines":["_"],"id":1332}],[{"start":{"row":61,"column":71},"end":{"row":61,"column":72},"action":"insert","lines":["-"],"id":1333}],[{"start":{"row":63,"column":59},"end":{"row":63,"column":81},"action":"remove","lines":["ExtractMedicalEntities"],"id":1334},{"start":{"row":63,"column":59},"end":{"row":63,"column":71},"action":"insert","lines":["LoadTestData"]}],[{"start":{"row":64,"column":16},"end":{"row":64,"column":40},"action":"remove","lines":["extract_medical_entities"],"id":1335},{"start":{"row":64,"column":16},"end":{"row":64,"column":30},"action":"insert","lines":["load_test_data"]}],[{"start":{"row":65,"column":36},"end":{"row":65,"column":38},"action":"remove","lines":["10"],"id":1336},{"start":{"row":65,"column":36},"end":{"row":65,"column":37},"action":"insert","lines":["6"]},{"start":{"row":65,"column":37},"end":{"row":65,"column":38},"action":"insert","lines":["0"]},{"start":{"row":65,"column":38},"end":{"row":65,"column":39},"action":"insert","lines":["0"]}],[{"start":{"row":68,"column":0},"end":{"row":69,"column":0},"action":"remove","lines":["        DB_TABLE_NAME: table.tableName,",""],"id":1337}],[{"start":{"row":68,"column":8},"end":{"row":68,"column":25},"action":"remove","lines":["MSG_DOC_S3_BUCKET"],"id":1338},{"start":{"row":68,"column":8},"end":{"row":68,"column":34},"action":"insert","lines":["TEST_DATA_TARGET_S3_BUCKET"]}],[{"start":{"row":69,"column":8},"end":{"row":69,"column":25},"action":"remove","lines":["MSG_DOC_S3_PREFIX"],"id":1339},{"start":{"row":69,"column":8},"end":{"row":69,"column":34},"action":"insert","lines":["TEST_DATA_TARGET_S3_PREFIX"]}],[{"start":{"row":69,"column":37},"end":{"row":69,"column":50},"action":"remove","lines":["message-docs/"],"id":1340},{"start":{"row":69,"column":37},"end":{"row":69,"column":56},"action":"insert","lines":["comprehend-results/"]}],[{"start":{"row":70,"column":0},"end":{"row":71,"column":0},"action":"remove","lines":["        COMPREHEND_RESULTS_S3_PREFIX: 'comprehend-results/'",""],"id":1341}],[{"start":{"row":72,"column":51},"end":{"row":72,"column":75},"action":"remove","lines":["extract-medical-entities"],"id":1342},{"start":{"row":72,"column":51},"end":{"row":72,"column":65},"action":"insert","lines":["load-test-data"]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":7},"action":"insert","lines":["// "],"id":1343},{"start":{"row":23,"column":4},"end":{"row":23,"column":7},"action":"insert","lines":["// "]},{"start":{"row":24,"column":4},"end":{"row":24,"column":7},"action":"insert","lines":["// "]},{"start":{"row":25,"column":4},"end":{"row":25,"column":7},"action":"insert","lines":["// "]},{"start":{"row":26,"column":4},"end":{"row":26,"column":7},"action":"insert","lines":["// "]},{"start":{"row":27,"column":4},"end":{"row":27,"column":7},"action":"insert","lines":["// "]}],[{"start":{"row":51,"column":8},"end":{"row":51,"column":11},"action":"insert","lines":["// "],"id":1344}],[{"start":{"row":128,"column":68},"end":{"row":129,"column":0},"action":"insert","lines":["",""],"id":1345},{"start":{"row":129,"column":0},"end":{"row":129,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":129,"column":4},"end":{"row":129,"column":68},"action":"insert","lines":["appointment_concierge_bucket.grantReadWrite(send_email_handler);"],"id":1346}],[{"start":{"row":129,"column":48},"end":{"row":129,"column":66},"action":"remove","lines":["send_email_handler"],"id":1347},{"start":{"row":129,"column":48},"end":{"row":129,"column":70},"action":"insert","lines":["load_test_data_handler"]}],[{"start":{"row":60,"column":0},"end":{"row":75,"column":0},"action":"remove","lines":["    // ----- lambda function to load test data ----- ","    const load_test_data_handler = new lambda.Function(this, 'load-test-data', {","      runtime: lambda.Runtime.PYTHON_3_8,","      code: lambda.Code.fromAsset('../AppointmentConcierge/LoadTestData'),","      handler: 'load_test_data.lambda_handler',","      timeout: cdk.Duration.seconds(600),","      logRetention: RetentionDays.THREE_MONTHS,","      environment: {","        TEST_DATA_TARGET_S3_BUCKET: appointment_concierge_bucket.bucketName,","        TEST_DATA_TARGET_S3_PREFIX: 'comprehend-results/',","      },","    });","    cdk.Tag.add(extract_entities_handler, 'Name', 'load-test-data')","    cdk.Tag.add(extract_entities_handler, 'application', 'Appointment Concierge')","",""],"id":1348}],[{"start":{"row":75,"column":0},"end":{"row":90,"column":0},"action":"insert","lines":["    // ----- lambda function to load test data ----- ","    const load_test_data_handler = new lambda.Function(this, 'load-test-data', {","      runtime: lambda.Runtime.PYTHON_3_8,","      code: lambda.Code.fromAsset('../AppointmentConcierge/LoadTestData'),","      handler: 'load_test_data.lambda_handler',","      timeout: cdk.Duration.seconds(600),","      logRetention: RetentionDays.THREE_MONTHS,","      environment: {","        TEST_DATA_TARGET_S3_BUCKET: appointment_concierge_bucket.bucketName,","        TEST_DATA_TARGET_S3_PREFIX: 'comprehend-results/',","      },","    });","    cdk.Tag.add(extract_entities_handler, 'Name', 'load-test-data')","    cdk.Tag.add(extract_entities_handler, 'application', 'Appointment Concierge')","",""],"id":1349}],[{"start":{"row":87,"column":16},"end":{"row":87,"column":40},"action":"remove","lines":["extract_entities_handler"],"id":1350},{"start":{"row":87,"column":16},"end":{"row":87,"column":38},"action":"insert","lines":["load_test_data_handler"]}],[{"start":{"row":88,"column":16},"end":{"row":88,"column":40},"action":"remove","lines":["extract_entities_handler"],"id":1351},{"start":{"row":88,"column":16},"end":{"row":88,"column":38},"action":"insert","lines":["load_test_data_handler"]}],[{"start":{"row":82,"column":20},"end":{"row":83,"column":0},"action":"insert","lines":["",""],"id":1352},{"start":{"row":83,"column":0},"end":{"row":83,"column":8},"action":"insert","lines":["        "]},{"start":{"row":83,"column":8},"end":{"row":83,"column":9},"action":"insert","lines":["S"]},{"start":{"row":83,"column":9},"end":{"row":83,"column":10},"action":"insert","lines":["T"]},{"start":{"row":83,"column":10},"end":{"row":83,"column":11},"action":"insert","lines":["A"]},{"start":{"row":83,"column":11},"end":{"row":83,"column":12},"action":"insert","lines":["R"]},{"start":{"row":83,"column":12},"end":{"row":83,"column":13},"action":"insert","lines":["T"]}],[{"start":{"row":83,"column":13},"end":{"row":83,"column":14},"action":"insert","lines":["_"],"id":1353},{"start":{"row":83,"column":14},"end":{"row":83,"column":15},"action":"insert","lines":["D"]},{"start":{"row":83,"column":15},"end":{"row":83,"column":16},"action":"insert","lines":["A"]},{"start":{"row":83,"column":16},"end":{"row":83,"column":17},"action":"insert","lines":["T"]},{"start":{"row":83,"column":17},"end":{"row":83,"column":18},"action":"insert","lines":["E"]}],[{"start":{"row":83,"column":18},"end":{"row":83,"column":19},"action":"insert","lines":[":"],"id":1354}],[{"start":{"row":83,"column":19},"end":{"row":83,"column":20},"action":"insert","lines":[" "],"id":1355}],[{"start":{"row":83,"column":20},"end":{"row":83,"column":22},"action":"insert","lines":["''"],"id":1356}],[{"start":{"row":83,"column":21},"end":{"row":83,"column":31},"action":"insert","lines":["2020-03-01"],"id":1357}],[{"start":{"row":83,"column":32},"end":{"row":83,"column":33},"action":"insert","lines":[","],"id":1358}],[{"start":{"row":83,"column":33},"end":{"row":84,"column":0},"action":"insert","lines":["",""],"id":1359},{"start":{"row":84,"column":0},"end":{"row":84,"column":8},"action":"insert","lines":["        "]},{"start":{"row":84,"column":8},"end":{"row":84,"column":9},"action":"insert","lines":["E"]},{"start":{"row":84,"column":9},"end":{"row":84,"column":10},"action":"insert","lines":["N"]}],[{"start":{"row":84,"column":10},"end":{"row":84,"column":11},"action":"insert","lines":["D"],"id":1360},{"start":{"row":84,"column":11},"end":{"row":84,"column":12},"action":"insert","lines":["_"]},{"start":{"row":84,"column":12},"end":{"row":84,"column":13},"action":"insert","lines":["D"]},{"start":{"row":84,"column":13},"end":{"row":84,"column":14},"action":"insert","lines":["A"]},{"start":{"row":84,"column":14},"end":{"row":84,"column":15},"action":"insert","lines":["T"]},{"start":{"row":84,"column":15},"end":{"row":84,"column":16},"action":"insert","lines":["E"]}],[{"start":{"row":84,"column":16},"end":{"row":84,"column":17},"action":"insert","lines":[":"],"id":1361}],[{"start":{"row":84,"column":17},"end":{"row":84,"column":18},"action":"insert","lines":[" "],"id":1362}],[{"start":{"row":84,"column":17},"end":{"row":84,"column":18},"action":"remove","lines":[" "],"id":1363},{"start":{"row":84,"column":17},"end":{"row":84,"column":31},"action":"insert","lines":[" '2020-03-01',"]}],[{"start":{"row":84,"column":25},"end":{"row":84,"column":26},"action":"remove","lines":["3"],"id":1364},{"start":{"row":84,"column":25},"end":{"row":84,"column":26},"action":"insert","lines":["9"]}],[{"start":{"row":84,"column":28},"end":{"row":84,"column":29},"action":"remove","lines":["1"],"id":1365},{"start":{"row":84,"column":28},"end":{"row":84,"column":29},"action":"insert","lines":["3"]}],[{"start":{"row":84,"column":31},"end":{"row":85,"column":0},"action":"insert","lines":["",""],"id":1366},{"start":{"row":85,"column":0},"end":{"row":85,"column":8},"action":"insert","lines":["        "]},{"start":{"row":85,"column":8},"end":{"row":85,"column":9},"action":"insert","lines":["N"]},{"start":{"row":85,"column":9},"end":{"row":85,"column":10},"action":"insert","lines":["U"]}],[{"start":{"row":85,"column":10},"end":{"row":85,"column":11},"action":"insert","lines":["M"],"id":1367},{"start":{"row":85,"column":11},"end":{"row":85,"column":12},"action":"insert","lines":["_"]},{"start":{"row":85,"column":12},"end":{"row":85,"column":13},"action":"insert","lines":["M"]},{"start":{"row":85,"column":13},"end":{"row":85,"column":14},"action":"insert","lines":["E"]}],[{"start":{"row":85,"column":14},"end":{"row":85,"column":15},"action":"insert","lines":["S"],"id":1368},{"start":{"row":85,"column":15},"end":{"row":85,"column":16},"action":"insert","lines":["S"]},{"start":{"row":85,"column":16},"end":{"row":85,"column":17},"action":"insert","lines":["A"]},{"start":{"row":85,"column":17},"end":{"row":85,"column":18},"action":"insert","lines":["G"]},{"start":{"row":85,"column":18},"end":{"row":85,"column":19},"action":"insert","lines":["E"]},{"start":{"row":85,"column":19},"end":{"row":85,"column":20},"action":"insert","lines":["S"]},{"start":{"row":85,"column":20},"end":{"row":85,"column":21},"action":"insert","lines":[":"]}],[{"start":{"row":85,"column":21},"end":{"row":85,"column":22},"action":"insert","lines":[" "],"id":1369}],[{"start":{"row":85,"column":22},"end":{"row":85,"column":23},"action":"insert","lines":["1"],"id":1370},{"start":{"row":85,"column":23},"end":{"row":85,"column":24},"action":"insert","lines":["0"]},{"start":{"row":85,"column":24},"end":{"row":85,"column":25},"action":"insert","lines":["0"]},{"start":{"row":85,"column":25},"end":{"row":85,"column":26},"action":"insert","lines":[","]}],[{"start":{"row":87,"column":57},"end":{"row":87,"column":58},"action":"remove","lines":[","],"id":1371}],[{"start":{"row":85,"column":22},"end":{"row":85,"column":25},"action":"remove","lines":["100"],"id":1372},{"start":{"row":85,"column":22},"end":{"row":85,"column":23},"action":"insert","lines":["'"]},{"start":{"row":85,"column":23},"end":{"row":85,"column":24},"action":"insert","lines":["1"]},{"start":{"row":85,"column":24},"end":{"row":85,"column":25},"action":"insert","lines":["0"]},{"start":{"row":85,"column":25},"end":{"row":85,"column":26},"action":"insert","lines":["0"]}],[{"start":{"row":85,"column":26},"end":{"row":85,"column":27},"action":"insert","lines":["'"],"id":1373}],[{"start":{"row":87,"column":57},"end":{"row":87,"column":58},"action":"insert","lines":[","],"id":1374}],[{"start":{"row":79,"column":47},"end":{"row":80,"column":0},"action":"insert","lines":["",""],"id":1375},{"start":{"row":80,"column":0},"end":{"row":80,"column":6},"action":"insert","lines":["      "]}],[{"start":{"row":80,"column":6},"end":{"row":80,"column":7},"action":"insert","lines":["m"],"id":1376},{"start":{"row":80,"column":7},"end":{"row":80,"column":8},"action":"insert","lines":["e"]},{"start":{"row":80,"column":8},"end":{"row":80,"column":9},"action":"insert","lines":["m"]},{"start":{"row":80,"column":9},"end":{"row":80,"column":10},"action":"insert","lines":["o"]},{"start":{"row":80,"column":10},"end":{"row":80,"column":11},"action":"insert","lines":["r"]},{"start":{"row":80,"column":11},"end":{"row":80,"column":12},"action":"insert","lines":["y"]},{"start":{"row":80,"column":12},"end":{"row":80,"column":13},"action":"insert","lines":["S"]}],[{"start":{"row":80,"column":13},"end":{"row":80,"column":14},"action":"insert","lines":["i"],"id":1377},{"start":{"row":80,"column":14},"end":{"row":80,"column":15},"action":"insert","lines":["z"]},{"start":{"row":80,"column":15},"end":{"row":80,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":80,"column":16},"end":{"row":80,"column":17},"action":"insert","lines":[":"],"id":1378}],[{"start":{"row":80,"column":17},"end":{"row":80,"column":18},"action":"insert","lines":[" "],"id":1379}],[{"start":{"row":80,"column":18},"end":{"row":80,"column":19},"action":"insert","lines":["5"],"id":1380},{"start":{"row":80,"column":19},"end":{"row":80,"column":20},"action":"insert","lines":["1"]},{"start":{"row":80,"column":20},"end":{"row":80,"column":21},"action":"insert","lines":["2"]}],[{"start":{"row":80,"column":21},"end":{"row":80,"column":22},"action":"insert","lines":[","],"id":1381}],[{"start":{"row":81,"column":36},"end":{"row":81,"column":37},"action":"remove","lines":["6"],"id":1382}],[{"start":{"row":81,"column":36},"end":{"row":81,"column":37},"action":"insert","lines":["1"],"id":1383},{"start":{"row":81,"column":37},"end":{"row":81,"column":38},"action":"insert","lines":["2"]}],[{"start":{"row":81,"column":37},"end":{"row":81,"column":38},"action":"remove","lines":["2"],"id":1384},{"start":{"row":81,"column":36},"end":{"row":81,"column":37},"action":"remove","lines":["1"]}],[{"start":{"row":81,"column":36},"end":{"row":81,"column":37},"action":"insert","lines":["9"],"id":1385}],[{"start":{"row":86,"column":25},"end":{"row":86,"column":26},"action":"insert","lines":["0"],"id":1386}],[{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["/"],"id":1387},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":["/"]}],[{"start":{"row":15,"column":6},"end":{"row":15,"column":8},"action":"remove","lines":["//"],"id":1388}],[{"start":{"row":15,"column":6},"end":{"row":15,"column":9},"action":"insert","lines":["// "],"id":1389}],[{"start":{"row":15,"column":6},"end":{"row":15,"column":9},"action":"remove","lines":["// "],"id":1390}],[{"start":{"row":15,"column":19},"end":{"row":15,"column":65},"action":"remove","lines":["cdk-appointmentconcierge035121dc-1jhcoc97i63qb"],"id":1392},{"start":{"row":15,"column":19},"end":{"row":15,"column":78},"action":"insert","lines":["arn:aws:s3:::cdk-appointmentconcierge035121dc-1mmu9cw6xkv85"]}],[{"start":{"row":15,"column":19},"end":{"row":15,"column":32},"action":"remove","lines":["arn:aws:s3:::"],"id":1393}],[{"start":{"row":15,"column":67},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":1394},{"start":{"row":16,"column":0},"end":{"row":16,"column":6},"action":"insert","lines":["      "]}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":13},"action":"insert","lines":["region?"],"id":1395}],[{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"remove","lines":["?"],"id":1396}],[{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"insert","lines":[":"],"id":1397}],[{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"insert","lines":[" "],"id":1398}],[{"start":{"row":16,"column":14},"end":{"row":16,"column":16},"action":"insert","lines":["''"],"id":1399}],[{"start":{"row":16,"column":16},"end":{"row":16,"column":17},"action":"insert","lines":[","],"id":1400}],[{"start":{"row":16,"column":15},"end":{"row":16,"column":24},"action":"insert","lines":["eu-west-1"],"id":1401}],[{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"insert","lines":["_"],"id":1402},{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"insert","lines":["n"]},{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"insert","lines":["a"]},{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"insert","lines":["m"]},{"start":{"row":16,"column":16},"end":{"row":16,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":16,"column":31},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":1403},{"start":{"row":17,"column":0},"end":{"row":17,"column":6},"action":"insert","lines":["      "]},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["s"]},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["a"]}],[{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"remove","lines":["a"],"id":1404},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"remove","lines":["s"]}],[{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["b"],"id":1405},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["u"]}],[{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"remove","lines":["u"],"id":1406},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"remove","lines":["b"]}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":31},"action":"remove","lines":["region_name: 'eu-west-1',"],"id":1407}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":6},"action":"remove","lines":["  "],"id":1408},{"start":{"row":16,"column":2},"end":{"row":16,"column":4},"action":"remove","lines":["  "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":2},"action":"remove","lines":["  "]},{"start":{"row":15,"column":67},"end":{"row":16,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"insert","lines":["r"],"id":1409}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"remove","lines":["r"],"id":1410}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"insert","lines":["b"],"id":1411}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"remove","lines":["b"],"id":1412}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"insert","lines":["b"],"id":1413}],[{"start":{"row":16,"column":7},"end":{"row":16,"column":8},"action":"insert","lines":["u"],"id":1414}],[{"start":{"row":16,"column":7},"end":{"row":16,"column":8},"action":"remove","lines":["u"],"id":1415},{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"remove","lines":["b"]}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"insert","lines":["b"],"id":1416}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"remove","lines":["b"],"id":1417}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"insert","lines":["b"],"id":1418}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"remove","lines":["b"],"id":1419}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"insert","lines":["a"],"id":1420}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"remove","lines":["a"],"id":1421}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"insert","lines":["a"],"id":1422}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"remove","lines":["a"],"id":1423}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"insert","lines":["r"],"id":1424},{"start":{"row":16,"column":7},"end":{"row":16,"column":8},"action":"insert","lines":["e"]},{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"insert","lines":["g"]},{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"insert","lines":["i"]},{"start":{"row":16,"column":10},"end":{"row":16,"column":11},"action":"insert","lines":["o"]},{"start":{"row":16,"column":11},"end":{"row":16,"column":12},"action":"insert","lines":["n"]}],[{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"insert","lines":["N"],"id":1425},{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"insert","lines":["a"]},{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"insert","lines":["m"]},{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":16},"action":"remove","lines":["regionName"],"id":1426}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":16,"column":6},"end":{"row":16,"column":6},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1602677269789}