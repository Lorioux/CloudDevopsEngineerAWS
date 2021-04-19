if "create" EQU "%1%" (
    set ACT=create-stack
) else (
    if "update" EQU "%1%" (
        set ACT=uppdate-stack
    )
    else (

    )
)  

aws cloudformation %ACT% ^
--stack-name %2 ^
--region us-east-1 ^
--template-body file://%3 ^
--parameters file://%4
--capabilities "CAPABILITY_IAM" "CAPABILITY_NAMED_IAM"
