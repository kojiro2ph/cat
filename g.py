# -*- coding: utf-8 -*-
import os
import sys
import re
import pip._vendor.requests

radi = "5000"                                       # 該当場所からの半径
#k = ""                                             # Google API Key
ptn = '^2'                                          # 郵便番号の正規表現    ※ 現在 : 東京都に設定

# 駅ファイル読み込み ---
with open("s.csv") as f:
    dt = f.read().splitlines()

# 駅ファイル読み込み ---
with open("t.csv") as f:
    t_ = f.read().splitlines()

ars = []
cnt = 0
for l in dt:
    #区切り文字で項目ごとに区切る ---
    f_ = l.split(",")
    #郵便番号で絞る ---
    rs = re.match(ptn,f_[2])
    if rs:
        pass
    else:
        continue

    if (f_[1] not in ars):
        cs = f_[1]      # 駅名
        ars.append(cs)
        clat = f_[5]    # lat
        clng = f_[4]    # lng
        
        print(str(len(ars)) + " : " + cs + " " + clat + " " + clng)

        for t in t_:
            fn = "data/" + cs + "-" + t + ".txt"
            if os.path.exists(fn):
                print("skip")
                continue
            cnt = cnt + 1
            sURL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + clat + "," + clng + "&radius=" + radi + "&type=" + t + "&key=" + k
            print(str(cnt) + " : " + cs + " " + t)
            r = pip._vendor.requests.get(sURL)
            #print(r.text)
            with open(fn, mode='w') as f:
                f.write(r.text.encode('utf_8'))
            #break

        if len(ars) >= 10:
            break
