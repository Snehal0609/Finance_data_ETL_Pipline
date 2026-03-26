##  Architecture
Bronze → Silver → Gold (Medallion Architecture)

##  Data Flow
Raw CSV → Bronze (Delta) → Silver (Cleaned) → Gold (Aggregated Metrics)

##  Key Features
- Delta Lake (ACID transactions)
- Modular pipeline design
- Config-driven architecture
- End-to-end orchestration

##  Azure Mapping
- ADF → Orchestrator
- ADLS → Data folder
- Databricks → PySpark jobs