from IPython.display import Image
import numpy as np
from scipy.stats import pearsonr


def answer_one(your_answer):
    '''
    your answer should be a letter a to e
    '''
    if your_answer == "rmse":
        print("That's right! RMSE is used to evaluate how well a regression prediction is performing.  The above is a classification situation, so only RMSE cannot be used.")
        return Image(filename='../../../images/you_right.png')

    else:
        print("Sorry, that's not correct.  Notice, most of these metrics can all be used for classification problems, but one cannot.  Which of these is not like the others?")

def answer_two(your_answer):
    '''
    your answer should be a letter
    a to c
    '''
    if your_answer == "At first glance, 88% seems not great given 90% accuracy's possible by predicting every movie won't be clicked.":
        return Image(filename='../../../images/yup.png')

    else:
        print("Sorry, that's not the best answer here.  Try again!")

def answer_three(your_answer):
    '''
    your answer should be a letter a to d
    '''
    if your_answer == "You are likely to overfit.":
        return Image(filename='../../../images/good_job.png')
    else:
        print("Sorry, that's not the best answer here.  Try again!")


def answer_four(your_answer):
    '''
    your answer should be a float
    '''
    if round(your_answer, 1) == 0.2:
        return Image(filename='../../../images/good_job.png')
    else:
        print("Sorry, that's not quite right.  Make sure you are dividing the number of rows in the test case by the total number of rows in the dataset.")
