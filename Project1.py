#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 4</b> 
#     
# Great, Ash! You've done a great job on all the comments and now your project has been accepted.
#     
# Thank you for your work and I wish you success in the following projects!

# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 3</b> 
#     
#     
# Ash, hello! Please use "groupby" method to complete the last task in the project

# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 2</b> 
#     
# You did a good job with the comments, but I still have a few more comments in the very end of the project, they are marked with version 2.0 and red. Please fix them and I will accept your project)

# <div style="border:solid blue 2px; padding: 20px">
#   
# **Hello Ash**
# 
# I am happy to review your project today!
# 
# You will find my comments in coloured cells marked as 'Reviewer's comment'. The cell colour will vary based on the contents - I am explaining it further below. 
# 
# **Note:** Please do not remove or change my comments - they will help me in my future reviews and will make the process smoother for both of us. 
# 
# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment</b> 
#     
# Such comment will mark efficient solutions and good ideas that can be used in other projects.
# </div>
# 
# <div class="alert alert-warning"; style="border-left: 7px solid gold">
# <b>⚠️ Reviewer's comment</b> 
#     
# The parts marked with yellow comments indicate that there is room for optimisation. Though the correction is not necessary it is good if you implement it.
# </div>
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment</b> 
#     
# If you see such a comment, it means that there is a problem that needs to be fixed. Please note that I won't be able to accept your project until the issue is resolved.
# </div>
# 
# You are also very welcome to leave your comments / describe the corrections you've done / ask me questions, marking them with a different colour. You can use the example below: 
# 
# <div class="alert alert-info"; style="border-left: 7px solid blue">
# <b>Student's comment</b>

# ## Basic Python - Project <a id='intro'></a>

# <div style="border:solid green 2px; padding: 20px">
#     
# <div class="alert alert-success">
# <b>Review summary</b> 
#     
# Ash, thanks for submitting the project. You've done a very good job and I enjoyed reviewing it.
#     
# - You completed all the tasks.
# - Your code was optimal and easy to read. 
# - You wrote your own functions.
#     
# There are only a few critical comments that need to be corrected. You will find them in the red-colored cells in relevant sections. If you have any questions please write them when you return your project. 
#     
# I'll be looking forward to getting your updated notebook.

# ## Introduction <a id='intro'></a>
# In this project, you will work with data from the entertainment industry. You will study a dataset with records on movies and shows. The research will focus on the "Golden Age" of television, which began in 1999 with the release of *The Sopranos* and is still ongoing.
# 
# The aim of this project is to investigate how the number of votes a title receives impacts its ratings. The assumption is that highly-rated shows (we will focus on TV shows, ignoring movies) released during the "Golden Age" of television also have the most votes.
# 
# ### Stages 
# Data on movies and shows is stored in the `/datasets/movies_and_shows.csv` file. There is no information about the quality of the data, so you will need to explore it before doing the analysis.
# 
# First, you'll evaluate the quality of the data and see whether its issues are significant. Then, during data preprocessing, you will try to account for the most critical problems.
#  
# Your project will consist of three stages:
#  1. Data overview
#  2. Data preprocessing
#  3. Data analysis

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 1</b> 
#     
# Title and introduction are essential parts of the project. Make sure you do not forget to include it in your further projects. 
#     
# It is optimal if introduction consists of:
#     
# - brief description of the situation;
# - goal of the project;
# - description of the data we are going to use.
# </div>

# ## Stage 1. Data overview <a id='data_review'></a>
# 
# Open and explore the data.

# You'll need `pandas`, so import it.

# In[1]:


import pandas as pd


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 1</b> Needed library has been added </div>

# Read the `movies_and_shows.csv` file from the `datasets` folder and save it in the `df` variable:

# <div class="alert alert-warning"; style="border-left: 7px solid gold">
# <b>⚠️ Reviewer's comment, v. 1</b> 
# 
# Please note that we shouldn't import pandas library again, we should do it only in the first cell of the project

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 2</b> 
#     
# Great!

# In[2]:


# reading the files and storing them to df

df=pd.read_csv('/datasets/movies_and_shows.csv')


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 1</b> The correct path to the file is specified: the slash at the beginning of the path is very important, as it indicates that you need to search for the file in the root folder. </div>

# Print the first 10 table rows:

# In[3]:


# obtaining the first 10 rows from the df table
# hint: you can use head() and tail() in Jupyter Notebook without wrapping them into print()
print(df.head())


# Obtain the general information about the table with one command:

# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 1</b> 
#     
# Please don't import the pandas library and reload the dataset again, we should do it only once in the very beginning of the project

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 2</b> 
#     
# Now it's perfect!

# In[4]:


# obtaining general information about the data in df

df.info()


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 1</b> 
#     
# Great - you've used a comprehensive set of methods to have a first look at the data.
#     

# The table contains nine columns. The majority store the same data type: object. The only exceptions are `'release Year'` (int64 type), `'imdb sc0re'` (float64 type) and `'imdb v0tes'` (float64 type). Scores and votes will be used in our analysis, so it's important to verify that they are present in the dataframe in the appropriate numeric format. Three columns (`'TITLE'`, `'imdb sc0re'` and `'imdb v0tes'`) have missing values.
# 
# According to the documentation:
# - `'name'` — actor/director's name and last name
# - `'Character'` — character played (for actors)
# - `'r0le '` — the person's contribution to the title (it can be in the capacity of either actor or director)
# - `'TITLE '` — title of the movie (show)
# - `'  Type'` — show or movie
# - `'release Year'` — year when movie (show) was released
# - `'genres'` — list of genres under which the movie (show) falls
# - `'imdb sc0re'` — score on IMDb
# - `'imdb v0tes'` — votes on IMDb
# 
# We can see three issues with the column names:
# 1. Some names are uppercase, while others are lowercase.
# 2. There are names containing whitespace.
# 3. A few column names have digit '0' instead of letter 'o'. 
# 

# ### Conclusions <a id='data_review_conclusions'></a> 
# 
# Each row in the table stores data about a movie or show. The columns can be divided into two categories: the first is about the roles held by different people who worked on the movie or show (role, name of the actor or director, and character if the row is about an actor); the second category is information about the movie or show itself (title, release year, genre, imdb figures).
# 
# It's clear that there is sufficient data to do the analysis and evaluate our assumption. However, to move forward, we need to preprocess the data.

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 1</b> 
#     
# Please note that it is highly recommended to add a conclusion / summary after each section and describe briefly your observations and / or major outcomes of the analysis.

# ## Stage 2. Data preprocessing <a id='data_preprocessing'></a>
# Correct the formatting in the column headers and deal with the missing values. Then, check whether there are duplicates in the data.

# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 1</b> 
#     
# And also please don't import the pandas library and reload the dataset again, we should do it only once in the very beginning of the project

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 2</b> 
#     
# Well done!

# In[5]:


# the list of column names in the df table

df.columns = df.columns.str.strip()
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace('0','o')


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 1</b> 
#     
# This is a good way to rename the columns.

# Change the column names according to the rules of good style:
# * If the name has several words, use snake_case
# * All characters must be lowercase
# * Remove whitespace
# * Replace zero with letter 'o'

# In[6]:


# renaming columns
df.columns


# Check the result. Print the names of the columns once more:

# In[7]:


# checking result: the list of column names
df.columns


# ### Missing values <a id='missing_values'></a>
# First, find the number of missing values in the table. To do so, combine two `pandas` methods:

# In[8]:


# calculating missing values
print(df.isnull().sum())  


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 1</b> 
#     
# The isnull() method is selected to find the missing values, it's great!

# Not all missing values affect the research: the single missing value in `'title'` is not critical. The missing values in columns `'imdb_score'` and `'imdb_votes'` represent around 6% of all records (4,609 and 4,726, respectively, of the total 85,579). This could potentially affect our research. To avoid this issue, we will drop rows with missing values in the `'imdb_score'` and `'imdb_votes'` columns.

# In[9]:


# dropping rows where columns with title, scores and votes have missing values
df.dropna(inplace=True)


# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 1</b> 
#     
# Please just use this code:
#     
#     df.dropna(inplace=True)
#     
# To remove all the missing values in the dataset

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 2</b> 
#     
# Yep, that's it!

# Make sure the table doesn't contain any more missing values. Count the missing values again.

# In[10]:


# counting missing values
print(df.isnull().sum())


# ### Duplicates <a id='duplicates'></a>
# Find the number of duplicate rows in the table using one command:

# In[11]:


# counting duplicate rows
duplicate_count = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_count}")


# Review the duplicate rows to determine if removing them would distort our dataset.

# In[12]:


# Produce table with duplicates (with original rows included) and review last 5 rows
duplicate_rows_df = df[df.duplicated(keep=False)]
duplicate_rows_df.tail()


# There are two clear duplicates in the printed rows. We can safely remove them.
# Call the `pandas` method for getting rid of duplicate rows:

# In[13]:


# removing duplicate rows
df = df.drop_duplicates()


# Check for duplicate rows once more to make sure you have removed all of them:

# In[14]:


# checking for duplicates
num_duplicates_after = df.duplicated().sum()
print(f"Number of duplicate rows after removal: {num_duplicates_after}")


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 1</b> 
#     
# Great, you found and removed the duplicates. And did very thorough check to make sure the duplicates are gone.

# Now get rid of implicit duplicates in the `'type'` column. For example, the string `'SHOW'` can be written in different ways. These kinds of errors will also affect the result.

# Print a list of unique `'type'` names, sorted in alphabetical order. To do so:
# * Retrieve the intended dataframe column 
# * Apply a sorting method to it
# * For the sorted column, call the method that will return all unique column values

# In[15]:


# viewing unique type names
unique_types = sorted(df['type'].unique())
print(unique_types)


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 1</b> 
#     
# This is good. 

# Look through the list to find implicit duplicates of `'show'` (`'movie'` duplicates will be ignored since the assumption is about shows). These could be names written incorrectly or alternative names of the same genre.
# 
# You will see the following implicit duplicates:
# * `'shows'`
# * `'SHOW'`
# * `'tv show'`
# * `'tv shows'`
# * `'tv series'`
# * `'tv'`
# 
# To get rid of them, declare the function `replace_wrong_show()` with two parameters: 
# * `wrong_shows_list=` — the list of duplicates
# * `correct_show=` — the string with the correct value
# 
# The function should correct the names in the `'type'` column from the `df` table (i.e., replace each value from the `wrong_shows_list` list with the value in `correct_show`).

# In[16]:


# function for replacing implicit duplicates
def replace_wrong_show(df, wrong_shows_list, correct_show):
    df['type'] = df['type'].replace(wrong_shows_list, correct_show)
    return df


# Call `replace_wrong_show()` and pass it arguments so that it clears implicit duplicates and replaces them with `SHOW`:

# In[17]:


# removing implicit duplicates
wrong_shows_list = ['shows', 'SHOW', 'tv shows', 'tv', 'tv series', 'Tv', 'TV', 'Tv Series', 'Show']
correct_show = 'show'


# Make sure the duplicate names are removed. Print the list of unique values from the `'type'` column:

# In[18]:


# viewing unique genre names
wrong_shows_list = ['shows', 'SHOW', 'tv shows', 'tv', 'tv series', 'Tv', 'TV', 'Tv Series', 'Show']
correct_show = 'show'
df = replace_wrong_show(df, wrong_shows_list, correct_show)

unique_genres = df['type'].unique()


print("Unique genre/type names in the 'type' column:")
print(unique_genres)


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 1</b> 
#     
# Yes, this is what was needed!

# ### Conclusions <a id='data_preprocessing_conclusions'></a>
# We detected three issues with the data:
# 
# - Incorrect header styles
# - Missing values
# - Duplicate rows and implicit duplicates
# 
# The headers have been cleaned up to make processing the table simpler.
# 
# All rows with missing values have been removed. 
# 
# The absence of duplicates will make the results more precise and easier to understand.
# 
# Now we can move on to our analysis of the prepared data.

# ## Stage 3. Data analysis <a id='hypotheses'></a>

# Based on the previous project stages, you can now define how the assumption will be checked. Calculate the average amount of votes for each score (this data is available in the `imdb_score` and `imdb_votes` columns), and then check how these averages relate to each other. If the averages for shows with the highest scores are bigger than those for shows with lower scores, the assumption appears to be true.
# 
# Based on this, complete the following steps:
# 
# - Filter the dataframe to only include shows released in 1999 or later.
# - Group scores into buckets by rounding the values of the appropriate column (a set of 1-10 integers will help us make the outcome of our calculations more evident without damaging the quality of our research).
# - Identify outliers among scores based on their number of votes, and exclude scores with few votes.
# - Calculate the average votes for each score and check whether the assumption matches the results.

# In[19]:


df


# To filter the dataframe and only include shows released in 1999 or later, you will take two steps. First, keep only titles published in 1999 or later in our dataframe. Then, filter the table to only contain shows (movies will be removed).

# In[20]:


# using conditional indexing modify df so it has only titles released after 1999 (with 1999 included)
# give the slice of dataframe new name

filtered_shows = df[df['release year'] >= 1999]


# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 1</b> 
#     
# Please don't create a new dataframe here. We should work with our df dataframe frome the previous cells, we should just **give the slice of dataframe new name** in the filtering

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 2</b> 
#     
# And it's great again!

# In[21]:


# repeat conditional indexing so df has only shows (movies are removed as result)
filtered_shows = filtered_shows[filtered_shows['type'] == 'show']


# The scores that are to be grouped should be rounded. For instance, titles with scores like 7.8, 8.1, and 8.3 will all be placed in the same bucket with a score of 8.

# In[22]:


# rounding column with scores

filtered_shows['score_bucket'] = filtered_shows['imdb score'].round().astype(int)


# It is now time to identify outliers based on the number of votes.

# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 1</b> 
#     
# Please count all unique values in each group instead of calculating average in the code cell below

# In[23]:


# Use groupby() for scores and count all unique values in each group, print the result
average_votes_per_score = filtered_shows.groupby('score_bucket').size()


# In[24]:


average_votes_per_score


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 2</b> 
#     
# The dataframe was filtered and grouped flawlessly

# Based on the aggregation performed, it is evident that scores 2 (24 voted shows), 3 (27 voted shows), and 10 (only 8 voted shows) are outliers. There isn't enough data for these scores for the average number of votes to be meaningful.

# To obtain the mean numbers of votes for the selected scores (we identified a range of 4-9 as acceptable), use conditional filtering and grouping.

# In[28]:


# filter dataframe using two conditions (scores to be in the range 4-9)
filtered_shows = filtered_shows[(filtered_shows['score_bucket'] >= 4) & (filtered_shows['score_bucket'] <= 9)]
average_votes_per_score = filtered_shows.groupby('score_bucket')['imdb votes'].mean().reset_index()
average_votes_per_score


# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 1</b> 
#     
# Please correct the code first according to the comments above so that it is possible to correctly complete the task here. Also, at the beginning of the code cell above, you are trying to filter in a dataset that does not exist

# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 2</b> 
#     
# Please:
#     
# * don't filter the 'imdb votes' column in the code cell above;
#     
# * show the result of the grouping from the "average_votes_per_score" on the screen;

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 3</b> 
#     
# You made the filtering very well

# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 3</b> 
#     
#     
# But please - `obtain the mean numbers of votes for the selected scores`. We should use "groupby" method here, now it is missing

# Now for the final step! Round the column with the averages, rename both columns, and print the dataframe in descending order.

# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 2</b> 
#     
# Please note that here we should - `Round the column with the averages, rename both columns, and print the dataframe in descending order.`

# In[ ]:


average_votes_per_score


# The assumption macthes the analysis: the shows with the top 3 scores have the most amounts of votes.

# ## Conclusion <a id='hypotheses'></a>

# The research done confirms that highly-rated shows released during the "Golden Age" of television also have the most votes. While shows with score 4 have more votes than ones with scores 5 and 6, the top three (scores 7-9) have the largest number. The data studied represents around 94% of the original set, so we can be confident in our findings.
