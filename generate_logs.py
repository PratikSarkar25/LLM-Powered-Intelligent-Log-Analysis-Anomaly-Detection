# import pandas as pd
# import random
# from datetime import datetime, timedelta

# levels = ["INFO", "WARN", "ERROR"]
# services = ["auth", "payment", "erp", "db", "network", "system", "security", "payroll"]

# messages = {
#     "INFO": [
#         "User login successful",
#         "Batch job completed",
#         "System running normally",
#         "Transaction processed",
#         "Service restarted"
#     ],
#     "WARN": [
#         "High memory usage",
#         "Multiple failed login attempts",
#         "Suspicious IP detected",
#         "Network latency high",
#         "Disk nearing capacity"
#     ],
#     "ERROR": [
#         "Database timeout",
#         "Payment API failure",
#         "Unauthorized access attempt",
#         "Connection pool exhausted",
#         "Transaction failed"
#     ]
# }

# rows = []
# start_time = datetime(2026, 4, 22, 9, 0, 0)

# for i in range(1000):
#     level = random.choice(levels)
#     service = random.choice(services)
#     message = random.choice(messages[level])
#     timestamp = start_time + timedelta(seconds=i * random.randint(5, 20))
    
#     rows.append([timestamp, level, service, message])

# df = pd.DataFrame(rows, columns=["timestamp", "level", "service", "message"])
# df.to_csv("sample_logs.csv", index=False)

# print("✅ Large log dataset generated!")




import pandas as pd
import random
from datetime import datetime, timedelta


# -----------------------------------
# Enterprise Services
# -----------------------------------
services = [
    "auth-service",
    "payment-service",
    "db-service",
    "api-gateway",
    "network-service",
    "erp-service",
    "security-service",
    "cache-service"
]


# -----------------------------------
# Log Templates
# -----------------------------------
log_templates = {

    "INFO": [
        "User login successful",
        "Batch job completed",
        "Service restarted successfully",
        "Transaction processed successfully",
        "Heartbeat received",
        "Cache refreshed",
        "API request completed"
    ],

    "WARN": [
        "High memory usage detected",
        "Disk nearing capacity",
        "Network latency high",
        "Slow database response",
        "Retrying failed API request",
        "Multiple failed login attempts"
    ],

    "ERROR": [
        "Database timeout",
        "Payment API failure",
        "Unauthorized access attempt",
        "Connection pool exhausted",
        "Transaction failed",
        "Redis cache unavailable",
        "JWT authentication failure",
        "API gateway timeout",
        "Database connection lost",
        "Node crashed unexpectedly"
    ]
}


# -----------------------------------
# Correlated Failure Chains
# -----------------------------------
incident_chains = [

    [
        ("ERROR", "auth-service",
         "JWT authentication failure"),

        ("ERROR", "cache-service",
         "Redis cache unavailable"),

        ("ERROR", "api-gateway",
         "API gateway timeout")
    ],

    [
        ("WARN", "network-service",
         "Network latency high"),

        ("ERROR", "db-service",
         "Database timeout"),

        ("ERROR", "payment-service",
         "Transaction failed")
    ]
]


# -----------------------------------
# Generate Logs
# -----------------------------------
rows = []

start_time = datetime(2026, 5, 1, 10, 0, 0)

current_time = start_time


for i in range(3000):

    # Random normal log
    level = random.choice(
        ["INFO", "INFO", "INFO",
         "WARN", "ERROR"]
    )

    service = random.choice(services)

    message = random.choice(
        log_templates[level]
    )

    rows.append([
        current_time,
        level,
        service,
        message
    ])

    # Generate correlated incidents
    if random.random() < 0.08:

        chain = random.choice(incident_chains)

        for lvl, svc, msg in chain:

            rows.append([
                current_time,
                lvl,
                svc,
                msg
            ])

    # Random time progression
    current_time += timedelta(
        seconds=random.randint(1, 10)
    )


# -----------------------------------
# Create DataFrame
# -----------------------------------
df = pd.DataFrame(
    rows,
    columns=[
        "timestamp",
        "level",
        "service",
        "message"
    ]
)


# -----------------------------------
# Save Dataset
# -----------------------------------
df.to_csv(
    "sample_logs.csv",
    index=False
)

print(
    f'✅ Generated enterprise log dataset '
    f'with {len(df)} logs'
)
