import logging

import telebot


class TelegramManager:
    def __init__(self, token, channel_id, timeout):
        self.channel_id = channel_id
        self.timeout = timeout
        self.bot = telebot.TeleBot(token)

    def create_post(self, body, attachments):
        try:
            # если длина текста до 1024, постим с вложением одним сообщением (текст тут - описание первого вложения)
            # иначе текст одним постом, вложение реплаем
            if len(body) <= 1024:
                first_attachment_with_caption = telebot.types.InputMediaPhoto(attachments[0], body, 'HTML')
                attachments[:] = [telebot.types.InputMediaPhoto(x) for x in attachments]
                attachments[0] = first_attachment_with_caption
                self.bot.send_media_group(self.channel_id, attachments)
            else:
                attachments[:] = [telebot.types.InputMediaPhoto(x) for x in attachments]
                message = self.bot.send_message(self.channel_id, body, parse_mode='HTML')
                # time.sleep(5)
                self.bot.send_media_group(self.channel_id, attachments, True, message.id)
        except Exception as e:
            logging.error('Exception: {}\nlen(body): {}, len(attachments): {}'.format(e, len(body), len(attachments)))


