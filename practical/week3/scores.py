from random import*

def main():

    # score = float(input("Enter score: "))
    score_result(score)


def score_result(score):
    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            print("Invalid score")
        elif 100 >= score > 90:
            print("Excellent")
        elif 90 >= score > 50:
            print("Passable")
        else:
            print("Bad")

score = randint(0,100)



main()

socre_file = "result.txt"
socre_out_file = open(socre_file, 'w')
result = ("{}  is  {}".format(score, score_result(score)))
print(result)
print(result)
print(result)

score_file.close()