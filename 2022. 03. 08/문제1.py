# 문자열을 입력받아서 공백을 제거한 후
# 모음(aeiouAEIOU)을 뺴고 출력

s = input()

res = s.replace(" ", "") # 공백 제거

mlist = "aeiouAEIOU" # 모음 리스트

for i in res:
    if i not in mlist: # 모음 리스트에 포함되지 않는다면
        res += i
    
print(res)