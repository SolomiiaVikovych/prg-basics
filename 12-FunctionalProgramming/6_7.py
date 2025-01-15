# Ratings of the four players
ratings = [
    (17, 15, 16, 17, 15),
    (16, 18, 19, 17, 19),
    (19, 15, 15, 19, 18),
    (18, 17, 19, 15, 16)
]

# Function to calculate the total score for each competitor
def calculate_total_score(scores):
    return sum(scores) - min(scores) - max(scores)

# Calculate the total scores for all competitors
total_scores = list(map(calculate_total_score, ratings))

# Display the total scores
print(total_scores)
