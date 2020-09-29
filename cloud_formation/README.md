## Commands

-
    - ```aws cloudformation deploy --stack-name cortijo-camera-stack --capabilities CAPABILITY_NAMED_IAM --template-file camera-sync-template.yml```
    - ```aws cloudformation delete-stack --stack-name cortijo-camera-stack```
-
    - ```aws cloudformation deploy --stack-name cortijo-dns-stack --capabilities CAPABILITY_NAMED_IAM --template-file dns-template.yml```
    - ```aws cloudformation delete-stack --stack-name cortijo-dns-stack```