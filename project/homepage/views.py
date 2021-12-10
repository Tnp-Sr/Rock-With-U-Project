from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Menu


#================= Global variable =================
checkLogin = 0
checkUser = 0
username = ''

#================= Class ================= 
class Stack:
    def __init__(self,lst = None):
        self.lst = lst if lst is not None else []
    def push(self,item):
        self.lst.append(item)
    def pop(self):
        self.lst.pop()
    def peek(self):
        return self.lst[-1]
    def size(self):
        return len(self.lst)
    def isEmpty(self):
        return len(self.lst) == 0
    def show(self):
        return self.lst
    def find(self,num):
        return self.lst[num]    

class Queue:
    def __init__(self,lst = None):
        self.lst = lst if lst is not None else []
    def size(self):
        return len(self.lst)
    def isEmpty(self):
        return len(self.lst) == 0
    def top(self):
        return self.lst[0]
    def enqueue(self,obj):
        self.lst.append(obj)
    def dequeue(self):
        return self.lst.pop(0)
    def show(self):
        return self.lst

class sorting:
    pass
#================= END Class ================= 




#================= การทำงาน ================= 

# Create your views here.
def index(request):
    return render(request,'index.html',
    {
        'checkLogin' : checkLogin,
        'username' : username
    })   

def menu_P1(request):
    return render(request,'menu1Recommend.html',
    {
        'checkLogin' : checkLogin,
        'username' : username
    })   

def menu_P2(request):
    return render(request,'menu2Beef.html',
    {
        'checkLogin' : checkLogin,
        'username' : username
    })   

def menu_P3(request):
    return render(request,'menu3Chicken.html',
    {
        'checkLogin' : checkLogin,
        'username' : username
    })   

def menu_P4(request):
    return render(request,'menu4Pork.html',
    {
        'checkLogin' : checkLogin,
        'username' : username
    })   

def menu_P5(request):
    return render(request,'menu5Fish.html',
    {
        'checkLogin' : checkLogin,
        'username' : username
    })   

def menu_P6(request):
    return render(request,'menu6Snack.html',
    {
        'checkLogin' : checkLogin,
        'username' : username
    })   

def menu_P7(request):
    return render(request,'menu7Icecream.html',
    {
        'checkLogin' : checkLogin,
        'username' : username
    })   

def menu_P8(request):
    return render(request,'menu8Drink.html',
    {
        'checkLogin' : checkLogin,
        'username' : username
    })   

def menuSearch(request):
    return render(request,'menuSearch.html',
    {
        'checkLogin' : checkLogin,
        'username' : username
    })   

def registerForm(request): 
    return render(request,'register.html',
    {
        'checkLogin' : checkLogin,
        'username' : username
    })   

def addUser(request): 
    if request.method == 'POST':
      checkUser = 0
      # ================= รับข้อมูลจาก form ใน register.html ================= 
      firstname = request.POST['firstname']
      lastname = request.POST['lastname']
      email = request.POST['email']
      username = request.POST['username']
      phone = request.POST['phone']
      password = request.POST['password']
      
      # ================= เช็คการกรอกข้อมูล ================= 
      if firstname != '' and lastname != '' and email != '' and username != '' and phone != '' and password != '' : 

            # ================= เช็คข้อมูลกับไฟล์ Users ================= 
            f = open('file/users.txt', 'r', encoding='utf8')
            s = f.readlines()
            if s != None:
                for line in s:
                  usedEmail = line.split()[2]
                  usedUsername = line.split()[3]
                  
                  if email == usedEmail:
                     checkUser = 1  # emailซำ้
                     break
                  if username == usedUsername:
                     checkUser = 2 # usernameซำ้
                     break
            f.close()      

            if checkUser == 0:
                f = open('file/login.txt', 'a', encoding='utf8')
                f.write(f"{username} {password}\n")
                f.close()

                f = open('file/users.txt', 'a', encoding='utf8')
                f.write(f"{firstname} {lastname} {email} {username} {phone}\n")
                f.close()
                return redirect('/loginForm')
          
            else :
                if checkUser == 1 :
                  messages.info(request,'email ถูกใช้ไปแล้ว')
                elif checkUser == 2 :
                  messages.info(request,'username ถูกใช้ไปแล้ว')
                return redirect('/registerForm')
    
      else :
          messages.info(request,'กรอกข้อมูลไม่ครบ') 
          return redirect('/registerForm')


def loginForm(request):
    return render(request,'login.html')

def login(request):
    if request.method == 'POST':
      # ================= รับข้อมูลจาก form ใน login.html ================= 
      global checkLogin 
      global username
      username = request.POST['username']
      password = request.POST['password']

      # ================= เช็คการกรอกข้อมูล ================= 
      if username != '' and password != '': 

      # ================= เช็คข้อมูลกับไฟล์ login ================= 
        f = open('file/login.txt', 'r', encoding='utf8')
        s = f.readlines()

        if s != None:
          for line in s:
             realUser = line.split()[0]
             realPassword = line.split()[1]
                 
             if username == realUser:
                if password == realPassword:
                    checkLogin = 1
                    break
        f.close()            
        if checkLogin == 1:
            return render(request,'index.html',
            {
                'checkLogin' : checkLogin,
                'username' : username
            })
        else :
            messages.info(request,'ไม่มีข้อมูลผู้ใช้')
            return redirect('/loginForm')

      else :
         messages.info(request,'กรอกข้อมูลไม่ครบ') 
         return redirect('/loginForm')

    return render(request,'login.html')

def logout(request): 
    global checkLogin

    checkLogin = 0
    return render(request,'index.html',
    {
        'checkLogin' : checkLogin,
        'username' : username
    })

def orderHistory(request):
    return render(request,'orderHistory.html',
    {
        'checkLogin' : checkLogin,
        'username' : username
    })

def orderQueue(request):
    return render(request,'orderQueue.html',
    {
        'checkLogin' : checkLogin,
        'username' : username
    })

def queueDetail(request):
    return render(request,'orderQueue.html',
    {
        'checkLogin' : checkLogin,
        'username' : username
    })   

def orderInfo(request):
    return render(request,'orderInfo.html',
    {
        'checkLogin' : checkLogin,
        'username' : username
    })   

def cartDetails(request):
    return render(request,'cartDetails.html',
    {
        'checkLogin' : checkLogin,
        'username' : username
    })   

def thanks(request):
    return render(request,'thanks.html',
    {
        'checkLogin' : checkLogin,
        'username' : username
    })   