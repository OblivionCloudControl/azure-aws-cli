#!/usr/bin/env python

import os
import sys

#sys.path.insert(0, os.path.abspath('lib'))
try:
    from setuptools import setup, find_packages
except ImportError:
    print("Azure AWS Login now needs setuptools in order to build. Install it using"
            " your package manager (usually python-setuptools) or via pip (pip"
            " install setuptools).")
    sys.exit(1)

setup(name='azure-aws-login',
      version='0.0.2',
      description='Retrieve temporary access credentials using Azure AD login',
      author='Andres Koetsier',
      author_email='andres@oblcc.com',
      url='http://oblcc.com/',
      license='GPLv3',
      install_requires=['boto3', 'requests'],
      scripts=[
         'bin/aad_aws_login'
      ],
      data_files=[],
)
