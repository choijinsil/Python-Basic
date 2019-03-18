
# coding: utf-8

# In[ ]:


# 제어문
# 조건문

'''
<if>
if( 조건 ) { 참; }
else { 거짓; }

if 조건 : 
    참
else 조건 : 
    거짓

<if else>
if( 조건 ){ 참; }
else if( 조건 ){ 참; }
...
else { 거짓; }

if 조건 : 
    참
elif 조건 : 
    참
...
else :
    거짓
    

switch(조건){
case 값 : 실행문;
case 값 : 실행문;
...
default : 실행문;
}

'''

print()


# In[ ]:


num = int( input( "정수 : " ) )
if num > 5 : 
    print( "크다" )    # 참
else :
    print( "작다" )    # 거짓
    
if num < 5 : 
    print( "작다" )    # 참
else :
    print( "크다" )    # 거짓


# In[ ]:


# 입력받은 값이 짝수면 "짝수" 출력 홀수면 "홀수" 출력
num = int( input( "정수 : " ) )
if num % 2 == 0 :
    print( "짝수" )
else : 
    print( "홀수" )


# In[ ]:


# Y나 y가 입력되면 "계속" 출력 그 외에는 "종료" 출력
yn = input( "계속할거냐[Y/y] : ")
if yn == 'Y' or yn == 'y' :
    print( "계속" )
else :
    print( "종료" )


# In[ ]:


score = int( input( "점수 : " ) )
if score >= 90 and score <= 100:
    print( "A학점" )
if score >= 80 and score < 90 :
    print( "B학점" )
if score >= 70 and score < 80 :
    print( "C학점" )
if score >= 60 and score < 70 :
    print( "D학점" )
if score >= 0 and score < 60 :
    print( "F학점" )


# In[ ]:


score = int( input( "점수 : " ) )
if score >= 0 and score <= 100 :
    if score >= 90 : 
        print( "A학점" )
    elif score >= 80 :
        print( "B학점" )
    elif score >= 70 :
        print( "C학점" )
    elif score >= 60 :
        print( "D학점" )
    else :
        print( "F학점" )
else :
    print( "0~100 사이만 입력하세요" )


# In[ ]:


# for
for i in range( 1, 10 ) :
    print( i, end="\t")
print()
for i in range( 10 ) :
    print ( i, end="\t")
print()
for i in range( 1, 11, 2) :
    print( i, end="\t")
print()
    
# 10 ~ 1
for i in range( 10, 0, -1) :
    print( i, end="\t")
print()

for i in range( 65, 91) :
    print( chr( i ), end="  ")
print()

# 1 ~ 10까지 합
sum = 0
for i in range( 1, 11 ) :
    sum += i
print( "합 :", sum )
# print( "합 : " + str( sum ) )

for i in range( 1, 10 ) :
    print( i , end="\t" )
else : 
    print( "반복문 끝" )
    


# In[ ]:


s = "ABCDE"
for ch in s :     # 열거형 - 문자열
    print( ch, end=" " )
print()

s = '''
3월 14일은 '콩팥의 날'이다.
콩팥은 몸속 노폐물을 걸러내 소변으로 배출하고
체액과 전해질을 정상으로 유지하는 기능을 한다.
콩팥이 망가지는 대표적인 병이 '만성콩팥병'이다.
3개월 이상 콩팥 기능이 떨어지는 질환으로
요독, 부종, 빈혈, 혈압 상승 등의 증상을 동반한다.
말기가 돼서야 증상이 나타나는데,
당뇨병이나 고혈압 등 위험 인자를 가지고 있는 환자는
반드시 정기적인 검사를 통해 콩팥 상태를 확인해야 한다.
'''
c = input( "찾을 문자 : " )
cnt = 0
for ch in s :
    if ch == c : 
        cnt += 1
print( "'" + c + "'" + "의 개수는 " + str(cnt) + "개" )


# In[ ]:


t = ( "홍길동", "김유신", "이순신", "대조영" )
for name in t :                 # 나열형 - 튜플
    print( name, end=" ")
print()

for i in range( 0, len(t), 2 ) : 
    print( t[i], end=" ")
print()


# In[ ]:


pets = [ "개", "고양이", "토끼", "거북이" ]
for pet in pets :               # 열거형 - 리스트
    print( pet, end=" ")
print()

for i in range( 0, len( pets ) ) : 
    print( pets[i], end=" " )
print()

# 리스트 축약
li = [ i for i in range( 1, 11 ) ]
l = [ i**2 for i in li if i%2==0]
print( l )


# In[ ]:


nations = set( [ "한국", "미국", "중국", "일본" ] )
for nation in nations : 
    print( nation, end=" " )
print()

# for i in range( 0, len(nations) ) :
#     print( nations[i], end=" ")
# print()

for i, nation in enumerate( nations ) :
    print( str( i ) + " : " + nation )
print()

for i, nation in enumerate( nations, 100) : 
    print( str( i ) + " : " + nation )
print()


# In[ ]:


# 다중 for문
# 리스트 - 튜플
lt = [ (1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12) ]
for t in lt : 
    print( t )
print()

for (a, b, c) in lt :    #리스트의 값이 튜플이면서 개수가 같을 때만 가능
    print( a, b, c)
print()

for t in lt : 
    for d in t :
        print(d, end=" ")
    print ()
print()

for i in range(0, len(lt) ) :     # 0 1 2 3
    for j in range( 0, len(lt[i]) ) :
        print(lt[i][j], end=" ")
    print ()
print()


# In[ ]:


scores = [ 34, 76, 39, 45, 68, 88, 92, 32, 85, 90]
# ~번 합격 ~번 불합격, 번호는 1번 부터
# 60점이상합격

for i in range( len( scores ) ) : 
    if scores[i] >= 60 :
        print("%02d번 합격" %(i+1))
    else :
        print("%02d번 불합격" %(i+1))
print()

for i,score in enumerate( scores, 1 ) : 
    if score >= 60 :
        print( str(i) + "번 합격")
    else :
        print( str(i) + "번 불합격")
print()


# In[ ]:


names = { 
    "a" : "홍길동",
    "e" : "김유신",
    "f" : "이순신",
    "c" : "대조영", 
    "h" : "강감찬" 
}

# keys()   [ "a", "e", "f", "c", "h"]
# values() [ "홍길동", "김유신", "이순신", "대조영", "강감찬" ]
# items()  [ ("a","홍길동"),("e","김유신"),("f","이순신"),("c","대조영"),("h","강감찬")]

for key in names.keys() : 
    print( "key : " + key )
    print( key + " : " + names.get( key ) )
print()
for value in names.values() : 
    print( value )
print()
for key, value in names.items() :
    print( key + ":" + value)
print()

# 딕셔너리 축약
li = [ i for i in range( 10 ) ]
print( li )

di = { i:i*2 for i in range( 10 ) }
print( di )


# In[ ]:


# while
for i in range( 1, 11 ) :
    print( i, end="\t" )
print()

i = 0
while i<10 :
    print( i, end="\t" )
    i += 1
else :
    print( i, end="\t")
print()

i = 0
while i<10 :
    i += 1
    print( i, end="\t" )
print()

i = 0
while True : 
    i += 1
    if i > 10 :
        break
    print( i, end="\t")
print()


# In[ ]:


# 다중 for
for i in range( 2, 10 ) :
    print( str(i) + "단" )
    for j in range( 1, 10 ) :
        print( str(i) + "*" + str(j) + " = " + str(i*j))
    print()
print()


# In[ ]:


for a in range( 2, 10 ) :
    print( str(a) + "단", end="\t")
print()

for i in range( 1, 10 ) :
    for j in range ( 2, 10 ) :
        print( str(j) + "*" + str(i) + "=" + str(i*j), end="\t")
    print()


# In[ ]:


import random
for i in range( 0, 6 ) :
    print( random.randint( 1, 45 ) )


# In[6]:


import random
a = random.randint(0, 9)
cnt = 1
while True :
    b = int( input( "값(0~9) : " ) )
    if b > a : 
        print("입력한 값이 큽니다.")
        cnt += 1
    elif b < a:
        print("입력한 값이 작습니다.")
        cnt += 1
    else : 
        break
print( str(cnt) + "번 만에 정답")

