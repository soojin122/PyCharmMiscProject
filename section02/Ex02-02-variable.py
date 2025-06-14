""" 파일명: Ex02-02-variable

변수(variable)
    데이터를 저장하는 컨테이너(상자)로, 값에 이름을
    붙여 나중에 쉽게 사용할 수 있게 해준다

    메모리의 특정 위치에 이름을 붙여서, 그곳의 저장된 데이터에 쉽게
    접근할 수 있게 해준다

변수명 규칙
    영문, 한글, 숫자, 밑줄(_)로 구성된다.
    특수문자(!@#$%^&*()_+ 등) 사용할 수 없다.
    대문자 소문자를 구분한다.
    변수명의 첫 글자를 숫자로 사용할 수 없다.
    키워드(list, dict, if, fo, and ... 등) 사용할 수 없다.
"""

# 변수 선언방법: 변수명 = 값
name = 'Alice'
print(name)
age = 25
print(age)
address = '''우편번호 12345
서울시 영등포구 여의도동 123-45
'''
print(address)

'''
잘못된 변수명 예시
'''
# 2mybar = 'Python1'
# my-var = 'Python2'
# my var = 'Python3'

'''
여러 값 할당
    Python을 사용하면 한줄에 여러 변수에 값을 할당할 수 있다.
'''
x, y, z = '피카츄', '라이츄', '파이리'
print(x)    # Ctrl + d 줄복사
print(y)
print(z)


'''
여러 변수에 대한 하나의 값
    한줄에 여러 변수에 동일한 값을 할당할 수 있다.
'''
x = y = z = '꼬부기'
print(x)
print(y)
print(z)

x = '잠만보'
print(x)








