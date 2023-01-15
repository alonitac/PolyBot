import json
import time
import boto3
import botocore
from loguru import logger
from common.utils import search_download_youtube_video
import os


def process_msg(msg):
    downloaded_videos = search_download_youtube_video(msg)
    s3 = boto3.client('s3')
    for k, v in downloaded_videos.items():
        """
        s3.upload_file(xlist[0], config.get('videos_bucket'), xlist[0], ExtraArgs={'Metadata': {'URL': xlist[1]}})
        s3.upload_file(video, config.get('videos_bucket'), video, ExtraArgs={'Metadata': {'URL': video}})
        """

        s3.upload_file(k, config.get('videos_bucket'), k)
        os.remove(f'./{k}')


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
    with open('C:/Users/shlomi/PycharmProjects/PolyBot/common/config.json') as f:
        config = json.load(f)

    sqs = boto3.resource('sqs', region_name=config.get('aws_region'))
    queue = sqs.get_queue_by_name(QueueName=config.get('bot_to_worker_queue_name'))

    main()
