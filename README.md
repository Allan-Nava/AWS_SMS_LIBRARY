# AWS SNS Python Library
[![Discord Chat](https://img.shields.io/badge/Discord-Chat-important)](https://discord.gg/nMTKrRZ) [![Python application](https://github.com/Allan-Nava/AWS_SMS_LIBRARY/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/Allan-Nava/AWS_SMS_LIBRARY/actions/workflows/pythonapp.yml)

#### Required boto3, python3


- Example of using:
```py
mobile = "mobile number"
message="this is the message "
aws = AWS_SMS()
aws.send_sms(message=message, subject='subject', phoneNumber=mobile)
```

https://aws.amazon.com/it/sns/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc
