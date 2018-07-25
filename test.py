import re
from urllib.request import urlopen
from urllib import request,parse
import urllib.request
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

#header范例：
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

# (url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
# GET http://cn.morningstar.com/quickrank/default.aspx HTTP/1.1
# Host: cn.morningstar.com
# Connection: keep-alive
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9
def test():
    url = "http://cn.morningstar.com/quickrank/default.aspx"
    headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36',
        # 'Content-Type':'application/x-www-form-urlencoded'
    }
    req = request.Request(url, headers=headers)
    page = request.urlopen(req).read()
    page = page.decode('utf-8')

    __EVENTTARGET= str(re.findall(r'id="__EVENTTARGET" value="(.+?)" />',page))
    num = str(re.findall(r'ctl00(.+?)cphMain',__EVENTTARGET))
    __EVENTARGUMENT= str(re.findall(r'id="__EVENTARGUMENT" value="(.+?)" />',page))
    __LASTFOCUS= str(re.findall(r'id="__LASTFOCUS" value="(.+?)" />',page))
    __VIEWSTATE= str(re.findall(r'id="__VIEWSTATE" value="(.+?)" />',page))
    __VIEWSTATEGENERATOR= str(re.findall(r'id="__VIEWSTATEGENERATOR" value="(.+?)" />',page))
    formdate ='__EVENTTARGET='+__EVENTTARGET+'&'+'__EVENTARGUMENT='+__EVENTARGUMENT+'&'+'__LASTFOCUS='+__LASTFOCUS+'&'+'__VIEWSTATE='+__VIEWSTATE+'&'+'__VIEWSTATEGENERATOR='+__VIEWSTATEGENERATOR+'&'
    data = {
        '__EVENTTARGET':__EVENTTARGET,
        '__EVENTARGUMENT':__EVENTARGUMENT,
        '__LASTFOCUS':__LASTFOCUS,
        '__VIEWSTATE':__VIEWSTATE,
        '__VIEWSTATEGENERATOR':__VIEWSTATEGENERATOR,
        'ctl00'+num+'cphMain'+num+'cblStarRating'+num+'0': '5',
        'ctl00'+num+'cphMain'+num+'cblStarRating5'+num+'0': '55',
        'ctl00'+num+'cphMain'+num+'cblGroup'+num+'0': 'O',
        'ctl00'+num+'cphMain'+num+'ddlCompany': '',
        'ctl00'+num+'cphMain'+num+'ddlPortfolio': '',
        'ctl00'+num+'cphMain'+num+'ddlWatchList': '',
        'ctl00'+num+'cphMain'+num+'txtFund': '%E5%9F%BA%E9%87%91%E5%90%8D%E7%A7%B0',
        'ctl00'+num+'cphMain'+num+'ddlPageSite': '10000'
    }

    headers2={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36',

        'Content-Type':'application/x-www-form-urlencoded'
    }

    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url, headers=headers2,data=data)
    page = request.urlopen(req).read()
    page = page.decode('utf-8')
    print(page)



def change_2_useable_code(htmlcode):
    """
    传出获取到的晨星排行榜的界面上面的数据（基金代码）
    :param htmlcode: 网页代码
    :return: 网页内基金code的list
    """
    htmlcode=htmlcode[htmlcode.index("<table id"):htmlcode.index("table>")+6].replace("\\n","").replace("\\t","").replace("\\r","").replace("&nbsp;","").replace("><",">\n<")
    print(htmlcode)
    outlist= re.findall(r'target="_blank">(.+?)</a>',htmlcode)
    finallist = []
    for i in outlist:
        tprint(i)
        strings = str(i)
        ifstings=strings[0]
        if ifstings == "\\":
            pass
        else:
            finallist.append(i)
    return finallist

if __name__ == '__main__':
    # f = open('C:\\Users\Administrator\Desktop\second请求.txt',"r",encoding='utf-8')
    # strings= format_removeal(f.read())
    # f.close()
    # # print(strings)
    # # lists = change_2_useable_code(strings)
    # outlist = re.findall(r'target="_blank">(.+?)</a>', strings)
    # filist=[]
    # for i in outlist:
    #     ifcode = i[0]
    #     # tprint(ifcode)
    #     if ifcode == '1':
    #         filist.append(i)
    #     elif ifcode =='2':
    #         filist.append(i)
    #     elif ifcode =='3':
    #         filist.append(i)
    #     elif ifcode =='4':
    #         filist.append(i)
    #     elif ifcode =='5':
    #         filist.append(i)
    #     elif ifcode =='6':
    #         filist.append(i)
    #     elif ifcode =='7':
    #         filist.append(i)
    #     elif ifcode =='8':
    #         filist.append(i)
    #     elif ifcode =='9':
    #         filist.append(i)
    #     elif ifcode =='0':
    #         filist.append(i)
    #     else:
    #         continue
    # print(filist)
    test()