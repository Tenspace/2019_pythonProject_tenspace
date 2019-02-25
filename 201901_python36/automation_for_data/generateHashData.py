import hashlib
import random
import csv
import requests
#

def generateInserQuery(listValues):

    insertValueList = []
    loopCnt = 0
    while(loopCnt != 11679):
        values = "" + numberGenerate(), platformGen(), random.choice(listValues), random.choice(listValues), \
                random.choice(listValues), random.choice(listValues), numberGenerate(), random.choice(listValues), random.choice(listValues), \
                random.choice(listValues), random.choice(listValues), random.choice(listValues), random.choice(listValues), random.choice(listValues), random.choice(listValues),\
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

def platformGen():
    platformList = ['facebook', 'kakaostory', 'instagram']
    return random.choice(platformList)


def numberGenerate():
    ranNum = "%0.12d" % random.randint(0, 999999999999)
    return str(ranNum)

def numberGenerate2():
    ranNum2 = "%0.2d" % random.randint(0, 99)

    return ranNum2

def alphabetGen():
    alphabetList = ['A', 'B', 'C', 'D']
    return random.choice(alphabetList)


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
    insert_command = """INSERT INTO facebook_score (
                 origin_ph, platform, page_id, username, gender, phone_number, birthday, address1, address2, address3,
                 company1, company2, company3, university1, university2, university3, contact1, contact2,
                 expression_negative, expression_positive, friends_all, friends_residence,
                 friends_company, friends_univ, friends_highschool, friends_native, take_news,
                 post_interest, post_up, feeling_cnt, following_cnt, follower_cnt, like_all_cnt,
                 like_movie_cnt, like_tv_cnt, like_music_cnt, like_book_cnt, like_sports_cnt,
                 like_athlete_cnt, like_restaurant_cnt, like_appgame_cnt, check_in, event, review,
                 like_cnt ,comment_cnt, share_cnt, place_cnt, place_add, post_cnt,
                 photo_of_oneself_cnt, photo_cnt, album_cnt, album_category_cnt, video_tag_oneself_cnt,
                 video_cnt, operation_year_period, friends_continuous_exchange, friends_rating_index,
                 friends_correlation_score, contents_regular
                 ) VALUES """ + generateInserQuery(hashValList)

    print(insert_command)

    with open('aster_7.sql', 'w') as out:
        out.write(insert_command)






#hashWordGenerate()



