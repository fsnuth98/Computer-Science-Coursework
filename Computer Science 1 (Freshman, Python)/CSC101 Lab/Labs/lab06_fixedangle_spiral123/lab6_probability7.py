'''
Franklin Nuth
Idrissa Jalloh
CSC101 Lab 6
Part 2: Probability of rolling 7
February 24 2017
'''



import random
nRolls = eval(input("H many times do you want to roll the dice? "))
countSevens = 0
for i in range(nRolls) : 
   die1 = random.randint(1,6)
   die2 = random.randint(1,6)
   #print("die 1:", die1, " die 2:", die2)
   if die1 + die2 == 7:
      countSevens += 1
#      print("We got a 7")

   
probability = countSevens / nRolls
print("The probability of rolling a seven is", probability)