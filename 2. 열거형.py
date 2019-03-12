
# coding: utf-8

# In[8]:


# 거듭제곱 연산자
print (5**3)

# 부호, 1의 보수연산자, 2의 보수 연산자
print(3-5)
print(+3+-5)

a=5
print(~a)# 1의 보수 연산자
print(~a+1)
print(-a) # 2의 보수 연산자

# 산술연산자
print(5 / 2) 
print(5/2.0)
print(5//2) #몫
print(5%1) #나머지


# In[29]:


a=12
b=20
print(a & b)
print(a | b)
print(a ^ b)

# 논리연산자
print( True and True )
print( False and True)
print(True and False)
print(False and False)

# 짧은 조건문
True and print("True and")
False and print("False and")
True or print("True or")
False or print("False or")

# 비교연산자
a, b=2, 2
print(a==b)
print(a!=b)
print(a>b)
print(a<b)

# 뒤의 단어에 앞의 단어가 포하되어 있는지?
print("H" in "Hello Python!!!")
# 소대문자는 다른 것으로 취급한다.


# In[54]:


# is == 참조값을 얘기 하는 것이다.
# is not !=
# print(12345==12345)
a="123"
b="123"

print(a is b)
print(a == b)
print("a : "+str(hex(id(a))))
print("b : "+str(hex(id(b))))
print("="*15)
c="HelloPython!!!"
d="HelloPython!!!"

#주소비교
print(c is d)

# 값 비교
print(c==d)
print("c : "+str(hex(id(c))))
print("b : "+str(hex(id(d))))
# 다른언어에서는 메모리를 하나만 만들지만 파이썬에서는 메모리를 두개 만든다. ==등호 사용시 주소비교를 해버리기 때문에 실제론 데이터 
# 비교를 해야 한다.
# 간단한 문자열은 주소값이 같다고 나오는데 긴문자열의 경우 다르다고 나온다. 


# In[55]:


a="동해물과 백두산이 마르고 닳도록"
b="""
동해물과 백두산이
마르고 닳도록
"""


# In[61]:


# 이런 연산은 문자열만 가능한 것이지, 숫자의 경우 에러가 난다. 
print("ABC"+"DEF")
print("ABC","DEF")
print("abc""def")

# print("ABC"+10) 이런 수식은 안된다.
print("ABC"+str(10)) # 숫자로 변환해야 한다.


# In[78]:


name="홍길동"
age=30
print("이름: "+name+"\t"+"나이: "+str(age) ) #age를 형변환 해줘야 한다.

# print는 기본적으로 줄바꿈이 포함되어 있다.
print("이름: "+name)
print("나이: "+str(age))

print("이름: "+name, end="\t") # 출력시 옆에 나란히 찍고 싶으면 end속성을 주면 된다.
print("나이: "+str(age))
print("이름: %s\t나이: %d" %(name, age)) # 변환문자, 자바의 출력방식인데 파이썬에서도 지원하는것

# format형식
print("이름: {0}\t 나이: {1}".format(name, age))
print("이름: {name}\t 나이: {age}".format(name="이순신",age=40))

# 실수를 출력할대는 %f라고 출력한다.
a=12345.6789
print("실수: %f" %(a))
print("실수: %10.2f" %(a)) # 전체는 10자리 인데 소수점은 2자리까지
print("실수: %0.2f" %(a)) # 데이터가 있으면 전체자리는 무시하고 소수점은 2자리까지
print("실수: %.2f" %(a)) # 데이터가 있으면 전체자리는 무시하고 소수점은 2자리까지 0은 어차피 신경안쓰니까


# In[83]:


# 정렬
b="Hello"
print("{0}".format(b))
print("{0:20}".format(b)) # 전체 출력을 20까지 무겠다 
print("{0:<20}".format(b)) # 왼쪽정렬
print("{0:>20}".format(b)) # 오른쪽정렬
print("{0:^20}".format(b)) # 가운데 정렬
print("{0:=^20}".format(b)) # =를 20개 출력
print("{0:-^20}".format(b)) #  - 를 20개 출력


# In[94]:


# 슬라이싱 0부터 시작한다.
s="Hello Python!!"
print(s)
print(s[6:])
print(s[:5])
print(s[-6:])
print(s[0:5])
print(s[0:-1]) #한자리 빼고 다 찍기
print(s[:]) # 문자 전체 출력


# In[115]:


str= "Hello World!"

print(len(str)) # 문자가 몇개있니?
print(str.count("!")) # 문자안에 !가 몇개 들어있니?
print(str.find("o")) #  문자안에 o가 4번째에 있다.
print(str.find("h")) #  문자안에 h가 -1번째에 있다.
print(str.find("lo")) #  문자안에 lo가 3번째에 있다.

print(",".join(str)) # 문자하니글자 마다 ,를 줘라!
print(str.upper()) # 문자를 대문자로 바꿔
print(str.lower()) #문자를 소문자로 바꿔라!
print(str.capitalize()) # 첫글자만 대문자로 바꿔라!

str="    a    a    a    a"
print(str) # 공백도 문자로 인식한다.
print(str.lstrip()) # 왼쪽의 트림제거
print(str.rstrip()) # 오른쪽의 트림제거
print(str.strip()) # 양쪽의 트림제거

str="aaa1234"
print(str.isalnum())
print(str.isalpha())
print(str.isdigit()) # 전부다 숫자니?

str="a,b,c,d,d"
print(str.split(",")) # , 기준으로 문자열을 자르자 . CSV처리에 유용하다.


# In[30]:


# 리스트
fruits = [ "apple", "pear", "banana", "mango", "orange" ]
print( list )
print( fruits[0] )
print( fruits[:] )
print( fruits[1:3] )
print( fruits[-1] )
for fruit in fruits : 
    print( fruit )
    
print( "요기요기>>"+ fruits[3][0] )
print( fruits[4][1:5] )

print( len( fruits ) )
print( max( fruits ) )
print( min( fruits ) )

fruits.append( "apple" )
print( fruits.count( "apple" ) )
print( fruits.index( "mango" ) )
print( fruits.insert( 2, "kiwi" ) )

print("pop: "+ fruits.pop() )
print( fruits.remove("kiwi" ) )
print( fruits[:] )
fruits.sort()
print( fruits[:] ) 


# In[31]:


f=["apple","pear","banana"]
g=["mango","orange","kiwi"]
f.append(g)
print(f[:])
print(f[3][2])


# In[45]:


# 튜플 - 추가 삭제가 불가능하다.
pets=("dog","cat","mouse","fish","spider")
print(pets)
print(pets[0])
print(pets[1:3])

# pets=pets, "monkey" # 추가가 아닌 새로 만든 것이다. 
# pet +="monkey" # 
# print(pets)

s="ABC"
s+="DEF"
print(s)

animal=list(pets) # pets을 list로 변경하면 추가 삭제가 가능하다.
animal+=["fly"]
print(animal)

pets=tuple(animal)
print(pets)

a,b,c,d,e,f=pets
print(a)


# In[68]:


# dictionary 사전 - Map
# 반복문을 돌릴수 없다.

url={
    "naver" : "www.naver.com",
    "daum" : "www.daum.net",
    "google" : "www.google.co.kr",
    "nate" : "www.nate.com",
    "encore" : {
    "first" : "www.encore.com",
    "second" : "www.playdata.com"
    }
}
print(len(url))
print(url["daum"])
print(url.get("naver"))

# key들 뽑아오기
print(type(url.keys()))
print(type(url.values()))
print(type(url.items()))


# key for문
for key in url.keys():
    print(key)
    
for value in url.values():
    print(value)
   
for item in url.items():
    print(item[0],":",item[1])    

print(url.get("encore")["first"])
print(url.get("encore").get("second"))
email=dict([2,4,6,7],["kim","lee","park","hong"])


# In[80]:


# set
countries= set(["korea","china","japan","vietnam"])
print(len(countries))
# print(countries[0]) # 불가능하다. set이기에
nations=countries.copy()
countries.remove("japan")
countries.remove("china")
countries.add("bhutan")
countries.add("thailand")
print(countries)
print(nations)

# 파이썬에만 있는 합집합이다.
union=countries | nations
print(union)
# 교집합
inter=countries & nations
print(inter)
# 차집합 (-교집합)
minus=countries - nations
print(minus)


# In[5]:


# 입력
a=input("정수입력: ")
b=input("정수 입력: ")
    
print(eval(a) + eval(b))
        


# In[11]:


print("5+2")
print(eval("5+2"))
print(eval("1.2*1.3"))

