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





user_name = input("what is your name? : ")

user_letter = list(user_name)
letter_num = len(user_name)
vowels = 0

for user_letters in user_letter:
    if user_letters =="A" or user_letters == "a" \
            or user_letters == "E" or user_letters == "e" \
            or user_letters =="I" or user_letters == "i" \
            or user_letters == "O" or user_letters == "o" \
            or user_letters =="U" or user_letters == "u":

        vowels += 1
print("Name: {}".format(user_name))
print("Out of {} letter, {} has {} vowels".format(letter_num ,user_name, vowels))



scores = []
score = int(input("Score: "))
while score >= 0:
    scores.append(score)
    score = int(input("Score: "))

# if len(score) >= 0:
#     print("your highest core is", max(scores))
# else:
#     print("No valid scores are entered.")
 try:
    print("Your highest score is", max(scores))
 except ValueError:
     print ("No valid scores are entered.")


a_list = []
a_tuple = ()


text = "This is a sentence"
words = text.split(" ")

long_words = [words for text in words if words.count('_') > 3]
print(long_words)




