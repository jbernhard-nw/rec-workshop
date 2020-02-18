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
    - Spearman's Correlation Coefficient
    - Kendall's Tau
    - Euclidean Distance
    - Manhattan Distance
    - Jaccard Similarity
    - Cosine Similarity
- Collaborative Filtering
    - User-user collaborative filtering
    - Item-item collaborative filtering
- Matrix Factorization
    - Latent Factors
    - FunkSVD

#### Navigating this Section

- [Slide Set 1: Measures of Similarity]()
    - [Notebook 1: Measures of Similarity]()
    - [Notebook 1: Measures of Similarity - Solutions]()
- [Slide Set 2: Collaborative Filtering]()
    - [Notebook 2: Collaborative Filtering]()
    - [Notebook 2: Collaborative Filtering - Solutions]()
- [Slide Set 3: Matrix Factorization for Recommendation Systems]()
    - [Notebook 3: Matrix Factorization]()
    - [Notebook 3: Matrix Factorization - Solutions]()
