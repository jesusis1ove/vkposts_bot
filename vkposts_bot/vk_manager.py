import logging

import vk_api
from vk_api import ApiError

from .utils import write_last_success_request


class VkManager:
    def __init__(self, vk_access_token, vk_login, vk_password, owners_id, counter_per_req):
        self.owners_id = owners_id
        self.counter_per_req = counter_per_req
        if vk_access_token != '':
            self.vk_session = vk_api.VkApi(token=vk_access_token)
        else:
            self.vk_session = vk_api.VkApi(login=vk_login, password=vk_password)
            self.vk_session.auth()

    def _get_latest_posts(self):
        vk = self.vk_session.get_api()
        response = []
        for owner in self.owners_id.keys():
            try:
                response.append(vk.wall.get(count=self.counter_per_req, owner_id=owner))
            except ApiError as e:
                logging.error(e)
        return response

    def get_updates(self, last_success_request, fields=None, attachments=True):
        latest_posts = self._get_latest_posts()
        write_last_success_request()
        result = []
        for owner_item in latest_posts:
            for item in owner_item["items"]:
                if item["marked_as_ads"] != 0:
                    continue
                if item["date"] < int(last_success_request):
                    continue
                if not "attachments" in item and attachments:
                    continue

                # body
                formed_post = dict()
                for field in item:
                    if field != 'attachments':
                        formed_post[field] = item[field]

                # additional
                if 'signer_id' in formed_post:
                    formed_post['signer_name'] = self.get_user_name_by_id(formed_post['signer_id'])
                if 'owner_id' in formed_post:
                    formed_post['owner_name'] = self.owners_id[formed_post['owner_id']]

                # attachments
                if attachments:
                    images = []
                    for attachment in item["attachments"]:
                        if attachment["type"] == "photo":
                            image = attachment["photo"]["sizes"][-1]["url"]
                            images.append(image)
                    if len(images) == 0:
                        continue
                    formed_post["attachments"] = images

                result.append(formed_post)

        result = sorted(result, key=lambda k: k['date'])
        return result

    def get_user_info_by_id(self, user_id, fields=None):
        return self.vk_session.method("users.get", {"user_id": user_id})

    def get_user_name_by_id(self, user_id):
        user_info = self.get_user_info_by_id(user_id)
        return "{} {}".format(user_info[0]["first_name"], user_info[0]["last_name"])
