me = {"身長":"170cm","体重":"69㎏","職業":"会計士"}
q = input("身長、体重、職業　聞きたいことは？")
if q in me:
    result = me[q]
    print(result)
else:
    print("それは秘密です")
me["好きなミュージシャン"]={"ミスチル":["ハナビ","抱きしめたい"],"サザン":["いとしのエリー","真夏の果実"]}
print(me)
me["好きなミュージシャン"]["ドリカム"]=["未来予想図","Love"]
print(me)
me["好きなミュージシャン"]["ドリカム"].append("未来予想図Ⅱ")
print(me)
print(me["好きなミュージシャン"]["ドリカム"])
print(me["好きなミュージシャン"]["ミスチル"])
me["好きなミュージシャン"]["ミスチル"].append("イノセント・ワールド")
print(me)
print(me["好きなミュージシャン"]["ミスチル"])