class Person:
    def __init__(self,id="",passwd=""):
        self.id=id
        self.passwd=passwd
    def setId(self,id):
        self.id=id
    def setPasswd(self,passwd):
        self.passwd=passwd
    def getId(self):
            return self.id
    def getPasswd(self):
        return self.passwd
    
   # 콘솔에서 실행하려면 메인이 있어야 한다.
if __name__=="__main__" :
    kim=Person()
    kim.setId("aaa")
    kim.setPasswd("111")
    print("아이디 : " +kim.getId())
    print("비밀번호 : "+kim.getPasswd())