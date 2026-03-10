Step-by-Step Setup Tutorial (For your repository or documentation)
Prerequisites: An active AWS Account and basic familiarity with the AWS Management Console.

Step 1: Database Setup (Amazon DynamoDB)
Navigate to the DynamoDB Console and click Create table.

Table name: CloudFacts

Partition key: FactID (Type: String).

Leave settings on Default (On-Demand) and click Create table.

Once active, go to Explore table items -> select your table -> Create item.

Add several items where FactID is a number (e.g., "1") and create a new String attribute named FactText containing a standard cloud computing fact.

Step 2: Compute & AI Logic (AWS Lambda)
Navigate to the Lambda Console and click Create function.

Name: CloudFunFacts | Runtime: Python 3.13. Click Create.

Under the Configuration tab, select General configuration and edit the Timeout to 20 seconds (to allow the AI model time to respond).

Under the Configuration tab, select Permissions, click the Execution Role link, and attach the following policies to grant your function necessary access:

AmazonDynamoDBReadOnlyAccess

AmazonBedrockFullAccess

In the Code source section, paste your Python script that connects to DynamoDB and calls bedrock.converse(). Click Deploy.

Step 3: API Layer (Amazon API Gateway)
Navigate to the API Gateway Console and click Create API.

Build an HTTP API.

Name: FunfactsAPI. Add an integration pointing to your CloudFunFacts Lambda function.

Configure Routes: Set the Method to GET and the Resource path to /funfact.

Configure CORS: This is required for your frontend to communicate with the API. Navigate to the CORS settings for your API and configure it as follows:

Allowed origins: *

Allowed methods: *

Allowed headers: *

Max age: 300

Navigate to Stages, select your default stage, and copy the Invoke URL.

Step 4: Frontend Hosting (AWS Amplify)
On your local machine, open your index.html file and locate the JavaScript fetch function.

Update the API_URL variable with your specific API Gateway Invoke URL (ensure it ends in /funfact).

Compress the index.html file into a ZIP archive (e.g., frontend.zip).

Navigate to the AWS Amplify Console.

Select Host your web app -> Deploy without Git provider.

Name your app (e.g., CloudFunFactsUI) and specify an environment name.

Drag and drop your ZIP file into the upload area and click Save and deploy.

Once deployment is complete, click the generated domain URL to test the live, full-stack application.
