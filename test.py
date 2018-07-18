from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.base_request import *

#

print()
a = base_request("http://app.fxh.io/api/coin/get?name=ethereum&page=1")
print(a)
# http://app.fxh.io/api/coin/get?name=ethereum&page=1
# http://app.fxh.io/api/coin/coinrank?page=1&sortfield=market&asc=0&update=1