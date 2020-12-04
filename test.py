# 20201204 wecode - git test
# 1 ~ 50의 자연수 중 짝수를 구하는 함수 생성하기

numList = list(range(1, 50))
answer = []

def getEven(numList):
    for i in numList:
        if i % 2 == 0:
           answer.append(i)

    return answer



getEven(numList)
