'''
list of utilities functions defined in this code:

- progression_bar: use to print a progression bar in the terminal
- smoothing: smoothes out plots (Lowess)
- make_title_dictionary: creates 2 dictionaries that allow to go from the
                        filename to the title of the movie
- prepare_dictionary: makes a dictionary with the smoothed arrays
'''

import sys
import os
import statsmodels.api as sm
import numpy as np

def progression_bar(i, Ntot, Nbars=60, char='-'):
    '''
    Shows a progression bar with Nbars
    parameters:
    -----------
    i: index of the files
    Ntot: total number of files
    Nbars: how many bars to fill
    char: character to show as progression
    '''
    nbars = int( (i+1)*1./Ntot * Nbars )
    sys.stdout.write('\r[' + nbars*char)
    sys.stdout.write((Nbars-nbars)*' '+']')
    sys.stdout.write('%d/%d'%(i, Ntot))
    sys.stdout.flush()

def smoothing(y_vals, frac=0.05):
    '''
    parameters:
    -----------
    y_vals: list of sentiment scores
    frac: parameter of smoothing

    returns:
    --------
    x_smooth_vals
    y_smooth_vals
    '''
    x_vals = np.arange(len(y_vals))
    lowess = sm.nonparametric.lowess(y_vals, x_vals, frac = frac)
    y_smooth_vals = lowess[:, 1]
    x_smooth_vals = lowess[:, 0]
    return x_smooth_vals, y_smooth_vals

def make_title_dictionary():
    '''
    this function relies on the creation of the 'successful_files.csv' by the
    scraping script.

    returns:
    --------
    two dictionaries:
       - with the filename as key (without extension) and title as value
       - with title as value and filename as key
    '''
    filename = '../data/scraping/successful_files.csv'
    if not os.path.isfile(filename):
        return 'Please make sure the csv %s exits' %(filename)
    with open(filename,'r') as f:
        text = f.read()
    lines = text.split('\n')
    filename_to_title = {}
    title_to_filename = {}
    for line in lines:
        if len(line)>=2:
            info = line.split(';')
            title = info[0]
            filename = info[3]
            filename_to_title[filename] = title
            title_to_filename[title] = filename

    return filename_to_title, title_to_filename

def prepare_dictionary(filename):
    '''
    returns:
    --------
    dictionary
        key (emotion, index)
        value (array of x, array of y - smoothed emotion counts)
    '''
    plotline = LoadPlotLine(filename)
    plotline.load_emotions()
    plotline.make_emotion_dictionary(list_emotions=range(10))
    return plotline.emotion_dictionary_smooth
