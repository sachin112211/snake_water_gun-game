import random
print('welcome to the snake water gun game')
user = input("enter your choice snake/water/gun: ")
choices =['snake','water','gun']
y = random.choice(choices)
print(y)
if y == user:
    print("retry")
elif user =='snake' and y =='water':
    print("you won")
elif user =='water' and y=='gun':
    print("you won")
elif user =='gun' and y=='snake':
    print('you won')
else:
    print("you loss")
