import pymysql as db
from utils import check_content

def make_db_con():
    host = 'localhost'
    port = 3306
    user = 'manager'
    passwd = 'Javascript'
    db_name = 'sidejob_proj'
    try:
        conn = db.connect(host=host, port=port,
        user=user, passwd=passwd, db=db_name, charset='utf8')
        cur = conn.cursor()
        return cur
    except:
        print("DB Connect Fail")

def save_data(data):
    if len(data['content']) < 150 and not check_content(data['content']):
        return
    else :
        con = make_db_con()
        print(data['sector'])


if __name__ == '__main__':
    make_db_con()
