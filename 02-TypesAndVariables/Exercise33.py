password = input('Enter your password:\n')
password_lenght = len(password)
strong_password = password_lenght>=8
print(f'Your password is valid: {strong_password}')