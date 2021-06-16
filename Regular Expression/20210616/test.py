import re


strings = ['sales1.xls','order3.xls','apac1.xls','na1.xls','na2.xls','sa1.xls','europe.xls','ca1.xls']

patterns = re.compile('[ns]a.\.xls')

for i in strings:
    print(patterns.search(i))

    
'''
python Regular Expression

re 모듈을 이용하여 정규표현식을 사용할 수 있다.

re.compile('정규표현식') : 기본적으로 검사할 정규표현식 패턴을 저장하는 곳이다.

re.match() : 문자열 '처음부터' 패턴과 매칭되는지 검사한다.

re.search() : 문자열 '전체'를 검사하여 매칭되는 패턴이 있는지 검사한다
'''