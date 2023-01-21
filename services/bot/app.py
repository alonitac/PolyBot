import json
import botocore
from Cryptodome import Math
from telegram.ext import Updater, MessageHandler, Filters
from loguru import logger
import boto3
from common.utils import search_download_youtube_video


class Bot:

    def __init__(self, token):
        # create frontend object to the bot programmer
        self.updater = Updater(token, use_context=True)

        # add _message_handler as main internal msg handler
        self.updater.dispatcher.add_handler(MessageHandler(Filters.text, self._message_handler))

    def start(self):
        """Start polling msgs from users, this function never returns"""
        self.updater.start_polling()
        logger.info(f'{self.__class__.__name__} is up and listening to new messages....')
        self.updater.idle()

    def _message_handler(self, update, context):
        """Main messages handler"""
        self.send_text(update, f'Your original message: {update.message.text}')

    def send_video(self, update, context, file_path):
        """Sends video to a chat"""
        context.bot.send_video(chat_id=update.message.chat_id, video=open(file_path, 'rb'), supports_streaming=True)

    def send_text(self, update, text, chat_id=None, quote=False):
        """Sends text to a chat"""
        if chat_id:
            self.updater.bot.send_message(chat_id, text=text)
        else:
            # retry https://github.com/python-telegram-bot/python-telegram-bot/issues/1124
            update.message.reply_text(text, quote=quote)


class QuoteBot(Bot):
    def _message_handler(self, update, context):
        to_quote = True

        if update.message.text == 'Don\'t quote me please':
            to_quote = False

        self.send_text(update, f'Hi, Your original message: {update.message.text}', quote=to_quote)


class YoutubeObjectDetectBot(Bot):
    vdict = {}
    s3dict = {}

    def __init__(self, token):
        super().__init__(token)
    """
    def tmessage(self, update, context):
        chat_id = str(update.effective_message.chat_id)
        self.send_text(update, f'sdfadsf...', chat_id=chat_id)
    """

    def _message_handler(self, update, context):

        try:
            chat_id = str(update.effective_message.chat_id)

            if "@" not in update.message.text:
                YoutubeObjectDetectBot.vdict = {}
                downloaded_videos = search_download_youtube_video(update.message.text, False, 7)
                """
                self.send_text(update, f'To upload the following video file write @file{i}', chat_id=chat_id)
                """
                i = 1
                for k, v in downloaded_videos.items():
                    self.send_text(update, f'To upload the following video file write @addfile{i} ', chat_id=chat_id)
                    self.send_text(update, f'*********************', chat_id=chat_id)
                    self.send_text(update, v, chat_id=chat_id)
                    self.send_text(update, f'*********************', chat_id=chat_id)
                    YoutubeObjectDetectBot.vdict[i] = k
                    i += 1

            elif "@addfile" in update.message.text.lower():
                self.send_text(update, f'You choose {update.message.text}', chat_id=chat_id)
                mes = update.message.text.lower()
                p = mes.replace('@addfile', '')
                msg = str(YoutubeObjectDetectBot.vdict[int(p)])
                response = workers_queue.send_message(
                    MessageBody=msg,
                    MessageAttributes={
                        'chat_id': {'StringValue': chat_id, 'DataType': 'String'}
                    }
                )
                logger.info(f'msg {response.get("MessageId")} has been sent to queue')
                self.send_text(update, f'Hii, Your message is being processed...', chat_id=chat_id)
            elif "@addall" in update.message.text.lower():
                self.send_text(update, f'You choose to Add all files', chat_id=chat_id)
                for k, v in YoutubeObjectDetectBot.vdict.items():
                    msg = v
                    response = workers_queue.send_message(
                        MessageBody=msg,
                        MessageAttributes={
                            'chat_id': {'StringValue': chat_id, 'DataType': 'String'}
                        }
                    )
                logger.info(f'msg {response.get("MessageId")} has been sent to queue')
                self.send_text(update, f'Hii, Your message is being processed...', chat_id=chat_id)
            elif "@list" in update.message.text.lower():
                s3_client = boto3.client("s3")
                bucket_name = config.get('videos_bucket')
                response = s3_client.list_objects_v2(Bucket=bucket_name)
                files = response.get("Contents")
                if files is not None:
                    c = 1
                    for file in files:
                        print(f"file_name: {file['Key']}, size: {file['Size']}")
                        fs = file['Size']/1048576
                        self.send_text(update, f"{c}:  file_name: {file['Key']},   size: {int(fs)}MB", chat_id=chat_id)
                        YoutubeObjectDetectBot.s3dict[c] = file['Key']
                        c += 1
                else:
                    self.send_text(update, f'list is empty', chat_id=chat_id)
            elif "@playlist" in update.message.text.lower():
                s3_client = boto3.client("s3")
                bucket_name = config.get('videos_bucket')
                response = s3_client.list_objects_v2(Bucket=bucket_name)
                files = response.get("Contents")
                if files is not None:

                    for file in files:
                        downloaded_videos = search_download_youtube_video(file['Key'], False)
                        for k, v in downloaded_videos.items():
                            self.send_text(update, v, chat_id=chat_id)

                else:
                    self.send_text(update, f'Playlist is empty', chat_id=chat_id)
            elif "@delfile" in update.message.text.lower():
                s3 = boto3.resource('s3')
                mes = update.message.text.lower()
                p = mes.replace('@delfile', '')
                self.send_text(update, f'You choose to delete file {p}', chat_id=chat_id)
                key = str(YoutubeObjectDetectBot.s3dict[int(p)])

                s3.Object(config.get('videos_bucket'), key).delete()
            elif "@delall" in update.message.text.lower():
                s3 = boto3.resource('s3')
                self.send_text(update, f'You choose to delete all files', chat_id=chat_id)
                for key in YoutubeObjectDetectBot.s3dict:
                    s3.Object(config.get('videos_bucket'), YoutubeObjectDetectBot.s3dict[key]).delete()
            else:
                self.send_text(update, f'Wrong command ,Please try again.', chat_id=chat_id)
            """
                            for k, v in YoutubeObjectDetectBot.vdict.items():
                    self.send_text(update, k, chat_id=chat_id)
                    self.send_text(update, v, chat_id=chat_id)
            
            
            if "@" in update.message.text:
                self.send_text(update, update.message.text, chat_id=chat_id)
            """
        except botocore.exceptions.ClientError as error:
            logger.error(error)
            self.send_text(update, f'Something went wrong, please try again...')


if __name__ == '__main__':

    with open('C:/Users/shlomi/PycharmProjects/PolyBot/secrets/.telegramToken') as f:
        _token = f.read()

    with open('C:/Users/shlomi/PycharmProjects/PolyBot/common/config.json') as f:
        config = json.load(f)

    sqs = boto3.resource('sqs', region_name=config.get('aws_region'))
    workers_queue = sqs.get_queue_by_name(QueueName=config.get('bot_to_worker_queue_name'))
    my_bot = YoutubeObjectDetectBot(_token)
    my_bot.start()
