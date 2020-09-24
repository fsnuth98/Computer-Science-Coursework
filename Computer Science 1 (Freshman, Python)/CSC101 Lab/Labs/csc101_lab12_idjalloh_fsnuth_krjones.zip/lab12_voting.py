''' 
Idrissa Jalloh 
Franklin Nuth
Kareem Jones
CSC101 Lab 12 
Part 4: Voting App
April 21 2017
'''
import math
import random
def show_candidates(candidates):
   print()
   print("*** Candidates ***")
   for name in candidates:
      print(name)
   print("****************")

def main():
   candidates = ["Alice", "Bob", "Carla", "Damien"]
   counters = [0, 0, 0, 0]

   vote = input("Enter name of candidate or q to quit: ")
   while vote != 'q':
        
      show_candidates(candidates)

       # Find index of name in list candidates
      candidate_pos = candidates.index(vote)

       # add 1 to the counter associated with this candidate
      counters[candidate_pos] += 1

      vote = input("Enter name of candidate or q to quit: ")
      

   # When the loop ends:
   # Find the highest value in counters
   h = max(counters)
   
   if counters.count(h) > 1 :
      print("We have a tie!")
      # we have a tie
      # counters = [3,8,5,8]
      # h = 8
      i = 0
      while i < len(counters):
         if counters[i] == h:
            # print name of candidate at i
            i += 1
      
   else:
      # single winner
      # Find the location of this value in the list of counters
      hc = counters.index(h)
      # Get and print the name of candidate with the highest voter count
      print("The winner is: ", candidates[hc]) 

main()