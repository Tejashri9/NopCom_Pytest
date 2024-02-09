import logging
import inspect

class LoggenClass:
    @staticmethod
    def log_generator():
        log_name = inspect.stack()[1][3] # runtime -getting filepath -class -method
        logger = logging.getLogger(log_name)  # gen logs
        logfile = logging.FileHandler("C:\\Users\\TEJASHRI\\Downloads\\nopcom class2 -feb2\\Logs\\log")
        log_format = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s ")
        logfile.setFormatter(log_format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger
