#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Torre Yang
# datetime:2018/12/9 18:16
import json
import requests
from connect_dataBase import ConnectDatabase
# db连接
db = "bookInfo"
connectDB = ConnectDatabase()
get_conf = connectDB.get_conf('databases_conf.json')
conn, cur = connectDB.connect_db(get_conf[db]["host"], get_conf[db]["user"],
                     get_conf[db]["password"], get_conf[db]["database"], get_conf[db]["port"])
url = "https://read.douban.com/j/kind/"
for page in range(1, 2263):
    payload = "{\"sort\":\"hot\",\"page\":%s,\"kind\":1,\"query\":\"\\n    query getFilterWorksList($works_ids: [ID!], $user_id: ID) {\\n      worksList(worksIds: $works_ids) {\\n        \\n    \\n    title\\n    cover\\n    url\\n    isBundle\\n  \\n    \\n    url\\n    title\\n  \\n    \\n    author {\\n      name\\n      url\\n    }\\n    origAuthor {\\n      name\\n      url\\n    }\\n    translator {\\n      name\\n      url\\n    }\\n  \\n    \\n    abstract\\n    editorHighlight\\n  \\n    \\n    isOrigin\\n    kinds {\\n      \\n    name @skip(if: true)\\n    shortName @include(if: true)\\n    id\\n  \\n    }\\n    ... on WorksBase @include(if: true) {\\n      wordCount\\n      wordCountUnit\\n    }\\n    ... on WorksBase @include(if: true) {\\n      \\n    isEssay\\n    ... on EssayWorks {\\n      favorCount\\n    }\\n    \\n    isNew\\n    \\n    averageRating\\n    ratingCount\\n    url\\n  \\n  \\n  \\n    }\\n    ... on WorksBase @include(if: false) {\\n      isColumn\\n      isEssay\\n      onSaleTime\\n      ... on ColumnWorks {\\n        updateTime\\n      }\\n    }\\n    ... on WorksBase @include(if: true) {\\n      isColumn\\n      ... on ColumnWorks {\\n        isFinished\\n      }\\n    }\\n    ... on EssayWorks {\\n      essayActivityData {\\n        \\n    title\\n    uri\\n    tag {\\n      name\\n      color\\n      background\\n      icon2x\\n      icon3x\\n      iconSize {\\n        height\\n      }\\n      iconPosition {\\n        x y\\n      }\\n    }\\n  \\n      }\\n    }\\n    highlightTags {\\n      name\\n    }\\n  \\n    ... on WorksBase @include(if: false) {\\n      \\n    fixedPrice\\n    salesPrice\\n    isRebate\\n  \\n    }\\n    ... on EbookWorks {\\n      \\n    fixedPrice\\n    salesPrice\\n    isRebate\\n  \\n    }\\n    ... on WorksBase @include(if: true) {\\n      ... on EbookWorks {\\n        id\\n        isPurchased(userId: $user_id)\\n        isInWishlist(userId: $user_id)\\n      }\\n    }\\n  \\n        id\\n        isOrigin\\n      }\\n    }\\n  \",\"variables\":{\"user_id\":\"\"}}" %(str(page))
    headers = {
        'accept': "application/json",
        'origin': "https://read.douban.com",
        'x-csrf-token': "null",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        'content-type': "application/json",
        'referer': "https://read.douban.com/category/?kind=105",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh,zh-CN;q=0.9",
        'cookie': "bid=_m_-fwoBQ5s; viewed=\"6786779\"; gr_user_id=61b9d770-57aa-4b52-a49a-730ec9f8e863; douban-fav-remind=1; ll=\"118172\"; _vwo_uuid_v2=D81E378C47145E03596AD10EB27054F12|4c080e88ec5dde0f476da38d132bdf7a; ct=y; ps=y; as=\"https://movie.douban.com/subject/30224728/\"; __utmc=30149280; _ga=GA1.3.935231865.1535875869; _gid=GA1.3.2120264910.1544330500; ap_v=0,6.0; __utma=30149280.935231865.1535875869.1544330273.1544344049.14; __utmz=30149280.1544344049.14.12.utmcsr=book-nav|utmccn=(not%20set)|utmcmd=douban; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=6849e0e6-8872-4c20-93a5-caa2422ce8ed; gr_cs1_6849e0e6-8872-4c20-93a5-caa2422ce8ed=user_id%3A0; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_6849e0e6-8872-4c20-93a5-caa2422ce8ed=true; _pk_ref.100001.a7dd=%5B%22%22%2C%22%22%2C1544349006%2C%22https%3A%2F%2Fbook.douban.com%2F%22%5D; _pk_ses.100001.a7dd=*; _pk_id.100001.a7dd=d345c908feaa15a9.1544330500.3.1544349024.1544344076.",
        'cache-control': "no-cache",
        'postman-token': "c206b02b-2d12-52cc-8aa9-829e0301ce47"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    with open('bookInfo.txt', 'wb') as f:
        f.write(response.text.encode('utf-8'))
        f.close()
    with open('bookInfo.txt', 'r', encoding='utf-8') as f:
        info = f.readlines()
        bookInfo = json.loads(info[0])
        if len(bookInfo["list"]) != 0:
            for book in bookInfo["list"]:
                try:
                    abstract = book["abstract"]
                    if len(book["author"]) != 0:
                        author = []
                        for a in book["author"]:
                            author.append(a["name"])
                        author = ','.join(author)
                    else:
                        if len(book["origAuthor"]) != 0:
                            author = book["origAuthor"][0]["name"]
                    averageRating = str(int(book["averageRating"]) * 2)
                    id = book["id"]
                    ratingCount = str(book["ratingCount"])
                    title = book["title"]
                    if len(book["kinds"]) != 0:
                        kind = []
                        for k in book["kinds"]:
                            kind.append(k["shortName"])
                        kinds = ','.join(kind)
                        # print(kinds)
                    else:
                        kinds = " "
                    SQL = 'insert into bookInfo(id, title, author, averageRating, ratingCount, kinds, abstract) values(%s, %s, %s, %s, %s, %s, %s)'
                    try:
                        # connectDB. get_fetch(conn, cur, SQL)
                        cur.execute(SQL, (id, title, author, averageRating, ratingCount, kinds, abstract))
                        conn.commit()
                    except:
                        print("插入SQL有误")
                        print(SQL, (id, title, author, averageRating, ratingCount, kinds, abstract))
                except:
                    print("插入数据有误")
        else:
            print("数据为NULL")
