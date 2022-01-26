import os

money = 0
print('1 : 돈 인출  2 : 돈 입금  3 : 잔고확인')
number = int(input('숫자를 입력하세요 : '))

# 1 입력시 돈 인출
if number == 1 :
    withdraw = int(input('인출할 금액을 입력하세요 : '))
    if withdraw > money:
        print('인출할 수 없습니다.')
        print('잔여 금액 : %d' %(money))
    else:
        print('잔여 금액 : ' + (money-withdraw))
        
# 2 입력시 돈 입금하기
elif number == 2:
    deposit = int(input('입금할 금액을 입력하세요 : '))
    if deposit < 0:
        print('잘못된 금액 입력입니다.')
    else:
        print('잔여 금액 : %d' %(money + deposit))

# 3 입력시 잔고 확인
elif number == 3:
    print('잔여 금액 : %d' %(money))

else:
    print('잘못된 숫자 입력입니다.')

os.system('pause')
