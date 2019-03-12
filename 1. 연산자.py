
# coding: utf-8

# In[ ]:


import keyword
print( keyword.kwlist )
print(len(keyword.kwlist))


# In[7]:


import keyword
print( keyword.kwlist )
print(len(keyword.kwlist))


# In[ ]:


a=10
print( type(a))
a="abc"
print( type(a))

b=10.5
print( type(b))
c=123456789123456789
print( type(c))
d=10+10j
print( type(d))
print( type("abc"))
print( type('abc'))
e='a'; print(e)

f="asdfzxcv"#한줄이 넘어간다면 문자 끝에 역슬래쉬를 붙여 줘야 한다.
print(f)

g="abc"
print(g)

# a=10; b=20
a,b=10,20
a,b=b,a  #교환
# 파이썬은 리턴값을 여러개 줄 수 있다.
get_ipython().run_line_magic('who', '')
del a,b
get_ipython().run_line_magic('who', '')
get_ipython().run_line_magic('pinfo', 'c')
help c? 


# In[24]:


# 형변환
a=10

print( type( float(a)))
print(( float(a)))

# float을 int로 변환시 소수점 아래가 잘린다.
b=10.5
print( type(int(b)))
print( int(b))

c=65
print(c)

print(chr(c))

print(str(c))

d=66
print(c+d)
# 숫자를 문자로 변환해서 더하면 문자 결과가 나온다.
print(chr(c)+chr(d))
# 원래 문자열+문자열 불가능함
# 
print("65"+"66")
print('65'+'66')
# 문자열 뒤에 더하기는 붙여라는 뜻이다.
print("c : "+str(c)+"\t"+"d : "+str(d) )


# In[25]:


# 진수 변환
a=20
print(bin(a))
print(oct(a))
print(hex(a))


# In[31]:


print(5/2.0)
print(5//2)

if 1:
    print("진실")
else:
    print("거짓")

