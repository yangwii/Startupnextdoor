import requests
import time
import MySQLdb


con = MySQLdb.connect(host='10.255.209.33', user='root', passwd='root', db='test', charset='gbk')
cusor = con.cursor()

sql_str = '''insert into zirooms(resblock_name
,usage_area,list_img,build_size,ids,room_code,title,sell_price,toliet_exist
,is_whole,balcony_exist,area_name,room_name,house_facing
,walking_distance_dt_first,room_status,dispose_bedroom_amount
,subway_line_code_first,bizcircle_code,compartment_face,bizcircle_name
,house_id,subway_station_code_first,duanzuFlag
,duanzuSellPrice, district_name) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

for i in xrange(30, 901, 10):
    payload = {'step': i}
    res = requests.post('http://m.ziroom.com/list/ajax-get-data', data=payload)
    for i in res.json()['data']:
        # print i['resblock_name'].encode('gbk')
        subway_station_code_first = ''
        subway_line_code_first = ''
        area_name = ''
        room_name = ''
        if i['subway_station_code_first']:
            subway_station_code_first = i['subway_station_code_first'].encode('gbk')
        if i['subway_line_code_first']:
            subway_line_code_first = i['subway_line_code_first'].encode('gbk')
        if i['area_name']:
            area_name = i['area_name'].encode('gbk')
        if i['room_name']:
            room_name = i['room_name'].encode('gbk')

        params = (i['resblock_name'].encode('gbk'), i['usage_area'], i['list_img'], i['build_size'], 
                    i['id'], i['room_code'], i['title'].encode('gbk'), i['sell_price'], i['toliet_exist'], i['is_whole'],
                    i['balcony_exist'], area_name, room_name, 
                    i['house_facing'].encode('gbk'), 
                    i['walking_distance_dt_first'], i['room_status'], i['dispose_bedroom_amount'], 
                    subway_line_code_first, ','.join(i['bizcircle_code']), 
                    i['compartment_face'].encode('gbk'), 
                    ','.join(i['bizcircle_name']).encode('gbk'), i['house_id'], 
                    subway_station_code_first, 
                    i['duanzuFlag'], i['duanzuSellPrice'], i['district_name'].encode('gbk'))
        n = cusor.execute(sql_str, params)
        con.commit()
        print n
    time.sleep(3)