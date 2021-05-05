아침에 손풀겸 [백준 9613번](https://www.acmicpc.net/problem/9613) 문제를 풀었다. 우선 문제를 보면 다음과 같다.

  - 문제 : 양의 정수 n개가 주어졌을때 가능한 모든 쌍의 GCD합을 구하는 프로그램 작성하시오
  
  - 입력 : 첫째 줄에 테스트 케이스의 개수 t (1 ≤ t ≤ 100)이 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있다. 각 테스트 케이스는 수의 개수 n (1 < n ≤ 100)가 주어지고, 다음에는 n개의 수가 주어진다. 입력으로 주어지는 수는 1,000,000을 넘지 않는다.
  
이제 문제를 풀면서 생각했던것들을 나열해봅시당
 
   1. 우선 당연히 GCD문제이기 떄문에 GCD함수를 Recursion을 이용해서 구해보자
   
   ```python
   def gcd(x,y):
    if y % x == 0:
        return x
    else:
        return gcd(y % x,x)
   ```
   
   2. 그 다음에 각 case에 대해 고려해보자. 우선 각 숫자들끼리의 조합(combination)을 해주어야한다. 경우의 수는 우선 nC2(n : 총 숫자개수, 2 : 두개끼리 묶으니)
   
   3. 이때 든 생각은 다음과 같다. 아니 이거 잘못하면 3중 for문 되겠는데?(1,2학년떄 2중 for문 썼다 데였던적이 많아 그로인한 ptsd가 많음)
      문제 성격상 2중 for문은 어쩔수 없다라는 생각이었지만 3중 for문을 굳이 가고싶지는 않았다.(O(n^2)도 하기싫은데 O(n^3)은 ㅗㅜㅑ;)
   
   4. 고민을 하던중 [itertools](https://python.flowdas.com/library/itertools.html)라는 모듈이 떠올랐다 itertools는 iterator 빌딩 블록을 구현하는 모듈이다.
      이중에서 combinations라는 모듈을 사용해 볼 것이다.이 combinations라는 모듈은 두개의 parameter를 받는다 
      
      - parameter1 : iterator(리스트,튜플 등)
      
      - parameter2 : r길이만큼 튜플로 원소들을 묶는다(r개씩). 추가적으로 반복되는 요소는 없다
      
      자 그럼 테스트를 해봅시다
      ```python
      import itertools as i
      
      a = [1,2,3,4,5,6,8,7,10,9]
      for p in list(i.combinations(a,2)):
          print(f'{p[0]} {p[1]}')
      ```
   5. 이제 이를 활용해 문제를 풀어보자
   
     ```python
     import sys
     import itertools as it

     def gcd(x,y):
         if y % x == 0:
           return x
         else:
           return gcd(y % x,x)

     count = int(sys.stdin.readline())

     for r in range(count):
         totalGCDSum = 0
         inp = list(map(int,sys.stdin.readline().split()))
         nums = inp[1:]

         for i in list(it.combinations(nums,2)):
             totalGCDSum += gcd(i[0],i[1])
         print(totalGCDSum)
     ```
      
