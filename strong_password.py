def my():
    password=input("enter the password")
    p=len(password)
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_chr = "!@#$%^&*()-+"
    n=0
    l=0
    u=0
    s=0
    i=0
    while i<len(password):
        if password[i] in numbers:
            n=n+1
        if password[i] in lower_case:
            l=l+1
        if password[i] in upper_case:
            u=u+1
        if password[i] in special_chr:
            s=s+1
        i=i+1
    if p>=6:
        if n>=1 and l>=1 and u>=1 and s>=1 :
            print("strong password")
        else:
            print("invilade")
    else:
        print("no")
    # password1=input("Enter your password:  ")
    # l,u,p,d,y=0,0,0,0,0
    # i=0
    # while i<len(password1):
    #     if (password1[i].islower()): 
    #             l+=1 
    #     if (password1[i].isupper()): 
    #             u+=1			 
    #     if (password1[i].isdigit()):
    #             d+=1
    #     if password1[i].isalnum():		
    #             p+=1
    #     else:
    #         y+=1
    #     i+=1	
    # if (l>=1 and u>=1 and p>=1 and d>=1 and y>=1 or l+p+u+d+y==len(password1)):
    #     print("valid password")
    # else:
    #     print("invalid password")        
my()
