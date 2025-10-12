import os
import sys
import logging

def setup_logger(name="PoultryDiseasesCNNLogger"):
    logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
    log_dir = "logs"
    log_filepath = os.path.join(log_dir, "running_logs.log")
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid adding handlers multiple times
    if not logger.handlers:
        file_handler = logging.FileHandler(log_filepath)
        stream_handler = logging.StreamHandler(sys.stdout)

        formatter = logging.Formatter(logging_str)
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger