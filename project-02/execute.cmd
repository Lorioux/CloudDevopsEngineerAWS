@echo off

IF "create" EQU "%1%" (
    set ACT=create-stack
    GOTO A
) ELSE (
    set ACT=update-stack
    GOTO A
)
:A
IF "network-stack" EQU "%2%" (
    aws cloudformation %ACT% ^
    --stack-name %2 ^
    --region us-east-1 ^
    --template-body file://network.yml ^
    --parameters file://networkparams.json ^
    --capabilities "CAPABILITY_IAM" "CAPABILITY_NAMED_IAM" ^
    --profile UdacityLabs
) ELSE (
    aws cloudformation %ACT% ^
    --stack-name %2 ^
    --region us-east-1 ^
    --template-body file://servers.yml ^
    --parameters file://serversparams.json ^
    --capabilities "CAPABILITY_IAM" "CAPABILITY_NAMED_IAM" ^
    --profile UdacityLabs
)
