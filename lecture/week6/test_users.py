from users import *

user1 = User("Tony")
print(user1)
user2 = User("Hellene", 1, 4)
print(user2)

user2.give_a_taco(user1)
print(user1)
print(user2)
