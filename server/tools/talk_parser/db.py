import pymysql as db
from utils import check_content, make_uid

def make_db_con():
    host = 'localhost'
    port = 3306
    user = 'manager'
    passwd = 'Javascript'
    db_name = 'sidejob_proj'
    try:
        return db.connect(host=host, port=port, user=user, passwd=passwd, db=db_name, charset='utf8mb4')
    except:
        print("DB Connect Fail")

def make_dic_cursor(con):
    return con.cursor(db.cursors.DictCursor)

def no_write():
    return "미기재"

def duplicate_msg(con, name, title, datetime):
    cur = make_dic_cursor(con)
    sql = """select writer_id from recruiting where title=%s and cdate=%s;"""
    cur.execute(sql, (title, datetime))
    recruits = cur.fetchall()
    if recruits :
        for rec in recruits:
            sql = """select * from writer where writer_id=%s;"""
            cur.execute(sql, rec['writer_id'])
            res = cur.fetchall()
            for writer in res:
                if name == writer['kakao_name']:
                    #print("already Posted Recruit")
                    cur.close
                    return True
    cur.close
    return False



def get_type(con, flag):
    if flag :
        type = 'side'
    else :
        type = 'job'
    try:
        cur = make_dic_cursor(con)
        sql = """select type_id from type where type=%s;"""
        cur.execute(sql, (type))
        res = cur.fetchone()
        cur.close()
        return res['type_id']

    except:
        cur = make_dic_cursor(con)
        type_id = make_uid()
        sql = """insert into `type` (`type_id`, `type`) values(%s, %s);"""
        cur.execute(sql,(type_id,type))
        con.commit()
        cur.close()
        return type_id

def get_company(con, comp, loca):
    cur = make_dic_cursor(con)
    if not comp and not loca: #회사명, 위치가 없는경우
        comp = no_write()
        loca = no_write()
        sql = """select * from company where name=%s and location=%s;"""
        cur.execute(sql, (comp,loca))
        res = cur.fetchone()
    elif comp and not loca: #회사명은 있으나 위치가 없는경우
        loca = no_write()
        sql = """select * from company where name=%s;"""
        cur.execute(sql, (comp))
        res = cur.fetchone()
    elif not comp and loca: #회사명은 없으나 위치가 있는경우
        comp = no_write()
        sql = """select * from company where location=%s;"""
        cur.execute(sql, (loca))
        res = cur.fetchone()
    else:#회사명과 위치가 있는경우
        sql = """select * from company where name=%s;"""
        cur.execute(sql, (comp))
        res = cur.fetchone()
        if res:
            _loca = res['location']
            if len(_loca) < len(loca):
                sql = """update company set location=%s where name=%s;"""
                cur.execute(sql, (loca, comp))
                con.commit()

    if res:
        comp_uid = res['comp_id']
        cur.close()
        return (comp_uid)

    cur.close()
    return False

def set_company(con, comp, loca):
    cur = make_dic_cursor(con)
    if not comp:
        comp = no_write()
    if not loca:
        loca = no_write()

    comp_uid = make_uid()
    sql = """insert into company(comp_id, name, location) values(%s, %s, %s);"""
    cur.execute(sql,(comp_uid,comp,loca))
    con.commit()
    cur.close()
    return comp_uid

def get_writer(con, k_id, k_name, email, phone):
    cur = make_dic_cursor(con)

    sql = """select * from writer where kakao_name=%s;"""
    cur.execute(sql, (k_name))
    res = cur.fetchone()
    if res:
        if res['kakao_id'] == no_write() and k_id:
            sql = """update writer set kakao_id=%s where kakao_name=%s;"""
            cur.execute(sql, (k_id, k_name))
        elif res['kakao_id'] != no_write() and k_id != res['kakao_id'] and k_id:
            pass
            #print("anothter id",k_id, res['kakao_id'])
            #raise ArithmeticError

        if res['email'] == no_write() and email:
            sql = """update writer set email=%s where kakao_name=%s;"""
            cur.execute(sql, (email, k_name))
        elif res['email'] != no_write() and email != res['email'] and email:
            pass
            #print("anothter email", email, res['email'])
            #raise ArithmeticError

        if res['phone'] != phone and phone:
            sql = """update writer set phone=%s where kakao_name=%s;"""
            cur.execute(sql, (phone, k_name))
        elif res['phone'] != no_write() and phone != res['phone'] and phone:
            pass
            #print("anothter phone", phone, res['phone'])
           # raise ArithmeticError
        cur.close()
        return res['writer_id']
    cur.close()
    return False

def set_writer(con, k_id, k_name, email, phone):
    cur = make_dic_cursor(con)
    if not k_id:
        k_id = no_write()
    if not email:
        email = no_write()
    if not phone:
        phone = no_write()

    writer_id = make_uid()
    sql = """insert into `writer` (`writer_id`, `kakao_id`, `kakao_name`, `email`, `phone`) values(%s, %s, %s, %s, %s);"""
    cur.execute(sql,(writer_id,k_id, k_name, email, phone))
    con.commit()
    return writer_id

def set_recruit(con, w_id, t_id, c_id, title, content, cdate):
    cur = make_dic_cursor(con)

    r_id = make_uid()

    sql = """insert into
    `recruiting` (`recr_id`,`writer_id`,`type_id`,`comp_id`,`title`,`content`,`hit`,`cdate`,`is_delete`)
    values(%s, %s, %s, %s, %s, %s, 0, %s, 0);"""

    cur.execute(sql, (r_id,w_id, t_id, c_id, title, content, cdate))
    con.commit()
    cur.close()
    return r_id

def set_detail(con, r_id, s_opt,skill, url, period, price, years, sec, f_h, detail):
    cur = make_dic_cursor(con)

    if not s_opt : s_opt = no_write()
    if not skill : skill = no_write()
    if not url : url = no_write()
    if not period : period = no_write()
    if not price : price = no_write()
    if not years : years = no_write()
    if not sec : sec = no_write()
    if not f_h : f_h = no_write()
    if not detail : detail = no_write()

    sql = """insert into
    `detail` (`recr_id`,`stock_opt`,`skill`,`url`,`period`,`price`,`years`,`sector`,`from_home`, `more_detail`)
    values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

    cur.execute(sql, (r_id, s_opt,skill, url, period, price, years, sec, f_h, detail))
    con.commit()
    cur.close()

def set_rating(con, r_id, merit):
    cur = make_dic_cursor(con)
    sql = """insert into `rating`
    values(%s, %s);"""
    cur.execute(sql, (r_id, merit[0]))
    con.commit()
    cur.close()
    pass

def save_data(data):

    if (len(data['content']) < 150 and data['matched'][0] == 0) or not check_content(data['content']):
        return

    con = make_db_con()

    if duplicate_msg(con, data['name'],data['title'],data['datetime']):
        return
    type_id = get_type(con, data['period'])

    comp_id = get_company(con, data['company'], data['location'])
    if not comp_id:
        comp_id = set_company(con, data['company'], data['location'])

    writer_id = get_writer(con, data['kakao_id'], data['name'], data['email'], data['phone'])
    if not writer_id:
        writer_id = set_writer(con, data['kakao_id'], data['name'], data['email'], data['phone'])

    recruit_id = set_recruit(con, writer_id, type_id, comp_id, data['title'],data['content'],data['datetime'])

    url = ','.join(data['url_list'])
    set_detail(con, recruit_id, data['stock_option'],data['skill'], url, data['period'], data['price'], data['years'], data['sector'], data['from_home'], data['more_detail'])
    set_rating(con, recruit_id, data['matched'])
    con.close()
