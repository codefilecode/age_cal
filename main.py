def knowage(i):
    yearA = year - i # 생일전년도
    yearB = year - i - 1 # 생일후년도
    ageA = year - yearA # 생일전
    ageB = year - yearB # 생일후
    iyearA = year - i + 1 # 세는나이 연도 # 1번 라인

    print("기준 년도를 적어주세요")
    year = int(input())

    print(year,"년을 기준으로 만 나이는 다음과 같습니다.")
    print("생일전 생일년도: %d년생" % yearA)
    print("생일후 생일년도: %d년생" % yearB)
    print("생일전 나이: %d세" % ageA)
    print("생일후 나이: %d세" % ageB)
    print(year,"년을 기준으로 세는 나이는 다음과 같습니다.")
    print("생년년도: %d년생" % iyearA)
    print("나이: %d세" % i)

def knowageyear(i): # 2번 라인
    ageA = year - yearA # 생일전
    ageB = year - yearB # 생일후

    print("기준 년도를 적어주세요")
    year = int(input())
    print(year,"년을 기준으로 만 나이는 다음과 같습니다.")
    print("생일전 생년월일: %d세" % ageA)
    print("생일후 생년월일: %d세" % ageB)
def knowagemouth(i):

def knowageday(i):



print(" === 만나이 계산기 === ")

age = int(input("나이를 입력해주세요 : "))

print("다음중 어느것에 해당하십니까?")
print("1 : 나이만 알고 있음")
print("2 : 나이와, 년도만 알고 있음")
print("3 : 년도 월만 알고 있음")
print("4 : 년월일을 알고 있음")
j = int(input())

if(j == 1):
    knowage(age)
elif(j == 2):
    knowageyear(age)
elif(j == 3):
    knowagemouth(age)
elif(j == 4):
    knowageday(age)
