
# coding: utf-8

# In[ ]:


# 파이썬은 참이어도 거짓이어도 실행된다.
# 제어문
# 조건문
'''
if (조건){참;}
else {거짓;}

if 조건:
    참
elif 조건:
    참
else :
    거짓
    
파이썬은 스위치가 없다.

switch(조건){
case 값: 실행문; break;
case 값: 실행문; break;
...
default: 실행문;
}
'''
print()


# # num=int(input("정수: "))
# if num>5:
#     print("크다") #참
# else :
#     print("작다") #거짓
#     
# if num<5:
#     print("작다") # 참
# else:
#     print("크다") # 거짓

# In[ ]:


num = int(input("정수: "))

if num%2==0:
    print("짝수")
else:
    print("홀수")


# In[ ]:


# Y나 y가 입력되면 "계속"  출력 그 외에는 "종료" 출력
yn= input("계속 할거냐[Y/y]:")
if yn=="Y" or yn=="y":
    print("계속")
else:
    print("종료")


# In[ ]:


score=int(input("점수: "))
if score >= 90 and score <= 100:
    print("A학점")
if score >= 80 and score < 90:
    print("B학점")
if score >= 70 and score < 80:
    print("C학점")
if score >= 60 and score < 70:
    print("D학점")
if score >=0 and score < 60:
    print("F학점")


# In[2]:


# 단점: 범위에 없는 값을 입력하면 a학점이나 f학점이 나온다.

score=int(input("점수: "))
if score>=0 and score <=100:
    if score >=90:
        print("A학점")
    elif score>=80:
        print("B학점")
    elif score>=70:
        print("C학점")
    elif score>=60:
        print("D학점")
    else:
        print("F학점")
else:
    print("0부터 100사이만 입력하세요")

