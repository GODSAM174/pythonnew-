Amount=int(input("please enter the amount for withdraw :"))

Note_1=Amount//100
Note_2=(Amount%100)//50
Note_3=(Amount%100)%50//10


print("notes of 100 rupee" ,Note_1)
print("notes of 50 rupee" ,Note_2) 
print("notes of 10 rupee " ,Note_3)