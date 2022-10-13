import requests


def __send_request(method, url, params):
    if params is not None:
        return method(url, params)
    return method(url)


def post_request(url, params):
    request = __send_request(requests.post, url, params)
    return request


def get_request(url, params=None):
    request = __send_request(requests.get, url, params)
    return request


def put_request(url, params):
    request = __send_request(requests.put, url, params)
    return request


def patch_request(url, params):
    request = __send_request(requests.patch, url, params)
    return request


def delete_request(url, params=None):
    request = __send_request(requests.delete, url, params)
    return request
