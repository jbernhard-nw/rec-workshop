import numpy as np
import pandas as pd
from IPython.display import Image


def answer_one(your_answer):
    '''
    your answer should be a letter
    a to c
    '''
    if your_answer == "ratings_dat is a dense representation of user-item ratings":
        return Image(filename='../../../images/you_right.png')

    else:
        print("Sorry, that's not correct. The timestamp makes this a bit different than the notes, but otherwise this is one specific representation of user-item data. Try again!")

def answer_two(your_answer):
    '''
    your answer should be a letter
    a to c
    '''
    if your_answer == "ratings_dat is a sparse representation of user-item ratings":
        return Image(filename='../../../images/yup.png')

    else:
        print("Sorry, that's not correct.  Try again!")

def create_pivot_df(ratings_df):
    '''
    returns sparse dataframe of ratings_df
    '''
    df = pd.pivot_table(ratings_df, values='rating', index='user_id', columns='movie_id')
    return df


def answer_three(your_answer):
    '''
    your answer should be a letter
    a to g
    '''
    if your_answer == (6384294, "don't fill missing values"):
        print("That's right!  You can find the number of missing values by using `df.isnull().sum().sum()` and you can create `pd.pivot_table(ratings_dat, values='rating', index='user_id', columns='movie_id')` using `pd.pivot_table(ratings_dat, values='rating', index='user_id', columns='movie_id')`.\n \n Different recommenders might require us to fill in values here, but in a recommendation engine - it is almost never a good idea to fill with the row or column average.  In this case, we should just leave the nans, and we might end up filling with some value outside the rage of possible values in the future.  Nice job!")
        return Image(filename='../../../images/good_job.png')

    else:
        print("Sorry, that's not correct.  Try again!")

def answer_four(your_answer):
    '''
    your answer should be a letter
    a to g
    '''
    if your_answer == 0.0014:
        return Image(filename='../../../images/you_got_it.png')
    elif your_answer > 0.0014:
        print("Sorry, you over estimated.  Find the total number of possible movie-user combos there are, and subtract the number of missing values.")
    else:
        print("Sorry, you under estimated.  Find the total number of possible movie-user combos there are, and subtract the number of missing values.")

def create_binary_df(df):
    '''
    df is sparse matrix with nans + ratings
    '''
    df_new = df.fillna(-1)
    binary_df = df_new.applymap(lambda val: 1 if val > -1 else 0)
    return binary_df

def check_binary_df(binary_df, ans_binary_df):
    '''
    check binary_df against ans_binary_df
    '''
    check_match = np.sum(np.sum(binary_df == ans_binary_df))
    total_cells = ans_binary_df.shape[0]*ans_binary_df.shape[1]
    return check_match == total_cells


def clean_movie_df(df):
    '''
    add genres to dataframe list of genres from dataframe
    '''
    df['year'] = df['movie_title'].apply(lambda val: int(val[-5:-1]))
    df['title'] = df['movie_title'].apply(lambda val: val[:-7])

    genres = []
    for genre in df['movie_genre']:
        try:
            genres.extend(genre.split('|'))
        except AttributeError:
            continue

    genres = list(set(genres))

    row_num = df.shape[0]
    for genre in genres:
        df[genre] = np.zeros(row_num)

    for genre in genres:
        for val in range(df.shape[0]):
            try:
                if genre in df.loc[val, 'movie_genre'].split('|'):
                    df.loc[val, genre] = 1
            except AttributeError:
                continue

    df = df.drop('movie_title', axis=1)
    df = df.drop('movie_genre', axis=1)

    return df
