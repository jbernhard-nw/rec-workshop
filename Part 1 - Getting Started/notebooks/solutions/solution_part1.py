from IPython.display import Image


def answer_one(your_answer):
    '''
    your answer to question 1 should be a letter
    a to e
    '''
    if your_answer == 'knowledge based recommenders':
        return Image(filename='../../../images/you_right.png')

    else:
        print("Sorry, that's not correct.  Try again!")

def answer_two(your_answer):
    '''
    your answer to question 1 should be a letter
    a to e
    '''
    if your_answer == 'collaborative filtering':
        return Image(filename='../../../images/yup.png')

    else:
        print("Sorry, that's not correct.  Try again!")

def answer_three(your_answer):
    '''
    your answer to question 1 should be a letter
    a to e
    '''
    if your_answer == 'content based recommender':
        return Image(filename='../../../images/you_got_it.png')

    else:
        print("Sorry, that's not correct.  Try again!")

def answer_four(your_answer):
    '''
    your answer to question 1 should be a letter
    a to e
    '''
    if your_answer == 'demographic recommender':
        return Image(filename='../../../images/good_job.png')

    else:
        print("Sorry, that's not correct.  Try again!")
