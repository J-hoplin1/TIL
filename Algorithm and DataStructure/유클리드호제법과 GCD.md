1. 유클리드 호제법이란?
===

 유클리드 호제법이란 2개의 자연수의 최대공약수를 구하는 알고리즘이다. 여기서 '호제법' 이란 두 수가 서로 상대방 수를

나누어 결국 원하는 수를 얻는 알고리즘을 의미한다.

예를 들어 a > b라고 할때

a를 b로 나눈 나머지를 r이라고 하면

b와 r의 최대공약수는 a와 b의 최대 공약수와 같다.

15와 6 라고 가정을하면 나머지는 3이된다

15와 6의 최대 공약수는 3, 6과 3의 최대공약수는 3이된다.

다시 b와 r을 나는 나머지인 r'이라고 하면

b와 r의 최대 공약수는 r r'의 최대 공약수와 같아진다(6,3 과 3,0 -> GCD : 3)

결론적으로 맨 마지막에 나오는 r r'의 나누기 나머지가 0이 될때 a와 b의 최대공약수가 나오는 것이다.

2. 관련 문제
===

URL : [https://www.acmicpc.net/problem/1934](https://www.acmicpc.net/problem/1934)


```python3
from typing import Any

'''
A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수

A,B의 최소공배수 구하기

'''
#유클리드 호제법을 사용한다.
#b가 a보다 큰 수라는 가정

# 결론적으로 두 수의 최소 공배수는 두 수의 곱  // 최대 공약수
def getGCD(a,b):
    if b % a == 0:
        return a
    else:
        return getGCD(b%a,a)

def getLCM(a,b) -> int:
    gcd = getGCD(a,b)
    return a * b // gcd

testCase = int(input())
result = []
for e in range(testCase):
    a,b = input().split()
    if int(a) > int(b):
        result.append(getLCM(int(b),int(a)))
    else:
        result.append(getLCM(int(a),int(b)))

for e in result:
    print(e)
```
