import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("student_data.csv")
print(data.head())
print(data.info())
print(data.describe())
data["Total"] = data["Python"] + data["DBMS"] + data["Java"]
top_student = data.loc[data["Total"].idxmax()]

print(top_student)
lowest_student = data.loc[data["Total"].idxmin()]

print("\nLowest Scoring Student:")
print(lowest_student)
high_scorers = data[data["Total"] > 250]

print("\nStudents scoring above 250:")
print(high_scorers)

data["Average"] = data["Total"] / 3

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "D"

data["Grade"] = data["Average"].apply(calculate_grade)

print(data)

plt.bar(data["Name"], data["Total"])
plt.title("Student Total Marks")
plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.figure(figsize=(6,6))

subject_average = [
    data["Python"].mean(),
    data["DBMS"].mean(),
    data["Java"].mean()
]

subjects = ["Python", "DBMS", "Java"]

plt.pie(subject_average, labels=subjects, autopct="%1.1f%%")

plt.title("Average Marks by Subject")
plt.show()
data.to_csv("student_report.csv", index=False)
print("Student report saved successfully!")