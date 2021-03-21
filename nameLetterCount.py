# This program asks for your name and returns the length

print("Hello! Plase enter your name: ")
userName = input()

print("Hi " + userName + ", it is nice to meet you!")


def countName(count):
    count = str(len(userName))
    return count


print("Your name has " + countName(userName) + " letters in it!")
