import time

import news
import  image
import pinjie
import wangyi
def creat():
    #拼接微博热板块
    weibo=['./small_images/title-weibo.png','./output/merge.png']
    ans=news.weibo_hot()
    image.creat_image(ans)
    pinjie.image_merge(weibo,output_name='part_weibo.png')
    #拼接网易模块
    wangyi_src=['./small_images/title-wangyi.png','./output/top.png','./output/评论.png']
    ans1=wangyi.get_hotlist()
    songName=[]
    comments=[]
    for i in range(0,len(ans1)):
        comment = []
        k=i+1
        songName.append('TOP{0}:{1}'.format(k,ans1[i]['song_name']))
        comments.append(ans1[i]['comment'])
        comments.append('用户:{0}  时间:{1}  赞:{2} 歌曲:{3}'.format(ans1[i]['name'],ans1[i]['time'],ans1[i]['zan'],ans1[i]['song_name']))
        comments.append('--------------------------\n')
    songName.insert(0,'\t\t\t\t\t\t\t◎网易飙升棒TOP3◎\n\n')
    songName.append('\n')
    comments.insert(0,'\t\t\t\t\t\t\t◎今日热评◎\n\n')
    image.creat_image(songName,src='top.png')
    image.creat_image(comments,src='评论.png')
    pinjie.image_merge(wangyi_src,output_name='part_wangyi.png')

    #拼接大板块
    filename = time.strftime("%Y-%m-%d", time.localtime())
    zong=['./output/part_weibo.png','./output/part_wangyi.png']
    pinjie.image_merge(zong,output_name='{}.png'.format(filename))