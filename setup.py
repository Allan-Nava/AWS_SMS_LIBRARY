# -*- coding: utf-8 -*-
#
from setuptools import setup
#
with open("README.md", "r") as fh:
    long_description = fh.read()
#
setup(
    name='aws-sms-library',
    version='0.23.0',
    url='https://github.com/Allan-Nava/AWS_SMS_LIBRARY',
    license='The MIT License',
    author='Allan Nava',
    author_email='allan.nava@hiway.media',
    keywords='aws,sms',
    description='aws-sms-library is a Python package providing access to the AWS SMS API.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['aws', 'aws.sms'],
    install_requires=['boto3==1.0.0'],
    tests_require=['httmock>=1.2.5'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Utilities'
    ]
)
#