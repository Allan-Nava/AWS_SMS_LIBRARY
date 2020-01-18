# coding: utf8
################################################################################
#
#   Autore          :   Allan Nava
#   Modificato      :   Allan Nava
#   Data            :   18/02/2020
#   Aggiornamento   :   18/01/2020
#
#
#################################################################################
#
#
from .aws_sms import AWS_SMS
#
aws = AWS_SMS()
#
aws.send_sms(message="prova", phoneNumber="+39numero")
#
