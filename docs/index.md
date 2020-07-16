
# AWS SNS Python Library

#### Required boto3, python3


- Example of using:
```py
mobile = "mobile number"
message="this is the message "
aws = AWS_SMS()
aws.send_sms(message=message, subject='subject', phoneNumber=mobile)
```

https://aws.amazon.com/it/sns/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc
