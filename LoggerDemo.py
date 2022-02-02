import logging

logging.basicConfig(filename="./Logs/automation.log", format='%(asctime)s :%(levelname)s : %(name)s :%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.setLevel(logging.ERROR)
logger.setLevel(logging.DEBUG)
logger.debug("This is debug message")
logger.info("This is info message")
