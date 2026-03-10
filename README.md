# AWS Serverless GenAI Cloud Facts Generator

## Author
Mohammed Zaidaan Shiraz

## Project Overview
This project is a full-stack, serverless web application that delivers dynamically generated cloud computing facts. It demonstrates a modern, event-driven architecture by integrating AWS serverless computing, NoSQL database management, and native Generative AI models. Rather than serving static data, the backend processes stored items through a Large Language Model (LLM) using the Bedrock Converse API to output unique, engaging content to the frontend.



## Architecture & Technologies
* **Frontend:** HTML/CSS/JavaScript hosted on AWS Amplify
* **API Layer:** Amazon API Gateway (HTTP API) with properly configured CORS policies
* **Compute:** AWS Lambda (Python 3.13)
* **Database:** Amazon DynamoDB (On-Demand)
* **Generative AI:** Amazon Bedrock (Amazon Nova Micro model)
* **Security & IAM:** Least-privilege IAM roles and policies restricting access between Lambda, DynamoDB, and Bedrock.

## How It Works
1. The client-side application hosted on AWS Amplify initiates an HTTP GET request via the user interface.
2. Amazon API Gateway intercepts the request and routes it to the designated AWS Lambda function.
3. The Python Lambda function executes a scan operation on the Amazon DynamoDB table to retrieve a base data point.
4. The Lambda function constructs a contextual prompt and invokes Amazon Bedrock (Nova Micro).
5. The foundation model processes the prompt and returns a transformed, witty iteration of the original fact.
6. The Lambda function formats the AI-generated response into a JSON payload and returns it through the API Gateway to the client.

## Repository Structure
* `/frontend` - Contains the user interface source code (`index.html`) and client-side API fetch logic.
* `/backend` - Contains the Python Lambda deployment package (`lambda_function.py`) handling database operations and LLM integration.

## Setup & Deployment
Please refer to the `SETUP.md` file (or the instructions below) for a complete guide on replicating this architecture in your own AWS environment.
