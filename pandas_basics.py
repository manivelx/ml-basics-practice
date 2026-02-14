import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [85, 45, 78, 92],
    "Study_Hours": [4, 2, 3, 5]
}

df = pd.DataFrame(data)

print(df)

print("Students > 3 hours:")
print(df[df["Study_Hours"] > 3])

print("Average Marks:", df["Marks"].mean())

df["Pass"] = df["Marks"] > 50
print(df)
