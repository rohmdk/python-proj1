letter = '''Dear <|NAME|>, \nGreeting from ABB sweden. \nYou have been selected for DevOps team. \nDate: <|DATE|>\nRegards ABB HR'''
#print(letter)
name = input("Please Enter your full name\n")
date = input("Please Enter your application Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)