import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    """Verify that the health check endpoint returns 200 OK and valid status."""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["total_products_loaded"] > 0
    assert data["total_batches_loaded"] > 0


def test_summary_metrics():
    """Verify that the summary metrics endpoint returns non-negative KPIs."""
    response = client.get("/api/summary")
    assert response.status_code == 200
    data = response.json()
    assert data["total_products"] > 0
    assert data["total_batches"] > 0
    assert data["total_units"] > 0
    assert data["near_expiry_count"] >= 0
    assert data["stockout_risk_count"] >= 0
    assert data["estimated_waste_usd"] >= 0.0
    assert data["simulated"] is True


def test_products_list():
    """Verify that the products list endpoint returns items with freshness classifications."""
    response = client.get("/api/products")
    assert response.status_code == 200
    products = response.json()
    assert isinstance(products, list)
    assert len(products) > 0

    first_item = products[0]
    assert "batch_id" in first_item
    assert "sku" in first_item
    assert "name" in first_item
    assert "category" in first_item
    assert "freshness_status" in first_item
    assert first_item["freshness_status"] in ["FRESH", "EXPIRING_SOON", "CRITICAL", "EXPIRED"]


def test_category_filter():
    """Verify that filtering by category works as expected."""
    response = client.get("/api/products?category=Produce")
    assert response.status_code == 200
    products = response.json()
    assert len(products) > 0
    for item in products:
        assert item["category"].lower() == "produce"


def test_search_filter():
    """Verify that search query filters by product name or SKU."""
    response = client.get("/api/products?search=Milk")
    assert response.status_code == 200
    products = response.json()
    assert len(products) > 0
    for item in products:
        assert "milk" in item["name"].lower() or "milk" in item["sku"].lower()


def test_recommendations():
    """Verify that sample recommendations are returned with valid structures."""
    response = client.get("/api/recommendations")
    assert response.status_code == 200
    recs = response.json()
    assert isinstance(recs, list)
    assert len(recs) > 0

    rec_types = {r["type"] for r in recs}
    assert "MARKDOWN" in rec_types
    assert "RESTOCK" in rec_types
    assert "TRANSFER" in rec_types
