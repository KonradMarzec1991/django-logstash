"""
Middleware module
"""
import logging
from datetime import datetime

LOG = logging.getLogger('django-logstash')


class LogstashLogger:
    """Middleware logger which sends data to ElasticSearch"""
    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def get_request_attrs(request):
        user = getattr(request, 'user')
        method = getattr(request, 'method').upper()
        path = getattr(request, 'get_full_path')()
        return user, method, path

    def __call__(self, request):
        response = self.get_response(request)
        user, method, path = self.get_request_attrs(request)

        time = datetime.utcnow().replace(microsecond=0).isoformat()
        status = response.status_code

        LOG.info(f'{time} {user} {method} {path} {status}')
        return response
