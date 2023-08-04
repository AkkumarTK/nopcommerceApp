import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        file_handler = logging.FileHandler('.\\Logs\\evidence.txt',)
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(message)s')
        file_handler.setFormatter(formatter)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        logging.getLogger().addHandler(file_handler)

        # the name will be set for each test step in 'pytest_bdd_before_step'
        logger = logging.getLogger("")
        return logger