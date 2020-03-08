# Part 3 - Recommendation Systems

In Part 2, you learned about the different data sources you might use when building a recommendation system.  The most important data for most any recommendation system is the user-item interaction data, which is represented in either a dense or sparse matrix with ratings or binary data values.

You might (attempt to) improve your recommendation system by including user or item information, which frequently involves:

* normalizing/standardizing quantitative variables
* creating dummy values for categorical variables
* creating embeddings or a tf-idf representation from content

In this section we will focus on making the most of the user-item data to provide useful recommendations.  First, you will learn about different measures of similarity.  Then you will use these measures of similarity to implement user-user or item-item collaborative filtering recommendations.

Then you will learn about latent factors and matrix factorization techniques, and how they can be used to implement state of art recommendation systems.

#### Terms & Concepts
- Measures of Similarity
    - Pearson's Correlation Coefficient
    - Cosine Similarity
    - Spearman's Correlation Coefficient
    - Jaccard Similarity
- Collaborative Filtering
    - User-user collaborative filtering
    - Item-item collaborative filtering
- Matrix Factorization
    - Latent Factors
    - FunkSVD

#### Navigating this Section

- [Slide Set 1: Recommendation Systems 101](https://github.com/jbernhard-nw/rec-workshop/blob/master/Part%203%20-%20Recommendation%20Systems/slides/PartIII_Recommendation_Systems_101.pdf)
- [Slide Set 2: Measures of Similarity](https://github.com/jbernhard-nw/rec-workshop/blob/master/Part%203%20-%20Recommendation%20Systems/slides/PartIII_Measures_of_Similarity.pdf)
    - [Notebook 2: Measures of Similarity](https://github.com/jbernhard-nw/rec-workshop/blob/master/Part%203%20-%20Recommendation%20Systems/notebooks/measures_of_similarity.ipynb)
    - [Notebook 2: Measures of Similarity - Solutions](https://github.com/jbernhard-nw/rec-workshop/blob/master/Part%203%20-%20Recommendation%20Systems/notebooks/solutions/measures_of_similarity-Solution.ipynb)
- [Slide Set 3: Collaborative Filtering](https://github.com/jbernhard-nw/rec-workshop/blob/master/Part%203%20-%20Recommendation%20Systems/slides/PartIII_Collaborative_Filtering.pdf)
    - [Notebook 3: Collaborative Filtering](https://github.com/jbernhard-nw/rec-workshop/blob/master/Part%203%20-%20Recommendation%20Systems/notebooks/collaborative_filtering.ipynb)
    - [Notebook 3: Collaborative Filtering - Solutions](https://github.com/jbernhard-nw/rec-workshop/blob/master/Part%203%20-%20Recommendation%20Systems/notebooks/solutions/collaborative_filtering-Solution.ipynb)
- [Slide Set 4: Matrix Factorization for Recommendation Systems]()
    - [Notebook 4: Matrix Factorization]()
    - [Notebook 4: Matrix Factorization - Solutions]()
