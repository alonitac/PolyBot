import json
import os
import string
import time
import boto3
import botocore
from loguru import logger
from utils import search_download_youtube_video
import telegram

def fix_file_name(file_name):
    for char in string.punctuation:
        file_name.replace(char, "")

    return file_name;

def process_msg(msg, chatid):

    with open('.telegramToken') as f:
        _token = f.read()
    bot = telegram.Bot(token=_token)
    #strList = path.str(split("["))
    #videoID = strList[len(strList) - 1].split("]", 1)
    #bot.send_message(chat_id=chatid, text="youtube.com/watch?v=" + videoID[0])

    with YouTubeDL() as ydl:
        videos = ydl.extract_info(f"ytsearch{1}:{msg}", download=False)['entries']

        if len(videos) == 0:
            bot.send_message(chat_id=chatid, text="The selected video was not found.")
        else:
            for video in videos:
                if video['is_live'] == True:
                    bot.send_message(chat_id=chatid, text="youtube.com/watch?v=" + video['id'])
                else:
                    if video['filesize'] > 1024 * 1024 * 1024 * 2:
                        bot.send_message(chat_id=chatid, text="youtube.com/watch?v=" + video['id'])
                    elif video['filesize'] > 1024 * 1024 * 50:



                        # download and upload if not exist on s3 bucket, then send URL, not video fileeee
                    else:
                        # download and upload if not exist on s3 bucket, then send video file


    paths = search_download_youtube_video(msg)

    for path in paths:
        with open('.telegramToken') as f:
            _token = f.read()
        bot = telegram.Bot(token=_token)
        strList = path.str(split("["))
        videoID = strList[len(strList) - 1].split("]", 1)
        bot.send_message(chat_id=chatid, text="youtube.com/watch?v=" + videoID[0])


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
                # logger.info("hey this is chat id: " + msg.message_attributes.get('chat_id').get('StringValue'))
                logger.info(f'processing message {msg}')
                process_msg(msg.body, msg.message_attributes.get('chat_id').get('StringValue'))

                # delete message from the queue after it was handled
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
