from datetime import datetime, timedelta
import datetime
import logging.handlers

import logging.handlers

# logger 인스턴스를 생성 및 로그 레벨 설정
logger = logging.getLogger('SerialTime')
logger.setLevel(logging.DEBUG)

# formatter 생성
formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

# fileHandler 와 StreamHandler 를 생성
file_max_bytes = 10 * 1024 * 1024  # log file size : 10MB

fileHandler = logging.handlers.RotatingFileHandler(
    r"C:\dev_tenspace\2019_python_project_syhan\201901_python36\automation_for_data\log_data\generateTime_log", maxBytes=file_max_bytes, backupCount=10)

streamHandler = logging.StreamHandler()

# handler 에 formatter 세팅
fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)

# Handler 를 logging 에 추가
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)



def generateTimeSerial():
    dt = datetime.datetime(2019, 2, 11, 10, 4, 44)
    end = datetime.datetime(2019, 4, 12, 4, 34, 23)
    step = datetime.timedelta(seconds=67)

    result = []

    while dt < end:
        result.append(dt.strftime('%Y-%m-%d %H:%M:%S'))
        dt += step

    print(result)
    logger.debug(result)
    logger.debug("================================================")
    i = 0
    while i <= len(result)-1:
        logger.debug(result[i])
        i += 1

generateTimeSerial()
