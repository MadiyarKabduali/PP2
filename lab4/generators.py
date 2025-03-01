#1
def squares(number):
    list=[]
    for i in range(1,number+1):
        list.append(pow(i,2))
    print(", ".join(map(str,list)))
    return 0

number=int(input("enter a number:"))
squares(number)

#2
def even(number):
    evenlist=[]
    for i in range(2,number+1,2):
        evenlist.append(i)
    print(", ".join(map(str,evenlist)))
    return 0

number=int(input("Enter a number:"))
even(number)

#3
def Divby3and4(number):
    divlist=[]
    for iter in range(0,number+1,3):
        if(iter%4==0):
            divlist.append(iter)
    print(", ".join(map(str,divlist)))
    return 0

number=int(input("Enter a number:"))
Divby3and4(number)

#4
def squares2(a,b):
    squarelist=[]
    for i in range(a,b+1):
        squarelist.append(pow(i,2))
    print(", ".join(map(str,squarelist)))
    return 0

a=int(input("Enter the number a:"))
b=int(input("Enter the number b:"))
squares2(a,b)

#5
def downTO0(number):
    list=[]
    for i in range(number,-1,-1):
        list.append(i)
    print(", ".join(map(str,list)))
    return 0

number=int(input("Enter a number:"))
downTO0(number)
