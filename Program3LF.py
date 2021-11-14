print("\n\033[31;1m The Life Stages of a Person\033[0m")
print()
Age = int(input("Enter your age: "))
if Age > -1 and Age <= 12:
    print("\n\033[34;1mKid\033[0m\033[33;1m")

elif Age >= 13 and Age <= 17:
    print("\n\033[34;1mTeen\033[0m\033[33;1m")

elif Age == 18:
    print("\n\033[34;1mDebut\033[0m\033[33;1m")

else:
    print("\n\033[34;1mAdult\033[0m\033[33;1m")