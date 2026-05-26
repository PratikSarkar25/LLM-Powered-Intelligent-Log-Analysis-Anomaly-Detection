# import pandas as pd

# def detect_anomalies(df):
#     issues = []
#     err = df[df['level']=='ERROR']
#     if len(err) > 0:
#         issues.append(f'{len(err)} ERROR events detected')
#     brute = df[df['message'].str.contains('failed login', case=False, na=False)]
#     if len(brute) > 0:
#         issues.append('Suspicious login activity detected')
#     return issues


import pandas as pd
from sklearn.ensemble import IsolationForest
from sentence_transformers import SentenceTransformer
import numpy as np


model = SentenceTransformer('all-MiniLM-L6-v2')


# -----------------------------------
# Embedding-Based Anomaly Detection
# -----------------------------------
def embedding_anomaly_detection(df):

    messages = df['message'].astype(str).tolist()

    embeddings = model.encode(messages)

    clf = IsolationForest(
        contamination=0.05,
        random_state=42
    )

    preds = clf.fit_predict(embeddings)

    anomaly_indices = np.where(preds == -1)[0]

    return anomaly_indices.tolist()


# -----------------------------------
# Frequency-Based Detection
# -----------------------------------
def frequency_anomalies(df):

    issues = []

    counts = (
        df.groupby(['service', 'event_type'])
        .size()
        .reset_index(name='count')
    )

    threshold = counts['count'].mean() * 2

    spikes = counts[counts['count'] > threshold]

    for _, row in spikes.iterrows():

        issues.append(
            f"Spike detected: "
            f"{row['service']} -> "
            f"{row['event_type']} "
            f"({row['count']} events)"
        )

    return issues


# -----------------------------------
# Critical Error Detection
# -----------------------------------
def critical_errors(df):

    issues = []

    critical = df[
        df['severity_score'] >= 3
    ]

    if len(critical) > 0:

        issues.append(
            f'{len(critical)} high severity events detected'
        )

    return issues


# -----------------------------------
# Login Attack Detection
# -----------------------------------
def brute_force_detection(df):

    issues = []

    brute = df[
        df['message']
        .str.contains(
            'failed login|unauthorized',
            case=False,
            na=False
        )
    ]

    if len(brute) > 5:

        issues.append(
            f'Suspicious authentication activity '
            f'({len(brute)} events)'
        )

    return issues


# -----------------------------------
# Main Detection Pipeline
# -----------------------------------
def detect_anomalies(df):

    issues = []

    # Rule-based checks
    issues.extend(critical_errors(df))

    issues.extend(brute_force_detection(df))

    issues.extend(frequency_anomalies(df))

    # ML-based anomaly detection
    anomaly_idx = embedding_anomaly_detection(df)

    if len(anomaly_idx) > 0:

        issues.append(
            f'{len(anomaly_idx)} semantic anomalies detected'
        )

    return issues


# -----------------------------------
# Testing
# -----------------------------------
if __name__ == '__main__':

    from parser import load_logs

    df = load_logs()

    anomalies = detect_anomalies(df)

    print('\nDetected anomalies:\n')

    for a in anomalies:
        print('-', a)
