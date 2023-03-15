a = '홍길동:010-1234-5678'

# 주어진 값이 몇 번 나오는가?
# count() : 문자열 내부에서 특정 문자가 등장하는 횟수를 알려 줌
# count(검색할 문자, start, end) : start 인덱스부터 end 인덱스까지 해당 문자가 몇 번 나오는지 검사

print(a.count('0')) # 2


# 주어진 값이 몇 번째에 처음으로 나오는가? 없으면 출력되는 값은? 비슷한 기능을 가진 2개의 메소드
# find(), index() : 특정 문자가 존재하는지 확인하고 존재하는 위치의 인덱스를 찾아줌

print(a.find('0')) # 4
print(a.index('0')) # 4
# 없을 때 출력되는 값이 다르다
# find : -1, index : 에러 발생


# 주어진 값이 몇 번째에 마지막으로 나오는가?
# rfind() : 찾고 싶은 문자가 여러 개 있다면 맨 마지막 인덱스를 반환

print(a.rfind('0')) # 6
print(a.rindex('0')) # 6


# 주어진 단어가 포함되어 있으면 True 혹은 False 반환
print('0' in a) # True


# 문자열 나눠 list로
l = list(a.split(':'))
print(l)

# 문자열 합치기
print(','.join(l)) # join()은 list만 사용 가능

# 문자열 바꾸기
print(a.replace(':', ','))