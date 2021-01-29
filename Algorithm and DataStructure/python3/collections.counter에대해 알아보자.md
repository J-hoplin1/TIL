collections모듈과 collections.Counter
===
***

### Collections 

- collections는 파이썬 범용 내장 컨테이너인 dictionary, list, set, tuple에 대한 대안을 제공하는 특수 컨테이너 데이터형들을 구현한다.

- 종류에는 다음과 같은것들이 있다.

|함수 혹은 메소드|설명|
|:---:|:---:|
|namedtuple()|이름 붙은 필드를 갖는 튜플 서브 클래스를 만들기 위한 팩토리 함수|
|deque|양쪽 끝에서 빠르게 추가 삭제를 할 수 있는 리스트류 컨테이너|
|ChainMap|여러 매핑의 단일 뷰를 만드는 딕셔너리류 클래스|
|Counter|해시 가능한 객체를 세는데 사용하는 딕셔너리 서브 클래스|
|OrderedDict|항목이 추가된 순서를 기억하는 딕셔너리 서브 클래스|
|defaultdict|누락된 값을 제공하기 위해 팩토리 함수를 호출하는 딕셔너리 서브 클래스|
|UserDict|더 쉬운 딕셔너리 서브 클래싱을 위해 딕셔너리 객체를 감싸는 래퍼|
|UserList|더 쉬운 리스트 서브 클래싱을 위해 리스트 객체를 감싸는 래퍼|
|UserString|더 쉬운 문자열 서브 클래싱을 위해 문자열 객체를 감싸는 래퍼|

### collections.Counter()

- Counter는 해시 가능한 객체를 세기 위한 딕셔너리 서브 클래스이다. key로는 각 요소가 되고 value로는 key의 개수들이 된다.

- 또한 Counter객체끼리는 subtract이 가능하다.

- 예시 코드

    ```python3
    from collections import Counter
    a = [1,1,1,1,2,2,2,1,1,1,2,2,2,3,3,3,3]

    b = [1,1,1,1,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2]

    print(f'{Counter(a)}\n{Counter(b)}\n{Counter(a) - Counter(b)}')

    '''
    Result

    Counter({1: 7, 2: 6, 3: 4})
    Counter({3: 10, 2: 8, 1: 4})
    Counter({1: 3})
    '''
    ```
