# 1. Write a program which accepts a sequence of comma-separated numbers from console and
#generate a list.

num = input("Enter numbers in sequence separated by commas :" )
print(num.split(','))

# 2. Create the below pattern using nested for loop in Python  
for i in range(1,5):
    print ("*"*i)
    if i == 4:
        for j in range(5,0,-1):
            print ("*"*j)
            
 # 3.Write a Python program to reverse a word after accepting the input from the user.
word = input ("Enter a word: ")
length = len(word)
length
n=1
print("Reverse of entered word is: ")
while length != 0:
    print (word[-n], end ="")
    n +=1
    length -=1