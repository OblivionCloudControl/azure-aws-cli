# Get temporary AWS credentials from Azure Active Directory

## Prerequisites
* Have AAD configured as an IdP in AWS IAM (https://azure.microsoft.com/en-us/documentation/articles/active-directory-saas-amazon-web-service/)
* Boto3

## Getting credentials
* Run `samlapi_formauth.py [email address] [AAD App Id]`
* This will store the AWS credentials in your AWS credentials file under the profile [email address]

You can specify the name of the iam-profile with `--profile-name [name]`.

This tool is compatible if MFA is enabled for the account. The types of MFA that are support by this tool:
* SMS
* Authenticator App push notification
* Authenticator App token

