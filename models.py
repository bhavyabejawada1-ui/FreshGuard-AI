from typing import List, Optional
from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    version: str
    message: str
    timestamp: str
    total_products_loaded: int
    total_batches_loaded: int


class Store(BaseModel):
    store_id: str
    store_name: str
    city: str
    address: str
    manager: str


class ProductBatchItem(BaseModel):
    batch_id: str
    sku: str
    name: str
    category: str
    unit: str
    unit_cost: float
    selling_price: float
    ideal_storage_temp: str
    store_id: str
    store_name: str
    quantity: int
    received_date: str
    expiry_date: str
    days_to_expiry: int
    freshness_status: str  # FRESH, EXPIRING_SOON, CRITICAL, EXPIRED
    reorder_threshold: int
    is_stockout_risk: bool
    estimated_waste_cost: float


class SummaryMetrics(BaseModel):
    total_products: int
    total_batches: int
    total_units: int
    near_expiry_count: int
    critical_expiry_count: int
    stockout_risk_count: int
    estimated_waste_usd: float
    estimated_waste_kg: float
    potential_revenue_at_risk_usd: float
    simulated: bool = True


class Recommendation(BaseModel):
    id: str
    type: str  # MARKDOWN, RESTOCK, TRANSFER
    sku: str
    product_name: str
    store_id: str
    store_name: str
    urgency: str  # CRITICAL, HIGH, MEDIUM
    title: str
    description: str
    action_detail: str
    estimated_savings_usd: float
    waste_reduction_kg: float
    status: str
    is_simulated: bool = True
