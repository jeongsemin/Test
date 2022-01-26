def div_price():
    print("총 금액을 입력하세요 : ")
    num = int(input())

    print("나눠야 하는 인원 수를 입력해주세요 : ")
    people = int(input())

    div = float(num/people)
    print("1인당 지불해야 하는 금액은 : ", div)
    
print("프로그램을 실행하시겠습니까? 1: 실행한다 2: 실행하지 않는다.")
selectnumber = int(input())

if selectnumber == 1:
    div_price()

else:
    print("프로그램 종료")