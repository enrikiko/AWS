aws cloudformation deploy --stack-name ecr --capabilities CAPABILITY_NAMED_IAM --template-file ecr.yml
aws cloudformation deploy --stack-name ecs --capabilities CAPABILITY_NAMED_IAM --template-file ecs.yml
aws cloudformation deploy --stack-name task-definition --capabilities CAPABILITY_NAMED_IAM --template-file task_definition.yml
