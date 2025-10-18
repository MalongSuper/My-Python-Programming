# This is finds all students with more than 99 percentile
import numpy as np


def percentile(scores):
    percentile_99th = np.percentile(scores, 99)
    high_percentile = np.where(scores > percentile_99th)[0]
    return high_percentile


student = 1000
student_score = np.random.randint(0, 101, size=student)
print("\t\t\t\t\t\t1000 Students Score")
print("--------------------------------------------------------------------------")
print(student_score)
result = percentile(student_score)
print(f"The Students who secured more than 99 percentile: {', '.join(map(str, result))}")
