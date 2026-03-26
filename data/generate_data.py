import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
NUM_CUSTOMERS = 100
NUM_TRANSACTIONS = 5000

categories = ["Food", "Rent", "Travel", "Shopping", "Bills"]

data = []
for i in range(NUM_TRANSACTIONS):
    transaction_date = datetime.now() - timedelta(days=random.randint(0, 365))
    amount = round(random.uniform(100, 5000), 2)
    transaction_type = random.choice(["credit", "debit"])

    if transaction_type == "debit":
        amount = -amount

    data.append({
        "transaction_id": i+1,
        "customer_id": random.randint(1, NUM_CUSTOMERS),
        "amount": amount,
        "category": random.choice(categories),
        "transaction_date": transaction_date
    })

df = pd.DataFrame(data)
df.to_csv("data/raw/transactions.csv", index=False)

print("Data generated")
