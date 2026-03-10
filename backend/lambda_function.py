import boto3
import random
import json

# Initialize AWS clients
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("CloudFacts")
bedrock = boto3.client("bedrock-runtime")

def lambda_handler(event, context):
    # 1. Fetch all facts from DynamoDB
    try:
        response = table.scan()
        items = response.get("Items", [])
    except Exception as e:
        print(f"DynamoDB error: {e}")
        items = []

    # Handle empty database scenario
    if not items:
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS"
            },
            "body": json.dumps({"fact": "Oops! The database is empty."})
        }

    # Pick a random fact
    random_item = random.choice(items)
    original_fact = random_item.get("FactText", "AWS S3 launched in 2006.")

    # 2. Format the prompt
    prompt = f"Take this cloud computing fact and make it fun, sarcastic, and engaging in 1 sentence. Keep it short and witty: {original_fact}"

    witty_fact = ""

    # 3. Call Amazon Nova Micro using the modern Converse API
    try:
        resp = bedrock.converse(
            modelId="us.amazon.nova-micro-v1:0",
            messages=[
                {
                    "role": "user",
                    "content": [{"text": prompt}]
                }
            ],
            inferenceConfig={
                "maxTokens": 100,
                "temperature": 0.7
            }
        )

        # 4. Parse the response (Notice how much cleaner this is!)
        witty_fact = resp["output"]["message"]["content"][0]["text"].strip()

    except Exception as e:
        print(f"Bedrock error: {e}")
        # If the AI fails, fallback to the original database fact
        witty_fact = original_fact

    # 5. Return response to API Gateway
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, OPTIONS"
        },
        "body": json.dumps({"fact": witty_fact})
    }