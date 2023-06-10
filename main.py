import random
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbol = "[]{}#*;._-"

ans = lower_case + upper_case + num + symbol

lenght = 12

password = "".join(random.sample(ans, lenght))

print("Le mot de passe est ", password)