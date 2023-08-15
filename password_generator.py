'''This project generate a randomly password based on user's choice of how many letters, numbers, and sumbols he would like on his
secured password'''


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list =[]

for number in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))  

for symbol in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))
    
for number in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

# print(password_list)
random.shuffle(password_list)
# print(password_list)  

final_password = ""
for item in password_list:
    final_password += item
print(f"Randomly order password: {final_password}")
