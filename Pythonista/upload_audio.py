#
# Pythonista script to upload audio file to S3 bucket.
#
# Based on https://www.jamesridgway.co.uk/transcribing-voice-notes-on-the-ipad-with-aws-transcribe/
#

import appex
import console
import keychain
import ui
import boto3
import boto3.session
from botocore.exceptions import ClientError


def main():
    console.clear()
    print()

    if not appex.is_running_extension():
        print('This script is intended to be run from the sharing extension.')
        return

    access_key_id = keychain.get_password('upload_audio', 'access_key_id')
    secret_access_key = keychain.get_password('upload_audio', 'secret_access_key')
    s3_bucket = keychain.get_password('upload_audio', 's3_bucket')
    s3_prefix = keychain.get_password('upload_audio', 's3_prefix')
    if access_key_id == None:
        access_key_id = console.input_alert('Enter access key ID:')
        keychain.set_password('upload_audio', 'access_key_id', access_key_id)
    if secret_access_key == None:
        secret_access_key = console.input_alert('Enter secret access key:')
        keychain.set_password('upload_audio', 'secret_access_key', secret_access_key)
    if s3_bucket == None:
        s3_bucket = console.input_alert('Enter S3 bucket name:')
        keychain.set_password('upload_audio', 's3_bucket', s3_bucket)
    if s3_prefix == None:
        s3_prefix = console.input_alert('Enter S3 folder (prefix) for upload:')
        keychain.set_password('upload_audio', 's3_prefix', s3_prefix)

    my_session = boto3.session.Session(
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key,
        region_name='me-south-1'
        )
    s3_client = my_session.client('s3')
    file_path = appex.get_file_path()
    file_name = file_path.split('/')[-1]

    try:
        response = s3_client.upload_file(
            file_path,
            s3_bucket,
            s3_prefix + '/' + file_name)
    except ClientError as e:
        print(e)
        return False
    console.alert(
        'Appointment Concierge',
        'Thank you. Your message has been received. A member of our customer ' \
        'service team will contact you.',
        'Ok', hide_cancel_button=True)
    return True


if __name__ == '__main__':
    main()
