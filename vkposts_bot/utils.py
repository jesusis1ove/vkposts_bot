import time


def get_last_success_request():
    with open('vkposts_bot/last_success_request.txt', 'r') as f:
        last_success_request = f.readline()
        if last_success_request == '':
            return time.time()
        return last_success_request


def write_last_success_request():
    with open('vkposts_bot/last_success_request.txt', 'w') as f:
        f.write(str(int(time.time())))
