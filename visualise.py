import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
credits_df = pd.read_csv('tmdb_5000_credits.csv')

# Display first few rows
print(credits_df.head())
# Count the number of cast members per movie
credits_df['cast_count'] = credits_df['cast'].apply(lambda x: len(eval(x)))

# Sort and get the top 10
top_cast_movies = credits_df[['title', 'cast_count']].sort_values(by='cast_count', ascending=False).head(10)

# Plot
plt.figure(figsize=(10,6))
plt.barh(top_cast_movies['title'], top_cast_movies['cast_count'], color='skyblue')
plt.xlabel('Number of Cast Members')
plt.title('Top 10 Movies with Most Cast Members')
plt.gca().invert_yaxis()
plt.show()

plt.figure(figsize=(10,6))
plt.hist(credits_df['cast_count'], bins=30, color='purple')
plt.xlabel('Number of Cast Members')
plt.ylabel('Frequency')
plt.title('Distribution of Number of Cast Members')
plt.show()


# Extract directors from crew data
credits_df['crew_director'] = credits_df['crew'].apply(lambda x: [crew['name'] for crew in eval(x) if crew['job'] == 'Director'])

# Flatten the list of directors
all_directors = credits_df.explode('crew_director')['crew_director'].dropna()

# Count occurrences and get top 10
top_directors = all_directors.value_counts().head(10)

# Plot
plt.figure(figsize=(10,6))
plt.barh(top_directors.index, top_directors.values, color='orange')
plt.xlabel('Number of Movies Directed')
plt.title('Top 10 Directors by Number of Movies')
plt.gca().invert_yaxis()
plt.show()
