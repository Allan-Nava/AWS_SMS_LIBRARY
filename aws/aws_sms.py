# coding: utf8
################################################################################
#
#   Author          :   Allan Nava
#   Modifier        :   Allan Nava
#   Date            :   04/11/2019
#   Update          :   18/01/2020
#
#   AWS SMS Python Library
#
#
#################################################################################
#
import logging
import os
from os import environ
#
import boto3
#
## This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)
#
#
class AWS_SMS(object):
    #
    AWS_ACCESS_KEY_ID     = 'aws access key id'
    AWS_SECRET_ACCESS_KEY = 'aws secret access key'
    client                = None
    #
    def __init__(self, client='sns'):
        """
            :client:    tipo di servizio
        """
        #
        self.client = client
        #
        try:
            logger.debug("AWS_SMS initiliaze -> %s " % self.client)
            if environ.get('AWS_ACCESS_KEY_ID') is not None and environ.get('AWS_SECRET_ACCESS_KEY') is not None:
                self.sns = boto3.client(
                    self.client,
                    # Hard coded strings as credentials, not recommended.
                    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                    region_name="eu-west-1",
                )
            else:
                self.sns = boto3.client(
                    self.client,
                    # Hard coded strings as credentials, not recommended.
                    aws_access_key_id=self.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=self.AWS_SECRET_ACCESS_KEY,
                    region_name="eu-west-1",
                )
        except Exception as e:
            raise Exception("AWS_SMS WS Endpoint not reachable: {}".format(e))
        #
    #
    #
    def __str__(self):
        return str(self.sns) + " " + self.client
    #
    # - Metodo per mandare un sms
    def send_sms(self, message="", subject="subject", phoneNumber=""):
        #
        result              = self.sns.publish(
            PhoneNumber=phoneNumber,
            Message=message,
            Subject=subject
        )
        return result
        #
    #
#
