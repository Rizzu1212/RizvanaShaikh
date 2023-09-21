# 1 
"""Count character 'e' in the below string.
	Input "geeksforgeeks". 
	Output: 4

	Count character '3' in the below string.
	Input "abccdefgaa."
	Output : 3
"""

import string


input_str ="geeksforgeeks"
input_char ="e"

occurence_count = sum([1 for char in input_str if char == input_char])
print(f"Occurence of '{input_char}' is: {occurence_count}")

input_str ="abccdefgaa"
input_char ="a"

occurence_count = sum([1 for char in input_str if char == input_char])
print(f"Occurence of '{input_char}' is: {occurence_count}")


# 2
""" Problem 2:  Determine whether a given string is Palindrome
 A string “madam” is a palindromic string because it reads the same forwards and backward. 
Input: “anna”
Output: true

Input: “India”
Output: false
"""
def palindrome(str):
    return str==str[::-1]
str=input("enter string: anna or india..:")
ans= palindrome(str)
if ans:
    print("true")
else:
    print("false:")
    





# 3 
""" Problem 3:  Biggest and smallest number in an array
 Write a program to print the biggest and smallest number in the array. 

Input: arr[] = {1, 2, 3, 4, 5}
Output: Maximum is: 5
Minimum is: 1

Input: arr[] = {5, 3, 7, 4, 2}
Output: Maximum is: 7
Minimum is: 2
"""
#method1
arr=[1,2,3,4,5]
arr.sort()
print("smallest element:",arr[0])
print("biggest element",arr[-1])

arr=[5,3,7,4,2]
arr.sort()
print("smallest element:",arr[0])
print("biggest element",arr[-1])

#method2
input_str = [1,2,3,4,5]
print("Maximum is:", max(input_str))
print("Minimum is:", min(input_str))

input_str = [5,3,7,4,2]
print("Maximum is:", max(input_str))
print("Minimum is:", min(input_str))

# 4
"""Problem 4:  Swap two Strings Without Using any Third Variable
 Input: a = "Hello", b = "World".
Output: Strings after swap: a = World and b = Hello
"""

first_string = "hello"
second_string = "world"

first_string, second_string = second_string, first_string
print("before swapping first string is:hello and second string is:worls")
print(f"String after swap: first_string = {first_string} and second_string = {second_string}")



# 5
"""Problem 5: Swap two numbers without using a temporary variable
 Input:integer a = "10", b = "50".
Output: Strings after swap: a = 50 and b = 10
"""

first_number = 10
second_number =50

first_number, second_number = second_number, first_number

print(f"Number after swap: first_number = {first_number} and second_number = {second_number}")


