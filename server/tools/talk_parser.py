import re
import os
import codecs

dirname = os.path.dirname(__file__)

def data_save(data):
    #윈도우 파일 저장시 문제가 되는 부분을 걸러냄. test 용이기때문에 실제로는 필요없음
    name = re.sub("[?|:|<|>|*|\|\"|/|[|]|]","",data['name'])
    datetime = re.sub("[:| ]",".",data['datetime'])

    resultdir = os.path.join(dirname, "./parser_test/result/")
    try:
        if not(os.path.isdir(resultdir)):
            os.makedirs(os.path.join(resultdir))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise

    if len(data['content']) < 150 and not check_content(data['content']):
        w_f = codecs.open(resultdir+"[x]%s_%s_.txt" % (datetime,name),'w','utf-8')
    else :
        w_f = codecs.open(resultdir+"[o]%s_%s.txt" % (datetime,name),'w','utf-8')

    content = ""
    data['url_list'] = find_url(data['content'])
    data['email'] = find_email(data['content'])
    for name in data:
        if data[name]:
            if name == 'url_list':
                content += "url : \n"
                for url in data[name] :
                    content += "\t%s \n" % (url)
            else:
                content += "%s : %s\n" % (name, data[name])

    w_f.write(content)
    w_f.close()

#날짜알림줄 확인
def is_date(line):
    is_date_filter = re.compile("(\d{4})년 (\d{1,2})월 (\d{1,2})")
    date = is_date_filter.search(line)
    if date:
        y = int(date.group(1))
        m = int(date.group(2))
        d = int(date.group(3))
        date = "%4d-%02d-%02d" % (y,m,d)
        return date
    return False

#메세지 시작줄 확인
def is_msg_start(line):
    msg_start_filter = re.compile("\[(.*)\] \[(\w{2}) (\d{1,2}):(\d{1,2})\] (.*)")
    start_line = msg_start_filter.match(line)
    if(start_line):
        name = start_line.group(1)
        h = int(start_line.group(3))
        m = int(start_line.group(4))
        if start_line.group(2) == '오후' :
            h += 12
        time = "%02d:%02d:00" % (h,m)
        start_line = start_line.group(5)
        return name, time, start_line
    return "","",""

#구인구직글인지 유효성 체크(단어 빈도수 높은순)
def check_content(content):
    filter = \
    ["개발","회사","경험","지원","업무","서비스","경력","개발자","근무","디자인","위치",\
    "프로젝트","구인","우대","협의","채용","페이","기획","디자이너","기술","서버","기간",\
    "업종","연봉","작업","관리","관련","모집","연차"]

    if any(word in content for word in filter):
        return True
    return False

#email 찾기
def find_email(line):
    email_filter = re.compile("[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}")
    email = email_filter.search(line)
    if email :
        email = email_filter.search(line).group()
    return email

#연락처 찾기
def find_phone(line):
    phone_filter = re.compile("(\+82\-)?[0-9]{2,3}\b?([-|_|.|,|–]+)\b?[0-9]{3,4}\b?([-|_|.|,|–]+)\b?[0-9]{4}")
    phone = phone_filter.search(line)
    if phone :
        phone = phone.group()
        return phone

#URL 찾기
def find_url(line):
    url_filter = re.compile("(?:(?:https?|ftp|file|blog):\/\/|www\.|ftp\.|blog\.)(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[-A-Z0-9+&@#\/%=~_|$?!:,.])*(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[A-Z가-힣0-9+&@#\/%=~_|$?!:,.]*)", re.IGNORECASE | re.MULTILINE)
    url_list = url_filter.findall(line)
    return url_list

def make_datetime(date,time):
    return "%s %s" % (date,time)



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
    "구인구직 경우 입니다.",
    ]
    if any(ignore_line in line for ignore_line in ignore_lines):
        return True
    return False

def data_reset():
    data = {
    'title' : '',
    'datetime' : '',
    'name' : '',
    'company' : '',
    'stock_option' : '',
    'sector' : '',
    'years' : '',
    'skill' : '',
    'kakao_id' : '',
    'phone' : '',
    'email' : '',
    'url_list' : [],
    'price' : '',
    'location' : '',
    'period' : '',
    'content' : '',
    }
    return data

def make_filter(words,last_group=".+"):
    return re.compile("(%s)([:| |\-|\(|\=]*)(%s)" % (words,last_group))

def find_kakao_id(line):
    filter = make_filter("카카오|카카오톡|카톡|카카오톡ID|카카오톡id|kakao|KAKAO|카톡 ID|카카오톡 ID", "[A-Za-z0-9]{4,15}")
    kakao = filter.search(line)
    if kakao :
        kakao = kakao.group(3).lstrip()
        if len(kakao) > 3 :
            return kakao

def find_price(line):
    filter = make_filter("급여|금액|시급|페이 \(연봉 min max, 협상 여부\)|페이|비용|연봉")
    price = filter.search(line)
    if price :
        if not '페이지' in price.group() and not '페이스' in price.group() :
            price = price.group(3).strip()
            return price

def find_company(line) :
    filter = make_filter("회사명")
    company = filter.search(line)
    if company :
        company = company.group(3).lstrip()
        return company

def find_location(line) :
    filter = make_filter("위치")
    location = filter.search(line)
    if location :
        location = location.group(3).lstrip()
        return location

def find_stock_option(line) :
    filter = make_filter("스톡옵션 여부|스톡옵션")
    stock_option = filter.search(line)
    if stock_option :
        stock_option = stock_option.group(3).lstrip()
        return stock_option

def find_skill(line) :
    filter = make_filter("필요스킬|업무 상세 / 필요스킬")
    skill = filter.search(line)
    if skill :
        skill = skill.group(3).lstrip()
        return skill

def find_sector(line) :
    filter = make_filter("업종|업무|직무")
    sector = filter.search(line)
    if sector :
        sector = sector.group(3).lstrip()
        return sector

def find_period(line) :
    filter = make_filter("기간")
    period = filter.search(line)
    if period :
        period = period.group(3).lstrip()
        return period

def find_years(line) :
    filter = make_filter("구인 연차")
    years = filter.search(line)
    if years :
        years = years.group(3).lstrip()
        return years

def kakao_chat(file_path):
    filename = os.path.join(dirname, file_path)
    f = codecs.open(filename,'r','utf-8')

    start_line = ''
    lines = f.readlines()
    data = data_reset()
    date = ""
    time = ""
    for line in lines:
        #초대 메시지 무시
        if is_ignore_line(line) : continue

        date_ret = is_date(line)
        if date_ret:
            if data['name']:
                data_save(data)
                data = data_reset()
            date = date_ret
            continue

        name_ret, time_ret, start_line = is_msg_start(line)
        if name_ret :
            if data['name'] :
                #연속적인 글 이나 나눠 쓴경우 두 글을 합쳐줌.
                if data['name'] == name_ret :
                    data['content'] += start_line
                    continue
                data_save(data)
                data = data_reset()
            data['datetime'] = make_datetime(date, time_ret)
            data['name'] = name_ret.lstrip()
            data['title'] = start_line.lstrip()
            data['content'] = start_line.lstrip()
            continue


        if not data['title'] : data['title'] = line.lstrip()
        if not data['kakao_id'] : data['kakao_id'] = find_kakao_id(line)
        if not data['phone'] : data['phone'] = find_phone(line)
        if not data['price'] : data['price'] = find_price(line)
        if not data['company'] : data['company'] = find_company(line)
        if not data['location'] : data['location'] = find_location(line)
        if not data['stock_option'] : data['stock_option'] = find_stock_option(line)
        if not data['skill'] : data['skill'] = find_skill(line)
        if not data['sector'] : data['sector'] = find_sector(line)
        if not data['period'] : data['period'] = find_period(line)
        if not data['years'] : data['years'] = find_years(line)

        data['content'] += line

    f.close()

kakao_chat("./parser_test/source.txt")
