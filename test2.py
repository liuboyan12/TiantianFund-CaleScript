import re
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.self_encapsulation_scripts import daysUnix

time = daysUnix()
date = open("C:\\Users\Administrator\Desktop"+'\\a20180809信号.txt')
context = date.read()
date.close()
# buylist ['110022', '110011', '519697', '180012', '570005', '519091', '040008', '070032', '270041', '510630', '519700', '519702', '540006', '163412', '165312', '690001', '160212', '519066', '202023', '519069', '002021', '110003', '519068', '166005', '020026', '340008', '160916', '570001', '163415', '163402', '159905', '481012', '040011', '159916', '163407', '310398', '090007', '202005', '166001', '166002']
# selllist ['217022', '519669', '233005', '320021', '121012', '128112', '050027', '166008', '050011', '340009']
_list = ['163412','510630','530020','519977','020026']


buylist = re.findall("buylist(.+?)]",context)
selllist = re.findall("selllist(.+?)]",context)

buylist=str(buylist)[3:]
buylist=eval(buylist[:-2]+"]")
selllist=str(selllist)[3:]
selllist=eval(selllist[:-2]+"]")

pinlist=[]
poutlist=[]
for i in _list:
    bsi = buylist.count(i)
    sei = selllist.count(i)
    if bsi != 0:
        pinlist.append(i)
    else:
        pass
    if sei != 0:
        poutlist.append(i)
    else:
        pass
print(pinlist)
print(poutlist)
redict= {time:{"buy":pinlist,"sell":poutlist}}
print(redict)

date2 = open("C:\\Users\Administrator\Desktop"+'\\a20180809信号.txt','w')
date2.write(str(redict))
date2.close()