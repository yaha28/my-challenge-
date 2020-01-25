color = ["blue", "red", "yellow"]
guess = input("何色でしょう？（入力してください）：")
if guess in color:
    print("当たり！")
else:
    print("ハズレ！")
