import logging
import logstash


class LogstashLogger:

    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = self.create_logger()

    @staticmethod
    def create_logger():
        logger = logging.getLogger('logstash')
        logger.setLevel(logging.INFO)
        logger.addHandler(logstash.TCPLogstashHandler('es', 5959, version=1))
        return logger

    def __call__(self, request):
        return self.get_response(request)