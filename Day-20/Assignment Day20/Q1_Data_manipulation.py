import pandas as pd
import numpy as np
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 90},
    {"name": "Eva", "score": 88}
]

df = pd.DataFrame(students)

scores = np.array(df["score"])

mean_score = np.mean(scores)
median_score = np.median(scores)
std_deviation = np.std(scores)

print("Mean score:", mean_score)
print("Median score:", median_score)
print("Standard Deviation:", std_deviation)
df["above_average"] = df["score"] > mean_score

print("\nFinal DataFrame:")
print(df)
