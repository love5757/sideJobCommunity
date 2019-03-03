import re
import os
import codecs

dirname = os.path.dirname(__file__)
#날짜알림줄 확인
def is_date(line):
    is_date_filter = re.compile("\d{4}년 \d{1,2}월 \d{1,2}일")
    date = is_date_filter.search(line)
    if date:
        date = date.group()
        date = date.replace(" ","-",3)
        return date
    return False

#메세지 시작줄 확인
def is_msg_start(line):
    msg_start_filter = re.compile("(\[.*\]) (\[\w{2} \d{1,2}:\d{1,2}\]) (.*)")
    start_line = msg_start_filter.match(line)
    if(start_line):
        name = start_line.group(1)
        time = start_line.group(2)
        start_line = start_line.group(3)
        return name, time, start_line
    return "","",""

#구인구직글인지 유효성 체크(단어 빈도수 높은순)
def check_content(content):
    filter = \
    ["개발","회사","경험","지원","업무","서비스","경력","개발자","근무","디자인","위치",\
    "프로젝트","구인","우대","협의","채용","페이","기획","디자이너","기술","서버","기간",\
    "업종","연봉","작업","문의","관리","관련","모집","연차"]

    if any(word in content for word in filter):
        return True
    return False

#email 찾기
def find_email(content):
    email_filter = re.compile("[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}")
    email = email_filter.search(content)
    if email :
        email = email_filter.search(content).group()
    return email

#연락처 찾기
def find_phone(content):
    phone_filter = re.compile("[0-9]{2,3}\b?([-|_|.|,|–]{1,3})\b?[0-9]{3,4}\b?([-|_|.|,|–]{1,3})\b?[0-9]{4}")
    phone = phone_filter.search(content)
    if phone :
        phone = phone.group()
        return phone

#URL 찾기
def find_url(content):
    url_filter = re.compile("(?:(?:https?|ftp|file|blog):\/\/|www\.|ftp\.|blog\.)(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[-A-Z0-9+&@#\/%=~_|$?!:,.])*(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[A-Z가-힣0-9+&@#\/%=~_|$?!:,.]*)", re.IGNORECASE | re.MULTILINE)
    url_list = url_filter.findall(content)
    return url_list

#TODO : datetime 형식으로 만들기
def make_datetime(date,time):
    pass

#TODO : kakao id 찾기
def find_kakao_id(content):
    pass

#TODO : 급여 찾기 ing 진행중
def find_price(content):
    price_filter = re.compile("(급여|금액|시급|페이|비용|연봉|페이 \(연봉 min max, 협상 여부\))\b?([:| ]*)?([가-힣0-9a-zA-Z| |,|-|\(|\)|~|.|/|:]*)")
    price = price_filter.search(content)
    if price :
        if "페이스" in price.group() : return
        if "페이지" in price.group() : return
        price = price.group(3)
        if not price :
            return ""
        return price

def data_save(data):
    #윈도우 파일 저장시 문제가 되는 부분을 걸러냄. test 용이기때문에 실제로는 필요없음
    name = re.sub("[?|:|<|>|*|\|\"|/|[|]|]","",data['name'])
    filename = os.path.join(dirname, "./parser_test/result/")
    if len(data['content']) < 100 and not check_content(data['content']):
        w_f = codecs.open(filename+"[x]%s_%s_.txt" % (data['date'],name),'w','utf-8')
    else :
        w_f = codecs.open(filename+"[o]%s_%s.txt" % (data['date'],name),'w','utf-8')

    content = "name : %s\n" % (data['name'])
    content += "title : %s\n" % (data['title'])
    email = find_email(data['content'])
    if email: content += "email : %s\n" % (email)

    phone = find_phone(data['content'])
    if phone: content += "phone : %s\n" % (phone)

    url_list = find_url(data['content'])
    if url_list:
        content += "url : \n"
        for url in url_list :
            content += "\t%s \n" % (url)

    kakao_id = find_kakao_id(data['content'])
    if kakao_id :
        content += "kakao id : %s" % (kakao_id)

    price = find_price(data['content'])
    if price :
        content += "price : %s\n" % (price)

    content += "content : \n %s" % data['content']
    w_f.write(content)
    w_f.close()

def is_ignore_line(line):
    ignore_lines = [
    "나갔습니다",
    "초대하였습니다.",
    "사이드 잡 양식입니다.",
    "위치 : 회사 명 및 위치 표기",
    "자택 여부 : (자택/회사)",
    "업종 : 디자인/기획/마케팅/개발",
    "페이 : 시간당, 페이지당, 일당, ...",
    "기간 : 1달, 2달, 프로잭트당",
    ]
    if any(ignore_line in line for ignore_line in ignore_lines):
        return True
    return False

def kakao_chat(file_path):
    filename = os.path.join(dirname, file_path)
    f = codecs.open(filename,'r','utf-8')
    data = {
    'title' : '',
    'date' : '',
    'time' : '',
    'name' : '',
    'content' : '',
    }

    start_line = ''
    lines = f.readlines()
    for line in lines:
        #초대 메시지 무시
        if is_ignore_line(line) : continue

        date_ret = is_date(line)
        if date_ret:
            if data['name']:
                data_save(data)
                data['name'] = ''
            data['date'] = date_ret
            continue

        name_ret, time_ret, start_line = is_msg_start(line)
        if name_ret :
            if data['name'] :
                #연속적인 글 이나 나눠 쓴경우 두 글을 합쳐줌.
                if data['name'] == name_ret :
                    data['content'] += start_line
                    continue
                data_save(data)
            data['name'] = name_ret
            data['time'] = time_ret
            data['title'] = start_line
            data['content'] = start_line
            continue
        if not data['title'] :
            data['title'] = line
        data['content'] += line
    f.close()

kakao_chat("./parser_test/source.txt")
