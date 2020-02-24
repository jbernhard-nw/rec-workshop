from IPython.display import Image
import numpy as np
from scipy.stats import pearsonr


def answer_one(your_answer):
    '''
    your answer should be a float identifying the correlation between the user_1 and user_2 vectors
    '''
    if your_answer == 0.9658597610592513:
        return Image(filename='../../images/you_right.png')

    else:
        print("Sorry, that's not correct.  Notice, a tuple of values is returned.  The first value is the correlation coefficient, while the second is a p-value for a hypothesis test testing if the correlation coefficient is different than zero.")

def answer_two(your_answer):
    '''
    your answer should be a letter
    a to d
    '''
    if your_answer == "user_1 and user_2 have a positive, linear relationship":
        print("That's right! The value of the correlation is quite close to 1 meaning there is a positive, linear relationship.")
        return Image(filename='../../images/yup.png')

    else:
        print("Sorry, that's not correct.  Try again!")

def answer_three(your_answer):
    '''
    your answer should be a float identifying the cosine similarity between user_1 and user_2
    '''
    if your_answer == 0.9903238090120656:
        return Image(filename='../../../images/good_job.png')
    else:
        print("Sorry the number is not correct. Please try again!")

def answer_four(your_answer):
    '''
    your answer should be a letter a-e
    '''
    if your_answer == "Subtract the standard deviation from each vector":
        return Image(filename='../../images/good_job.png')
    else:
        print("Sorry this is not correct.  Please try again!")

def answer_five(your_answer):
    '''
    your answer should be a 'float' identifying the correlation coefficient between user_1 and user_2 when a nan is present
    '''
    if np.isnan(your_answer):
        print("That's right!  The correlation when a nan is present is also nan.")
        return Image(filename='../../images/good_job.png')

    else:
        print("Sorry, that's not correct.  Try again!")

def answer_six(your_answer):
    '''
    your answer should be a 'float' identifying the correlation coefficient between user_1 and user_2 when a nan is present
    '''
    if your_answer == 0.9628704197969145:
        print("That's right!  It looks like you successfully removed the nan and computed the correlation coefficient.")
        return Image(filename='../../images/good_job.png')

    else:
        print("Sorry, that's not correct.  Try again!")

def compute_correl_2(vec1, vec2):
    '''
    inputs:
    vec1 - np.array
    vec2 - np.array

    return:
    pearson correlation between two vectors where indices with a nan in
    either vector are removed from both vectors
    '''
    indices = np.logical_not(np.logical_or(np.isnan(vec1), np.isnan(vec2)))
    vec1, vec2 = vec1[indices], vec2[indices]

    return pearsonr(vec1, vec2)[0]

def answer_seven(your_answer):
    '''
    your answer should be a 'float' identifying the jaccard similarity between x and y
    '''
    if your_answer == 0.6:
        print("That's right!  It looks like you successfully computed the jaccard similarity!")
        return Image(filename='../../images/good_job.png')

    else:
        print("Sorry, that's not correct.  Try again!")
