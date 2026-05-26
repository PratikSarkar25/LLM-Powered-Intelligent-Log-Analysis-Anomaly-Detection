# import pandas as pd

# def load_logs(path='sample_logs.csv'):
#     df = pd.read_csv(path)
#     df['timestamp'] = pd.to_datetime(df['timestamp'])
#     return df




import pandas as pd
import re
from datetime import datetime


# -----------------------------
# Severity Mapping
# -----------------------------
SEVERITY_MAP = {
    'INFO': 1,
    'WARN': 2,
    'ERROR': 3,
    'CRITICAL': 4
}


# -----------------------------
# Event Template Extraction
# -----------------------------
def extract_template(message):

    msg = str(message)

    # Replace numbers
    msg = re.sub(r'\d+', '<NUM>', msg)

    # Replace IP addresses
    msg = re.sub(
        r'(?:\d{1,3}\.){3}\d{1,3}',
        '<IP>',
        msg
    )

    # Replace UUID-like patterns
    msg = re.sub(
        r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}',
        '<ID>',
        msg,
        flags=re.IGNORECASE
    )

    return msg


# -----------------------------
# Event Type Detection
# -----------------------------
def detect_event_type(message):

    msg = str(message).lower()

    if 'timeout' in msg:
        return 'timeout'

    if 'login' in msg or 'authentication' in msg:
        return 'authentication'

    if 'payment' in msg:
        return 'payment'

    if 'database' in msg or 'db' in msg:
        return 'database'

    if 'network' in msg:
        return 'network'

    if 'memory' in msg:
        return 'memory'

    if 'disk' in msg:
        return 'disk'

    return 'general'


# -----------------------------
# Main Parser
# -----------------------------
def load_logs(path='sample_logs.csv'):

    df = pd.read_csv(path)

    # Convert timestamp
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Normalize columns
    df['level'] = df['level'].str.upper()

    # Severity score
    df['severity_score'] = (
        df['level']
        .map(SEVERITY_MAP)
        .fillna(1)
    )

    # Event templates
    df['template'] = (
        df['message']
        .apply(extract_template)
    )

    # Event category
    df['event_type'] = (
        df['message']
        .apply(detect_event_type)
    )

    # Unique event id
    df['event_id'] = (
        df['event_type'] + '_' +
        df['severity_score'].astype(str)
    )

    return df


# -----------------------------
# Testing
# -----------------------------
if __name__ == '__main__':

    df = load_logs()

    print(df.head())
    print(df.columns)

