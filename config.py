from pathlib import Path
from datetime import date

# Base directory paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# CSV Data paths
PRODUCTS_FILE = DATA_DIR / "products.csv"
BATCHES_FILE = DATA_DIR / "inventory_batches.csv"
STORES_FILE = DATA_DIR / "stores.csv"
RECOMMENDATIONS_FILE = DATA_DIR / "sample_recommendations.csv"

# Reference date for demonstration (matches dataset timestamps)
DEMO_REFERENCE_DATE = date(2026, 10, 10)
