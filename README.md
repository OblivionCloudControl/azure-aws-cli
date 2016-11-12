# Get temporary AWS credentials from Azure Active Directory

## Prerequisites
* Have AAD configured as an IdP in AWS IAM (https://azure.microsoft.com/en-us/documentation/articles/active-directory-saas-amazon-web-service/)
* Boto3

## Getting credentials
### For getpass input
* Run `aad_aws_login [AAD App Id] --username [email address]`

### For 1Password OPVault input
* Run `aad_aws_login [AAD App ID] --opvault-path "[path to 1Password.opvault]" --opvault-title "[title of 1Password item]"`

### Profile
* This will store the AWS credentials in your AWS credentials file under the profile [email address]

You can specify the name of the iam-profile with `--profile-name [name]`.

The AAD App id can be found by using the last part of the single sign-on url you can find on the application dashboard.

You might want to use an alias to have the login simplified like `aws_login='aad_aws_login 1234567890abcdef --username foo@bar.com --profile-name foo-bar'`.

## MFA
This tool is compatible if MFA is enabled for the account. The types of MFA that are support by this tool:
* SMS
* Authenticator App push notification
* Authenticator App token

## Installation
`pip install -e git+https://github.com/OblivionCloudControl/azure-aws-cli.git\#egg=aad-aws-login`
