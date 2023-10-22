import logging


class Logger:
    @staticmethod
    def sample_logger():
        logger = logging.getLogger('custom_logger')
        logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter(fmt="%(asctime)s | %(levelname)s | %(message)s | %(module)s",
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        fh = logging.FileHandler(filename="Logs/logs.log", mode='a')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger


# if __name__ == '__main__':
#     logger1 = Logger.sample_logger()
#     logger1.info("This is the 2nd statement")
#     logger1.error("This is the 2nd statement")
#     logger1.debug("This is the 3rd statement")
#     logger1.warning("This is the 4th statement")
