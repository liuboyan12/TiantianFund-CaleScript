# A = 1
# Tst = 2
# exec("use%s=A"%Tst)
# print(use2)
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


keylist1 = {'002001':[1,2,3]}
keylist1.update({'002001':[4]})
print(keylist1)