answer = [3, 6, 9]
while True:
    a = input("0から9までの数字を入力してください：")
    if a == "q":
        break
    try:
        a = int(a)
    except ValueError:
        print("数字か\"q\"を入力してください")
        continue
    if a in answer:
        print("正解")
        break
    else:
        print("違います")
    