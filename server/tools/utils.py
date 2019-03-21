import uuid

def make_uid():
    return str(uuid.uuid4()).replace("-","",4)

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
    'from_home' : '',
    'period' : '',
    'content' : '',
    'category' : '',
    'more_detail' : '',
    'matched' : [0]
    }
    return data

def make_datetime(date,time):
    return "%s %s" % (date,time)

#구인구직글인지 유효성 체크(단어 빈도수 높은순)
def check_content(content):
    filter = \
    ["개발","회사","지원","업무","서비스","경력","개발자","근무","디자인","위치",\
    "프로젝트","구인","우대","협의","채용","페이","기획","디자이너","기술","기간",\
    "업종","연봉","작업","관리","관련","모집","연차"]

    if any(word in content for word in filter):
        return True
    return False

if __name__ == '__main__':
    test = make_uid()
