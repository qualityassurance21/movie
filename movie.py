#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Torre Yang
# datetime:2018/12/8 16:13
# 自动爬去豆瓣电影并存储到MySQL
# 1.将电影爬取, 用json解析, 整理insert语句
# 2.每20条请求数据
import requests
import json
from connect_dataBase import ConnectDatabase
# db连接
db = "movieRecommend"
connectDB = ConnectDatabase()
get_conf = connectDB.get_conf('databases_conf.json')
conn, cur = connectDB.connect_db(get_conf[db]["host"], get_conf[db]["user"],
                     get_conf[db]["password"], get_conf[db]["database"], get_conf[db]["port"])
styleList = ['剧情', '喜剧', '动作', '爱情', '科幻', '动画', '悬疑', '惊悚', '恐怖', '犯罪', '同性',
             '音乐', '歌舞', '传记', '历史', '战争', '西部', '奇幻', '冒险', '灾难', '武侠', '情色']
for style in styleList:
    for page in range(0, 10000, 20):
        # 爬取电影
        url = "https://movie.douban.com/j/new_search_subjects"
        querystring = {"sort": "U", "range": "0,10", "tags": "", "start": str(page), "genres": style}
        headers = {
            'accept': "application/json, text/plain, */*",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            'cookie': "bid=_m_-fwoBQ5s; viewed=\"6786779\"; gr_user_id=61b9d770-57aa-4b52-a49a-730ec9f8e863; douban-fav-remind=1; ll=\"118172\"; __yadk_uid=5FTjZRsoRfx37KphAWlnzE1Ov8aD8V7P; _vwo_uuid_v2=D81E378C47145E03596AD10EB27054F12|4c080e88ec5dde0f476da38d132bdf7a; __utmc=30149280; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1544253710%2C%22https%3A%2F%2Fm.douban.com%2Fmovie%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.935231865.1535875869.1544253710.1544254710.9; __utmz=30149280.1544254710.9.9.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1213887491.1539515359.1544253710.1544254710.4; __utmb=223695111.0.10.1544254710; __utmz=223695111.1544254710.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmb=30149280.6.5.1544254739226; _pk_id.100001.4cf6=7662f226b551fb18.1539515359.3.1544255494.1539517497.; ct=y",
            'postman-token': "020d3689-c97f-e133-9bbc-0404415be286"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        movieJson = json.loads(response.text)
        # print(response.text)
        if len(movieJson["data"]) != 0:
            for movie in movieJson["data"]:
                try:
                    directors = movie["directors"][0]
                    rate = movie["rate"]
                    casts = movie["casts"][0]
                    star = movie["star"]
                    title = movie["title"]
                    id = movie["id"]
                    style = style
                    # print(casts)
                    SQL = 'insert into movieinfo(id, title, casts, directors, rate, star, style) values(%s, %s, %s, %s, %s, %s, %s)'
                    # SQL = "insert into movieinfo(id, title, directors, rate, star, style) values({0}, {1}, {2}, {3}, {4}, {5})".format(id, title, directors, rate, int(star)/10, style)
                    # print(SQL)
                    try:
                        # connectDB. get_fetch(conn, cur, SQL)
                        # print(SQL, (id, title, casts, directors, rate, star, style))
                        cur.execute(SQL, (id, title, casts, directors, rate, star, style))
                        conn.commit()
                    except:
                        print("插入数据有误")
                        print(SQL, (id, title, casts, directors, rate, star, style))
                except:
                    print("NULL")

        else:
            print("电影为空")




