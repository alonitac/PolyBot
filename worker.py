import json
import boto3
from loguru import logger
from utils import search_download_youtube_video


with open('config.json') as f:
    config = json.load(f)

sqs = boto3.resource('sqs', region_name=config.get('aws_region'))
queue = sqs.get_queue_by_name(QueueName=config.get('bot_to_worker_queue_name'))


def process_msg(msg):
    search_download_youtube_video(msg)

    # TODO upload the downloaded video to your S3 bucket


def lambda_handler(event, context):
    logger.info(f'New event {event}')

    # TODO complete the code that processes all records (use use process_msg())
