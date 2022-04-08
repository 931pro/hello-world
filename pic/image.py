from PIL import Image, ImageFont, ImageDraw
import pinjie
# n_im= Image.new("RGB", (400,1000), "#323232")
# n_im.save('./01.png')
# n_im.show()

# im = Image.open("01.png") # 打开文件
# print(im.format, im.size, im.mode)
# draw = ImageDraw.Draw(im) #修改图片
# fonts = ImageFont.truetype("C:\\WINDOWS\\Fonts\\SIMYOU.ttf", 14)
# str='电脑看啥看电脑卡德克士那肯定那时可能打开暗示的可能啥的可能啥看你的看地块三点开你啥课都能看到卡哪款三道坎思考电脑上看到看到看啥看电脑看看到你斯卡迪那是你          多岁的萨可能大看你的所看多卡所女多看多扩那所扩多所那扩多女卡撒奥奥奥奥奥奥奥奥奥奥奥奥奥奥奥奥奥奥奥奥奥奥奥奥奥奥奥奥奥奥奥'
# #font = ImageFont.truetype(None, size = 40)#"C:\Users\Administrator\Desktop\每天小程序homework_day\0000\Helvetica Bold.ttf", 36) #更改文字字体
#
# print(fonts.getsize(str))
# draw.text((200,800),str ,font=fonts,fill='#fff') #利用ImageDraw的内置函数，在图片上写入文字
# im.show()
# im.save('01.png')


# coding=utf-8
import re


LINE_CHAR_COUNT = 25*2  # 每行字符数：30个中文字符(=60英文字符)
CHAR_SIZE = 30
TABLE_WIDTH = 4

def line_break(line):
    ret = ''
    width = 0
    for c in line:
        if len(c.encode('utf8')) == 3:  # 中文
            if LINE_CHAR_COUNT == width + 1:  # 剩余位置不够一个汉字
                width = 2
                ret += '\n' + c
            else: # 中文宽度加2，注意换行边界
                width += 2
                ret += c
        else:
            if c == '\t':
                space_c = TABLE_WIDTH - width % TABLE_WIDTH  # 已有长度对TABLE_WIDTH取余
                ret += ' ' * space_c
                width += space_c
            elif c == '\n':
                width = 0
                ret += c
            else:
                width += 1
                ret += c
        if width >= LINE_CHAR_COUNT:
            ret += '\n'
            width = 0
    if ret.endswith('\n'):
        return ret
    return ret + '\n'
def creat_image(ans,src='merge.png'):
    imgSrc = []
    j=0
    for i in ans:
        j+=1
        output_str =i
        output_str = line_break(output_str)
        d_font = ImageFont.truetype('C:/Windows/Fonts/msyhl.ttc', CHAR_SIZE)
        lines = output_str.count('\n')  # 计算行数

        image = Image.new("RGB", (LINE_CHAR_COUNT*CHAR_SIZE // 2+50, (CHAR_SIZE+10)*lines), "white")
        draw_table = ImageDraw.Draw(im=image)
        draw_table.text(xy=(25, 0), text=output_str, fill='black', font= d_font, spacing=4)  # spacing调节机制不清楚如何计算
        image_name='./small_images/{}.png'.format(j)
        image.save(image_name,'PNG')  # 保存在当前路径下，格式为PNG
        imgSrc.append(image_name)
        image.close()

    pinjie.image_merge(images=imgSrc,output_name=src)