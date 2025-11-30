import logging


class FileLogger:
    def __init__(self, filename):
        self.filename = filename
        self.logger = logging.getLogger(filename)
        self.logger.setLevel(logging.INFO)
        self.handler = logging.FileHandler(filename, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt= '%d-%m-%Y %H:%M:%S')
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)

    def stop_logging(self):
        self.logger.removeHandler(self.handler)
        self.handler.close()

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warn(msg)

    def error(self, msg):
        self.logger.error(msg)