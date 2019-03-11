import sys

import requests
from requests.auth import HTTPBasicAuth
from six.moves.urllib.parse import urlparse

from fineract.exceptions import BadCredentialsException, ResourceNotFoundException, BadArgsException, FineractException

at_least_python3 = sys.hexversion >= 0x03000000


class RequestHandler:

    def __init__(self, username, password, base_url, tenant, timeout):
        self.__headers = {
            'Content-Type': 'application/json',
            'Fineract-Platform-TenantId': tenant
        }
        self.__locale = 'en'
        self.__date_format = 'yyyy-MM-dd'
        self.__auth = HTTPBasicAuth(username, password)
        self.__timeout = timeout
        o = urlparse(base_url)
        if o.scheme != 'https':
            assert False, 'A https scheme is required'

        self.__base_url = base_url if base_url[-1] == '/' else base_url + '/'

    def make_request(self, method, url, **kwargs):
        res = requests.request(method, url, **kwargs)
        if not res.ok:
            err_data = res.json()
            message = self.__create_err_message(err_data)
            raise self.__create_exception(res.status_code, message)
        else:
            return res.json()

    def __create_err_message(self, data):
        message = data['defaultUserMessage']
        if 'errors' in message:
            message += ' {}'.format([item['defaultUserMessage'] for item in data['errors']])
        return message

    def __create_exception(self, status, output):
        mappings = {
            '400': BadArgsException,
            '401': BadCredentialsException,
            '403': BadCredentialsException,
            '404': ResourceNotFoundException
        }
        cls = mappings.get(str(status), FineractException)

        return cls(status, output)

    @property
    def base_url(self):
        return self.__base_url
