import json
import time
import boto3
import botocore
from loguru import logger
from utils import search_download_youtube_video
import os


def clean_dir(path):
    """ method deletes unnecessary videos file from directory """
    if os.path.exists(path):
        try:
            os.remove(path)
        except:
            print("Could not remove file:", path)

def process_msg(msg):
    files_name = search_download_youtube_video(msg)
    s3_client = boto3.client('s3')
    for file_name in files_name:
        try:
            s3_client.upload_file(file_name, "shay-polybot-s3", f"videos/{file_name}")
        except any as e:
            logger.error(e)
        print(file_name)
        clean_dir(file_name)
    return logger.info(f"file's name {files_name} was uploaded to s3 bucket to: videos/{file_name}")


def main():
    while True:
        try:
            messages = queue.receive_messages(
                MessageAttributeNames=['All'],
                MaxNumberOfMessages=1,
                WaitTimeSeconds=10
            )
            for msg in messages:
                logger.info(f'processing message {msg}')
                process_msg(msg.body)

                # delete message from the queue after is was handled
                response = queue.delete_messages(Entries=[{
                    'Id': msg.message_id,
                    'ReceiptHandle': msg.receipt_handle
                }])
                if 'Successful' in response:
                    logger.info(f'msg {msg} has been handled successfully')

        except botocore.exceptions.ClientError as err:
            logger.exception(f"Couldn't receive messages {err}")
            time.sleep(10)


if __name__ == '__main__':
    with open('config.json') as f:
        config = json.load(f)

    sqs = boto3.resource('sqs', region_name=config.get('aws_region'))
    queue = sqs.get_queue_by_name(QueueName=config.get('bot_to_worker_queue_name'))

    main()
