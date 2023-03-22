select = 0
contact = {}
count = 0


while select != 5:
    print("1 : 전화번호 등록")
    print("2 : 전화번호 삭제")
    print("3 : 전화번호 검색")
    print("4 : 전화번호 전체보기")
    print("5 : 종료")
    select = int(input("번호를 선택하세요. : "))
    
    if select == 1:
        info = input("이름:전화번호 형태로 입력하세요.\n")
        infoList = info.split(':')
        
        contact[infoList[count]] = infoList[count+1]
        count += 1
        
    elif select == 2:
        delName = input("삭제할 이름을 입력하세요.\n")
        if delName in contact:
            del contact[delName]
            count -= 1
        else:
            print("해당 이름이 존재하지 않습니다.\n")
            
    elif select == 3:
        searchName = input("검색할 이름을 입력하세요.\n")
        if searchName in contact:
            print(contact[searchName])
        else:
            print("해당 이름이 존재하지 않습니다.\n")
            
    elif select == 4:
        print(contact, '\n')
        