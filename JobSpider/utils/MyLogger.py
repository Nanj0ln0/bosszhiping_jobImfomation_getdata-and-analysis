import os
import logging
from datetime import datetime


def MyLoggerInit(log_dir,log_prefix = "log"):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    name = "%s_%s.txt"%(log_prefix,datetime.now().strftime("%Y%m%d_%H%M%S"))

    filepath = os.path.join(log_dir,name)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    file_output = logging.FileHandler(filepath, encoding='utf-8')  # 指定utf-8格式编码，避免输出的日志文本乱码
    file_output.setLevel(logging.INFO)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    # 设置格式
    formatter = logging.Formatter('%(asctime)s %(module)s:%(lineno)s %(levelname)s %(message)s')

    file_output.setFormatter(formatter)
    console.setFormatter(formatter)

    logger.addHandler(file_output)
    logger.addHandler(console)

    logger.info("logfile=%s",filepath)

    return logger
