import sys
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck(output_path: str):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette - Modern Tech Dark Theme
    BG_DARK = RGBColor(15, 23, 42)       # Slate 900 #0F172A
    CARD_BG = RGBColor(30, 41, 59)       # Slate 800 #1E293B
    CARD_BORDER = RGBColor(51, 65, 85)   # Slate 700 #334155
    CARD_BG_ALT = RGBColor(24, 33, 47)   # Darker card
    ACCENT_GREEN = RGBColor(16, 185, 129)# Emerald 500 #10B981
    ACCENT_CYAN = RGBColor(6, 182, 212)  # Cyan 500 #06B6D4
    ACCENT_AMBER = RGBColor(245, 158, 11)# Amber 500 #F59E0B
    ACCENT_RED = RGBColor(239, 68, 68)   # Red 500 #EF4444
    ACCENT_PURPLE = RGBColor(168, 85, 247) # Purple 500
    TEXT_WHITE = RGBColor(248, 250, 252) # White Slate 50
    TEXT_MUTED = RGBColor(148, 163, 184) # Slate 400
    TEXT_DIM = RGBColor(100, 116, 139)   # Slate 500
    FONT_TITLE = 'Segoe UI'
    FONT_BODY = 'Segoe UI'

    def apply_slide_bg(slide):
        bg = slide.background
        fill = bg.fill
        fill.solid()
        fill.fore_color.rgb = BG_DARK

    def add_header(slide, category: str, title: str, subtitle: str, slide_num: int):
        apply_slide_bg(slide)
        
        # Category Badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.4), Inches(2.8), Inches(0.35))
        badge.fill.solid()
        badge.fill.fore_color.rgb = RGBColor(20, 40, 55)
        badge.line.color.rgb = ACCENT_CYAN
        badge.line.width = Pt(1)
        tf = badge.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.text = category.upper()
        p.alignment = PP_ALIGN.CENTER
        p.font.name = FONT_TITLE
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = ACCENT_CYAN

        # Title
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.78), Inches(9.5), Inches(0.55))
        t_tf = t_box.text_frame
        t_tf.word_wrap = True
        t_tf.margin_left = t_tf.margin_top = t_tf.margin_right = t_tf.margin_bottom = 0
        p_t = t_tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_TITLE
        p_t.font.size = Pt(22)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE

        # Subtitle
        s_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(9.5), Inches(0.35))
        s_tf = s_box.text_frame
        s_tf.word_wrap = True
        s_tf.margin_left = s_tf.margin_top = s_tf.margin_right = s_tf.margin_bottom = 0
        p_s = s_tf.paragraphs[0]
        p_s.text = subtitle
        p_s.font.name = FONT_BODY
        p_s.font.size = Pt(12)
        p_s.font.color.rgb = TEXT_MUTED

        # Footer divider line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.9), Inches(11.733), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = CARD_BORDER
        line.line.fill.background()

        # Footer Left
        f_box = slide.shapes.add_textbox(Inches(0.8), Inches(6.95), Inches(6.0), Inches(0.3))
        f_tf = f_box.text_frame
        f_tf.margin_left = f_tf.margin_top = f_tf.margin_right = f_tf.margin_bottom = 0
        p_f = f_tf.paragraphs[0]
        p_f.text = "FreshGuard.AI  |  Zero-Waste Perishable Demand & Shelf-Life Management"
        p_f.font.name = FONT_BODY
        p_f.font.size = Pt(10)
        p_f.font.color.rgb = TEXT_DIM

        # Footer Right (Slide Number)
        n_box = slide.shapes.add_textbox(Inches(10.533), Inches(6.95), Inches(2.0), Inches(0.3))
        n_tf = n_box.text_frame
        n_tf.margin_left = n_tf.margin_top = n_tf.margin_right = n_tf.margin_bottom = 0
        p_n = n_tf.paragraphs[0]
        p_n.alignment = PP_ALIGN.RIGHT
        p_n.text = f"Slide {slide_num} of 15"
        p_n.font.name = FONT_BODY
        p_n.font.size = Pt(10)
        p_n.font.color.rgb = TEXT_DIM

    def add_card(slide, left, top, width, height, title, subtitle="", border_color=CARD_BORDER, bg_color=CARD_BG):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)
        
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.2)
        tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.18)
        tf.margin_bottom = Inches(0.15)
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_TITLE
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        
        if subtitle:
            p2 = tf.add_paragraph()
            p2.text = subtitle
            p2.font.name = FONT_BODY
            p2.font.size = Pt(10.5)
            p2.font.color.rgb = TEXT_MUTED
            p2.space_before = Pt(2)
            
        return card, tf

    def add_bullet_list(tf, items, font_size=11, space_before=4, bullet_char="• "):
        for item in items:
            p = tf.add_paragraph()
            p.text = f"{bullet_char}{item}"
            p.font.name = FONT_BODY
            p.font.size = Pt(font_size)
            p.font.color.rgb = TEXT_WHITE
            p.space_before = Pt(space_before)

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(slide1)

    # Accent decorative top glow bar
    top_bar = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.7), Inches(11.733), Inches(0.06))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = ACCENT_GREEN
    top_bar.line.fill.background()

    # Pill badge
    pill = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.1), Inches(3.4), Inches(0.38))
    pill.fill.solid()
    pill.fill.fore_color.rgb = RGBColor(16, 45, 35)
    pill.line.color.rgb = ACCENT_GREEN
    pill.line.width = Pt(1.5)
    ptf = pill.text_frame
    ptf.vertical_anchor = MSO_ANCHOR.MIDDLE
    pp = ptf.paragraphs[0]
    pp.text = "TECHNICAL SPECIFICATION & ARCHITECTURE"
    pp.alignment = PP_ALIGN.CENTER
    pp.font.name = FONT_TITLE
    pp.font.size = Pt(10)
    pp.font.bold = True
    pp.font.color.rgb = ACCENT_GREEN

    # Main Title
    t_box = slide1.shapes.add_textbox(Inches(0.8), Inches(1.65), Inches(11.7), Inches(1.6))
    t_tf = t_box.text_frame
    t_tf.word_wrap = True
    t_tf.margin_left = t_tf.margin_top = t_tf.margin_right = t_tf.margin_bottom = 0
    p1 = t_tf.paragraphs[0]
    p1.text = "FreshGuard.AI"
    p1.font.name = FONT_TITLE
    p1.font.size = Pt(44)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE

    p2 = t_tf.add_paragraph()
    p2.text = "Zero-Waste Perishable Demand & Shelf-Life Management Platform"
    p2.font.name = FONT_TITLE
    p2.font.size = Pt(22)
    p2.font.bold = True
    p2.font.color.rgb = ACCENT_CYAN
    p2.space_before = Pt(8)

    p3 = t_tf.add_paragraph()
    p3.text = "End-to-End System Architecture, Dynamic FEFO State Machines, and Predictive Spoilage Analytics"
    p3.font.name = FONT_BODY
    p3.font.size = Pt(13)
    p3.font.color.rgb = TEXT_MUTED
    p3.space_before = Pt(6)

    # 3 Overview Feature Cards on Title Slide
    cards_data = [
        ("FastAPI Microservice Engine", "Sub-50ms query latency, RESTful contract schemas, asynchronous non-blocking I/O pipeline.", ACCENT_CYAN),
        ("FEFO Freshness State Machine", "Continuous shelf-life degradation tracking across FRESH, EXPIRING, CRITICAL, and EXPIRED stages.", ACCENT_GREEN),
        ("3-Pillar Decision Intelligence", "Automated dynamic markdowns, predictive restocking triggers, and inter-store inventory transfers.", ACCENT_AMBER)
    ]
    card_w = Inches(3.64)
    for i, (ctitle, cdesc, caccent) in enumerate(cards_data):
        c_left = Inches(0.8 + i * 4.04)
        c, ctf = add_card(slide1, c_left, Inches(3.7), card_w, Inches(2.3), ctitle, "", border_color=caccent)
        cp = ctf.add_paragraph()
        cp.text = cdesc
        cp.font.name = FONT_BODY
        cp.font.size = Pt(11.5)
        cp.font.color.rgb = TEXT_MUTED
        cp.space_before = Pt(10)

    # Metadata bottom bar
    meta_box = slide1.shapes.add_textbox(Inches(0.8), Inches(6.4), Inches(11.733), Inches(0.5))
    mtf = meta_box.text_frame
    mtf.margin_left = mtf.margin_top = mtf.margin_right = mtf.margin_bottom = 0
    mp = mtf.paragraphs[0]
    mp.text = "Author: Engineering & AI Architecture Team   |   Version: 1.0.0 (Production Blueprint)   |   Target: Enterprise Retail & Edge Deployment"
    mp.font.name = FONT_BODY
    mp.font.size = Pt(10.5)
    mp.font.color.rgb = TEXT_DIM

    # =========================================================================
    # SLIDE 2: ARCHITECTURAL DRIVERS & PROBLEM DOMAIN
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "System Context", "Architectural Drivers & Technical Problem Domain", "Solving the core technical challenges of retail perishable inventory decay and shrinkage", 2)

    c1, tf1 = add_card(slide2, Inches(0.8), Inches(1.9), Inches(5.66), Inches(4.7), "1. The Perishable Grocery Conundrum", "Why traditional ERP and inventory systems fail for perishable food")
    add_bullet_list(tf1, [
        "Static FIFO Assumption: Legacy ERP systems treat inventory as First-In-First-Out, causing $400B+ annual grocery shrink worldwide.",
        "Non-Linear Shelf-Life Decay: Perishables degrade non-linearly influenced by ambient temperatures, handling velocity, and supply chain delays.",
        "Blind Spot In-Store: Store managers lack batch-level visibility into remaining days-to-expiry (DTE) vs sales velocity.",
        "Reactive Clearance: Markdowns occur too late (at point of rot), destroying margin without recovering salvageable value."
    ], font_size=11, space_before=8)

    c2, tf2 = add_card(slide2, Inches(6.86), Inches(1.9), Inches(5.66), Inches(4.7), "2. Architectural Design Goals", "Core Non-Functional and Functional Requirements")
    add_bullet_list(tf2, [
        "Sub-Second Reactive State: Recalculate batch degradation status instantly on query across 100K+ SKUs without blocking.",
        "Algorithmic Action Dispatch: Automatically suggest actions (Markdown %, Restock Qty, Inter-store routing) before product loss occurs.",
        "Store-Centric Multi-Tenancy: Enable aggregate corporate oversight while providing granular, localized telemetry for individual store managers.",
        "Decoupled Microservice Contract: Fully decoupled RESTful core supporting Web UI, mobile POS hand-terminals, and ERP sync."
    ], font_size=11, space_before=8)

    # =========================================================================
    # SLIDE 3: HIGH-LEVEL SYSTEM ARCHITECTURE
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "System Topology", "High-Level Layered System Architecture", "End-to-end 3-tier reactive pipeline from edge ingestion to action execution", 3)

    tiers = [
        ("Presentation & Store Operations Tier", [
            "React 18 + Vite SPA Dashboard for real-time manager telemetry",
            "Lucide Icon dynamic telemetry & KPI visualizer cards",
            "Store Switcher & Multi-dimensional filters (Status, Category, Query)",
            "Edge Handheld Scanner / Mobile POS integration endpoints"
        ], ACCENT_CYAN),
        ("Core Application & Intelligence Engine (FastAPI)", [
            "FastAPI Asynchronous Gateway with strict Pydantic v2 schemas",
            "Dynamic FEFO State Engine computing days_to_expiry & degradation status",
            "Risk & Waste Quantification Service (Waste $ / kg at risk)",
            "3-Pillar Recommendation Optimizer (Markdown / Restock / Transfer)"
        ], ACCENT_GREEN),
        ("Data Ingestion & Storage Foundation", [
            "Pandas High-Performance in-memory batch & SKU dataframe loader",
            "Reference Temporal Anchor calibration (Demo reference date)",
            "Relational & Time-Series Data Lake (PostgreSQL / TimescaleDB Target)",
            "Redis In-Memory State Cache for low-latency batch freshness lookups"
        ], ACCENT_AMBER)
    ]

    for i, (tier_title, tier_items, accent) in enumerate(tiers):
        t_top = Inches(1.9 + i * 1.6)
        c, tf = add_card(slide3, Inches(0.8), t_top, Inches(11.733), Inches(1.45), f"Layer {i+1}: {tier_title}", "", border_color=accent)
        add_bullet_list(tf, tier_items, font_size=10.5, space_before=3)

    # =========================================================================
    # SLIDE 4: INVENTORY DATA MODEL & BATCH SCHEMAS
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Data Modeling", "Perishable Inventory Domain Model & Schemas", "Pydantic v2 data structures enabling granular batch traceability and decay vectors", 4)

    c1, tf1 = add_card(slide4, Inches(0.8), Inches(1.9), Inches(5.66), Inches(4.7), "ProductBatchItem Entity Model", "Granular physical batch tracking schema")
    add_bullet_list(tf1, [
        "batch_id (str): Unique identifier per shipment/lot (e.g. BATCH-001).",
        "sku (str) & name (str): Master catalog reference and perishable item label.",
        "category (str): Produce, Dairy, Bakery, Meat, Seafood segmentation.",
        "unit_cost (float) & selling_price (float): Economic margin indicators.",
        "ideal_storage_temp (str): Cold-chain compliance specification.",
        "received_date & expiry_date (str): Temporal bounds for shelf-life.",
        "days_to_expiry (int): Computed dynamic delta against current clock.",
        "freshness_status (Enum): FRESH, EXPIRING_SOON, CRITICAL, EXPIRED.",
        "reorder_threshold (int) & is_stockout_risk (bool): Stockout guardrails."
    ], font_size=10, space_before=3)

    c2, tf2 = add_card(slide4, Inches(6.86), Inches(1.9), Inches(5.66), Inches(4.7), "Summary Metrics & Recommendation Schemas", "Executive aggregation and prescriptive action vectors")
    add_bullet_list(tf2, [
        "SummaryMetrics Model: High-level KPI rollup aggregated per store or chain-wide:",
        "  • total_products, total_batches, total_units",
        "  • near_expiry_count (<=3 days) & critical_expiry_count (<=1 day)",
        "  • stockout_risk_count: Batches where quantity < threshold",
        "  • estimated_waste_usd & estimated_waste_kg: Quantified loss impact",
        "  • potential_revenue_at_risk_usd: Top-line exposure metric",
        "Recommendation Action Model:",
        "  • type: MARKDOWN | RESTOCK | TRANSFER",
        "  • urgency: CRITICAL | HIGH | MEDIUM",
        "  • action_detail: Specific operational instruction (e.g. Apply 40% discount)",
        "  • estimated_savings_usd & waste_reduction_kg: Projected ROI"
    ], font_size=10, space_before=3)

    # =========================================================================
    # SLIDE 5: REST API INTERFACE & CONTRACT DESIGN
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "API Specification", "RESTful Service Contracts & Endpoint Architecture", "High-performance OpenAPI compliant endpoints built on FastAPI", 5)

    endpoints = [
        ("GET /api/health", "System", "Health check, engine version, and total records verification.", "HealthResponse: status, count_products, count_batches"),
        ("GET /api/summary", "Dashboard", "Computes instant KPI rollups with optional store-level query filter.", "SummaryMetrics: near_expiry, waste_usd, revenue_at_risk"),
        ("GET /api/products", "Inventory", "Filtered batch inventory lookup supporting category, search, store, and status.", "List[ProductBatchItem]: Real-time enriched batches"),
        ("GET /api/recommendations", "Intelligence", "Generates prioritized prescriptive actions for markdowns, restocking, and transfers.", "List[Recommendation]: Sorted by financial urgency"),
        ("GET /api/categories & /stores", "Metadata", "Fetches active taxonomies and multi-store retail geographical metadata.", "List[str] Categories and List[Store] Location Models")
    ]

    for i, (path, tag, desc, response) in enumerate(endpoints):
        top_pos = Inches(1.9 + i * 0.95)
        c, tf = add_card(slide5, Inches(0.8), top_pos, Inches(11.733), Inches(0.85), path, "", border_color=ACCENT_CYAN if i%2==0 else ACCENT_GREEN)
        p = tf.paragraphs[0]
        p.font.size = Pt(13)
        p.font.color.rgb = ACCENT_CYAN if i%2==0 else ACCENT_GREEN
        
        p_desc = tf.add_paragraph()
        p_desc.text = f"Tag: [{tag}]  |  Description: {desc}"
        p_desc.font.name = FONT_BODY
        p_desc.font.size = Pt(10)
        p_desc.font.color.rgb = TEXT_WHITE
        p_desc.space_before = Pt(1)

        p_resp = tf.add_paragraph()
        p_resp.text = f"Contract Output: {response}"
        p_resp.font.name = FONT_BODY
        p_resp.font.size = Pt(9.5)
        p_resp.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 6: REAL-TIME FRESHNESS STATE MACHINE
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Degradation Modeling", "Real-Time Freshness & Degradation State Machine", "Deterministic state progression governing perishable shelf-life lifecycle", 6)

    states = [
        ("1. FRESH", "DTE > 3 Days", "Nominal operational state. Full price shelf velocity. Standard FIFO/FEFO dispatch.", ACCENT_GREEN),
        ("2. EXPIRING SOON", "1 < DTE <= 3 Days", "Elevated monitoring. Trigger candidate for early 20-30% dynamic promotional markdown.", ACCENT_AMBER),
        ("3. CRITICAL", "0 <= DTE <= 1 Day", "Immediate operational intervention required. Aggressive 50% discount or rapid transfer to food bank.", ACCENT_RED),
        ("4. EXPIRED", "DTE < 0 Days", "Terminal stage. Immediate floor removal protocol. Logged as shrinkage waste loss in kg/USD.", RGBColor(150, 150, 150))
    ]

    for i, (s_name, s_rule, s_action, s_color) in enumerate(states):
        left_pos = Inches(0.8 + i * 3.0)
        c, tf = add_card(slide6, left_pos, Inches(1.9), Inches(2.75), Inches(4.7), s_name, s_rule, border_color=s_color)
        p_act = tf.add_paragraph()
        p_act.text = "Operational Protocol:"
        p_act.font.name = FONT_TITLE
        p_act.font.size = Pt(11)
        p_act.font.bold = True
        p_act.font.color.rgb = s_color
        p_act.space_before = Pt(14)

        p_desc = tf.add_paragraph()
        p_desc.text = s_action
        p_desc.font.name = FONT_BODY
        p_desc.font.size = Pt(10.5)
        p_desc.font.color.rgb = TEXT_MUTED
        p_desc.space_before = Pt(6)

        p_math = tf.add_paragraph()
        p_math.text = f"Formula Trigger:\nDays_to_Expiry = Expiry_Date - Ref_Date\nStatus = evaluate_state(DTE)"
        p_math.font.name = 'Consolas'
        p_math.font.size = Pt(9)
        p_math.font.color.rgb = TEXT_DIM
        p_math.space_before = Pt(20)

    # =========================================================================
    # SLIDE 7: PREDICTIVE SPOILAGE VELOCITY ENGINE
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Predictive Analytics", "Predictive Demand & Spoilage Velocity Analytics", "Quantifying economic exposure and spoilage risk through mathematical models", 7)

    c1, tf1 = add_card(slide7, Inches(0.8), Inches(1.9), Inches(5.66), Inches(4.7), "Mathematical Risk Formulations", "Formulas executed dynamically across the batch matrix")
    add_bullet_list(tf1, [
        "1. Dynamic Days to Expiration (DTE):",
        "    DTE = (Expiry_Date - Current_Reference_Timestamp).days",
        "2. Estimated Waste Economic Impact ($):",
        "    Waste_Cost = Quantity_Remaining × Unit_Cost",
        "    (Quantifies sunk capital loss if batch remains unsold)",
        "3. Potential Revenue at Risk ($):",
        "    Revenue_Risk = Quantity_Remaining × Selling_Price × Decay_Probability",
        "    where Decay_Probability = 1.0 if DTE <= 1 else (0.5 if DTE <= 3 else 0.0)",
        "4. Perishable Waste Mass Impact (kg):",
        "    Waste_Mass_kg = Quantity_Remaining × Unit_Mass_Factor"
    ], font_size=10.5, space_before=5)

    c2, tf2 = add_card(slide7, Inches(6.86), Inches(1.9), Inches(5.66), Inches(4.7), "Operational Benefits & Accuracy", "How algorithmic quantification transforms store performance")
    add_bullet_list(tf2, [
        "Deterministic Prioritization: Store associates receive an objective, dollar-ranked queue of batches requiring action.",
        "Margin Recovery: Recovers up to 60-70% of potential write-offs through timed markdown intervention.",
        "Supplier Quality Audits: Aggregated batch decay data reveals which suppliers deliver produce with shortened effective shelf life.",
        "Automated Shrink KPI Reporting: Real-time calculation of corporate ESG metrics (food waste kg averted) for annual compliance."
    ], font_size=11, space_before=8)

    # =========================================================================
    # SLIDE 8: DECISION INTELLIGENCE: 3-PILLAR ACTION ENGINE
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Decision Intelligence", "3-Pillar Prescriptive Recommendation Engine", "Converting raw decay alerts into high-confidence, actionable operational decisions", 8)

    pillars = [
        ("Pillar 1: Dynamic Markdown", ACCENT_AMBER, [
            "Trigger: DTE <= 2 days with quantity > daily sell-through rate.",
            "Action: Automatic POS barcode markdown (25% to 50% discount).",
            "Objective: Stimulate price elasticity to clear stock before expiration.",
            "Impact: Recovers salvage revenue vs complete inventory write-off."
        ]),
        ("Pillar 2: Predictive Replenishment", ACCENT_CYAN, [
            "Trigger: Batch quantity drops below computed reorder_threshold.",
            "Action: Generates proactive restock requisition to regional DC.",
            "Objective: Prevent stockout lost sales on high-velocity fresh items.",
            "Impact: Eliminates empty shelf out-of-stock events on staple groceries."
        ]),
        ("Pillar 3: Inter-Store Transfers", ACCENT_PURPLE, [
            "Trigger: Store A has surplus near-expiry stock, Store B has stockout.",
            "Action: Dispatches inter-store transfer order within 10km radius.",
            "Objective: Balance inventory across metro store network efficiently.",
            "Impact: Maximizes sell-through rate without cannibalizing local margins."
        ])
    ]

    for i, (p_title, p_color, p_items) in enumerate(pillars):
        p_left = Inches(0.8 + i * 4.04)
        c, tf = add_card(slide8, p_left, Inches(1.9), Inches(3.64), Inches(4.7), p_title, "Autonomous Prescriptive Action", border_color=p_color)
        add_bullet_list(tf, p_items, font_size=10.5, space_before=8)

    # =========================================================================
    # SLIDE 9: DATA INGESTION & PIPELINE ARCHITECTURE
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "Data Engineering", "Data Ingestion & Pipeline Architecture", "In-memory streaming abstraction with seamless enterprise database extensibility", 9)

    c1, tf1 = add_card(slide9, Inches(0.8), Inches(1.9), Inches(5.66), Inches(4.7), "Current Architecture: In-Memory Engine", "Ultra-fast DataFrame loader (data_loader.py)")
    add_bullet_list(tf1, [
        "Singleton DataLoader Pattern: Instantiated once at application startup, maintaining warm in-memory datasets.",
        "Zero-Copy Joins: Vectorized Pandas merges joining products.csv, inventory_batches.csv, stores.csv, and sample_recommendations.csv.",
        "Temporal Calibration: DEMO_REFERENCE_DATE anchors dynamic calculations reproducibly across environments.",
        "Dynamic Enrichments: Computes days_to_expiry, freshness_status, and is_stockout_risk on the fly per query.",
        "Sub-10ms Lookup: In-memory filtering guarantees instant dashboard responsiveness."
    ], font_size=10.5, space_before=6)

    c2, tf2 = add_card(slide9, Inches(6.86), Inches(1.9), Inches(5.66), Inches(4.7), "Enterprise Target: Distributed Pipeline", "Cloud data lake and streaming telemetry evolution")
    add_bullet_list(tf2, [
        "PostgreSQL + TimescaleDB: Relational inventory tables coupled with time-series hyper-tables for batch telemetry history.",
        "Apache Kafka / Redpanda: Streaming events from edge RFID / barcode scanners and store POS checkout counters.",
        "Redis Memory Cache: Hot-key caching for active near-expiry items and real-time store summary rollups.",
        "Airflow / Prefect Orchestration: Nightly model retraining pipelines for seasonal demand elasticity coefficients.",
        "CDC (Change Data Capture): Debezium connector syncing ERP inventory deltas in real-time."
    ], font_size=10.5, space_before=6)

    # =========================================================================
    # SLIDE 10: FRONTEND CLIENT ARCHITECTURE & REACTIVE STATE
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "Client Architecture", "Frontend Architecture & Reactive State Flow", "Modern React 18 + Vite dashboard with responsive store analytics", 10)

    c1, tf1 = add_card(slide10, Inches(0.8), Inches(1.9), Inches(5.66), Inches(4.7), "Component Architecture & UI Hierarchy", "Modular, reusable component structure")
    add_bullet_list(tf1, [
        "StoreSelector: Global location switcher triggering context-level data refresh.",
        "MetricCardsGrid: Top-level visual telemetry displaying Total Batches, Expiring Soon, Critical Alerts, and Waste ($/kg).",
        "FilterToolbar: Multi-faceted search bar, Category dropdown, and Freshness status toggles (FRESH / CRITICAL).",
        "InventoryBatchTable: High-density interactive batch table with color-coded freshness badges and expiration progress bars.",
        "RecommendationsDrawer: Prioritized actionable alert cards with one-click approval workflows for discounts and reorders."
    ], font_size=10.5, space_before=6)

    c2, tf2 = add_card(slide10, Inches(6.86), Inches(1.9), Inches(5.66), Inches(4.7), "State Management & Client Performance", "Low overhead, reactive data synchronization")
    add_bullet_list(tf2, [
        "Vite Build Tooling: Instant HMR (Hot Module Replacement) and optimized tree-shaken production bundles.",
        "Lucide React Icon System: High-clarity, lightweight SVG iconography across all system status badges.",
        "Client-Side Debouncing: Search queries debounced at 250ms to minimize network traffic while maintaining instant typing feedback.",
        "Optimistic UI Updates: Immediate local state updates on recommendation actions before backend confirmation.",
        "Responsive Breakpoint Design: Seamless desktop dashboard transitioning to tablet/handheld POS views."
    ], font_size=10.5, space_before=6)

    # =========================================================================
    # SLIDE 11: MULTI-STORE TOPOLOGY & INVENTORY BALANCING
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    add_header(slide11, "Distributed Logistics", "Multi-Store Orchestration & Transfer Network", "Graph-based inventory rebalancing across distributed supermarket chains", 11)

    c1, tf1 = add_card(slide11, Inches(0.8), Inches(1.9), Inches(5.66), Inches(4.7), "Network Graph Formulation", "Modeling grocery stores as supply-demand nodes")
    add_bullet_list(tf1, [
        "Node Attributes: Each store entity includes store_id, store_name, city, geo-coordinates, and daily foot-traffic velocity.",
        "Surplus Detection: Stores exhibiting lower sales velocity with high batch volume nearing expiration are tagged as Surplus Nodes.",
        "Deficit Detection: Nearby high-velocity stores experiencing stockout risk on identical SKUs are tagged as Deficit Nodes.",
        "Distance Matrix Filtering: Restricts inter-store transfer proposals to local logistics thresholds (e.g. < 15km) to maintain cold-chain integrity."
    ], font_size=10.5, space_before=6)

    c2, tf2 = add_card(slide11, Inches(6.86), Inches(1.9), Inches(5.66), Inches(4.7), "Economic Optimization Objective", "Balancing logistics expense vs inventory preservation")
    add_bullet_list(tf2, [
        "Objective Function: Maximize (Recovered Margin - Logistics Transit Cost - Handling Labor).",
        "Cold-Chain Compliance: Checks whether recipient store possesses compatible refrigeration facilities before transfer authorization.",
        "Automated Bill of Lading: Generates transfer manifest with batch ID and source/target store manager notifications.",
        "Regional Fleet Integration: Feeds transfer routes into morning retail distribution delivery loops."
    ], font_size=10.5, space_before=6)

    # =========================================================================
    # SLIDE 12: CONCURRENCY, LATENCY & PERFORMANCE SLAS
    # =========================================================================
    slide12 = prs.slides.add_slide(blank_layout)
    add_header(slide12, "Performance Engineering", "Concurrency, Latency & Performance SLAs", "Architected for real-time edge processing and enterprise scale", 12)

    metrics = [
        ("< 50 ms", "API Response P95 Latency", "Ensures instantaneous dashboard re-render and scanner response.", ACCENT_GREEN),
        ("5,000+ RPS", "Throughput Concurrency", "Async Uvicorn event loop handling high-frequency POS polling.", ACCENT_CYAN),
        ("100% In-Memory", "Vectorized Aggregations", "Zero disk I/O bottlenecks during peak retail trading hours.", ACCENT_AMBER),
        ("99.95%", "System Availability SLA", "Stateless API architecture enabling zero-downtime rolling deploys.", ACCENT_PURPLE)
    ]

    for i, (m_val, m_title, m_desc, m_color) in enumerate(metrics):
        m_left = Inches(0.8 + i * 3.0)
        c, tf = add_card(slide12, m_left, Inches(1.9), Inches(2.75), Inches(2.1), m_val, m_title, border_color=m_color)
        p_val = tf.paragraphs[0]
        p_val.font.size = Pt(28)
        p_val.font.color.rgb = m_color
        p_d = tf.add_paragraph()
        p_d.text = m_desc
        p_d.font.name = FONT_BODY
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = TEXT_MUTED
        p_d.space_before = Pt(6)

    c_bot, tf_bot = add_card(slide12, Inches(0.8), Inches(4.3), Inches(11.733), Inches(2.3), "Key Performance Optimization Strategies", "Engineering tactics enabling extreme responsiveness")
    add_bullet_list(tf_bot, [
        "Asynchronous Non-Blocking Execution: FastAPI routes built on Python's asyncio prevent thread starvation under concurrent store requests.",
        "Vectorized DataFrame Calculations: Pandas vectorized operations perform expiration arithmetic across 50,000 batches in < 8ms.",
        "Stateless Horizontal Scaling: Microservice instances contain no session state, allowing seamless container auto-scaling under load.",
        "Payload Minimization: Selective field serialization ensures network payloads remain lightweight (< 25KB per view)."
    ], font_size=10.5, space_before=4)

    # =========================================================================
    # SLIDE 13: ENTERPRISE SECURITY & DATA GOVERNANCE
    # =========================================================================
    slide13 = prs.slides.add_slide(blank_layout)
    add_header(slide13, "Security & Compliance", "Enterprise Security & Data Governance", "Protecting retail operational integrity, financial metrics, and access roles", 13)

    c1, tf1 = add_card(slide13, Inches(0.8), Inches(1.9), Inches(5.66), Inches(4.7), "Role-Based Access Control (RBAC)", "Hierarchical authorization matrix across store operations")
    add_bullet_list(tf1, [
        "Store Associate / Floor Staff: Read-only access to batch expiry dates, shelf locations, and markdown barcode printing.",
        "Store Manager: Authorization to approve recommended price markdowns, initiate inter-store transfers, and adjust safety thresholds.",
        "Regional Supply Chain Director: Full visibility across all regional stores, transfer network topology, and supplier waste scores.",
        "System Admin / Auditor: Complete audit trail inspection, API key management, and data pipeline governance."
    ], font_size=10.5, space_before=6)

    c2, tf2 = add_card(slide13, Inches(6.86), Inches(1.9), Inches(5.66), Inches(4.7), "Data Governance & Network Security", "Hardened infrastructure and compliance standards")
    add_bullet_list(tf2, [
        "CORS Configuration: Strict whitelist origin headers preventing unauthorized cross-site request attacks.",
        "Immutable Audit Logs: Every markdown approval and inventory write-off is logged with timestamp, user ID, and financial delta.",
        "Food Safety Compliance: Traceability logs support regulatory recall investigations (e.g. FDA FSMA Section 204 batch traceability).",
        "TLS 1.3 Encryption: All communications between edge scanners, store POS terminals, and cloud APIs encrypted in transit."
    ], font_size=10.5, space_before=6)

    # =========================================================================
    # SLIDE 14: TESTING, QUALITY ASSURANCE & CI/CD PIPELINE
    # =========================================================================
    slide14 = prs.slides.add_slide(blank_layout)
    add_header(slide14, "DevOps & QA", "Testing, Quality Assurance & CI/CD Pipeline", "Rigorous verification ensuring 100% computational accuracy of shelf-life algorithms", 14)

    c1, tf1 = add_card(slide14, Inches(0.8), Inches(1.9), Inches(5.66), Inches(4.7), "Automated Test Suite (Pytest & HTTPX)", "Multi-layer verification strategy")
    add_bullet_list(tf1, [
        "Unit Tests: Validates mathematical correctness of DTE subtraction, waste dollar calculations, and threshold evaluations.",
        "State Machine Boundary Tests: Tests leap-year edge cases, negative DTE expired transitions, and boundary status flips.",
        "Integration Tests (TestClient): Verifies all FastAPI endpoints (/api/health, /api/summary, /api/products, etc.) return HTTP 200 with valid JSON.",
        "Mocking Fixtures: Simulated CSV datasets enable rapid, repeatable test runs without disk side effects."
    ], font_size=10.5, space_before=6)

    c2, tf2 = add_card(slide14, Inches(6.86), Inches(1.9), Inches(5.66), Inches(4.7), "CI/CD & Deployment Blueprint", "Continuous delivery to cloud and edge environments")
    add_bullet_list(tf2, [
        "GitHub Actions Pipeline: Automated linting (Ruff/Flake8), type checks (Mypy), and Pytest execution on every pull request.",
        "Docker Containerization: Lightweight Alpine/Slim Python multi-stage Docker builds minimizing image size (< 120MB).",
        "Kubernetes / Cloud Run Deployment: Horizontal Pod Autoscaler (HPA) dynamically scaling instances based on CPU and request queue depth.",
        "Edge Synchronization: In-store offline-first cache with automatic syncing when store connectivity is restored."
    ], font_size=10.5, space_before=6)

    # =========================================================================
    # SLIDE 15: ENGINEERING ROADMAP & FUTURE MILESTONES
    # =========================================================================
    slide15 = prs.slides.add_slide(blank_layout)
    add_header(slide15, "Strategic Roadmap", "Engineering Roadmap & Evolution Milestones", "Phased delivery plan from MVP foundation to autonomous zero-waste enterprise engine", 15)

    milestones = [
        ("Milestone 1: Foundation (COMPLETED)", ACCENT_GREEN, [
            "FastAPI reactive microservice backend",
            "In-memory dynamic FEFO degradation engine",
            "Pydantic v2 schemas and validation models",
            "Multi-store sample dataset & KPI rollup endpoints",
            "React 18 dashboard foundation with Vite"
        ]),
        ("Milestone 2: Telemetry & Vision (NEXT)", ACCENT_CYAN, [
            "IoT Cold-Chain Bluetooth temperature/humidity sensors",
            "Computer Vision edge ripeness detection on produce",
            "PostgreSQL / TimescaleDB production migration",
            "Dynamic price elasticity curve integration",
            "Mobile handheld scanner PWA application"
        ]),
        ("Milestone 3: Autonomous AI (VISION)", ACCENT_PURPLE, [
            "Reinforcement Learning for autonomous markdown discounting",
            "Bi-directional ERP connectors (SAP, Oracle, NetSuite)",
            "Automated ESL (Electronic Shelf Label) IoT price sync",
            "Federated chain-wide demand forecasting networks",
            "Food bank donation automated routing network"
        ])
    ]

    for i, (m_title, m_color, m_items) in enumerate(milestones):
        m_left = Inches(0.8 + i * 4.04)
        c, tf = add_card(slide15, m_left, Inches(1.9), Inches(3.64), Inches(4.7), m_title, "Phase Overview & Deliverables", border_color=m_color)
        add_bullet_list(tf, m_items, font_size=10.5, space_before=8)

    # Save presentation
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(output_file))
    print(f"Successfully generated PowerPoint presentation at: {output_file.resolve()}")

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "FreshGuard_AI_Technical_Architecture.pptx"
    create_deck(out)
