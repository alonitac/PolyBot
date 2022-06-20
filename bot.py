from telegram.ext import Updater, MessageHandler, Filters
from utils import search_download_youtube_video
from loguru import logger
import os


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
        return \
        context.bot.send_video(chat_id=update.message.chat_id, video=open(file_path, 'rb'), supports_streaming=True)[
            'video']

    def send_text(self, update, text, quote=False):
        """Sends text to a chat"""
        # retry https://github.com/python-telegram-bot/python-telegram-bot/issues/1124
        update.message.reply_text(text, quote=quote)


class QuoteBot(Bot):

    def _message_handler(self, update, context):
        to_quote = True

        if update.message.text == 'Don\'t quote me please':
            to_quote = False

        self.send_text(update, f'Your original message: {update.message.text}', quote=to_quote)


class YoutubeBot(Bot):
    last_cached = {}

    def clean_dir(self, path):
        if os.path.exists(path):
            try:
                os.remove(path)
            except:
                print("Could not remove file:", path)

    def video_down(self, video_text, ):
        video_file_path, video_you_t_id = search_download_youtube_video(video_text, 1, YoutubeBot.last_cached)
        return video_file_path, video_you_t_id

    def _message_handler(self, update, context):

        file_path, video_you_t_id = self.video_down(update.message.text)

        if video_you_t_id in YoutubeBot.last_cached:
            logger.info(f'Video id: {video_you_t_id} was in use before!')
            context.bot.send_video(chat_id=update.message.chat_id,
                                   video=YoutubeBot.last_cached[video_you_t_id],
                                   supports_streaming=True)
        else:
            file_id = self.send_video(update, context, file_path)['file_id']
            YoutubeBot.last_cached.update({video_you_t_id: file_id})
        self.clean_dir(file_path)


if __name__ == '__main__':
    with open('.telegeamToken') as f:
        _token = f.read()

    my_bot = YoutubeBot(_token.strip())
    my_bot.start()
