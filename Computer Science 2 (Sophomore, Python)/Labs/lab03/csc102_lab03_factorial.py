'''
CSC102 - Lab 03
Problem 1: Factorial
Franklin Nuth
Rasul Rasulov
February 2nd, 2018
'''

TABS = 1

def factorial(n):
   """Calculates n factorial"""
   global TABS
   print("\t" * TABS, "->calculating factorial of ", n)
   if n==0:
      return 1
   elif n<0:
      return 0
   else:
      TABS +=1
      print("\t" * TABS, "need factorial of", n-1)        
      answer = factorial(n-1)
      print("\t" * TABS, "<-factorial of=", n-1, " is", answer)
      TABS -= 1 
      return n * answer      
      

n = int(input("Enter a natural number: ")) 
print("The factorial of", n, "is", factorial(n))

"""
1. Paste in the space below the output produced by the program in calculating 5!

"3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)]
Python Type "help", "copyright", "credits" or "license" for more information.
[evaluate csc102_lab03_factorial.py]
Enter a natural number: 5
	 ->calculating factorial of  5
		 need factorial of 4
		 ->calculating factorial of  4
			 need factorial of 3
			 ->calculating factorial of  3
				 need factorial of 2
				 ->calculating factorial of  2
					 need factorial of 1
					 ->calculating factorial of  1
						 need factorial of 0
						 ->calculating factorial of  0
						 <-factorial of= 0  is 1
					 <-factorial of= 1  is 1
				 <-factorial of= 2  is 2
			 <-factorial of= 3  is 6
		 <-factorial of= 4  is 24
The factorial of 5 is 120"

2. How many distinct calls are made to the factorial function to calculate
   the factorial of 5?

"I think that 6 distinct calls are made to the factorial function for factorial 5." 

3. Examine the output of your program. How many lines were printed by the program?

"There are 17 lines printed by the program."

4. What does the group of lines progressively indented represent in calculating a factorial?

"They represent the the simplifying of the 5 factorial."

5. What does the group of lines progressively out-dented represent?

"They represent that the factorial cannot be lower than zero." 

6. What happens if you try to calculate the factorial of a negative number? 
   Fix the bug in the factorial function so the function returns 0 as the 
   factorial of a negative number.

"If I try to calculate the factorial of a negative number, my program crashes and gets an error."

"""