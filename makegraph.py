import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# dFloor
# log_11-37.csv　：　床に座る

dFloor01 = pd.read_csv("log_11-37.csv", encoding='utf-8')

# dCushion
# log_08-35.csv　：　[床直] 床に直置き
# log_11-00.csv　：　[床置] 床に直置き（NG)
# log_16-28.csv　：　[床直] 床に直置き

dCushion01 = pd.read_csv("log_16-28.csv", encoding='utf-8')
dCushion02 = pd.read_csv("log_11-00.csv", encoding='utf-8')
dCushion03 = pd.read_csv("log_08-35.csv", encoding='utf-8')


# dAirflow
# log_09-35.csv　：　隙間あり旋風無 -> 1820 旋風強
# log_17-15.csv　：　[床置] 旋風強

dAirflow01 = pd.read_csv("log_17-15.csv", encoding='utf-8')
dAirflow02 = pd.read_csv("log_09-35.csv", encoding='utf-8')



def anacsv(testType, testData):
    tmpList = []
    tmpList.append(testType)
    #平均
    tmpList.append( round(testData["temperature"].mean(),2) )
    tmpList.append( round(testData["humidity"].mean(),2) )
    #中央値
    tmpList.append(testData["temperature"].median())
    tmpList.append(testData["humidity"].median())
    return( tmpList )

dfResult = []
tests = [
    ["dFloor01",dFloor01]
    ,["dCushion01",dCushion01]
    ,["dAirflow01",dAirflow01]
]

for test in tests:
    tmp = []
    tmp = anacsv( test[0], test[1])
    dfResult.append(tmp)

#dfResult.append(tmpList)
dfResult

fig = plt.figure(figsize=(12,8), dpi=144)
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(dFloor01["no"], dFloor01["temperature"], label="床に座る")
ax1.plot(dCushion01["no"], dCushion01["temperature"], label="クッションに座る")
ax1.plot(dAirflow01["no"], dAirflow01["temperature"], label="クッション＋扇風機に座る")

ax2.plot(dFloor01["no"], dFloor01["humidity"], label="床に座る")
ax2.plot(dCushion01["no"], dCushion01["humidity"], label="クッションに座る")
ax2.plot(dAirflow01["no"], dAirflow01["humidity"], label="クッション＋扇風機に座る")


# グラフタイトル
#ax1.set_title("比較")

# グラフ軸
ax1.set_xlabel("経過時間[秒]")
ax1.set_ylabel("温度[℃]")
ax2.set_xlabel("経過時間[秒]")
ax2.set_ylabel("湿度[%]")

# ラベル表示
plt.legend()
#plt.show()
fig.savefig("result01.png")