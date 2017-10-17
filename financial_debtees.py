"""
Author:        Emil Hozan
Date Created:  10-09-2017
Date Modified: 10-17-2017


Purpose:

This is a running program that takes user input regarding entities to which money is owed to. Entered information is stored into a list.

They are then prompted to enter the total amount owed to each respective entity. This information is pulled from the previously created list, then stored in a dictionary where each entity their associated owed amount.
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
print("This program is going to prompt you to first start by entering an entity to which monies are owed.")
print()
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
  print("") # Spacing
  print("==================================================") # Formatting

print("==================================================") # Formatting
print("These are your provided entries: ")
print() # Spacing
print(m)
print() # Spacing
print("==================================================")
print ("Thank you for your input, until next time")
print() # Spacing
print() # Spacing
print() # Spacing
print() # Spacing
print() # Spacing







"""
This Segment covers iterating through the "list: m" and adding the current owed amount and creating "dictionary: d"

"""
print("==================================================") # Formatting
print("---------------GATHERING OWED AMOUNT--------------") # Spacing

d = {} # Empty dictionary
running_Sum = 0 # Total being gathered for all entities
total_Owed = 0.00


# Start by looping through the "list: m"
for entered_Entity in m:

  try:
    # Prompt for associated amount respective to entity
    total_Owed = input("How much is owed to: " + entered_Entity + "?")
    print(float(total_Owed))
  
  
  """
    if total_Owed.isalpha:
      running_Sum = running_Sum + int(str(total_Owed[1::1]))
  else:
    running_Sum = running_Sum + int(total_Owed)

  d[entered_Entity] = str("$" + total_Owed)
  """


print("This is the summary of your entered debtees and the corresponding debt owed to them: ")
print(d)
print("This is the total owed for all debts: ")
print(running_Sum)
"""
The below allows me to iterate through my list, indexing each from 0+

d = dict(enumerate(m)) # Empty dictionary to get m into
print(d)
"""