import re

from urllib.request import urlopen
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.adjust_string import format_removeal

def tprint(obj, except_word=""):
    """
    #脚本编辑打印辅助工具
    ┏━━━━┳━━┓
    ┃传入值  ┃类型┃
    ┣━━━━╋━━┫
    ┃任何变量┃ all┃
    ┗━━━━┻━━┛
    #要复制到编写的函数中使用，不可跨py使用
    """
    for name, item in globals().items():
        if item == obj and name != except_word:
            print(name + ':',type(obj))
            print(obj)
            print()
page=urlopen('http://cn.morningstar.com/quickrank/default.aspx')
htmlcode = format_removeal(str(page.read()))
print(htmlcode)

# url = 'http://cn.morningstar.com/handler/quicktake.ashx?command=fee&fcid=0P00015XQU&randomid=0.41830457233925933'
# headers = {'Accept': 'application/json, text/javascript, */*',
#            'Accept-Encoding': 'gzip, deflate, sdch',
#            'Accept-Language': 'zh-CN,zh;q=0.8',
#            'Cache-Control': 'max-age=0',
#            'Content-Type': 'application/x-www-form-urlencoded',
#            'Cookie': 'ASP.NET_SessionId=ztqnzlbcb5qyuwi3puhbtuy2; __utmt=1; __utma=172984700.1526292971.1508480165.1509435578.1509498541.13; __utmb=172984700.8.10.1509498541; __utmc=172984700; __utmz=172984700.1508480165.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_eca85e284f8b74d1200a42c9faa85464=1508893317,1509074039,1509095099,1509435578; Hm_lpvt_eca85e284f8b74d1200a42c9faa85464=1509502708; BIGipServercn=2241222154.20480.0000',
#            'Host': 'cn.morningstar.com',
#            'Proxy-Connection': 'keep-alive',
#            'Referer': 'http://cn.morningstar.com/quicktake/0P00015XQU',
#            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
#            'X-Requested-With': 'XMLHttpRequest'}

# i =int(htmlcode.find('<span id="cphMain_gridResult_lblRowNo_0">1</span>'))
# htmlcode=htmlcode[i:]
# tprint(htmlcode)
#
#
#
#
# stirngs = '<a>6666<i>'
# a = re.findall('(?<=<a>).*?(?=<i>)',stirngs)
# print(a)