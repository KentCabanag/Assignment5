print("\n\033[31;4mThe Life Stages of a Person\033[0m")
print()
Age = int(input("Enter your age: "))
if Age > -1 and Age <= 12:
    print("\n\033[34;1m'Kid'\033[0m")

elif Age >= 13 and Age <= 17:
    print("\n\033[34;1m'Teen'\033[0m")

elif Age == 18:
    print("\n\033[34;1m'Debut'\033[0m")

else:
    print("\n\033[34;1m'Adult'\033[0m")