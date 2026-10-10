from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from app.data_loader import data_loader
from app.models import (
    HealthResponse,
    SummaryMetrics,
    ProductBatchItem,
    Recommendation,
    Store,
)

app = FastAPI(
    title="FreshGuard AI - Perishable Demand & Shelf-Life Management API",
    description="Backend API for zero-waste grocery inventory, freshness tracking, and replenishment recommendations.",
    version="1.0.0",
)

# Configure CORS to allow frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For hackathon/local development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
def root():
    return {
        "project": "FreshGuard AI",
        "tagline": "Zero-Waste Grocery Perishable Demand & Shelf-Life Management",
        "version": "1.0.0",
        "milestone": "Milestone 1 - Foundation & Interactive Inventory Dashboard",
        "documentation": "/docs",
    }


@app.get("/api/health", response_model=HealthResponse, tags=["System"])
def health_check():
    """Verify backend health and data loading status."""
    return HealthResponse(
        status="healthy",
        version="1.0.0",
        message="FreshGuard AI backend is running smoothly.",
        timestamp=datetime.now().isoformat(),
        total_products_loaded=len(data_loader.products_df),
        total_batches_loaded=len(data_loader.batches_df),
    )


@app.get("/api/summary", response_model=SummaryMetrics, tags=["Dashboard"])
def get_summary(store_id: Optional[str] = Query(None, description="Optional store filter")):
    """Get high-level summary KPIs (total products, near-expiry, stockout risks, estimated waste)."""
    return data_loader.get_summary_metrics(store_id=store_id)


@app.get("/api/products", response_model=List[ProductBatchItem], tags=["Inventory"])
def get_products(
    store_id: Optional[str] = Query(None, description="Filter by store ID"),
    category: Optional[str] = Query(None, description="Filter by product category"),
    search: Optional[str] = Query(None, description="Search query across product name, SKU, or batch"),
    freshness: Optional[str] = Query(None, description="Filter by freshness status (FRESH, EXPIRING_SOON, CRITICAL, EXPIRED)"),
):
    """Get inventory batch list with filters and dynamic freshness status."""
    return data_loader.get_batches(
        store_id=store_id,
        category=category,
        search=search,
        freshness=freshness,
    )


@app.get("/api/categories", response_model=List[str], tags=["Inventory"])
def get_categories():
    """Get all unique product categories."""
    return data_loader.get_categories()


@app.get("/api/stores", response_model=List[Store], tags=["Stores"])
def get_stores():
    """Get all grocery store locations."""
    return data_loader.get_stores()


@app.get("/api/recommendations", response_model=List[Recommendation], tags=["Recommendations"])
def get_recommendations(store_id: Optional[str] = Query(None, description="Filter by store ID")):
    """Get sample recommendations for markdown, replenishment, and inter-store transfers."""
    return data_loader.get_recommendations(store_id=store_id)
