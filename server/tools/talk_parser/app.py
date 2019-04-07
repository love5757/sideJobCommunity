import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import re
import os
import codecs
from talk_parser import find_url, find_date, find_years, find_email, find_skill, \
                find_price, find_phone, find_sector, find_period, find_company,\
                find_location, find_kakao_id, find_msg_start, find_ignore_line,\
                find_stock_option, find_work_from_home
from utils import make_datetime, data_reset
from db import save_data

"""
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
    w_f.write(content)
    w_f.close()
"""



def talk_parser(file="..\parser_test\source.txt"):
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, file)
    f = codecs.open(filepath,'r','utf-8')

    start_line = ''
    lines = f.readlines()
    data = data_reset()
    date = ""
    time = ""
    for line in lines:
        #초대 메시지 무시
        line = line.rstrip('\n')
        if find_ignore_line(line) : continue

        date_ret = find_date(line)
        if date_ret:
            if data['name']:
                data['url_list'] = find_url(data['content'])
                data['email'] = find_email(data['content'])
                save_data(data)
                data = data_reset()
            date = date_ret
            continue

        name_ret, time_ret, start_line = find_msg_start(line)
        if name_ret :
            if data['name'] :
                #연속적인 글 이나 나눠 쓴경우 두 글을 합쳐줌.
                if data['name'] == name_ret :
                    data['content'] += start_line
                    continue
                data['url_lidst'] = find_url(data['content'])
                data['email'] = find_email(data['content'])
                save_data(data)
                data = data_reset()
            data['datetime'] = make_datetime(date, time_ret)
            data['name'] = name_ret.lstrip()
            line = start_line.lstrip()

        if not data['title'] : data['title'] = line[:149]
        if not data['kakao_id'] : data['kakao_id'] = find_kakao_id(line)
        if not data['phone'] : data['phone'] = find_phone(line)
        if not data['price'] : data['price'] = find_price(line, data['matched'])
        if not data['company'] : data['company'] = find_company(line, data['matched'])
        if not data['location'] : data['location'] = find_location(line, data['matched'])
        if not data['stock_option'] : data['stock_option'] = find_stock_option(line, data['matched'])
        if not data['skill'] : data['skill'] = find_skill(line, data['matched'])
        if not data['sector'] : data['sector'] = find_sector(line, data['matched'])
        if not data['period'] : data['period'] = find_period(line, data['matched'])
        if not data['years'] : data['years'] = find_years(line, data['matched'])
        if not data['from_home'] : data['from_home'] = find_work_from_home(line, data['matched'])

        data['content'] += line

    f.close()

if __name__ == "__main__":
    talk_parser()
#kakao_chat("./parser_test/source.txt")
