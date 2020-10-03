## Commands

- ```aws cloudformation deploy --stack-name cortijo-lamda-s3bucket-stack --capabilities CAPABILITY_NAMED_IAM --template-file lambda-s3bucket-template.yml```
- ```aws cloudformation delete-stack --stack-name cortijo-lamda-s3bucket-stack```

- ```aws cloudformation deploy --stack-name cortijo-camera-stack --capabilities CAPABILITY_NAMED_IAM --template-file camera-sync-template.yml```
- ```aws cloudformation delete-stack --stack-name cortijo-camera-stack```

- ```aws cloudformation deploy --stack-name cortijo-dns-stack --capabilities CAPABILITY_NAMED_IAM --template-file dns-template.yml```
- ```aws cloudformation delete-stack --stack-name cortijo-dns-stack```

- ```aws cloudformation deploy --stack-name cortijo-domain-stack --capabilities CAPABILITY_NAMED_IAM --template-file domain-template.yml```
- ```aws cloudformation delete-stack --stack-name cortijo-domain-stack```

- ```aws cloudformation deploy --stack-name cortijo-dynamo-stack --capabilities CAPABILITY_NAMED_IAM --template-file dynamo-template.yml```
- ```aws cloudformation delete-stack --stack-name cortijo-dynamo-stack```
