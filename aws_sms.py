# coding: utf8
################################################################################
#
#   Author          :   Allan Nava
#   Modifier        :   Allan Nava
#   Date            :   04/11/2019
#
#   AWS SMS Library
#
#
#################################################################################
#
import boto3, logging
#
## This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)
#
#
class AWS_SMS(object):
    #
    AWS_ACCESS_KEY_ID     = 'aws access key id'
    AWS_SECRET_ACCESS_KEY = 'aws secret access key'
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
            self.sns = boto3.client(
                self.client,
                # Hard coded strings as credentials, not recommended.
                aws_access_key_id=self.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=self.AWS_SECRET_ACCESS_KEY
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
        #data                = self._prepare_request()
        #data["PhoneNumber"] = "+393409477141"
        #data["Message"]     = "message"
        result              = self.sns.publish(
            PhoneNumber=phoneNumber,
            Message=message,
            Subject=subject
        )
        #result              = self.make_request("publish", data)
        return result
        #
    #
#
