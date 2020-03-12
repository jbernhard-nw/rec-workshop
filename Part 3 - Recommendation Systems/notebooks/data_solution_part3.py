from IPython.display import Image
import numpy as np
from scipy.stats import pearsonr


def answer_one(your_answer):
    '''
    your answer should be a letter associated with your completion of the sentence
    '''
    if your_answer == "as latent factors":
        print("That's right! Matrix factorization provides matrices that provide a user's latent (not explicit) feelings towards different elements of the items.")
        return Image(filename='../../images/you_right.png')

    else:
        print("Sorry, that's not correct. Try again!")

def answer_two(your_answer):
    '''
    your answer should be a letter associated with your completion of the sentence
    '''
    if your_answer == "latent factors related to items":
        print("That's right! Matrix factorization provides one matrix related to the latent factors associated with a user, and a second matrix related to the latent factors associated with the item.")
        return Image(filename='../../images/you_right.png')

    else:
        print("Sorry, that's not correct. Try again!")

def answer_three(your_answer):
    '''
    your answer should be a letter associated with your completion of the sentence
    '''
    if your_answer == "mostly 0's":
        print("That's right! The third (middle) matrix is a matrix with 0's everywhere except along the diagonal.  The values along the diagonal give a measurement of how much each latent factor matters towards creating the original matrix.")
        return Image(filename='../../images/you_right.png')

    else:
        print("Sorry, that's not correct. Try again!")

def answer_four(your_answer):
    '''
    your answer should be a list of movie ids
    '''
    if your_answer == set([71853, 119174, 96895, 327597, 113277]):
        return Image(filename='../../images/good_job.png')

    else:
        print("Sorry, that's not correct.  If you need help take a look at the code in the solution notebook.")
