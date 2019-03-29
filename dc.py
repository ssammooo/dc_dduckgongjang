from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import time
import random

def img_down(m, postnum, title, idx, keyword) :
    href = m.a.get("href")
    href = "http://gall.dcinside.com" + href

    html = urlopen(href).read()
    soup = BeautifulSoup(html, 'html.parser')

    # href 퍼오기 물밑작업
    link2 = soup.find_all("ul", {"class": "appending_file"})
    file_link = list()
    cnt = 0

    for i in link2:
        print("post_num = " + postnum)
        print("title = " + title)
        li = i.find_all('li')

        for j in li:
            print('filename = ' + j.a.text)
            file_link.append(j.a.get('href'))

            # 다운로드 링크 replace
            a = 'https://image.dcinside.com/download.php'
            b = 'https://dcimg8.dcinside.co.kr/viewimage.php'
            file_link_rename = file_link[cnt].replace(a, b)

            img_file = urlopen(file_link_rename)

            # 현재 디렉토리 안에서 img폴더 생성
            if not os.path.isdir("./" + keyword + "/"):
                os.mkdir("./"+ keyword +"/")

            # 중복 오버라이트 방지
            now = time.localtime()
            pre_time = \
                str(now.tm_mday) + \
                str(now.tm_hour) + \
                str(now.tm_min) + \
                str(now.tm_sec)

            # 확장자 슬라이스
            extension = j.a.text
            file_extension = extension[-10:-1] + extension[len(extension) - 1]
            random_d = random.randrange(1,5930)

            if extension == '.gif' :
                pass

            f = open("./" + keyword + "/" +
                     pre_time + "_" + str(idx) + "(" +
                     str(random_d) + ")" + file_extension, "wb")
            f.write(img_file.read())

            cnt += 1
    print("(" + href + ")")

def area1(title, m, postnum, idx) :
    # 제목 키워드
    if '워' in title:
        img_down(m, postnum, title, idx, "워너원")
    elif '레' in title:
        img_down(m, postnum, title, idx, "레드벨벳")
    elif '세' in title:
        img_down(m, postnum, title, idx, "김세정")
    elif '희' in title:
        img_down(m, postnum, title, idx, "김소희")
    elif '성' in title:
        img_down(m, postnum, title, idx, "하성운")
    elif '위' in title:
        img_down(m, postnum, title, idx, "위키미키")
    elif '검' in title:
        img_down(m, postnum, title, idx, "박보검")
    elif '붐' in title:
        img_down(m, postnum, title, idx, "라붐")
    elif '친' in title:
        img_down(m, postnum, title, idx, "여친")
    elif '앤' in title:
        img_down(m, postnum, title, idx, "온앤오프")
    elif '호' in title:
        img_down(m, postnum, title, idx, "강동호")
    elif '피' in title:
        img_down(m, postnum, title, idx, "인피니트")
    elif 'e' in title:
        img_down(m, postnum, title, idx, "EXID")
    elif 'E' in title:
        img_down(m, postnum, title, idx, "EXID")
    elif 'k' in title:
        img_down(m, postnum, title, idx, "아이콘")
    elif 'K' in title:
        img_down(m, postnum, title, idx, "아이콘")
    elif '아' in title:
        img_down(m, postnum, title, idx, "아이콘")
    else:
        pass

# 배진영, 윤지성, 러블리즈, 조이, 정세운, 원더걸스, 프리스틴, 이의진,
# 포르테디콰, 정승환, 이대휘, txt, 이해인, 유선호, 비투비, 이새롬
def area2(title, m, postnum, idx) :
    if '배' in title:
        img_down(m, postnum, title, idx, "배진영")
    elif '윤' in title:
        img_down(m, postnum, title, idx, "윤지성")
    elif '블' in title:
        img_down(m, postnum, title, idx, "러블리즈")
    elif '조' in title:
        img_down(m, postnum, title, idx, "조이")
    elif '세' in title:
        img_down(m, postnum, title, idx, "정세운")
    elif '걸' in title:
        img_down(m, postnum, title, idx, "메이드인원더걸스")
    elif '프' in title:
        img_down(m, postnum, title, idx, "프리스틴")
    elif '의' in title:
        img_down(m, postnum, title, idx, "이의진")
    elif '콰' in title:
        img_down(m, postnum, title, idx, "포디콰")
    elif '환' in title:
        img_down(m, postnum, title, idx, "정승환")
    elif '휘' in title:
        img_down(m, postnum, title, idx, "이머휘")
    elif 't' in title:
        img_down(m, postnum, title, idx, "TXT")
    elif 'T' in title:
        img_down(m, postnum, title, idx, "TXT")
    elif '해' in title:
        img_down(m, postnum, title, idx, "이해인")
    elif '유' in title:
        img_down(m, postnum, title, idx, "유선호")
    elif '투' in title:
        img_down(m, postnum, title, idx, "비투비")
    elif '롬' in title:
        img_down(m, postnum, title, idx, "이새롬")
    else:
        pass

# 태민, 임나영, 아스트로, 김재환, 엔플라잉, 오마이걸, 뉴이스트, 하이라이트, 모모랜드
# 민경훈, 로이킴, 김준수, 황치열, 아이들, 옹성우, 다이아, 송민호
def area3(title, m, postnum, idx) :
    if '태' in title:
        img_down(m, postnum, title, idx, "태민")
    elif '나' in title:
        img_down(m, postnum, title, idx, "임나영")
    elif '아.스' in title:
        img_down(m, postnum, title, idx, "아스트로")
    elif '아/스' in title:
        img_down(m, postnum, title, idx, "아스트로")
    elif '환' in title:
        img_down(m, postnum, title, idx, "김재환")
    elif '플' in title:
        img_down(m, postnum, title, idx, "엔플라잉")
    elif '걸' in title:
        img_down(m, postnum, title, idx, "오마이걸")
    elif '뉴' in title:
        img_down(m, postnum, title, idx, "뉴이스트")
    elif '하' in title:
        img_down(m, postnum, title, idx, "하이라이트")
    elif '랜' in title:
        img_down(m, postnum, title, idx, "모모랜드")
    elif '훈' in title:
        img_down(m, postnum, title, idx, "민경훈")
    elif '킴' in title:
        img_down(m, postnum, title, idx, "로이킴")
    elif '준' in title:
        img_down(m, postnum, title, idx, "김준수")
    elif '치' in title:
        img_down(m, postnum, title, idx, "황치열")
    elif '들' in title:
        img_down(m, postnum, title, idx, "아이들")
    elif '옹' in title:
        img_down(m, postnum, title, idx, "옹성우")
    elif '다' in title:
        img_down(m, postnum, title, idx, "다이아")
    elif '송' in title:
        img_down(m, postnum, title, idx, "송민호")
    else:
        pass

# 에이프릴, hot, 국카스텐, 포레스텔라, 남태현, 박우진, 정채연, 위너, 최민기
# 안형섭, 휘성, 마마무, 임영민, 우주소녀, 에버글로우, 체리블렛, itzy
def area4(title, m, postnum, idx) :
    if '릴' in title:
        img_down(m, postnum, title, idx, "에이프릴")
    elif 'h' in title:
        img_down(m, postnum, title, idx, "HOT")
    elif 'H' in title:
        img_down(m, postnum, title, idx, "HOT")
    elif '텐' in title:
        img_down(m, postnum, title, idx, "국카스텐")
    elif '텔' in title:
        img_down(m, postnum, title, idx, "포터스텔라")
    elif '태' in title:
        img_down(m, postnum, title, idx, "남태현")
    elif '진' in title:
        img_down(m, postnum, title, idx, "박우진")
    elif '채' in title:
        img_down(m, postnum, title, idx, "정채연")
    elif '위' in title:
        img_down(m, postnum, title, idx, "위너")
    elif '최' in title:
        img_down(m, postnum, title, idx, "최민기")
    elif '안' in title:
        img_down(m, postnum, title, idx, "안형섭")
    elif '휘' in title:
        img_down(m, postnum, title, idx, "휘성")
    elif '마' in title:
        img_down(m, postnum, title, idx, "마마무")
    elif '영' in title:
        img_down(m, postnum, title, idx, "임영민")
    elif '녀' in title:
        img_down(m, postnum, title, idx, "우주소녀")
    elif '글' in title:
        img_down(m, postnum, title, idx, "에버글로우")
    elif '체' in title:
        img_down(m, postnum, title, idx, "체리블렛")
    elif 'z' in title:
        img_down(m, postnum, title, idx, "ITZY")
    elif 'Z' in title:
        img_down(m, postnum, title, idx, "ITZY")
    else:
        pass

# got7, 라이관린, 청하, 강승윤, 보아, 딕펑스, 정동하, 김사무엘, 이달의소녀
# 프로미스나인, 구구단, iu, 김도아, 김태우, day6, 2ne1, 젝스키스
def area5(title, m, postnum, idx) :
    if 't' in title:
        img_down(m, postnum, title, idx, "GOT7")
    elif 'T' in title:
        img_down(m, postnum, title, idx, "GOT7")
    elif '관' in title:
        img_down(m, postnum, title, idx, "라이관린")
    elif '청' in title:
        img_down(m, postnum, title, idx, "청하")
    elif '윤' in title:
        img_down(m, postnum, title, idx, "강승윤")
    elif '보' in title:
        img_down(m, postnum, title, idx, "보아")
    elif '딕' in title:
        img_down(m, postnum, title, idx, "딕펑스")
    elif '정' in title:
        img_down(m, postnum, title, idx, "정동하")
    elif '엘' in title:
        img_down(m, postnum, title, idx, "김사무엘")
    elif '녀' in title:
        img_down(m, postnum, title, idx, "이달의소녀")
    elif '로' in title:
        img_down(m, postnum, title, idx, "프로미스나인")
    elif '단' in title:
        img_down(m, postnum, title, idx, "구구단")
    elif '유' in title:
        img_down(m, postnum, title, idx, "아이유")
    elif 'u' in title:
        img_down(m, postnum, title, idx, "아이유")
    elif 'U' in title:
        img_down(m, postnum, title, idx, "아이유")
    elif '도' in title:
        img_down(m, postnum, title, idx, "김도아")
    elif '태' in title:
        img_down(m, postnum, title, idx, "언더나인틴김태우")
    elif 'd' in title:
        img_down(m, postnum, title, idx, "DAY6")
    elif 'D' in title:
        img_down(m, postnum, title, idx, "DAY6")
    elif 'n' in title:
        img_down(m, postnum, title, idx, "2NE1")
    elif 'N' in title:
        img_down(m, postnum, title, idx, "2NE1")
    elif '젝' in title:
        img_down(m, postnum, title, idx, "젝스키스")
    else:
        pass

# 황민현, 박지훈, 블랙핑크, 스트레이키즈, 김종현(JR), jbj95, 태연
def area6(title, m, postnum, idx) :
    if '황' in title:
        img_down(m, postnum, title, idx, "황민현")
    elif '지' in title:
        img_down(m, postnum, title, idx, "박지훈")
    elif '블' in title:
        img_down(m, postnum, title, idx, "블랙핑크")
    elif '스' in title:
        img_down(m, postnum, title, idx, "스트레이키즈")
    elif '종' in title:
        img_down(m, postnum, title, idx, "김종현")
    elif 'j' in title:
        img_down(m, postnum, title, idx, "JBJ95")
    elif 'J' in title:
        img_down(m, postnum, title, idx, "JBJ95")
    elif '태' in title:
        img_down(m, postnum, title, idx, "태연")
    else:
        pass


def crawling(gall_id, page, area):
    url = 'http://gall.dcinside.com/mgallery/board/lists?id=' +\
          gall_id + "&page=" + page +'&search_head=' + area
    #url = 'https://gall.dcinside.com/mgallery/board/lists/?id=noraeinjeung'
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    link = soup.find_all("tr", {"class" : "ub-content us-post"})

    idx = 1

    for m in link :
        if m.find("em", {"class" : "icon_survey"}) :
            pass
        elif m.find("em", {"class" : "icon_notice"}) :
            pass

        # 짤방있는것만 크롤링
        elif m.find("em", {"class" : "icon_pic"}) :
            postnum = m.find("td", {"class" : "gall_num"}).text
            title = m.a.text

            if area == '10' :
                area1(title, m, postnum, idx)
            elif area == '20' :
                area2(title, m, postnum, idx)
            elif area == '30':
                area3(title, m, postnum, idx)
            elif area == '40' :
                area4(title, m, postnum, idx)
            elif area == '50':
                area5(title, m, postnum, idx)
            elif area == '60':
                area6(title, m, postnum, idx)

        idx += 1


if __name__=="__main__":

    # 1구역 : 10
    # gid, 끝 page, area 순
    print("************** 떡 모 으 미 **************")
    print("**********저장경로=실행파일경로**********")
    print("**************자짤 구별못함**************")

    #gid = input("갤러리 id (기본값 : noraeinjeung, 기본값시 그냥 엔터) : ")
    gid = ""
    area = input("구역(1,2,3,4,5,6) : ")
    page = int(input("마지막페이지(해당구역탭의 마지막페이지) : "))
    area = area + '0'

    if gid == "" :
        gid = 'noraeinjeung'

    for i in range(page, 0, -1) :
        crawling(gid, str(i), area)
