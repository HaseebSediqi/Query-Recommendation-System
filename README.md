# Query-Recommendation-System

## Project Description
This project implements a Query Recommendation System that generates synthetic data and applies collaborative filtering techniques to recommend queries based on user preferences and similarities. The system simulates a dataset of books, users, and user queries, and then makes query recommendations by comparing past user interactions and query patterns.

## Features
### Synthetic Data Generation:

<b>A)Synthetic Data Generation:</b>
Generates datasets for books, users, and user queries, which serve as input for the recommendation engine.
Datasets include:</br>
1) Book Information: Publisher, Title, Author, and Year of Publication.</br>
2) User Information: A list of user IDs.</br>
3) User Queries: Simulated queries that form the basis for recommendation predictions.</br>

<b>B)Query-Based Collaborative Filtering:</b>
The system employs collaborative filtering methods to recommend queries by:
User-User Similarity: Identifies users with similar query patterns.
Query-Query Similarity: Recommends new queries based on their similarity to previous user queries.

## Data Generation
The Generator.py script creates synthetic data in three main parts:

- Book Dataset: Information such as Publisher, Title, Author, and Year of Publication.
- User Dataset: A list of users, each identified by a unique User ID.
- Query Dataset: Simulated user queries that ask for books based on attributes like publisher, title, and year of publication.


## Query Recommendation Engine
The <I>utils.py</I> file contains the key functions for the query recommendation system:

- <b>User Similarity Calculation:</b> Computes a similarity matrix between users based on their queries.
- <b>Query Similarity Calculation:</b> Calculates similarity between different user queries.
- <b>Collaborative Filtering Predictions:<br></b>
  1)User-Based Recommendations: Predicts new queries for a user by identifying similar users and their query patterns.<br>
  2)Query-Based Recommendations: Recommends queries that are similar to past queries made by the user.

## Jupyter Notebooks
### part A.ipynb:
Handles data loading, preprocessing, and setting up the basic recommendation system infrastructure.
Implements basic query and user similarity calculations to prepare for collaborative filtering.
### part A1.ipynb:
Continues from part A by refining the model, running more detailed similarity computations, and possibly fine-tuning model parameters.
Includes testing of the recommendation system with different scenarios and metrics like RMSE.
### part B.ipynb:
Focuses on evaluating the performance of the query recommendation system using a testing dataset.
Implements a final evaluation phase to assess the accuracy of the recommendations, including error metrics (e.g., RMSE).
How to Run
