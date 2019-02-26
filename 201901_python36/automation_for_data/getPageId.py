import logging
import logging.handlers
from datetime import datetime

import pymysql

now = datetime.now()
currentTime = '%s_%s_%s' % (now.year, now.month, now.day)
# logger 인스턴스를 생성 및 로그 레벨 설정
logger = logging.getLogger('kakaoStory_pageID_logging')
logger.setLevel(logging.DEBUG)

# formatter 생성
formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

# fileHandler 와 StreamHandler 를 생성
file_max_bytes = 10 * 1024 * 1024  # log file size : 10MB

fileHandler = logging.handlers.RotatingFileHandler(
    # kakaoStory_pageID
    r"C:\dev_tenspace\2019_python_project_syhan\201901_python36\automation_for_data\log_data\kakaoStory_pageID_log_"
    + currentTime, maxBytes=file_max_bytes, backupCount=10)

streamHandler = logging.StreamHandler()

# handler 에 formatter 세팅
fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)

# Handler 를 logging 에 추가
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

class GetPageID:

    def __init__(self):
        try:
            self.connection = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='1234',
                db='aster',
                charset='utf8mb4')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print('DB connection completed')

        except Exception as e:
            print('Cannot connect to Database: ', e)

    def getPageID_from_facebook(self):

        return

    def getPageID_from_kakaostory(self):
        try:
            select_sql = 'SELECT search_log_mobile, ' \
                                'search_log_kakaotalk_name, ' \
                                'search_log_real_name, ' \
                                'search_log_kakaostory_url, ' \
                                'search_log_kakaostory_id ' \
                         'FROM search_log ' \
                         'WHERE search_log_kakaotalk_name IS NOT NULL'

            self.cursor.execute(select_sql)
            #self.cursor.executemany()

            # 데이타 Fetch
            rows = self.cursor.fetchall()
            print(rows)  # 전체 rows

            for row in rows:
                logging.debug('search_log_mobile    search_log_real_name    search_log_kakaotalk_name   search_log_kakaostory_url')

                if row[3] is '' or row[3] is None:
                    logger.debug('No KakaoStory URL, =SKIP=')
                else:
                    logger.debug('{}, {}, {}, {}'.format(row[0], row[2], row[1], row[3]))

            # Connection 닫기
            self.connection.close()
        except Exception as e:
            print('getPageID_from_facebook execution error', e)

    def getPageID_from_instagram(self):

        return


getDataClass = GetPageID()
getDataClass.getPageID_from_kakaostory()