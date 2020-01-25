with open ("st.txt","w", encoding="utf-8") as f:
    f.write("Pythonからこんにちは！！ご機嫌よう！")

my_list = []

with open ("st.txt","r", encoding="utf-8") as f:
    my_list.append(f.read())
print(my_list)
