# -*- coding: utf-8 -*-
"""
Author:        Emil Hozan
Date Created:  10-09-2017
Date Modified: 10-27-2017


Purpose:
    Prompts user(s) to input entities to which monies are owed. It is then saved in a file for use later.

"""

# Full list of debtees
m = list_of_Companys_Money_Is_Owed_To = []

# Defining iterating numerator
i = 0 



# Below starts the program itself
print("==================================================") # Formatting for now
print("NOTE: \nTo terminate the program at any time, enter q/quit") # Notice to users
print() # Spacing
print("==================================================") # Formatting for now


# Greet the user
print("-------------INTRODUCTION AND PURPOSE-------------")
print()
print("This program prompts you to enter an entity \n" +
      "to which monies are owed. Information gathered \n" + 
      "will be stored in a file for later use.")
print("==================================================")



# Begin by promtping use, then capturing the data
while True: # Marking the while loop as True until user exits the program
 
  i += 1 # Incrementing counter plus 1
  print("Your current iteration: " + str(i)) # Print current iteration cycle
  print("-------------------------") # Formatting
  print() # Spacing
  
  
  a = input("Enter an entity that you owe money to: ") # Prompt user for input
  print() # Spacing 

  
  if a.lower() == "quit" or a.lower() == "q" or a == "": # Test user input; validation
    print("Input request to terminate this program") # User escape from program
    print() # Spacing
    break # Should the above match, terminate program

	
  m.append(a) # Add initial entry to list
    
  print(m) # Print the item(s) added until now
  print() # Spacing
  print("==================================================") # Formatting



""" Opens and creates the filename below and writes the contents gathered until now """
file_lod = open('list_Of_Debtees.txt', 'w') # file_lod = "handler" of copying file

for line in m: # for each entry in list: m
    file_lod.write(line) # write the entry
    file_lod.write("\n") # then create a new line
    
file_lod.close() # close the file



print("==================================================") # Formatting
print("These are your provided entries: ")
print() # Spacing
print(m) # print the list: m one final time
print() # Spacing
print("==================================================")
print("Here is the output of the saved file: ")
print('It is stored in the current directory as \"list_Of_Debtees.txt\" ')
print()

file_lod_ro = open('list_Of_Debtees.txt', 'r') # file_lod_ro = "handler" of the open file in read only mode

for line in file_lod_ro:
    print(line, end="") # print each line and only return carriage to next line 1x
    
file_lod_ro.close() # close the file


print()
print("==================================================")
print ("Thank you for your input, until next time!")
print() # Spacing
