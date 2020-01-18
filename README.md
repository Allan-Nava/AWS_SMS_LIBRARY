# AWS SNS Python Library

#### Required boto3, python3


- Example of using:
```py
mobile = "mobile number"
message="this is the message "
aws = AWS_SMS()
aws.send_sms(message=message, subject='subject', phoneNumber=mobile)
```
