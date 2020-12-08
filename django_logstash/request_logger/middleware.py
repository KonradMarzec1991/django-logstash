"""
Middleware module
"""
from datetime import datetime
import logging
import logstash


class LogstashLogger:
    """Middleware logger which sends data to ElasticSearch"""
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = self.create_logger()

    @staticmethod
    def create_logger():
        """Logger handles sending data to logstash"""
        logger = logging.getLogger('logstash')
        logger.setLevel(logging.INFO)
        logger.addHandler(logstash.TCPLogstashHandler('es', 5959, version=1))
        logger.addHandler(logging.StreamHandler())
        return logger

    @staticmethod
    def get_request_attrs(request):
        user = getattr(request, 'user')
        method = getattr(request, 'method')
        path = getattr(request, 'path')

        return user, method, path

    def __call__(self, request):
        response = self.get_response(request)
        user, method, path = self.get_request_attrs(request)

        time = datetime.utcnow().replace(microsecond=0).isoformat()
        status = response.status_code

        self.logger.info(f'{time} {user} {method} {path} {status}')
        return response
