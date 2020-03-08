from IPython.display import Image
import numpy as np
from scipy.stats import pearsonr


def answer_one(your_answer):
    '''
    your answer should be a list of movie ids
    '''
    if your_answer == [8579674, 8367814, 6751668, 2584384, 5727208]:
        return Image(filename='../../../images/you_right.png')

    else:
        print("Sorry, that's not correct. This set of rankings only depends on the number of times a movie was seen, and does not use the ratings at all.")

def answer_two(your_answer):
    '''
    your answer should be a dictionary
    '''
    if len(your_answer) == 3287 and your_answer[30] == [8579674, 8367814, 6751668, 2584384, 5727208]:
        print("This looks right! You should have the same five ratings for each user_id. And this test passed!")
        return Image(filename='../../../images/yup.png')

    else:
        print("Sorry, that's not correct.  Try again!")

def answer_three(your_answer):
    '''
    your answer should be a list of letters associated with true statements in order from smallest letter to largest letter
    '''
    if your_answer == ["The popularity recommendations remove movies a user has already watched.", "The popularity recommendations are based on the ratings received by each movie."]:
        return Image(filename='../../../images/good_job.png')
    else:
        print("Sorry, that is incorrect.  There are two statements that are true from the list. Please try again!")

def answer_four(your_answer):
    '''
    your answer should be a list of movie ids
    '''
    if your_answer == [8579674, 8367814, 6751668, 2584384, 5727208]:
        return Image(filename='../../../images/good_job.png')

    else:
        print("Sorry, that's not correct.  You should be able to run similar code to the example.  However, you need to remove the target = rating portion.")


def answer_five(your_answer):
    '''
    your answer should be a 'float' identifying the correlation coefficient between user_1 and user_2 when a nan is present
    '''
    if your_answer == ["The top 5 recommendations for question 4 are the same as the top 5 for question 1.", "Both questions 4 and 1 use recommendations based on the times a movie was watched.", "One benefit of using turicreate is that it easily removes movies you've already watched."]:
        return Image(filename='../../../images/good_job.png')

    else:
        print("Sorry, that's not correct.  Actually all of these statements are true! Try again!")

def answer_six(your_answer):
    '''
    your answer should be a 'float' identifying the correlation coefficient between user_1 and user_2 when a nan is present
    '''
    if your_answer == [4916630, 7545266, 783640, 8367814, 5774060]:
        return Image(filename='../../../images/good_job.png')

    else:
        print("Sorry, that's not correct. You should be providing the top 5 recommendations from the item recommender.  Yours don't seem to match. Try again!")

def answer_seven(your_answer):
    '''
    your answer should be a list of movie ids
    '''
    if your_answer == [42, 28, 15]:
        return Image(filename='../../../images/good_job.png')

    else:
        print("Sorry, that's not correct.  You should be able to run similar code to the example.  However, you need to remove the target = rating portion.")

def answer_eight(your_answer):
    '''
    your answer should be a list of movie ids
    '''
    if your_answer == [5727208, 7549996, 8291806]:
        return Image(filename='../../../images/good_job.png')

    else:
        print("Sorry, that's not correct.  Make sure you are using the item similarity model, and you are looking at the correct item_id.")
