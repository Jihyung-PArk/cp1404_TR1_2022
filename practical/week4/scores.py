"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""



def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    score_sub = score_subject(score_values)
    display_subject_details(score_sub, subjects)




def score_subject (score_values):
    subject = []
    for i in range(len(score_values[0])):
        score_each_subject = []

        # print(subjects[i], "Scores:")
        for score in score_values:
            score_each_subject.append(score.pop(0))
        subject.append(score_each_subject)
            # print(score)
        # print("Max:", max(score_values[i]))
        # print()
    return subject


def display_subject_details(score_sub, subject_names):
    for i, score_each_subject in enumerate(score_sub):
        print(subject_names[i], "Scores:")
        for score in score_each_subject:
            print("{:>2}".format(score))
        print("Max: {:3}".format(max(score_each_subject)))
        print("Min: {:3}".format(min(score_each_subject)))
        print("Avg: {:6.2f}\n".format(
            (sum(score_each_subject) / len(score_each_subject))))


main()