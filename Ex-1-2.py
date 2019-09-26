import time
list1=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
list2=[2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31]
list3=[4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31]
list4=[8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31]
list5=[16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
result=list()
print('1-31까지 마음에 드는 숫자를 정해주세요')
time.sleep(3)  # 3초 멈추기
print('정하셧나요?\n3장의 카드를 보고 마음에 드는게 있으면o, 없으면x를 입력해주세요!')
def checkNum(i):
    if (i+1) % 5 ==0:
        print(" ")
def guessNum(c,result):
    if c=='o' or c=='0':
        result.append(1)
    elif c=='x' or c=='X':
        result.append(0)
def checkType(a):
    if a=='o' or a=='x' or a=='X':
        return False
    elif a!='o' or a!='x' or a!='X':
        return True
while True :
    for i in range(0,len(list1)):
        print("|",list1[i],end=' | ')
        checkNum(i)
    print("\n")
    a=input("마음에 드는 숫자가 있나요?(있으면o,없으면x)\n")
    if checkType(a):
        print("잘못입력하셧습니다 다시시작할게요")
        continue;
    guessNum(a,result)
    
    for i in range(0,len(list2)):
        print("|",list2[i],end=' | ')
        checkNum(i)
    print("\n")
    a=input("마음에 드는 숫자가 있나요?(있으면o,없으면x)\n")
    if checkType(a):
        print("잘못입력하셧습니다 다시시작할게요")
        continue;
    guessNum(a,result)
    
    for i in range(0,len(list3)):
        print("|",list3[i],end=' | ')
        checkNum(i)
    print("\n")
    a=input("마음에 드는 숫자가 있나요?(있으면o,없으면x)\n")
    if checkType(a):
        print("잘못입력하셧습니다 다시시작할게요")
        continue;
    guessNum(a,result)
    
    for i in range(0,len(list4)):
        print("|",list4[i],end=' | ')
        checkNum(i)
    print("\n")
    a=input("마음에 드는 숫자가 있나요?(있으면o,없으면x)\n")
    if checkType(a):
        print("잘못입력하셧습니다 다시시작할게요")
        continue;
    guessNum(a,result)
    
    for i in range(0,len(list5)):
        print("|",list5[i],end=' | ')
        checkNum(i)
    print("\n")
    a=input("마음에 드는 숫자가 있나요?(있으면o,없으면x)\n")
    if checkType(a):
        print("잘못입력하셧습니다 다시시작할게요")
        continue;
    guessNum(a,result)
    break;
mSum=0
for i in range(0,len(result)):
    mSum+=pow(2,i)*result[i]
print("당신의 숫자:",mSum,"입니다.")
