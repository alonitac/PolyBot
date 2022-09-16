from telegram.ext import Updater, MessageHandler, Filters
from utils import search_download_youtube_video
from loguru import logger


class Bot:

    def __init__(self, _token):
        # create frontend object to the bot programmer
        self.updater = Updater(_token, use_context=True)

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

    def send_text(self, update,  text, quote=False):
        """Sends text to a chat"""
        # https://github.com/python-telegram-bot/python-telegram-bot/issues/1124
        update.message.reply_text(text, quote=quote)


class QuoteBot(Bot):
    def _message_handler(self, update, context):
        to_quote = True

        if update.message.text == 'Don\'t quote me please':
            to_quote = False

        self.send_text(update, f'Your original message: {update.message.text}', quote=to_quote)


from utils import search_download_youtube_video
class YoutubeBot(Bot):
    def __init__(self):
        super(YoutubeBot, self).__init__(self)
        self._cache = dict()

    def _message_handler(self, update, context):
        query_txt = update.message.text
        if query_txt in self._cache:
            videos = self._cache[query_txt]
        else:
            videos = search_download_youtube_video(query_txt)
            self._cache[query_txt] = videos
        self.send_text(update, f'the video you requested was downloaded to {videos[0]}')
        self.send_video(update, context, videos[0])


if __name__ == '__main__':
    with open('.telegramToken') as f:
        _token = f.read()

    my_bot = QuoteBot(_token)
    my_bot.start()

    youtube_bot = YoutubeBot(_token)
    youtube_bot.start()

