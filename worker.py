import json
import time
import boto3
import botocore
from loguru import logger
import os
import telegram
import pymongo

from utils import search_download_youtube_video

def process_msg(msg, chatid):
    #myclient = pymongo.MongoClient("mongodb+srv://itay:itay@cluster0.jjvfg14.mongodb.net/?retryWrites=true&w=majority")

    #mydb = myclient["mydatabase"]
    #mycol = mydb["customers"]

    #mydict = {"name": "matt", "address": "Hi"}

    #x = mycol.insert_one(mydict)

    paths = search_download_youtube_video(msg)

    for path in paths:
        s3 = boto3.client('s3')
        s3.upload_file(Bucket='itay-bucket1', Key="dir-1/" + path, Filename=path)

        with open('.telegramToken') as f:
            _token = f.read()

        bot = telegram.Bot(token=_token)
        bot.send_video(chat_id=chatid, video=open(path, 'rb'), timeout=200)

        os.remove(path)

    # TODO upload the downloaded video to your S3 bucket


def main():
    while True:
        logger.info("waiting for new request")
        try:
            messages = queue.receive_messages(
                MessageAttributeNames=['All'],
                MaxNumberOfMessages=1,
                WaitTimeSeconds=20
            )

            for msg in messages:
                #logger.info("hey this is chat id: " + msg.message_attributes.get('chat_id').get('StringValue'))
                logger.info(f'processing message {msg}')
                process_msg(msg.body, msg.message_attributes.get('chat_id').get('StringValue'))

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

    logger.info("Worker started, awaiting new action")

    main()
