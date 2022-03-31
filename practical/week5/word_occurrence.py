word_to_count = {}

sentence = input("Text: ")

words = sentence.split()
for i in words:
    occurrence = word_to_count.get(i, 0)

    word_to_count[i] = occurrence + 1


other_thing = list(word_to_count.keys())
other_thing.sort()



for thing in other_thing:

    print("{0:{1}} : {2}".format(thing, max(len(other_thing) for i in other_thing), word_to_count[thing]))