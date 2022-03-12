vowel_str = 'aieou'

user_name = input('Enter your name: ')

while len(user_name) == 0:

    user_name = input('Enter your name: ')

no_of_vowels = 0

for i in range(len(user_name)):

    if user_name[i].lower() in vowel_str:

        no_of_vowels += 1

print('Out of {} characters, {} has {} vowels'

      .format(len(user_name), user_name, no_of_vowels))


words = "one two three".split()

for i in range(len(words)): #capitalise each word
    words[i] = words[i].title()
text = ", ".join(words)
print(text)


numbers = [10, 20, 30]
things = numbers
numbers.append(40)
print(numbers)
print(things)

new_things = numbers.copy()
new_things[0] = 5
print(numbers)
print(things)
print(new_things)

numbers.append(50)

print(numbers)
print(things)
print(new_things)

