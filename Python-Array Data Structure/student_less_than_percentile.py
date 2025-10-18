# This is finds all students with less than 1 percentile
import numpy as np


def percentile(scores):
    percentile_1th = np.percentile(scores, 1)
    high_percentile = np.where(scores < percentile_1th)[0]
    return high_percentile


student = 1000
student_score = np.random.randint(0, 101, size=student)
print("\t\t\t\t\t\t1000 Students Score")
print("--------------------------------------------------------------------------")
print(student_score)
result = percentile(student_score)
print(f"The Students who secured less than 1 percentile: {', '.join(map(str, result))}")
