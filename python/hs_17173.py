#!/usr/bin/python
# -*- coding:utf-8 -*-
import json,sys
import requests
import mysql

reload(sys)
sys.setdefaultencoding('utf-8')

my = mysql.MyDB()

hs_17173_url = "http://cha.17173.com/hs/list"
he_17173_json_url = "http://cha.17173.com/hs/list/async?_n=1495176347285"

def getPage(page):

    post_data = {"page":page}

    response = requests.post(he_17173_json_url, data = post_data)

    json_data = json.loads(response.content)

    if json_data['status'] == 'success':
        card_data = json_data['data']
        sql = "insert into hs_card (name,career,card_set,card_type,cost,race,atk,health,rarity,windfury,taunt,freeze,battlecry,stealth,combo,charge,grant_charge,spellpower,silence,enrage,divine_shield,deathrattle,secret,mission,lifesteal,img_url,card_url) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for one in card_data:
            img_url  = 'http://i1.17173cdn.com/8hpoty/YWxqaGBf/images/resource/new_middler/' + one['card_id'] + '.png?version=201612021432'
            card_url = 'http://cha.17173.com/hs/info/card_zhcn/' + str(one['id'])
            if one.has_key('lifesteal'):
                lifesteal = one['lifesteal']
            else:
                lifesteal = 0
            sql_data = (one['name'],one['class'],one['card_set'],one['card_type'],one['cost'],one['race'],one['atk'],one['health'],one['rarity'],one['windfury'],one['taunt'],one['freeze'],one['battlecry'],one['stealth'],one['combo'],one['charge'],one['grant_charge'],one['spellpower'],one['silence'],one['enrage'],one['divine_shield'],one['deathrattle'],one['secret'],one['mission'],lifesteal,img_url,card_url)
            my.insertOne(sql, sql_data)
        getPage(page+1)
    else:
       print "第" + str(page) + "页获取失败" + json_data['status']

if __name__ == "__main__":
    getPage(1)
