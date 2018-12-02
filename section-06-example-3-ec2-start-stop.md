# Section 6 - Real World Example 3 - AWS Automation - EC2 Start Stop

## 33. Overview Of The Lambda Service
- Create cron job using Lambda to stop EC2 at night and start EC2 in the morning


## 34. Deploying The EC2 Start And Stop Lambda Functions
- `handler.py`
    - Get all EC2 instances 
    - Start/stop EC2 instances 
- `serverless.yml`
    - `functions.function.events`: `schedule: cron(* * * * * *)`: trigger a function based on a schedule
    - `functions.function.events`: `schedule: rate(x minutes)`: trigger a function based on a certain rate
    - Schedules are managed in AWS as CloudWatch events


## 35. Next Steps / Ideas
- Use tags to include/exclude instances
- Use tags to have separate schedules