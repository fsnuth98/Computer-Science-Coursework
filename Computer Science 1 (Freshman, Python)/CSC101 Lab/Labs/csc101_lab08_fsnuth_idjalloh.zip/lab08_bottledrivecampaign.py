'''
Idrissa jalloh
Franklin Nuth
CSC101 Lab 8
Part 3: Bottle Drive Campaign
March 24 2017
'''

total_bottles = 0

# A
for day in range(1,5): # campaign days: 1,2,3 and 4
   total_bottles_today = 0
   bottles_donated = eval(input('Enter number of bottles donated or -1 or quit:'))
   while bottles_donated != -1:
      total_bottles_today += bottles_donated
      bottles_donated = eval(input('Enter number of bottles donated or -1 or quit:'))
   print('Total bottles donated today:', total_bottles_today)
   total_bottles += total_bottles_today
# E
print('Total bottles donate:', total_bottles)
print('Total value of donations:', total_bottles * 0.05)