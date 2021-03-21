# This program asks for your name and returns the length

print("Hello! Please enter your name: ")
userName = input()

print("Hi " + userName + ", it is nice to meet you!")


def count_name():
    count = str(len(userName))
    return count


print("Your name has " + count_name() + " letters in it!")
