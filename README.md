# AWS SNS library

#### Required boto3


- Example of usigin:
```py
mobile = "mobile number"
message="this is the message "
aws = AWS_SMS()
aws.send_sms(message=message, subject='subject', phoneNumber=mobile)
```
