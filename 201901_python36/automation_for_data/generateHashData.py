import hashlib
import random
import csv
import requests
from datetime import datetime, timedelta
import datetime
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


def generateInserQuery(listValues):

    insertValueList = []
    loopCnt = 0
    returnTimeStamp = generateTimeSerial()
    while(loopCnt != 17670):
        values = "" + returnTimeStamp[loopCnt], numberGenerate(), platformGen(), random.choice(listValues), random.choice(listValues), \
                random.choice(listValues), random.choice(listValues), numberGenerate(), random.choice(listValues), random.choice(listValues), \
                random.choice(listValues), random.choice(listValues), random.choice(listValues), random.choice(listValues), \
                random.choice(listValues), random.choice(listValues),\
                random.choice(listValues), random.choice(listValues), random.choice(listValues), numberGenerate2(),\
                numberGenerate2(), numberGenerate(), numberGenerate(), numberGenerate(),\
                numberGenerate(), numberGenerate(), numberGenerate(), '', '',\
                '', '', '', numberGenerate(), numberGenerate(), numberGenerate(),\
                numberGenerate(), numberGenerate(), numberGenerate(), numberGenerate(),\
                numberGenerate(), numberGenerate(), numberGenerate(),\
                numberGenerate(), numberGenerate(), numberGenerate(), numberGenerate(), numberGenerate(), numberGenerate(), '',\
                numberGenerate(), numberGenerate(), numberGenerate(), numberGenerate(), numberGenerate(),\
                numberGenerate(), numberGenerate(), numberGenerate(),\
                numberGenerate(), numberGenerate(),\
                numberGenerate(), numberGenerate(), numberGenerate(), numberGenerate2(), numberGenerate2(), numberGenerate2(), alphabetGen() + ""
        loopCnt += 1
        insertValueList.append(values)

    return str(insertValueList).replace('[', '').replace(']', '')


# def hashWordGenerate1():
#     word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
#
#     response = requests.get(word_site)
#     WORDS = response.content.splitlines()
#     hashList = []
#
#     with open('hashVal3.csv', 'w') as writeFile:
#         for eachWord in WORDS:
#             hash2 = hashlib.md5(eachWord).hexdigest()
#             writeFile.write(hash2 + '\n')
#
#     writeFile.close()
#


def generateTimeSerial():
    dt = datetime.datetime(2019, 2, 11)
    end = datetime.datetime(2019, 4, 12, 4, 34, 23)
    step = datetime.timedelta(seconds=118)

    result = []

    while dt < end:
        result.append(dt.strftime('%Y-%m-%d %H:%M:%S'))
        dt += step

    logger.debug(result)
    return result



def platformGen():
    platformList = ['facebook', 'kakaostory', 'instagram']
    return random.choice(platformList)


def numberGenerate():
    ranNum = "%0.12d" % random.randint(0, 999999999999)
    return str(ranNum)

def numberGenerate2():
    ranNum2 = "%0.2d" % random.randint(0, 99)

    return str(ranNum2)

def alphabetGen():
    # alphabetList = ['A', 'B', 'C', 'D']
    # return random.choice(alphabetList)
    import numpy as np
    DICT_VAR = {'A': 500, 'B': 1000, 'C': 5000, 'D': 8000}

    keys, weights = zip(*DICT_VAR.items())
    probs = np.array(weights, dtype=float) / float(sum(weights))
    # sample_np = np.random.choice(keys, 2, p=probs)
    sample_np = np.random.choice(keys, 1, p=probs)
    sample = [str(val) for val in sample_np]

    #print(str(sample).replace('[', '').replace(']', ''))
    return str(sample).replace('[\'', '').replace('\']', '')

def hashWordGenerate2():
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    hashList = []


    for eachWord in WORDS:
        hash2 = hashlib.md5(eachWord).hexdigest()
        #writeFile.write(hash2 + '\n')
        hashList.append(hash2)


    return hashList



if __name__ == '__main__':

    #1. 기본 실행
    hashValList = hashWordGenerate2()

    #print(random.choice(hashValList))
    #b75c360edbcc27b6e659f9a3786f7aac

    #2. 쿼리 생성 실행
    #print(generateInserQuery(hashValList))
    insert_command = """INSERT INTO crawler_score (
                 insertedTime, origin_ph, platform, page_id, username, gender, phone_number, birthday, address1, address2, address3,
                 company1, company2, company3, university1, university2, university3, contact1, contact2,
                 expression_negative, expression_positive, friends_all, friends_residence,
                 friends_company, friends_univ, friends_highschool, friends_native, take_news,
                 post_interest, post_up, feeling_cnt, following_cnt, follower_cnt, like_all_cnt,
                 like_movie_cnt, like_tv_cnt, like_music_cnt, like_book_cnt, like_sports_cnt,
                 like_athlete_cnt, like_restaurant_cnt, like_appgame_cnt, check_in, event, review,
                 like_cnt ,comment_cnt, share_cnt, place_cnt, place_add, post_cnt,
                 photo_of_oneself_cnt, photo_cnt, album_cnt, album_category_cnt, video_tag_oneself_cnt,
                 video_cnt, operation_year_period, friends_continuous_exchange, friends_rating_index,
                 friends_correlation_score, contents_regular, tscore, cscore, mscore, user_rate
                 ) VALUES """ + generateInserQuery(hashValList)

    print(insert_command)

    with open('aster_20190306.sql', 'w') as out:
        out.write(insert_command)






#hashWordGenerate()



