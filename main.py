def knowage(i):
    print("년도를 적어주세요")
    year = int(input())

    print("태어난 년도는 %d년 ~ %d년입니다.")
    print("만 나이는 %d세 ~ %d세 입니다.")
    print("한국식 세는 나이는 %d세 입니다.")
def knowageyear():

def knowagemouth():

def knowageday():
    print("만나이는 %d세 입니다.")
    print("한국식 세는 나이는 %d세 입니다.")


print(" === 만나이 계산기 === ")

age = int(input("나이를 입력해주세요 : "))

print("다음중 어느것에 해당하십니까?")
print("1 : 나이만 알고 있음")
print("2 : 년도만 알고 있음")
print("3 : 년도 월만 알고 있음")
print("4 : 년월일을 알고 있음")
j = int(input())

if(j == 1):
    knowage(age)
elif(j == 2):
    knowageyear()
elif(j == 3):
    knowagemouth()
elif(j == 4):
    knowageday()
