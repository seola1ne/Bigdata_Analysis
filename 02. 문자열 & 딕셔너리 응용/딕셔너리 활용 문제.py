# 딕셔너리 생성
a = {"홍길동" : "010-1234-5678"}


# 딕셔너리 추가
a["홍길순"] = '010-0000-1111'
print(a)


# 특정 키의 값 삭제
del a["홍길동"]


# 키 확인 ( True / False )
print("홍길순" in a)
print('010-0000-1111' in a)


# key와 value들만 따로 필요할 때
print(list(a.keys()))
print(list(a.values()))