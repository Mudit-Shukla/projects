import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Create a Secure password for your account")
#number_of_letters= int(input("How many letters would you like in your password?\n"))
number_of_letters = random.randint(4, 7)

#number_of_symbols = int(input(f"How many symbols would you like?\n"))
number_of_symbols = random.randint(2, 5)

#number_of_numbers = int(input(f"How many numbers would you like?\n"))
number_of_numbers = random.randint(2, 5)

password_list = []

for char in range(0, number_of_letters):
  password_list.append(random.choice(letters))

for char in range(0, number_of_symbols):
  password_list += random.choice(symbols)

for char in range(0, number_of_numbers):
  password_list += random.choice(numbers)

#print(password_list)
random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

def get_password():
    return password

print(f"Your password is: {password}")

