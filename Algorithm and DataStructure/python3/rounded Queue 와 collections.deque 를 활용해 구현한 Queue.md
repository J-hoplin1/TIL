1. 일반적인 rounded queue

  ```python
  from typing import Any


class roundedQue(object):
    
    def __init__(self, capacity):
        self.front = 0 # 큐의 front의 index Value
        self.rear = 0 # 큐의 rear의 index Value
        self.dataAmount = 0 # 큐 내 데이터 개수
        self.capacity = capacity # 큐의 최대 개수 
        self.que = [None] * self.capacity # 큐 본체

    #큐가 비었을 경우에 대한 예외클래스
    class QueueEmpty(Exception):
        pass
    #큐가 가득 찼을 경우에 대한 예외 클래스
    class QueueFull(Exception):
        pass 
    
    # isEmpty : 큐가 비었는지를 반환, boolean
    def isEmpty(self) -> bool:
        return self.dataAmount <= 0
    
    # isFull : 큐가 가득 찼는지를 반환, boolean
    def isFull(self) -> bool:
        return self.dataAmount >= self.capacity
    
    # enque : 큐에 데이터를 넣는 메소드, None
    def enque(self,data):
        if self.isFull():
            raise roundedQue.QueueFull
        else:
            self.que[self.rear] = data
            self.rear += 1
            self.dataAmount+=1
            if self.rear >= self.capacity: # rounded Queue이므로
                self.rear = 0
    
    # deque : 큐에서 데이터를 꺼내는 메소드, Any
    def deque(self) -> Any:
        if self.isEmpty():
            raise roundedQue.QueueEmpty
        else:
            returnValue = self.que[self.front]
            self.que[self.front] = None
            self.front += 1
            self.dataAmount -=1
            if self.front >= self.capacity:
                self.front = 0
            return returnValue
    
    # peek : 큐의 가장 앞쪽의 데이터를 반환한다
    def peek(self) -> Any:
        if self.isEmpty():
            raise queue.isEmpty
        else:
            return self.que[self.front]
    
    #find : 큐의 parameter로 건네온 데이터의 첫번째로 나오는 index를 찾는다.
    def find(self,searchData) -> Any: 
        for t in range(self.dataAmount):
            logicIndex = (t + self.front) % self.capacity
            if self.que[logicIndex] == searchData:
                return self.que[logicIndex]
        return -1

    def count(self,searchData):
        count = 0
        for t in range(self.dataAmount):
            logicIndex = (t + self.front) % self.capacity
            if self.que[logicIndex] == searchData:
                count += 1
        return count
    
    # 매직메소드 __contains__ : in 연산자를 사용할 수 있도록 해준다
    def __contains__(self,value):
        return self.count(value)

    def clear(self):
        self.front = self.rear = self.dataAmount = 0
        self.que = [None for _ in range(self.capacity)]
    
    def dump(self):
        if self.isEmpty():
            raise queue.QueueEmpty
        else:
            print(*self.que, end='  ')
  ```
 
2. collections.deque를 활용해 구현한 Queue

  ```python
  '''
collections.deque를 이용해서 Queue를 구현해보자

collections.deque의 특징은 내부적으로 doubly 링크드 리스트로 표현이 된다.
양 끝 모두 접근이 가능하다. 하지만 deque의 가운데 부분 검색, 삽입, 제거는 느리다.

collections.deque의 주요 속성 및 함수 및 메소드

maxlen속성 : deque의 최대 크기를 나타내는 속성으로 읽기 전용이다. 크기 제한이 없으면 None이다.

append(x) : 흔히 아는 append

appendleft(x) : deque의 왼쪽에 x값을 append 해준다

clear() : deque의 모든 원소 삭제, 크기 0으로

copy() : deque의 얕은 복사 실행

count(x) : deque안에 x와 같은 원소의 개수를 반환

index(x) : deque안에 있는 x 가운데 가장 앞쪽에 있는 원소의 위치 반환

insert(i, x) : x를 deque의 i 위치에 삽입한다. 크기제한있는 deque인 경우 maxlen을 초과하게되면 IndexError 을 반환

pop() : pop연산

popleft() : pop연산을 왼쪽에 대해 실행

remove(value) : value의 첫번째 항목 삭제, 원소 없는 경우 ValueError 내보낸다.

reverse() : deque의 원소를 역순으로 재정렬, None 반화

'''

from typing import Any

class queue(object):

    def __init__(self,capacity):
        self.capacity = capacity
        self.que = deque([],self.capacity)
    
    #큐가 비었을 경우에 대한 예외 클래스
    class QueEmpty(Exception):
        pass

    class QueFull(Exception):
        pass
    
    def isEmpty(self):
        return not self.que # 비었을 경우 True 반환 아닌 경우 False반환
    
    def isFull(self):
        return len(self.que) >= self.que.maxlen
    
    def enque(self,data):
        if self.isFull():
            raise queue.isFull
        else:
            self.que.append(data)
    
    def deque(self):
        if self.isEmpty():
            raise queue.isEmpty
        else:
            return self.que.popleft()
    
    def peek(self):
        if self.isEmpty():
            raise queue.isEmpty
        else:
            return self.que[0]
    
    def count(self,searchData):
        self.que.count(searchData)
    
    def find(self,searchData):
        self.que.index(searchData)
    
    def __contains__(self,value):
        return self.count(value)
    
    def dump(self):
        if self.isEmpty():
            raise queue.isEmpty
        else:
            print(*self.que, end=' ')
  ```

3. Queue를 구현할때 기본/외부 클래스 사용하는 두가지 방법과 그중 collections.deque를 사용하는 이유

  - 사실 Queue를 지원하는 경우 두가지 방법이 있다고한다.
    
    - collections.deque를 사용하는 방법
    
    - queue.queue를 사용하는 방법
  
  - 당장 저 두개만 보고 판단하면 일반적으로 queue.queue를 사용하는게 맞지 않을까? 라는 생각이 들 수 있다.하지만
  결론은 반대로 queue를 구현할때는 collections.deque를 사용하는게 맞다고 한다.
  
  - 이유는 deque는 각 명령을 O(1)로 지원하는 반면 [queue.queue모듈은 멀티쓰레드 환경을 지원](https://docs.python.org/ko/3/library/queue.html)하기 때문에 더 느리다고 한다.
  
  - 그리고 collections.deque는 시작점의 값을 넣고 빼거나 끝점의 값을 넣고 빼는데 최적화된 연산속도를 제공하여 리스트보다 훨씬 월등한 옵션을 지니고 있다고 한다.
  
  - 결론적으로 코딩테스트 혹은 속도가 관건인 Queue를 구현할 때는 rounded queue의 구현보다 collections.deque를 통한 구현이 더 효율적이다.
  
  - Rounded Queue와 Collections.deque간의 차이 체감 문제
  
    - 큐1 : https://www.acmicpc.net/problem/10845
    
    - 큐2 : https://www.acmicpc.net/problem/18258
