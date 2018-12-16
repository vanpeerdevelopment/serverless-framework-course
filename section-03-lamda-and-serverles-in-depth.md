# Section 3 - AWS Lambda & Serverless - In Depth

## 15. Create AWS Lambda Function Using Any Runtime
- `serverless create --template aws-nodejs --path hello-world-nodejs`
- `serverless create --template aws-java-maven --path hello-world-java`


## 16. YAML Crash Course
- Key value pairs
- Nested objects (using tabs)
- Arrays (using `-`)
- Multiline strings (using `|` first line)
- Single line strings spanning multiple lines (using `>` on first line)


## 17. JSON To YAML Practice Exercise
- Exercise


## 18. Functions Timeout And Memory
#### At Provider Level
- `provider.timeout: <in seconds>`
- `provider.memorySize: <in mb>` 

#### At Function Level
- `functions.hello.timeout: <in seconds>`
- `functions.hello.memorySize: <in mb>`
- Overrides values at provider level


## 19. IAM Permissions for Lambda Functions
- Add custom `provider.iamRoleStatements` to add permissions to lambdas


## 20. Environment Variables In AWS Lambda
#### At Provider Level
- `provider.environment.ENV`

#### At Function Level
- `functions.hello.environment.ENV`
- Overrides values at provider level


## 21. VPC For Lambda Functions
- Lambda can be deployed in a subnet inside a VPC
- Security groups can be assigned to lambdas

#### At Provider Level
- `provider.vpc.securityGroupIds`
- `provider.vpc.subnetIds`

#### At Function Level
- `functions.hello.vpc.securityGroupIds`
- `functions.hello.vpc.subnetIds`
- Overrides values at provider level


## 22. AWS Lmabda Pricing
- [Pricing](https://aws.amazon.com/lambda/pricing/)
- Per call:
    - First 1.000.000 requests free per month
    - $0,2 per 1.000.000 requests thereafter
- Per duration (in increments of 100ms):
    - 400.000 GB-seconds free per month
    - $1 for 600.000 GB-seconds thereafter