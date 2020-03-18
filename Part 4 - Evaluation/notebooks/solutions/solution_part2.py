from IPython.display import Image
import numpy as np
from scipy.stats import pearsonr


def answer_one(your_answer):
    '''
    your answer should be a letter a to d
    '''
    if your_answer == "both recommenders give recommendations, but they don't match one another":
        return Image(filename='../../images/you_right.png')

    else:
        print("Sorry, that's not correct.  Try looking at the recommended values for user 0.")


def final_thoughts():
    '''
    This function will print final thoughts once you have completed the notebook
    '''

    print("One of the reasons turicreate is so popular is because of how well it handles a number of edge cases that show up when building recommendation systems from scratch, as you saw with the handling of this new user.  However, this still doesn't handle the edge case of a new item.  You can probably think of some ways you might recommend a new item to start getting ratings.")


    print("Next you'll look at an easy way to compare different recommendation systems, as well as how to store your system to be used later.")
