from IPython.display import Image


def answer_one(your_answer):
    '''
    your answer to question 1 should be a letter
    a to e
    '''
    if your_answer == "Demographic Based Recommender":
        print("That's right! A demographic recommender would require information about our user")
        return Image(filename='../../../images/you_right.png')

    elif your_answer == "Knowledge Based Recommender":
        print("Though we would also need user input to complete a knowledge based recommender, you could imagine receiving this input and applying to this data to retrieve recommendations.")

    elif your_anwer == "Utility Based Recommender":
        print("This data wouldn't be great for a utility based recommender, but technically we could build one.")

    else:
        print("Sorry, that's not correct.  Try again!")

def answer_two(your_answer):
    '''
    your answer to question 1 should be a letter
    a to e
    '''
    if your_answer == 'ratings_dat':
        print("That's right! For collaborative filtering, we only need to know the relationship between the users and movies (items).  This is acheived completely through the ratings_dat.")
        return Image(filename='../../../images/yup.png')

    else:
        print("Sorry, that's not correct.  Try again!")

def answer_three(your_answer):
    '''
    your answer to question 1 should be a letter
    a to e
    '''
    if your_answer == (3287, 1945, 7.66, 0, 10, 0):
        return Image(filename='../../../images/good_job.png')

    if your_answer[0] == 3287:
        print("The number of users looks correct!")
    else:
        print("Sorry, the number of users you have doesn't look correct.")
    if your_answer[1] == 1945:
        print("The number of movies looks correct!")
    else:
        print("Sorry the number of movies you have doesn't look correct.")
    if your_answer[2] == 7.66:
        print("The average rating looks correct!")
    else:
        print("Sorry the average rating doesn't look correct.")
    if your_answer[3] == 0:
        print("The minimum rating looks correct!")
    else:
        print("Sorry the minimum rating does not look correct.")
    if your_answer[4] == 10:
        print("The max rating looks correct!")
    else:
        print("Sorry the max rating does not look correct.")
    if your_answer[5] == 0:
        print("The number of missing movies looks correct!")
    else:
        print("Sorry the number of missing movies does not look correct.")

def answer_four(your_answer):
    '''
    your answer to question 1 should be a letter
    a to e
    '''
    if your_answer == ("The Lord of the Rings: The Return of the King", "Amadeus"):
        return Image(filename='../../../images/good_job.png')

    else:
        print("Sorry, that's not correct.  Try again!")
