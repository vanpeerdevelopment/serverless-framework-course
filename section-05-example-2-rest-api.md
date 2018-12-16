# Section 5 - Real World Example 2 - REST API

## 28. Overview Of REST API Service
- Create REST API using API Gateway, Lambda and DynamoDB


## 29. Building The REST API
- Do `npm install` before deploying
- `handler.js`
    - `aws-sdk`: aws npm package
    - return a json object with `statusCode` and `body` when working with API Gateway
- `serverless.yml`
    - `${opt:variable}`: variable passed when running `serverless`
    - `resources`: pass a CloudFormation template to create necessary resources, e.g. DynamoDB table


## 30. Deploying The REST API
- API Gateway automatically created
- DynamoDB table automatically created


## 31. Test the REST API
- Test using postman, insomnia, ...


## 32. REST API - Next Steps Ideas
- Validation
- Authentication and authorization