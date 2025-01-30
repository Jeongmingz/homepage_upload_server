import boto3
from botocore.config import Config

from share import return_env_value


def return_admin_r2_client():
	return boto3.client(
	's3',
		endpoint_url=return_env_value("CLOUDFLARE_R2_ENDPOINT"),
		aws_access_key_id=return_env_value("CLOUDFLARE_R2_ACCESS_ADMIN_KEY_ID"),
		aws_secret_access_key=return_env_value("CLOUDFLARE_R2_ACCESS_ADMIN_KEY_SECRET"),
		config=Config(signature_version='s3v4'),
		region_name='auto'
		)

def return_readonly_r2_client():
	return boto3.client(
		's3',
		endpoint_url=return_env_value("CLOUDFLARE_R2_ENDPOINT"),
		aws_access_key_id=return_env_value("CLOUDFLARE_R2_ACCESS_READONLY_KEY_ID"),
		aws_secret_access_key=return_env_value("CLOUDFLARE_R2_ACCESS_READONLY_KEY_SECRET"),
		config=Config(signature_version='s3v4'),
		region_name='auto'
		)