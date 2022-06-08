import logging
import time

from vkposts_bot.tg_manager import TelegramManager
from vkposts_bot.vk_manager import VkManager
from vkposts_bot.utils import get_last_success_request

from config import VK_ACCESS_TOKEN, VK_LOGIN, VK_PASSWORD, OWNERS_ID, COUNTER_PER_REQ, TAGS, \
    POST_HTML_TEMPLATE, ATTACHMENTS, MAIN_TIMEOUT, TG_TOKEN, CHANNEL_ID, TG_REQUEST_TIMEOUT


logging.basicConfig(filename='app.log',
                    level=logging.INFO,
                    format=f"%(asctime)s - [%(levelname)s] - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")


def start():
    vk = VkManager(VK_ACCESS_TOKEN, VK_LOGIN, VK_PASSWORD, OWNERS_ID, COUNTER_PER_REQ)
    tg = TelegramManager(TG_TOKEN, CHANNEL_ID, TG_REQUEST_TIMEOUT) # нахуя tg req timeout
    while True:
        last_success_request = get_last_success_request()
        vk_posts = vk.get_updates(last_success_request, attachments=ATTACHMENTS)
        logging.info('post count: {}'.format(len(vk_posts)))
        for post in vk_posts:
            tg.create_post(get_post_html_body(post), post['attachments'])
            time.sleep(TG_REQUEST_TIMEOUT)
        time.sleep(MAIN_TIMEOUT)
        

def get_post_html_body(post):
    post_html = POST_HTML_TEMPLATE
    for key, value in post.items():
        if post_html.find(key) >= 0:
            post_html = post_html.replace('%' + key, str(value))
    if len(TAGS) > 0:
        tag_list = get_tag_list(post['text'])
        post_html = post_html + '\n\n' + ' '.join(tag_list)
    return post_html


def get_tag_list(post_body):
    tag_list = []
    post_body = post_body.lower()
    for tag in TAGS.keys():
        if not post_body.find(tag) == -1:
            tag_list.append(TAGS[tag])
    return tag_list


if __name__ == '__main__':
    start()



