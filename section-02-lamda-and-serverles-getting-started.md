# Section 2 - AWS Lambda & Serverless - Getting Started

## 6. AWS Console Changes
- AWS console might be updated


## 7. AWS Lambda Console
- Create function: from scratch, blueprint, application repository
- Create function
    - Name
    - Role: new role from policy templates, existing role
- Create and run test event
- Monitoring


## 8. Installing Serverless
1. nvm/node
    - [`zsh-nvm`](https://github.com/lukechilds/zsh-nvm)
    - `nvm install 8.10`
    - `nvm alias serverless 8.10`
2. Serverless
    - `npm install -g serverless`
3. Serverless login
    - `serverless login`
4. AWS IAM user
    - Name: `serverless-admin`
    - Access type: `Programmatic access`
    - Permissions: `AdministratorAccess`
5. Configure AWS serverless-admin profile
    - `serverless config credentials --provider aws --key <KEY> --secret <SECRET> --profile serverless-admin`
    - AWS serverless profile is stored in `~/.aws/credentials`
    
    
## 9. Deploying Our First Function
- `serverless create --template aws-python --path hello-world-python`
    - `.gitignore`
    - `handler.py`: python script returning `hello-world`
    - `serverless.yml`: service configuration
        - Add app: `app: <serverless application name>`
        - Add tenant: `tenant: dietervp`
        - Add profile: `provider.profile: serverless-admin`
        - Add region: `provider.region: eu-central-1` 
- `serverless deploy --verbose`
    - Creates CloudFormation stack
    - Creates S3 bucket
    - Upload CloudFormation template to S3
    - Update CloudFormation stack
    - Creates IAM role
    - Creates CloudWatch log group
    - Creates Lambda function
    - Creates Lambda function version
    
    
## 10. Running The Function From The CLI
- `serverless invoke -f hello -l`


## 11. Updating The Function From The CLI
#### Deploy stack
- Update function
- Redeploy stack: `serverless deploy --verbose`
- Slow
- Needs to be used when something besides function is updated

#### Deploy function
- Update function
- Redeploy function: `serverless deploy function -f hello`
- Fast
- Can be used when only function is updated


## 12. Fetching The Function Logs From The CLI
#### AWS Console
- Log Group in CloudWatch per service and stage
- Log Stream per update


#### Serverless
- `serverless logs -f hello`: print logs
- `serverless logs -f hello -t`: tail logs


## 13. Removing The Function
- `serverless remove`: removes function and all created resources


## 14. Section Summary
- Check this document

