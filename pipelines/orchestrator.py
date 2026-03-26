import subprocess

subprocess.run(["python", "src/bronze/ingest_transactions.py"])
subprocess.run(["python", "src/silver/transform_transactions.py"])
subprocess.run(["python", "src/gold/business_metrics.py"])

print("Pipeline completed")
