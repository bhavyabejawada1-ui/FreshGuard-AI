from datetime import datetime, date
from typing import List, Dict, Any, Optional
import pandas as pd
from app.config import (
    PRODUCTS_FILE,
    BATCHES_FILE,
    STORES_FILE,
    RECOMMENDATIONS_FILE,
    DEMO_REFERENCE_DATE,
)


class GroceryDataLoader:
    """Loads and computes freshness & risk metrics from CSV data files."""

    def __init__(self, reference_date: Optional[date] = None):
        self.reference_date = reference_date or DEMO_REFERENCE_DATE
        self._load_datasets()

    def _load_datasets(self) -> None:
        """Reads CSV files into pandas DataFrames."""
        self.products_df = pd.read_csv(PRODUCTS_FILE)
        self.batches_df = pd.read_csv(BATCHES_FILE)
        self.stores_df = pd.read_csv(STORES_FILE)
        self.recs_df = pd.read_csv(RECOMMENDATIONS_FILE)

    def reload(self) -> None:
        """Reload datasets from disk."""
        self._load_datasets()

    def get_enriched_batches(self) -> pd.DataFrame:
        """Merges batches with product and store details, and computes freshness metrics."""
        # Merge batch with product info
        merged = self.batches_df.merge(self.products_df, on="sku", how="left")
        # Merge with store info
        merged = merged.merge(self.stores_df, on="store_id", how="left")

        # Compute days to expiry relative to reference date
        expiry_series = pd.to_datetime(merged["expiry_date"]).dt.date
        days_left = (expiry_series - self.reference_date).apply(lambda d: d.days)
        merged["days_to_expiry"] = days_left

        # Freshness classification
        def classify_freshness(days: int) -> str:
            if days < 0:
                return "EXPIRED"
            elif days <= 1:
                return "CRITICAL"
            elif days <= 3:
                return "EXPIRING_SOON"
            else:
                return "FRESH"

        merged["freshness_status"] = merged["days_to_expiry"].apply(classify_freshness)

        # Stockout risk flag
        merged["is_stockout_risk"] = merged["quantity"] <= merged["reorder_threshold"]

        # Waste calculations
        # Estimated waste cost: full unit cost of items that are critical or near-expiry
        merged["estimated_waste_cost"] = merged.apply(
            lambda row: round(row["quantity"] * row["unit_cost"], 2)
            if row["freshness_status"] in ["CRITICAL", "EXPIRING_SOON", "EXPIRED"]
            else 0.0,
            axis=1,
        )

        return merged

    def get_batches(
        self,
        store_id: Optional[str] = None,
        category: Optional[str] = None,
        search: Optional[str] = None,
        freshness: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """Filters and returns enriched inventory batch items as dictionaries."""
        df = self.get_enriched_batches()

        if store_id and store_id != "ALL":
            df = df[df["store_id"] == store_id]

        if category and category != "ALL":
            df = df[df["category"].str.lower() == category.lower()]

        if freshness and freshness != "ALL":
            df = df[df["freshness_status"].str.upper() == freshness.upper()]

        if search:
            query = search.strip().lower()
            df = df[
                df["name"].str.lower().str.contains(query)
                | df["sku"].str.lower().str.contains(query)
                | df["batch_id"].str.lower().str.contains(query)
                | df["category"].str.lower().str.contains(query)
            ]

        # Sort so critical & near-expiry items appear at the top
        df = df.sort_values(by=["days_to_expiry", "quantity"], ascending=[True, True])

        return df.to_dict(orient="records")

    def get_summary_metrics(self, store_id: Optional[str] = None) -> Dict[str, Any]:
        """Calculates store or aggregate KPI metrics."""
        df = self.get_enriched_batches()

        if store_id and store_id != "ALL":
            df = df[df["store_id"] == store_id]

        near_expiry_batches = df[df["freshness_status"].isin(["CRITICAL", "EXPIRING_SOON"])]
        critical_batches = df[df["freshness_status"] == "CRITICAL"]
        stockout_batches = df[df["is_stockout_risk"]]

        # Estimated waste cost in USD
        waste_usd = round(near_expiry_batches["estimated_waste_cost"].sum(), 2)

        # Approximate waste weight in kg (avg 0.45 kg per packaged perishable unit)
        units_at_risk = near_expiry_batches["quantity"].sum()
        waste_kg = round(units_at_risk * 0.45, 1)

        # Potential retail revenue lost
        retail_loss = round(
            (near_expiry_batches["quantity"] * near_expiry_batches["selling_price"]).sum(),
            2,
        )

        return {
            "total_products": int(df["sku"].nunique()),
            "total_batches": int(len(df)),
            "total_units": int(df["quantity"].sum()),
            "near_expiry_count": int(len(near_expiry_batches)),
            "critical_expiry_count": int(len(critical_batches)),
            "stockout_risk_count": int(len(stockout_batches)),
            "estimated_waste_usd": float(waste_usd),
            "estimated_waste_kg": float(waste_kg),
            "potential_revenue_at_risk_usd": float(retail_loss),
            "simulated": True,
        }

    def get_categories(self) -> List[str]:
        """Returns sorted unique category names."""
        return sorted(self.products_df["category"].dropna().unique().tolist())

    def get_stores(self) -> List[Dict[str, Any]]:
        """Returns list of store locations."""
        return self.stores_df.to_dict(orient="records")

    def get_recommendations(self, store_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """Returns simulated recommendations."""
        df = self.recs_df.copy()
        if store_id and store_id != "ALL":
            df = df[df["store_id"] == store_id]
        return df.to_dict(orient="records")


# Singleton instance
data_loader = GroceryDataLoader()
