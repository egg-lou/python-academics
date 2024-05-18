usernames = ["Yeji", "Lucy", "Chaeryong"]
passwords = ["1234", "5678", "9101"]

input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

account_found = False

for i in range(len(usernames)):
    if input_username == usernames[i] and input_password == passwords[i]:
        print(f"Welcome {input_username}!")
        account_found = True
        break

if not account_found:
    print("Account not found!")
