import re

def make_filter(words,last_group=".+"):
    return re.compile("(%s)([:| |\-|\(|\=]*)(%s)" % (words,last_group))

#날짜알림줄 확인
def find_date(line):
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
def find_msg_start(line):
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

def find_ignore_line(line):
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

def find_kakao_id(line):
    filter = make_filter("카카오|카카오톡|카톡|카카오톡ID|카카오톡id|kakao|KAKAO|카톡 ID|카카오톡 ID", "[A-Za-z0-9]{4,15}")
    kakao = filter.search(line)
    if kakao :
        kakao = kakao.group(3).lstrip()
        if len(kakao) > 3 :
            return kakao

def find_price(line, matched):
    filter = make_filter("급여|금액|시급|페이 \(연봉 min max, 협상 여부\)|페이|비용|연봉")
    price = filter.search(line)
    if price :
        if not '페이지' in price.group() and not '페이스' in price.group() :
            price = price.group(3).strip()
            matched[0] += 1
            return price

def find_company(line, matched) :
    filter = make_filter("회사명")
    company = filter.search(line)
    if company :
        company = company.group(3).lstrip()
        matched[0] += 1
        return company

def find_location(line, matched) :
    filter = make_filter("위치")
    location = filter.search(line)
    if location :
        location = location.group(3).lstrip()
        matched[0] += 1
        return location

def find_stock_option(line, matched) :
    filter = make_filter("스톡옵션 여부|스톡옵션")
    stock_option = filter.search(line)
    if stock_option :
        stock_option = stock_option.group(3).lstrip()
        matched[0] += 1
        return stock_option

def find_skill(line, matched) :
    filter = make_filter("필요스킬|업무 상세 / 필요스킬")
    skill = filter.search(line)
    if skill :
        skill = skill.group(3).lstrip()
        matched[0] += 1
        return skill

def find_sector(line, matched) :
    filter = make_filter("업종|업무|직무")
    sector = filter.search(line)
    if sector :
        sector = sector.group(3).lstrip()
        matched[0] += 1
        return sector

def find_period(line, matched) :
    filter = make_filter("기간")
    period = filter.search(line)
    if period :
        period = period.group(3).lstrip()
        matched[0] += 1
        return period

def find_years(line, matched) :
    filter = make_filter("구인 연차")
    years = filter.search(line)
    if years :
        years = years.group(3).lstrip()
        matched[0] += 1
        return years

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
