import random
import time
import requests
import urllib.request,os,json
from lxml import etree
import base64,codecs
from Crypto.Cipher import AES
from selenium import webdriver
import demo
# data={
#     "csrf_token": "",
#     "cursor": "-1",
#     "offset": "0",
#     "orderType": "1",
#     "pageNo": "1",
#     "pageSize": "20",
#     "rid": "R_SO_4_1886366521",
#     "threadId": "R_SO_4_1886366521",
# }
#
#

def to_16(key):
    while len(key) % 16 != 0:
        key += '\0'
    return str.encode(key)

def AES_encrypt(text, key, iv):
    bs = AES.block_size
    pad2 = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    encryptor = AES.new(to_16(key), AES.MODE_CBC,to_16(iv))
    encrypt_aes = encryptor.encrypt(str.encode(pad2(text)))
    encrypt_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
    return encrypt_text

def RSA_encrypt(text, pubKey, modulus):
    text=text[::-1]
    rs=int(codecs.encode(text.encode('utf-8'), 'hex_codec'), 16) ** int(pubKey, 16) % int(modulus, 16)
    return format(rs, 'x').zfill(256)

#获取i值的函数，即随机生成长度为16的字符串



url='https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

g = '0CoJUm6Qyw8W8jud'#buU9L(["爱心", "女孩", "惊恐", "大笑"])的值
b = "010001"#buU9L(["流泪", "强"])的值
# buU9L(Rg4k.md)的值
c = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
iv = "0102030405060708"  # 偏移量
i = "prdx2S1dwjk3Pez9"
headers = {
      "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",

      }




def get_params(data):
        data=json.dumps(data);
        return AES_encrypt(AES_encrypt(data,g,iv),i,iv)

def get_encSecKey(i,b,c):
        return RSA_encrypt(i,b,c)

def get_collect(data):
    resp=requests.post(url,headers=headers,data={
        "params":get_params(data),
        "encSecKey":get_encSecKey(i,b,c)
    })
    resp.encoding='utf-8'
    resp_json=json.loads(resp.text)
    if(resp_json['data']['hotComments']!=None):
        return resp_json['data']['hotComments']
    else:
        return resp_json['data']['comments']

def get_comments(data,name):#返回评论的时间 人 内容 点赞数  time name comment zan song_name
    print('正在获取歌曲"{}"的热评信息'.format(name))
    lis=get_collect(data)
    res=[]
    for i in lis:
        COMMENT=i['content']
        TIME=i['timeStr']
        ZAN=i['likedCount']
        NAME=i['user']['nickname']
        detail={
            "time":TIME,
            "comment":COMMENT,
            "name":NAME,
            "zan":ZAN,
            "song_name":name
        }
        res.append(detail)
    print("热评获取完毕！")
    return res
def get_hotlist():
    #此函数得到真正的要返回的热评数组 得到100首歌曲的数据集 我们只返回前三首的五条评论
    browser = webdriver.Firefox()
    name=demo.get_songs_name(browser)#歌名集合
    id_list=demo.get_songs_id(browser)#歌曲id集合
    q=[]
    #循环三次要是要很多组数据=自行更改
    for k in range(0,3):
        num=k+1
        print("排名:{}".format(num))
        data={
        "csrf_token": "",
        "cursor": "-1",
        "offset": "0",
        "orderType": "1",
        "pageNo": "1",
        "pageSize": "20",
        "rid": "R_SO_4_{}".format(id_list[k]),
        "threadId": "R_SO_4_{}".format(id_list[k])
         }
        datas=get_comments(data,name[k])
        q.append(datas)

    filename=time.strftime("%Y-%m-%d ", time.localtime())

    now_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    f=open("./text/{}.txt".format(filename),'a',encoding='utf-8')
    f.write(now_time+'\n');
    for k in range(0,len(q)):
        num=k+1;
        print('正在写入第{}首歌曲热评信息'.format(num))
        for z in range(0,len(q[k])):
            f.write('--------------------------------------------------' + '\n')
            f.write('歌名:' + q[k][z]['song_name'] + '\t' + '排名:' + '{}'.format(num) + '\n')
            f.write('--------------------------------------------------' + '\n')
            f.write(q[k][z]['comment']+'\n')
            f.write('--------------------------------------------------' + '\n')
            f.write('用户:'+q[k][z]['name']+'\t'+'发布时间:'+q[k][z]['time']+'\n')
            f.write('\n\n')
        print('第{}首歌曲热评写入完毕！'.format(num))
    f.close()
    browser.close()
    write_list=[]
    for i in q:
            k=random.randint(0,14)
            write_list.append(i[k])
    return write_list  #返回三首歌 15条歌曲的评论
