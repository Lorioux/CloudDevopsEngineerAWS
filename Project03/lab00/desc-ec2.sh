#!/bin/sh -

rm -f ./inventory
read instancename

echo "[all]" > ./inventory

command="$(aws ec2 describe-instances --region us-east-1 \
--filters "Name=tag:Name, Values='$instancename'" \
--query "Reservations[*].Instances[*].PublicIpAddress" \
--output text)"

echo $command > tmp
read ip < tmp 

echo $ip >> ./inventory

cat ./inventory
rm -f tmp