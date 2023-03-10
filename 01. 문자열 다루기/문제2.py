# 여러 문장으로 구성된 복문을 입력받아
# 문장의 첫 자를 대문자로 바꾸어
# 한 줄에 한 문장씩 출력

s = input()

s = s.split('.') # 마침표 기준 분리
s.pop()

for i in range(len(s)):
    s[i] = s[i].lstrip() # 첫 공백 제거
    s[i] = s[i].capitalize() # 첫 문자 대문자
    print(s[i] + ".")