answer = input("好きな食べ物は？：")
with open ("answer.txt", "w", encoding="utf-8") as f:
    f.write(answer)

import csv
movies = [["トップガン","Risky Business","マイノリティ・リポート"],["タイタニック","The Revenant","Inception"],["Training Day","man on Fire","Flight"],["以上です。今日はここまで。"]]
with open ("list.csv", "w", encoding="utf-8") as l:
    w = csv.writer(l, delimiter=",")
    for movie_list in movies:
        w.writerow(movie_list)
