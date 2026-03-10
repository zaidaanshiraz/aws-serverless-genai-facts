# Step-by-Step Setup Tutorial

This guide walks you through setting up the AWS services required to run the application end-to-end.

## Prerequisites

- An active AWS account
- Basic familiarity with the AWS Management Console

---

## Step 1: Database Setup (Amazon DynamoDB)

1. Open the **Amazon DynamoDB** console.
2. Select **Create table**.
3. Configure the table:
   - **Table name:** `CloudFacts`
   - **Partition key:** `FactID` (Type: **String**)
4. Leave all other settings as default (On-Demand capacity) and select **Create table**.
5. After the table status becomes **Active**, add sample data:
   - Go to **Explore table items**
   - Select the `CloudFacts` table
   - Select **Create item**
6. Create multiple items with the following attributes:
   - `FactID` (String): use numeric values as strings (for example: `"1"`, `"2"`, `"3"`)
   - `FactText` (String): a short cloud computing fact

---

## Step 2: Compute & AI Logic (AWS Lambda)

1. Open the **AWS Lambda** console.
2. Select **Create function**.
3. Configure the function:
   - **Function name:** `CloudFunFacts`
   - **Runtime:** Python 3.13
4. Select **Create function**.

### Configure timeout

1. In the Lambda function page, open the **Configuration** tab.
2. Go to **General configuration** and select **Edit**.
3. Set **Timeout** to **20 seconds** (to allow time for the model to respond).
4. Save changes.

### Configure IAM permissions

1. In the **Configuration** tab, go to **Permissions**.
2. Select the **Execution role** link to open the role in IAM.
3. Attach the following managed policies to the role:
   - `AmazonDynamoDBReadOnlyAccess`
   - `AmazonBedrockFullAccess`

### Deploy the code

1. Return to the Lambda function page.
2. In **Code source**, paste/upload your Python code that:
   - Reads items from DynamoDB
   - Calls Amazon Bedrock using `bedrock.converse()`
3. Select **Deploy**.

---

## Step 3: API Layer (Amazon API Gateway)

1. Open the **Amazon API Gateway** console.
2. Select **Create API**.
3. Choose **HTTP API** (Build).
4. Configure the API:
   - **API name:** `FunfactsAPI`
   - **Integration:** select your `CloudFunFacts` Lambda function

### Configure routes

1. Create a route with:
   - **Method:** `GET`
   - **Resource path:** `/funfact`

### Configure CORS

CORS is required for browser-based clients (your frontend) to call the API.

1. Open the **CORS** settings for your HTTP API.
2. Configure the following (adjust as needed for production):
   - **Allowed origins:** `*`
   - **Allowed methods:** `*`
   - **Allowed headers:** `*`
   - **Max age:** `300`
3. Save changes.

### Copy the invoke URL

1. Go to **Stages**.
2. Select the default stage.
3. Copy the **Invoke URL**. You will use it in the frontend (ensure your final URL ends with `/funfact`).

---

## Step 4: Frontend Hosting (AWS Amplify)

1. On your local machine, open `index.html`.
2. Find the JavaScript `fetch` call (or API configuration).
3. Update `API_URL` with your API Gateway invoke URL, ensuring it ends with `/funfact`.

### Package the frontend

1. Create a ZIP archive containing `index.html` (for example: `frontend.zip`).

### Deploy with Amplify

1. Open the **AWS Amplify** console.
2. Select **Host your web app**.
3. Choose **Deploy without Git provider**.
4. Configure the deployment:
   - **App name:** for example, `CloudFunFactsUI`
   - **Environment name:** choose an appropriate environment name
5. Upload (drag and drop) your ZIP file.
6. Select **Save and deploy**.

### Verify deployment

1. After deployment completes, open the generated Amplify domain URL.
2. Confirm the application loads and successfully calls the API.

---
