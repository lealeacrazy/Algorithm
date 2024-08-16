# Ex1 - String 
# Enter text and display it one by one
# text = input("enter your text")
# indext = 0 
# while indext<(len(text)):
#     print(text[indext])
#     indext += 1

# Ex2 - String
# Enter text and display number of letter
# text = input(":")
# index = 0
# for i in range (len(text)):
#     index += 1
# print(index)

# Ex3 - String
# Enter text and check if it contains capital letter or not
# Display "Yes" if capital
# display "No" if all lowercase letter
# text = input("your text: ")
# for i in range(len(text)):
#     if text[i].isupper():
#         print("yes")
#     else:
#         print("no")

# Ex4 - String 
# We have text = "3 4 5 6"
# Q1 - display number 1 by one without space
# Q2 - Sum all number (Total: 18)
#A1
# text = "3 4 5 6"
# nospace =""
# for i in range(len(text)):
#     if text[i]==" ":
#         nospace +=""
#     else:
#         nospace += text[i]
# print(nospace)
#A2
# text=input(":")
# sum = 0
# for i in range (len(text)):
#     sum += int(text[i])
# print(sum)

# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text
# Q2 - Sum all number 
# Q3 - Sum only even number 
# Q4 - Reverse
#A1
# text = "454639"
# countodd =0
# counteven=0
# for i in range(len(text)):
#     if i % 2 == 1:
#         countodd += 1
#     if i % 2 == 0:
#         counteven+=1
# print(counteven)
# print(countodd)
#A2
# text = "454639"
# sum = 0
# for i in range(len(text)):
#     sum += int(text[i])
# print(sum)
#A3
# text = "454639"
# print(text[::-1])

# Ex6 - Number
# Enter number and check 
# if odd number print "Odd" otherwise print "Even"
# num = int(input("your number: "))
# if num % 2 == 1:
#     print("odd numbner")
# else:
#     print("even number")

#7 :number
# Enter number in range 10 - 20 until you enter other number out of range
# display "Continue" if number in range 10 - 20
# display "Out of range" if number difference from range 10 - 20
#num = int(input("Enter a number: "))
# sum = 0
# while sum<10:
#     print("out of rang")
#     num = int(input("Enter a number: "))
#     sum+=num  
# if sum<20:
#     print("countinue")
# else:
#     print("out of range")

# Ex8 - String
# We have text = "9394884039"
# Q1 - How many number 8 in string
# Q2 - What is first index of letter 8
# text = "9394884039"
# count8 = 0
# firstletter8 = -1
# for i in range(len(text)):
#     if text[i]=="8":
#         count8 += 1
#     if firstletter8 == -1:
#         firstletter8 = i
# print("count8", count8)
# print("firstletter8", firstletter8)

# Ex9 - String
# We have string = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"
# Q2 - Multiple each letter by 2 result = "6 8 10 12"
#string = "3 4 5 6"
# no_space= string.replace(" ", "")
# print(no_space)
# numbers = string.split()
# doubled_numbers = [str(int(num) * 2) for num in numbers]
# result_doubled = " ".join(doubled_numbers)
# print( result_doubled)

# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0
# input("Please enter your number : ")
# max = 0
# min = 0
# for i in range(5):
#     number = int(input("Enter number : "))
#     if max == 0 and min == 0:
#         max = number
#         min = number
#     else:
#         if number > max:
#             max = number
#         if number < min:
#             min = number
# print("max : ", max)
# print("min : ", min)



