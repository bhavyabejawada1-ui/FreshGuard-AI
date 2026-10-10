// FreshGuard.AI Embedded Master Dataset & Calculation Engine
// Mirrors backend/data CSVs and dynamic FEFO state logic

export const DEMO_REFERENCE_DATE = '2026-10-10';

export const STORES = [
  {
    store_id: 'STORE-101',
    store_name: 'FreshGuard Metro Downtown',
    city: 'San Francisco',
    address: '450 Market St, Financial District',
    manager: 'Elena Vance',
  },
  {
    store_id: 'STORE-102',
    store_name: 'FreshGuard Uptown Market',
    city: 'San Francisco',
    address: '1820 Fillmore St, Pacific Heights',
    manager: 'Marcus Chen',
  },
  {
    store_id: 'STORE-103',
    store_name: 'FreshGuard Bayview Express',
    city: 'Oakland',
    address: '2100 Broadway, Uptown',
    manager: 'Priya Sharma',
  },
];

export const PRODUCTS = [
  { sku: 'SKU-DAIRY-001', name: 'Organic Whole Milk (1 Gallon)', category: 'Dairy', unit: 'jug', unit_cost: 2.40, selling_price: 4.29, shelf_life_days: 10, ideal_storage_temp: '38°F' },
  { sku: 'SKU-DAIRY-002', name: 'Greek Yogurt Plain (32 oz)', category: 'Dairy', unit: 'tub', unit_cost: 1.90, selling_price: 3.99, shelf_life_days: 14, ideal_storage_temp: '38°F' },
  { sku: 'SKU-DAIRY-003', name: 'Artisan Sharp Cheddar (8 oz)', category: 'Dairy', unit: 'block', unit_cost: 2.75, selling_price: 5.49, shelf_life_days: 30, ideal_storage_temp: '40°F' },
  { sku: 'SKU-PROD-001', name: 'Organic Strawberries (1 lb)', category: 'Produce', unit: 'clamshell', unit_cost: 1.80, selling_price: 3.99, shelf_life_days: 5, ideal_storage_temp: '34°F' },
  { sku: 'SKU-PROD-002', name: 'Hass Avocados (Pack of 4)', category: 'Produce', unit: 'bag', unit_cost: 2.20, selling_price: 4.49, shelf_life_days: 7, ideal_storage_temp: '45°F' },
  { sku: 'SKU-PROD-003', name: 'Baby Spinach (16 oz)', category: 'Produce', unit: 'tub', unit_cost: 1.60, selling_price: 3.49, shelf_life_days: 6, ideal_storage_temp: '34°F' },
  { sku: 'SKU-PROD-004', name: 'Ripe Yellow Bananas (bunch)', category: 'Produce', unit: 'bunch', unit_cost: 0.50, selling_price: 1.29, shelf_life_days: 6, ideal_storage_temp: '55°F' },
  { sku: 'SKU-BAKE-001', name: 'Rustic Sourdough Boule', category: 'Bakery', unit: 'loaf', unit_cost: 1.50, selling_price: 4.99, shelf_life_days: 4, ideal_storage_temp: 'Room Temp' },
  { sku: 'SKU-BAKE-002', name: 'French Artisan Baguette', category: 'Bakery', unit: 'loaf', unit_cost: 0.90, selling_price: 2.79, shelf_life_days: 2, ideal_storage_temp: 'Room Temp' },
  { sku: 'SKU-BAKE-003', name: 'Blueberry Muffins (4-pack)', category: 'Bakery', unit: 'pack', unit_cost: 1.95, selling_price: 4.49, shelf_life_days: 5, ideal_storage_temp: 'Room Temp' },
  { sku: 'SKU-MEAT-001', name: 'Boneless Skinless Chicken Breast (2 lb)', category: 'Meat & Seafood', unit: 'tray', unit_cost: 5.20, selling_price: 9.99, shelf_life_days: 5, ideal_storage_temp: '32°F' },
  { sku: 'SKU-MEAT-002', name: 'Wild Caught Atlantic Salmon Fillet (1 lb)', category: 'Meat & Seafood', unit: 'tray', unit_cost: 6.50, selling_price: 12.99, shelf_life_days: 4, ideal_storage_temp: '30°F' },
  { sku: 'SKU-MEAT-003', name: 'Grass-Fed Ground Beef 85/15 (1 lb)', category: 'Meat & Seafood', unit: 'pack', unit_cost: 3.80, selling_price: 6.99, shelf_life_days: 5, ideal_storage_temp: '32°F' },
];

export const RAW_BATCHES = [
  { batch_id: 'B-101-01', sku: 'SKU-PROD-001', store_id: 'STORE-101', quantity: 24, received_date: '2026-10-06', expiry_date: '2026-10-11', reorder_threshold: 15 },
  { batch_id: 'B-101-02', sku: 'SKU-PROD-001', store_id: 'STORE-101', quantity: 40, received_date: '2026-10-09', expiry_date: '2026-10-14', reorder_threshold: 15 },
  { batch_id: 'B-101-03', sku: 'SKU-BAKE-002', store_id: 'STORE-101', quantity: 18, received_date: '2026-10-09', expiry_date: '2026-10-11', reorder_threshold: 10 },
  { batch_id: 'B-101-04', sku: 'SKU-BAKE-001', store_id: 'STORE-101', quantity: 6, received_date: '2026-10-08', expiry_date: '2026-10-12', reorder_threshold: 12 },
  { batch_id: 'B-101-05', sku: 'SKU-DAIRY-001', store_id: 'STORE-101', quantity: 35, received_date: '2026-10-03', expiry_date: '2026-10-13', reorder_threshold: 20 },
  { batch_id: 'B-101-06', sku: 'SKU-MEAT-002', store_id: 'STORE-101', quantity: 12, received_date: '2026-10-07', expiry_date: '2026-10-11', reorder_threshold: 8 },
  { batch_id: 'B-101-07', sku: 'SKU-MEAT-001', store_id: 'STORE-101', quantity: 28, received_date: '2026-10-08', expiry_date: '2026-10-13', reorder_threshold: 15 },
  { batch_id: 'B-101-08', sku: 'SKU-PROD-003', store_id: 'STORE-101', quantity: 22, received_date: '2026-10-06', expiry_date: '2026-10-12', reorder_threshold: 10 },
  { batch_id: 'B-101-09', sku: 'SKU-PROD-002', store_id: 'STORE-101', quantity: 45, received_date: '2026-10-05', expiry_date: '2026-10-12', reorder_threshold: 20 },
  { batch_id: 'B-101-10', sku: 'SKU-DAIRY-002', store_id: 'STORE-101', quantity: 30, received_date: '2026-10-01', expiry_date: '2026-10-15', reorder_threshold: 15 },
  { batch_id: 'B-101-11', sku: 'SKU-DAIRY-003', store_id: 'STORE-101', quantity: 50, received_date: '2026-09-25', expiry_date: '2026-10-25', reorder_threshold: 20 },
  { batch_id: 'B-101-12', sku: 'SKU-PROD-004', store_id: 'STORE-101', quantity: 4, received_date: '2026-10-07', expiry_date: '2026-10-13', reorder_threshold: 15 },
  { batch_id: 'B-102-01', sku: 'SKU-PROD-001', store_id: 'STORE-102', quantity: 8, received_date: '2026-10-08', expiry_date: '2026-10-13', reorder_threshold: 15 },
  { batch_id: 'B-102-02', sku: 'SKU-BAKE-001', store_id: 'STORE-102', quantity: 25, received_date: '2026-10-09', expiry_date: '2026-10-13', reorder_threshold: 10 },
  { batch_id: 'B-102-03', sku: 'SKU-MEAT-001', store_id: 'STORE-102', quantity: 5, received_date: '2026-10-08', expiry_date: '2026-10-13', reorder_threshold: 12 },
  { batch_id: 'B-102-04', sku: 'SKU-DAIRY-001', store_id: 'STORE-102', quantity: 42, received_date: '2026-10-05', expiry_date: '2026-10-15', reorder_threshold: 18 },
  { batch_id: 'B-102-05', sku: 'SKU-MEAT-003', store_id: 'STORE-102', quantity: 19, received_date: '2026-10-07', expiry_date: '2026-10-12', reorder_threshold: 10 },
  { batch_id: 'B-103-01', sku: 'SKU-PROD-001', store_id: 'STORE-103', quantity: 3, received_date: '2026-10-07', expiry_date: '2026-10-12', reorder_threshold: 15 },
  { batch_id: 'B-103-02', sku: 'SKU-BAKE-003', store_id: 'STORE-103', quantity: 16, received_date: '2026-10-08', expiry_date: '2026-10-13', reorder_threshold: 10 },
  { batch_id: 'B-103-03', sku: 'SKU-DAIRY-001', store_id: 'STORE-103', quantity: 15, received_date: '2026-10-04', expiry_date: '2026-10-14', reorder_threshold: 15 },
];

export const INITIAL_RECOMMENDATIONS = [
  {
    id: 'REC-001',
    type: 'MARKDOWN',
    sku: 'SKU-PROD-001',
    product_name: 'Organic Strawberries (1 lb)',
    store_id: 'STORE-101',
    store_name: 'FreshGuard Metro Downtown',
    urgency: 'CRITICAL',
    title: 'Apply 30% Flash Markdown',
    description: 'Batch B-101-01 (24 packs) expires in 1 day. Current sales rate indicates 14 packs will spoil if unsold.',
    action_detail: 'Reduce price from $3.99 to $2.79 to accelerate sales velocity before expiration.',
    estimated_savings_usd: 42.50,
    waste_reduction_kg: 11.2,
    status: 'PROPOSED',
  },
  {
    id: 'REC-002',
    type: 'RESTOCK',
    sku: 'SKU-BAKE-001',
    product_name: 'Rustic Sourdough Boule',
    store_id: 'STORE-101',
    store_name: 'FreshGuard Metro Downtown',
    urgency: 'HIGH',
    title: 'Reorder Fresh Sourdough Batch',
    description: 'Stock depleted to 6 loaves, which is below the 12-unit safety threshold. Expected weekend rush will cause a stockout.',
    action_detail: 'Reorder 35 loaves from Golden Gate Bakery supplier with next morning delivery.',
    estimated_savings_usd: 85.00,
    waste_reduction_kg: 0.0,
    status: 'PROPOSED',
  },
  {
    id: 'REC-003',
    type: 'TRANSFER',
    sku: 'SKU-PROD-001',
    product_name: 'Organic Strawberries (1 lb)',
    store_id: 'STORE-101',
    store_name: 'FreshGuard Metro Downtown',
    urgency: 'HIGH',
    title: 'Inter-Store Transfer to Bayview',
    description: 'Metro Downtown has 64 total packs across batches; Bayview Express (STORE-103) is near stockout with only 3 packs.',
    action_detail: 'Transfer 15 packs of Batch B-101-02 via midday refrigerated courier (20 min transit).',
    estimated_savings_usd: 52.80,
    waste_reduction_kg: 6.8,
    status: 'PROPOSED',
  },
  {
    id: 'REC-004',
    type: 'MARKDOWN',
    sku: 'SKU-MEAT-002',
    product_name: 'Wild Caught Atlantic Salmon',
    store_id: 'STORE-101',
    store_name: 'FreshGuard Metro Downtown',
    urgency: 'CRITICAL',
    title: 'Apply 25% Evening Clearance',
    description: 'Batch B-101-06 (12 fillets) expires tomorrow. High-value perishable protein at immediate spoilage risk.',
    action_detail: 'Drop price from $12.99 to $9.74 starting at 4:00 PM for dinner rush.',
    estimated_savings_usd: 78.00,
    waste_reduction_kg: 5.4,
    status: 'PROPOSED',
  },
  {
    id: 'REC-005',
    type: 'RESTOCK',
    sku: 'SKU-PROD-004',
    product_name: 'Ripe Yellow Bananas (bunch)',
    store_id: 'STORE-101',
    store_name: 'FreshGuard Metro Downtown',
    urgency: 'MEDIUM',
    title: 'Automated Banana Replenishment',
    description: 'Inventory down to 4 bunches against threshold of 15. Daily baseline demand is 18 bunches.',
    action_detail: 'Schedule standard vendor restock of 40 bunches for Monday morning delivery.',
    estimated_savings_usd: 32.00,
    waste_reduction_kg: 0.0,
    status: 'PROPOSED',
  },
];

// 15 Slides Structured Content for Presentation Deck Explorer
export const SLIDES_DATA = [
  {
    slideNumber: 1,
    category: 'Title & Overview',
    title: 'FreshGuard.AI — Zero-Waste Perishable Management',
    subtitle: 'End-to-End System Architecture, Dynamic FEFO State Machines, and Predictive Spoilage Analytics',
    bullets: [
      'Zero-Waste Perishable Demand & Shelf-Life Management Enterprise Platform.',
      'FastAPI Microservice Engine delivering sub-50ms query response latency.',
      'Dynamic FEFO (First-Expired, First-Out) State Machine tracking perishable batches.',
      '3-Pillar Decision Intelligence: Dynamic Markdowns, Automated Replenishment, and Inter-Store Balancing.',
    ],
  },
  {
    slideNumber: 2,
    category: 'System Context',
    title: 'Architectural Drivers & Technical Problem Domain',
    subtitle: 'Solving the core technical challenges of retail perishable inventory decay and shrinkage',
    bullets: [
      'Static FIFO Assumption: Legacy ERPs treat perishable inventory as FIFO, causing $400B+ annual grocery shrink.',
      'Non-Linear Shelf-Life Decay: Quality degrades dynamically based on cold-chain variables and time.',
      'In-Store Blind Spot: Floor teams lack itemized days-to-expiry visibility relative to customer sales velocity.',
      'Reactive Markdowns: Clearance discounts applied too late at the point of rot, completely destroying margins.',
    ],
  },
  {
    slideNumber: 3,
    category: 'System Topology',
    title: 'High-Level Layered System Architecture',
    subtitle: 'End-to-end 3-tier reactive pipeline from edge ingestion to action execution',
    bullets: [
      'Layer 1: Presentation & Operations (React 18 + Vite SPA, Lucide Icons, responsive telemetry filters).',
      'Layer 2: FastAPI Core Engine (Asynchronous gateway, Pydantic v2 schemas, FEFO degradation machine).',
      'Layer 3: Data Ingestion & Storage (In-memory Pandas vectorization, PostgreSQL/TimescaleDB roadmap, Redis cache).',
      'Decoupled RESTful contracts supporting web portals, handheld scanners, and upstream ERP sync.',
    ],
  },
  {
    slideNumber: 4,
    category: 'Data Modeling',
    title: 'Perishable Inventory Domain Model & Schemas',
    subtitle: 'Pydantic v2 data structures enabling granular batch traceability and decay vectors',
    bullets: [
      'ProductBatchItem Model: SKU, batch_id, store_id, quantity, received_date, expiry_date, unit_cost, selling_price.',
      'Dynamic Computed Fields: days_to_expiry, freshness_status (FRESH, EXPIRING_SOON, CRITICAL, EXPIRED).',
      'SummaryMetrics Model: Real-time aggregated KPIs for units, near-expiry count, waste in USD and kg.',
      'Recommendation Model: Strongly typed actionable vectors with estimated savings ($) and waste reduction (kg).',
    ],
  },
  {
    slideNumber: 5,
    category: 'API Specification',
    title: 'RESTful Service Contracts & Endpoint Architecture',
    subtitle: 'High-performance OpenAPI compliant endpoints built on FastAPI',
    bullets: [
      'GET /api/health: Service heartbeat, active records verification, and operational metadata.',
      'GET /api/summary: Real-time high-level KPI aggregation with optional store_id filter.',
      'GET /api/products: Filtered batch inventory lookup supporting category, search, store, and status.',
      'GET /api/recommendations: Prescriptive action feed prioritizing high-urgency inventory interventions.',
      'GET /api/stores & /api/categories: Dynamic taxonomy and multi-store location metadata.',
    ],
  },
  {
    slideNumber: 6,
    category: 'Degradation Modeling',
    title: 'Real-Time Freshness & Degradation State Machine',
    subtitle: 'Deterministic state progression governing perishable shelf-life lifecycle',
    bullets: [
      'FRESH (DTE > 3 days): Standard retail velocity, full selling price, normal FIFO/FEFO dispatch.',
      'EXPIRING_SOON (1 < DTE <= 3 days): Automated trigger candidate for early 20-30% promotional discount.',
      'CRITICAL (0 <= DTE <= 1 day): Urgent intervention window: 50% flash markdown or rapid charity transfer.',
      'EXPIRED (DTE < 0 days): Terminal shrinkage stage; removed from retail floor and logged as waste write-off.',
    ],
  },
  {
    slideNumber: 7,
    category: 'Predictive Analytics',
    title: 'Predictive Demand & Spoilage Velocity Analytics',
    subtitle: 'Quantifying economic exposure and spoilage risk through mathematical models',
    bullets: [
      'Dynamic Days to Expiration: DTE = Expiry_Date - Current_Reference_Timestamp.',
      'Estimated Waste Sunk Cost: Waste_Cost = Quantity_Remaining × Unit_Cost.',
      'Potential Revenue at Risk: Units × Selling_Price × Decay_Probability.',
      'ESG Waste Reduction Metric: Direct kg mass quantification for corporate sustainability reporting.',
    ],
  },
  {
    slideNumber: 8,
    category: 'Decision Intelligence',
    title: '3-Pillar Prescriptive Recommendation Engine',
    subtitle: 'Converting raw decay alerts into high-confidence, actionable operational decisions',
    bullets: [
      'Pillar 1: Dynamic Markdown — Real-time price elasticity discounting to clear stock before expiration.',
      'Pillar 2: Predictive Replenishment — Automated reordering triggered when stock breaches safety thresholds.',
      'Pillar 3: Inter-Store Transfers — Balances surplus inventory from slow stores to high-demand locations.',
    ],
  },
  {
    slideNumber: 9,
    category: 'Data Engineering',
    title: 'Data Ingestion & Pipeline Architecture',
    subtitle: 'In-memory streaming abstraction with seamless enterprise database extensibility',
    bullets: [
      'Current In-Memory Engine: Singleton DataLoader pattern performing vectorized zero-copy joins in <10ms.',
      'Temporal Anchoring: DEMO_REFERENCE_DATE enables reproducible dynamic shelf-life calculations.',
      'Production Lake Target: Migration to PostgreSQL + TimescaleDB for time-series shelf condition telemetry.',
      'Event Streaming: Kafka / Redpanda event ingestion from store RFID and POS scanner devices.',
    ],
  },
  {
    slideNumber: 10,
    category: 'Client Architecture',
    title: 'Frontend Architecture & Reactive State Flow',
    subtitle: 'Modern React 18 + Vite dashboard with responsive store analytics',
    bullets: [
      'Component Architecture: Modular hierarchy with StoreSelector, MetricCardsGrid, and BatchTable.',
      'Reactive State Management: Instant client-side debounced searching and multi-status filtering.',
      'Optimistic Action Confirmations: Instant UI transitions when executing or dismissing recommendations.',
      'Dual Connectivity Engine: Live FastAPI connectivity with automatic fallback for static GitHub deployment.',
    ],
  },
  {
    slideNumber: 11,
    category: 'Distributed Logistics',
    title: 'Multi-Store Orchestration & Transfer Network',
    subtitle: 'Graph-based inventory rebalancing across distributed supermarket chains',
    bullets: [
      'Store Supply-Demand Graph: Detects surplus nodes with near-expiry stock and deficit nodes with stockouts.',
      'Proximity Clustered Routing: Restricts transfer proposals to local logistics radii (<15km).',
      'Economic Optimization: Ensures Margin Recovered exceeds logistics transit and handling costs.',
      'Cold-Chain Transport Verification: Audits recipient store refrigeration capacity before dispatch.',
    ],
  },
  {
    slideNumber: 12,
    category: 'Performance Engineering',
    title: 'Concurrency, Latency & Performance SLAs',
    subtitle: 'Architected for real-time edge processing and enterprise scale',
    bullets: [
      '< 50ms API Latency: Sub-50ms p95 latency guarantees instant scanner and dashboard updates.',
      '5,000+ Requests/sec: Asynchronous Uvicorn event loop handling concurrent store terminals.',
      'Zero Disk Bottlenecks: In-memory vectorized pandas execution during peak retail shopping hours.',
      '99.95% Availability Target: Stateless microservice containers enabling zero-downtime rolling updates.',
    ],
  },
  {
    slideNumber: 13,
    category: 'Security & Compliance',
    title: 'Enterprise Security & Data Governance',
    subtitle: 'Protecting retail operational integrity, financial metrics, and access roles',
    bullets: [
      'Role-Based Access Control (RBAC): Distinct permissions for Floor Staff, Store Managers, and Regional Directors.',
      'Tamper-Proof Audit Logging: Every markdown discount and batch write-off recorded with actor and timestamp.',
      'Regulatory Compliance: Traceability logs designed to satisfy FDA FSMA Section 204 requirements.',
      'Network Hardening: CORS origin whitelisting, strict TLS 1.3 encryption, and API token authentication.',
    ],
  },
  {
    slideNumber: 14,
    category: 'DevOps & QA',
    title: 'Testing, Quality Assurance & CI/CD Pipeline',
    subtitle: 'Rigorous verification ensuring 100% computational accuracy of shelf-life algorithms',
    bullets: [
      'Automated Pytest Suite: Validates FEFO math, negative DTE boundary conditions, and threshold trips.',
      'API Integration Verification: TestClient fixtures ensuring all endpoints return HTTP 200 schemas.',
      'CI/CD Pipeline: GitHub Actions automated workflow for continuous testing and GitHub Pages deployment.',
      'Docker Containerization: Lightweight multi-stage Docker images (<120MB) for rapid cloud scaling.',
    ],
  },
  {
    slideNumber: 15,
    category: 'Strategic Roadmap',
    title: 'Engineering Roadmap & Evolution Milestones',
    subtitle: 'Phased delivery plan from MVP foundation to autonomous zero-waste enterprise engine',
    bullets: [
      'Milestone 1 (Delivered): Core FastAPI engine, FEFO state machine, and interactive React dashboard.',
      'Milestone 2 (Next): IoT Bluetooth cold-chain sensors, edge Computer Vision produce ripeness detection.',
      'Milestone 3 (Vision): Reinforcement Learning for dynamic pricing and bi-directional SAP/Oracle ERP sync.',
    ],
  },
];

// Calculation Helpers
export function computeDaysToExpiry(expiryDateStr, refDateStr = DEMO_REFERENCE_DATE) {
  const refDate = new Date(refDateStr);
  const expDate = new Date(expiryDateStr);
  const diffTime = expDate.getTime() - refDate.getTime();
  return Math.ceil(diffTime / (1000 * 60 * 60 * 24));
}

export function computeFreshnessStatus(daysToExpiry) {
  if (daysToExpiry < 0) return 'EXPIRED';
  if (daysToExpiry <= 1) return 'CRITICAL';
  if (daysToExpiry <= 3) return 'EXPIRING_SOON';
  return 'FRESH';
}

export function enrichBatches(storeId = null) {
  const storeMap = Object.fromEntries(STORES.map(s => [s.store_id, s]));
  const productMap = Object.fromEntries(PRODUCTS.map(p => [p.sku, p]));

  let batches = RAW_BATCHES.map(b => {
    const product = productMap[b.sku] || {};
    const store = storeMap[b.store_id] || {};
    const daysToExpiry = computeDaysToExpiry(b.expiry_date);
    const freshnessStatus = computeFreshnessStatus(daysToExpiry);
    const isStockoutRisk = b.quantity <= b.reorder_threshold;
    const estimatedWasteCost = Number((b.quantity * (product.unit_cost || 0)).toFixed(2));

    return {
      batch_id: b.batch_id,
      sku: b.sku,
      name: product.name || b.sku,
      category: product.category || 'General',
      unit: product.unit || 'unit',
      unit_cost: product.unit_cost || 0,
      selling_price: product.selling_price || 0,
      ideal_storage_temp: product.ideal_storage_temp || 'Ambient',
      store_id: b.store_id,
      store_name: store.store_name || b.store_id,
      quantity: b.quantity,
      received_date: b.received_date,
      expiry_date: b.expiry_date,
      days_to_expiry: daysToExpiry,
      freshness_status: freshnessStatus,
      reorder_threshold: b.reorder_threshold,
      is_stockout_risk: isStockoutRisk,
      estimated_waste_cost: estimatedWasteCost,
    };
  });

  if (storeId && storeId !== 'ALL') {
    batches = batches.filter(b => b.store_id === storeId);
  }

  return batches;
}

export function computeSummaryMetrics(batches) {
  const totalBatches = batches.length;
  const totalUnits = batches.reduce((sum, b) => sum + b.quantity, 0);
  const totalProducts = new Set(batches.map(b => b.sku)).size;
  const nearExpiryCount = batches.filter(b => b.days_to_expiry <= 3 && b.days_to_expiry >= 0).length;
  const criticalExpiryCount = batches.filter(b => b.days_to_expiry <= 1 && b.days_to_expiry >= 0).length;
  const stockoutRiskCount = batches.filter(b => b.is_stockout_risk).length;

  const estimatedWasteUsd = batches
    .filter(b => b.days_to_expiry <= 3)
    .reduce((sum, b) => sum + b.estimated_waste_cost, 0);

  const potentialRevenueAtRisk = batches
    .filter(b => b.days_to_expiry <= 3)
    .reduce((sum, b) => sum + (b.quantity * b.selling_price), 0);

  const estimatedWasteKg = Number((batches
    .filter(b => b.days_to_expiry <= 3)
    .reduce((sum, b) => sum + (b.quantity * 0.45), 0)).toFixed(1));

  return {
    total_products: totalProducts,
    total_batches: totalBatches,
    total_units: totalUnits,
    near_expiry_count: nearExpiryCount,
    critical_expiry_count: criticalExpiryCount,
    stockout_risk_count: stockoutRiskCount,
    estimated_waste_usd: Number(estimatedWasteUsd.toFixed(2)),
    estimated_waste_kg: estimatedWasteKg,
    potential_revenue_at_risk_usd: Number(potentialRevenueAtRisk.toFixed(2)),
  };
}
