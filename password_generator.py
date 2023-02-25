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






# password = ""
# for number in range(1, nr_letters + 1):
#   letters_choose = random.choice(letters)
#   password += letters_choose
# for symbol in range(1, nr_symbols + 1):
#   symbols_choose = random.choice(symbols)
#   password += symbols_choose   
# for number in range(1, nr_numbers + 1):
#   numbers_choose = random.choice(numbers)
#   password += numbers_choose
# # print(f"Original Password: {password}")  

# final_password = ""
# password_lenght = len(password)
# # print(f"lenght is : {password_lenght}")

# for char in range(1, password_lenght + 1):  
#   if password != "":    
#     # print(f"The original password now looks like {password}")
#     char_chose = random.choice(password)
#     final_password += char_chose
#     # print(f"This character will be replaced: {char_chose}\n")
#     password = password.replace(char_chose, "", 1)

# print(f"Randomly order password: {final_password}")
# # print(f"The final password lenght is {len(final_password)}")