# import requests
#
# url = "http://cn.morningstar.com/quickrank/default.aspx"
# headers={
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'Accept-Encoding':'gzip, deflate',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36'
# }
# resq = requests.get(url=url,headers=headers)
# print(resq)
# keylist1=[1,2,3,4,5]
# keylist2=[2,4,5]
# tradedict={}
# for buyin in keylist1:
#     for sellout in keylist2:
#         if buyin >= sellout:
#             continue
#         if buyin < sellout:
#             ptradedict = {"t" + str(keylist1.index(buyin)): [buyin, sellout]}
#             tradedict.update(ptradedict)
#             break
# print(tradedict)
#
# for i in tradedict.keys():
#     pair = tradedict[i]
#     print(pair)
#     buydate = pair[0]
#     print(buydate)
#     selldate = pair[1]
for i in [1,2,3,4,6]:

    f= open("C:\\Users\Administrator\Desktop\pnull.txt",'a')
    print(i,file=f)
    f.close()