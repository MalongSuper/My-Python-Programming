# Confusion Matrix for Multi-Classification
from sklearn.metrics import confusion_matrix
import pandas as pd


# Define a function to get all the metrics for a specific class.
def get_components(confusion_matrix, k):
    tp = confusion_matrix[k, k]
    fp = confusion_matrix[:, k].sum() - tp
    fn = confusion_matrix[k, :].sum() - tp
    tn = confusion_matrix.sum() - (tp + fp + fn)
    return tp, fp, fn, tn


true_data = [0, 1, 0, 2, 2, 1, 0, 0, 0, 1, 1, 2, 2, 2, 1]
pred_data = [0, 0, 2, 2, 1, 1, 0, 0, 0, 2, 0, 0, 2, 2, 1]
cm = confusion_matrix(true_data, pred_data)
# Convert the confusion matrix to a pandas DataFrame
row_labels = ["Predicted: 0", "Predicted: 1", "Predicted: 2"]
col_labels = ["Actual: 0", "Actual: 1", "Actual: 2"]
cm_df = pd.DataFrame(cm, index=row_labels, columns=col_labels)
print(cm_df)

# Get the unique labels
unique_labels = pd.Series(true_data).unique().tolist()

# Iterate through every class, display the components, and calculate the metrics:
for i in unique_labels:
    print(f"Label: {i}")
    tp, fp, fn, tn = get_components(cm, i)
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    specificity = tn / (tn + fp)
    f1_score = (2 * recall * precision) / (recall + precision)
    print(f"TP: {tp}; FP: {fp}; FN: {fn}; TN: {tn}")
    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"Specificity: {specificity}")
    print(f"F1 Score: {f1_score}")
    print()
