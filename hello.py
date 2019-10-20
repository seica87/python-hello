# print('hello Py!!!!')
# print("hello world!!!!!!!!!!!!!!!!")
# print("git!!!!!!!!!!!!!!!!!!!!!!!")

# dup = 1
# while dup <=10:
#      print(dup)
#      dup = dup+1


#prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit

# Enter number : """
# number = 0
# while number != 4:
#      print(prompt)
#      number = int(input())


# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())
#     print('*' * 79)
#     print("your input nuber : {}".format(number))
#     print('*' * 79)

# import time
# while True:
#     print("컨트롤+C를 눌러 빠져나오세요.")
#     time.sleep(1)

# lst = [1,10]

# for a in lst:
#     print(a)

# scores = [100, 90, 80, 70, 100]

# tot=0

# for score in scores:
#     tot = tot + score

# avg = tot / len(scores)

# print("총점은 {}점 입니다.".format(tot))
# print("평균은 {}점 입니다.".format(avg))

# for i in range(1,101):
#     print(i)

# star = ("*")
# num = 0
# while num < 5:
#     num = num + 1
#     print(star*num)

# for a in range(1,6): print(star*a)

# 더하기 함수
# def add(a, b):
#     return a + b

# c = add(10, 10)

# print(c)

# 빼기 함수
# def sub(a, b):
    
#     return a + b

# c = sub(20, 10)
# print(sub)

# 연습하기
# def add_mul(choice, *args):
#     result = 0
#     if choice == "add":
#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result

# c = add_mul("b", 1,2,3,4)
# print(c)

#



# f = open("newfile.txt", 'a')
# f.write('good bye')
# f.close()

# f = open("newfile.txt", 'w')
# for i in range(10):
#     f.write('{} Line.\n'.format(i+1))
# f.close()

# f = open('newfile.txt')

# e = open('sq19-sa-04 - 10.50.0.14.log')

# while True:
#     line = e.readline()
#     print(line)

#     if not line:
#         break

# line = f.readline()
# print(line)

# log = e.readlines()
# print(log)

# for i in log:
#     print(i)



# f.close()
# e.close()


# f = open('newfile.txt', 'a')

# for i in range(11, 20):
#     line = '{} line\n'.format(i)
#     f.write(line)

# f.close

# with open('newfile.txt') as f:
#     print(f.read())


# import sys

# args = sys.argv[1:]

# for i in args:
#     print(i)



# def is_odd(a):
#     tnf = a % 2
#     if tnf == 0:
#         print('짝수입니다.')
#     else:
#         print('홀수입니다.')

# print('종료 하려면 0을 입력하세요.')
# while True:
#     a = int(input('숫자를 입력하세요\n:'))
#     if a == 0:
#         break
#     is_odd(a)



print('## 1번 문제')
a = 80
b = 75
c = 55

print((a+b+c)/3)

print('## 2번 문제')
자연수 = 2
one = 자연수 % 2

if one == 0:
    print('짝수인뎁쇼?')
else:
    print('홀수입니다만?')

print('## 3번 문제')
홍길동 = '881120-1068234'
생년월일 = 홍길동[:6]
식별번호 = 홍길동[7:]

print('생년월일은 {}'.format(생년월일))
print('식별변호는 {}'.format(식별번호))

print('## 4번 문제')
print(홍길동[7])


print('## 5번 문제')
replace = "a:b:c:d"
print(replace.replace(':', '#'))


print('## 6번 문제')
listnum = [1, 3, 5, 4, 2]
listnum.sort()
listnum.reverse()
print(listnum)

print('## 7번 문제')
life = " ".join(['life', 'is', 'to', 'sort'])
print(life)

print('## 8번 문제')
tupa = (1, 2, 3)
tupb = (4,)
print(tupa + tupb)

print('## 9번 문제')
dica = dict()
dicb = dict()
dicc = dict()
dicd = dict()
dica['name'] = 'python'
dicb[('a',)] = 'python'
# dicc[[1]] = 'python' 리스트는 변하는 값이므로 딕셔너리에서 사용할 수 없다.
dicd[250] = 'python'

print(dica)
print(dicb)
# print(dicc)
print(dicd)

print('## 10번 문제') 
trace = {'a':90, 'b':80, 'c':70}
pop = trace.pop('b')
print(trace)
print(pop)

print('## 11번 문제') 
rm = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5]
rmm = set(rm)
rmmm = list(rmm)
print(rmmm)

print('## 12번 문제')

first = second = [1, 2, 3]
second[0] = 4
print(first)


## 오늘은 MAC개발 환경 셋팅