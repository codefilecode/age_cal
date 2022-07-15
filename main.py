def knowage():
    age = int(input("나이를 입력해주세요 : "))
    print("기준 년도를 적어주세요")
    year = int(input())

    yearA = year - age # 생일전년도
    yearB = year - age + 1 # 생일후년도
    ageA = year - yearA # 생일전
    ageB = year - yearB # 생일후
    iyearA = year - age + 1 # 세는나이 연도

    print(year,"년을 기준으로 만 나이는 다음과 같습니다.")
    print("생일전 생일년도: %d년생" % yearA)
    print("생일후 생일년도: %d년생" % yearB)
    print("생일전 나이: %d세" % ageA)
    print("생일후 나이: %d세" % ageB)
    print(year,"년을 기준으로 세는 나이는 다음과 같습니다.")
    print("생년년도: %d년생" % iyearA)
    print("나이: %d세" % age)

def knowageyear():
    print("만나이는 %d세 입니다.")
    print("한국식 세는 나이는 %d세 입니다.")
def knowagemouth():
    print("만나이는 %d세 입니다.")
    print("한국식 세는 나이는 %d세 입니다.")
def knowageday():
    print("만나이는 %d세 입니다.")
    print("한국식 세는 나이는 %d세 입니다.")


print(" === 만나이 계산기 === ")
print("다음중 어느것에 해당하십니까?")
print("1 : 나이만 알고 있음")
print("2 : 년도만 알고 있음")
print("3 : 년도 월만 알고 있음")
print("4 : 년월일을 알고 있음")
j = int(input())

if(j == 1):
    knowage()
elif(j == 2):
    knowageyear()
elif(j == 3):
    knowagemouth()
elif(j == 4):
    knowageday()
