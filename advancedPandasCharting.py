# Wallace Tyner

# Display Student ID
print("waltyn4684")

# Import pandas for DataFrames
import pandas as pd

# Import matplotlib for graphing
import matplotlib.pyplot as plt

# -----------------------------
# Student roster
# -----------------------------

students = [
    ["James", "James", "Sarah", "Sarah", "Michael",
     "Michael", "Ashley", "Ashley", "David", "David",
     "Emily", "Emily", "Joshua", "Joshua", "Olivia",
     "Olivia", "Daniel", "Daniel", "Sophia", "Sophia"],

    ["Math", "Science", "Math", "Science", "Math",
     "Science", "Math", "Science", "Math", "Science",
     "Math", "Science", "Math", "Science", "Math",
     "Science", "Math", "Science", "Math", "Science"]
]

# Create indexes for Student and Subject
index = pd.MultiIndex.from_arrays(
    students,
    names=("Student", "Subject")
)

# Create DataFrame of grades
df = pd.DataFrame(
    {
        "Grade": [
            88, 91,
            94, 89,
            78, 84,
            92, 95,
            85, 87,
            97, 94,
            82, 80,
            90, 93,
            76, 79,
            99, 96
        ]
    },
    index=index
)

# Display DataFrame
print(df)

# -----------------------------
# Group grades by subject
# -----------------------------

averageGrades = df.groupby(
    by=["Subject"]
).mean()

print(averageGrades)

# -----------------------------
# Create graph
# -----------------------------

averageGrades["Grade"].plot(kind="bar")

plt.xlabel("Average Grade by Subject")

plt.xticks(rotation=0)

plt.title("waltyn4684 Grouped Grade Chart")

plt.show()
