# 4. Accept a name from the user and display that in lower case using lower() function

def lowercae_name(user_name):
    '''This function returns the user_name in lower case'''
    return user_name.lower()

user_name = input('Enter your name: ')
result = lowercae_name(user_name)

print(result)
