# Methodology
1. Generate a reproducible synthetic dataset (seed 42) with 15,000 tickets plus intentional quality issues.
2. Profile and clean data using documented, reversible rules; raw files remain unchanged in `data/raw`.
3. Load normalized tables into SQLite with foreign keys and analytical indexes.
4. Execute 38 catalogued read-only SQL queries; export every result to `exports/`.
5. Build the Streamlit dashboard, notebook, tests, and Markdown business report from the same database.
