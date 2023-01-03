"""
The user runs the program. The program asks the user
 to enter "head" or "tail".  The user flips a coin on their
desk, table, floor, etc., and then enters "head" or "tail".
The user does the same over and over again.
"""

while True:
  # Get user input and strip space chars from it
  with open("../file/sides.txt","r") as file:
    sides = file.readlines()
  user_action = input("Throw the coin and enter head or tail here: ") + "\n"


  sides.append(user_action)

  with open("../file/sides.txt","w") as file:
          file.writelines(sides)

  nr_heads = sides.count("head\n")
  percentage = nr_heads / len(sides) * 100

  print(f"Heads: {percentage}%")
