# Recommendation Systems in Python
========================================================

Contents
-----------
- [Part 1: Getting Started]()
- [Part 2: What data should I use?]()
- [Part 3: How do I find relevant recommendations?]()
- [Part 4: How do I know if my recommendations are good?]()
- [Part 5: Extras]()


Instructor
-----------

- [Joshua Bernhard](https://www.linkedin.com/in/joshuabernhard/) My career can be described as educating others, and then educating myself to ensure that how I am educating others is relevant.

**Teaching:** Iowa State University, University of Colorado, Galvanize, Udacity, General Assembly

**Experience:** Championship Production, Clovis Oncology, KPMG, NerdWallet

About the workshop
------------------
Recommendations are everywhere.  Netflix wants to recommend you movies and shows you will watch.  Stitch Fix wants to recommend you clothes you will wear.  NerdWallet wants to recommend you financial products that will improve your life and that you will be approved for, and Amazon wants to recommend you... well everything.

Prerequisites
-------------
This workshop assumes familiarity with Jupyter notebooks and basics of pandas, matplotlib and numpy.



Obtaining the Tutorial Material
--------------------------------


If you are familiar with git, it is most convenient if you clone the GitHub repository. This
is highly encouraged as it allows you to easily synchronize any changes to the material.

```
git clone https://github.com/jbernhard-nw/rec-workshop.git
```

If you are not familiar with git, you can download the repository as a .zip file by heading over to the GitHub repository (https://github.com/jbernhard-nw/rec-workshop) in your browser and click the green “Download” button in the upper right.

![](images/download-repo.png)

Please note that I may add and improve the material until shortly before the tutorial session, and we recommend you to update your copy of the materials one day before the tutorials. If you have a GitHub account and forked/cloned the repository via GitHub, you can sync your existing fork with via the following commands:

```
git pull origin master
```

Installation Notes
------------------

This tutorial will require recent installations of

- [NumPy](http://www.numpy.org)
- [SciPy](http://www.scipy.org)
- [matplotlib](http://matplotlib.org)
- [pandas](http://pandas.pydata.org)
- [turicreate](https://github.com/apple/turicreate)
- [scikit-learn](http://scikit-learn.org/stable/) (>=0.22.1)
- [IPython](http://ipython.readthedocs.org/en/stable/)
- [Jupyter Notebook](http://jupyter.org)

The last one is important, you should be able to type:

    jupyter notebook

in your terminal window and see the notebook panel load in your web browser.
Try opening and running a notebook from the material to see check that it works.

For users who do not yet have these  packages installed, a relatively painless way to install all the requirements is to use a Python distribution
such as [Anaconda](https://www.continuum.io/downloads), which includes
the most relevant Python packages for science, math, engineering, and
data analysis; Anaconda can be downloaded and installed for free
including commercial use and redistribution.
The code examples in this tutorial require Python 3.5 or later.

After obtaining the material, we **strongly recommend** you to open and execute
a Jupyter Notebook `jupyter notebook check_env.ipynb` that is located at the
top level of this repository. Inside the repository, you can open the notebook
by executing

```bash
jupyter notebook check_env.ipynb
```

inside this repository. Inside the Notebook, you can run the code cell by
clicking on the "Run Cells" button as illustrated in the figure below:

![](images/check_env-1.png)


Finally, if your environment satisfies the requirements for the tutorials, the executed code cell will produce an output message as shown below:

![](images/check_env-2.png)

References
-----------
* [Andreas Mueller's course](https://github.com/amueller/ml-workshop-1-of-4/) was used as a template for the overall layout of this workshop.  You will see certain installations and overall patterns are similar between our repositories.
