# Section 4 - Real World Example 1 - S3 Thumbnails

## 23. Overview Of S3 Thumbnail Generator Service
- Create thumbnail when image is uploaded to S3


## 24. Prerequisite: Docker Installatioin
- Install docker


## 25. Implementation Of Thumbnail Service - Part 1
- `handler.py`
    - Get bucket and key from event
    - Get image with key from S3 bucket
    - Convert image to thumbnail
    - Generate new filename
    - Upload thumbnail to S3
- `serverless.yml`
    - `functions.hello.events`: events which trigger the function
    - `custom.<variable>`: custom variable which can be used in `serverless.yml` by `${self:custom.bucket}`
    - `plugins.<plugin>`: custom behavior which will run during `serverless deploy`, e.g. install and upload all npm dependencies 


## 26. Implementation Of Thumbnail Service - Part 2
- Check everything on AWS


## 27. Thumbnail Service - Next Step Ideas 
- Error handling
- Measure timeouts for different image sizes
- Alert using SNS on failure
- Put image metadata in DynamoDB
