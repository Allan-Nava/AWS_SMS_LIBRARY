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
import aws_sms
#
aws = aws_sms.AWS_SMS()
#
aws.send_sms(message="prova", phoneNumber="+39numero")
#
