#By AKM
#Contact-adityanick08@gmail.com


import time,os,keyboard  

def bmsg():
    os.system("cls")     
    print('''
 -----------------------------------------------
 |                                             |
 |                CUSTOM MESSAGE               |
 |                                             |
 |   Description  -  Input a message x which   |
 |   u  have  to  send for y number of  time   |
 |   with  some  time  gap z . Works  on any   |
 |   text  field. increase  the time gap  if   |
 |   incomplete    messages     are    sent.   |
 |                                             |
 -----------------------------------------------    
    ''')

def banner():
    os.system("cls") 
    print("""
 -------------------------------------------
 |                                         |
 |        ENTER 1 FOR CUSTOM MESSAGE       |
 |                                         |
 | Description  -  Input a message x which |
 | u  have  to  send for y number of  time |
 | with  some  time  gap z . Works  on any |
 | text  field. increase  the time gap  if |
 | incomplete    messages     are    sent. |
 |                                         |
 -------------------------------------------
                                      By AKM

     ENTER ANY OTHER NUMBER FOR INSTANT
               "jai shree ram" 

                [0]  -  EXIT                                        
 """)

def bjai():
    os.system("cls")     
    print('''
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%%%%%%%%%%%%%::::*%%%%%%%%%%%%%::::*%%%%%%%%*::::*%%%%%!::::*%%%%%%%%%%%%!::::*%%%%%%
 %%%%%%%%%%%%%%%!....:%%%%%%%%%%%%%....*%%%%%%*:...:*%%%%%%:....:*%%%%%%%%%%!.....!%%%%%%
 %%%%%%%%%%%%%%*......:%%%%%%%%%%%%:...*%%%%%!...:!%%%%%%%%:.....:%%%%%%%%%!......!%%%%%%
 %%%%%%%%%%%%%*:..:!...!%%%%%%%%%%%:...*%%%*:...!%%%%%%%%%%:......:%%%%%%%!.......!%%%%%%
 %%%%%%%%%%%%%:..:*%:..:*%%%%%%%%%%:...*%%!...:*%%%%%%%%%%%:...:...:%%%%%!...::...!%%%%%%
 %%%%%%%%%%%%!...!%%*...:%%%%%%%%%%:...*!:...!%%%%%%%%%%%%%:...!!...:%%%!...:*:...!%%%%%%
 %%%%%%%%%%%*...:%%%%!...!%%%%%%%%%:...:.....:*%%%%%%%%%%%%:...!%!...:%*...:%%:...!%%%%%%
 %%%%%%%%%%%:...*%%%%%:...*%%%%%%%%:.....:!...:*%%%%%%%%%%%:...!%%!...:...:*%%:...!%%%%%%
 %%%%%%%%%%!....::::::....:%%%%%%%%:...:!%%*:...!%%%%%%%%%%:...!%%%!.....:*%%%:...!%%%%%%
 %%%%%%%%%*....:::::::::...!%%%%%%%:...*%%%%%:...:*%%%%%%%%:...!%%%%!...:*%%%%:...!%%%%%%
 %%%%%%%%%:...!%%%%%%%%*....*%%%%%%:...*%%%%%%!...:*%%%%%%%:...!%%%%%!::*%%%%%:...!%%%%%%
 %%%%%%%%!...:%%%%%%%%%%!...:%%%%%%....*%%%%%%%*:...!%%%%%%:...!%%%%%%%%%%%%%%:...!%%%%%%
 %%%%%%%*::::*%%%%%%%%%%%::::!%%%%%::::*%%%%%%%%%::::!%%%%%::::!%%%%%%%%%%%%%%::::!%%%%%%
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 ''')



def jai():
    bjai()
    print(" Enter b in any input to go back\n")
    x=input(" PRESS ENTER TO START  >> ")
    if str(x).lower()=='b':
        return
    print("\n CLICK ON A TEXT FIELD IN 3 SECOND")
    print(" Press b to stop\n")
    time.sleep(3)
    x="jai shree ram"
    while True :
         keyboard.write(x)
         time.sleep(0.03)
         keyboard.write("\n")
         try: 
             if keyboard.is_pressed('b'): 
                 print(' Stopping')
                 time.sleep(2)
                 break               
         except:
             pass  

def msg():
     bmsg()
     print(" Enter b in any input to go back\n")
     x=str(input(" Enter text >> "))
     if x.lower()=='b':
        return
     a=input(" No of msg >> ")
     if str(a).lower()=='b':
        return
     sl=input(" gap in sec >> ")
     if int(sl)==0:
         sl=0.03
     if str(sl).lower()=='b':
        return
     print("\n CLICK ON A TEXT FIELD IN 5 SECOND")
     print(" Press b to stop\n")
     n=0
     time.sleep(5)
     for i in range(int(a) ) :
           n=n+1
           keyboard.write(x)
           time.sleep(int(sl))
           keyboard.write("\n")
           try: 
             if keyboard.is_pressed('b'): 
                 bmsg()      
                 print(' Stopping')
                 print( " MESSAGE SENT = "+str(n))
                 time.sleep(2)
                 break               
           except:
                 pass
     bmsg()      
     print( " MESSAGE SENT = "+str(n))
     time.sleep(2)

while True:
    banner()
    
    try:
        c=int(input(" ENTER CHOICE >> "))
        if c==1:
            msg()
        
        elif c==0:
            os._exit(0)
        elif c!=1 & c!=0:
            jai()
    except Exception  as e:
        banner()
        print(" ENTER CHOICE >> INVALID CHOICE!")
        time.sleep(1)   