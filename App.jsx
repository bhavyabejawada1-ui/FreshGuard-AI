import React, { useState, useMemo } from 'react';
import {
  ShieldAlert,
  Layers,
  AlertTriangle,
  Clock,
  Sparkles,
  TrendingDown,
  RefreshCw,
  Search,
  Filter,
  Download,
  Presentation,
  CheckCircle2,
  XCircle,
  ExternalLink,
  ChevronRight,
  ChevronLeft,
  ArrowRight,
  Store as StoreIcon,
  ShoppingBag,
  Zap
} from 'lucide-react';

import {
  STORES,
  PRODUCTS,
  INITIAL_RECOMMENDATIONS,
  SLIDES_DATA,
  DEMO_REFERENCE_DATE,
  enrichBatches,
  computeSummaryMetrics,
} from './data/mockData';

export default function App() {
  const [selectedStore, setSelectedStore] = useState('ALL');
  const [activeTab, setActiveTab] = useState('dashboard'); // 'dashboard' | 'recommendations' | 'slides'
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('ALL');
  const [selectedFreshness, setSelectedFreshness] = useState('ALL');
  const [recommendations, setRecommendations] = useState(INITIAL_RECOMMENDATIONS);
  const [currentSlideIndex, setCurrentSlideIndex] = useState(0);
  const [toastMessage, setToastMessage] = useState(null);

  // Compute enriched batches based on selected store
  const allEnrichedBatches = useMemo(() => {
    return enrichBatches(selectedStore);
  }, [selectedStore]);

  // Compute metrics from batches
  const metrics = useMemo(() => {
    return computeSummaryMetrics(allEnrichedBatches);
  }, [allEnrichedBatches]);

  // Filtered batch inventory list
  const filteredBatches = useMemo(() => {
    return allEnrichedBatches.filter((b) => {
      const matchSearch =
        b.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
        b.sku.toLowerCase().includes(searchQuery.toLowerCase()) ||
        b.batch_id.toLowerCase().includes(searchQuery.toLowerCase());

      const matchCategory =
        selectedCategory === 'ALL' || b.category.toLowerCase() === selectedCategory.toLowerCase();

      const matchFreshness =
        selectedFreshness === 'ALL' || b.freshness_status === selectedFreshness;

      return matchSearch && matchCategory && matchFreshness;
    });
  }, [allEnrichedBatches, searchQuery, selectedCategory, selectedFreshness]);

  // Unique categories
  const categories = useMemo(() => {
    const set = new Set(PRODUCTS.map((p) => p.category));
    return ['ALL', ...Array.from(set)];
  }, []);

  // Filtered recommendations
  const filteredRecommendations = useMemo(() => {
    if (selectedStore === 'ALL') return recommendations;
    return recommendations.filter((r) => r.store_id === selectedStore);
  }, [recommendations, selectedStore]);

  const showToast = (msg) => {
    setToastMessage(msg);
    setTimeout(() => {
      setToastMessage(null);
    }, 3500);
  };

  const handleExecuteRec = (id, actionType) => {
    setRecommendations((prev) =>
      prev.map((r) => (r.id === id ? { ...r, status: 'EXECUTED' } : r))
    );
    showToast(`Successfully executed ${actionType} recommendation (${id})`);
  };

  const handleDismissRec = (id) => {
    setRecommendations((prev) => prev.filter((r) => r.id !== id));
    showToast(`Dismissed recommendation alert (${id})`);
  };

  const currentSlide = SLIDES_DATA[currentSlideIndex];

  return (
    <div className="app-container">
      {/* Toast Notification */}
      {toastMessage && (
        <div className="toast-notice">
          <CheckCircle2 size={20} color="#10B981" />
          <span>{toastMessage}</span>
        </div>
      )}

      {/* Main Header */}
      <header className="app-header">
        <div className="brand-section">
          <div className="brand-icon-wrapper">
            <ShieldAlert size={28} />
          </div>
          <div className="brand-text">
            <h1>
              FreshGuard.AI
              <span className="badge-pill-outline" style={{ fontSize: '0.7rem' }}>v1.0.0</span>
            </h1>
            <p className="brand-tagline">
              Zero-Waste Perishable Demand & Shelf-Life Management Engine
            </p>
          </div>
        </div>

        <div className="header-actions">
          {/* Store Selector */}
          <div className="store-select-wrap">
            <StoreIcon size={16} style={{ position: 'absolute', left: '12px', color: '#94A3B8' }} />
            <select
              id="store-select"
              className="store-select"
              style={{ paddingLeft: '36px' }}
              value={selectedStore}
              onChange={(e) => setSelectedStore(e.target.value)}
            >
              <option value="ALL">All Network Stores (3 Locations)</option>
              {STORES.map((s) => (
                <option key={s.store_id} value={s.store_id}>
                  {s.store_name} ({s.city})
                </option>
              ))}
            </select>
          </div>

          {/* Download PowerPoint Button */}
          <a
            href="./FreshGuard_AI_Technical_Architecture.pptx"
            download="FreshGuard_AI_Technical_Architecture.pptx"
            className="btn btn-secondary"
            title="Download the full 15-slide PowerPoint deck"
          >
            <Download size={16} />
            <span>Download Deck (.pptx)</span>
          </a>

          {/* Live Date Chip */}
          <div className="badge-pill-outline" style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <Clock size={13} color="#10B981" />
            <span>Ref Date: {DEMO_REFERENCE_DATE}</span>
          </div>
        </div>
      </header>

      {/* Tab Navigation */}
      <nav className="tabs-navigation">
        <button
          className={`nav-tab ${activeTab === 'dashboard' ? 'active' : ''}`}
          onClick={() => setActiveTab('dashboard')}
        >
          <Layers size={16} />
          <span>Inventory & Telemetry</span>
          <span className="tab-badge">{filteredBatches.length}</span>
        </button>

        <button
          className={`nav-tab ${activeTab === 'recommendations' ? 'active' : ''}`}
          onClick={() => setActiveTab('recommendations')}
        >
          <Sparkles size={16} />
          <span>AI Recommendations</span>
          <span className="tab-badge">{filteredRecommendations.length}</span>
        </button>

        <button
          className={`nav-tab ${activeTab === 'slides' ? 'active' : ''}`}
          onClick={() => setActiveTab('slides')}
        >
          <Presentation size={16} />
          <span>Technical Architecture Deck</span>
          <span className="tab-badge">15 Slides</span>
        </button>
      </nav>

      {/* ==================================================================== */}
      {/* TAB 1: DASHBOARD & INVENTORY TELEMETRY */}
      {/* ==================================================================== */}
      {activeTab === 'dashboard' && (
        <main>
          {/* Summary Metric KPI Cards */}
          <section className="metrics-grid">
            <div className="metric-card accent-emerald">
              <div className="metric-header">
                <span className="metric-title">Active Batches</span>
                <div className="metric-icon icon-emerald"><ShoppingBag size={18} /></div>
              </div>
              <div className="metric-value">{metrics.total_batches}</div>
              <div className="metric-subtext">{metrics.total_units} total perishable units</div>
            </div>

            <div className="metric-card accent-amber">
              <div className="metric-header">
                <span className="metric-title">Near Expiry (≤3d)</span>
                <div className="metric-icon icon-amber"><Clock size={18} /></div>
              </div>
              <div className="metric-value">{metrics.near_expiry_count}</div>
              <div className="metric-subtext">Batches requiring markdown or transfer</div>
            </div>

            <div className="metric-card accent-rose">
              <div className="metric-header">
                <span className="metric-title">Critical Expiry (≤1d)</span>
                <div className="metric-icon icon-rose"><AlertTriangle size={18} /></div>
              </div>
              <div className="metric-value">{metrics.critical_expiry_count}</div>
              <div className="metric-subtext">Immediate flash clearance candidate</div>
            </div>

            <div className="metric-card accent-cyan">
              <div className="metric-header">
                <span className="metric-title">Stockout Risks</span>
                <div className="metric-icon icon-cyan"><TrendingDown size={18} /></div>
              </div>
              <div className="metric-value">{metrics.stockout_risk_count}</div>
              <div className="metric-subtext">Quantity below reorder threshold</div>
            </div>

            <div className="metric-card accent-purple">
              <div className="metric-header">
                <span className="metric-title">Waste at Risk</span>
                <div className="metric-icon icon-purple"><Zap size={18} /></div>
              </div>
              <div className="metric-value">${metrics.estimated_waste_usd.toLocaleString()}</div>
              <div className="metric-subtext">{metrics.estimated_waste_kg} kg estimated mass</div>
            </div>
          </section>

          {/* Filtering Toolbar */}
          <div className="toolbar-card">
            <div className="search-box">
              <Search size={18} />
              <input
                id="search-input"
                type="text"
                placeholder="Search SKU, product name, or batch ID..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
              />
            </div>

            {/* Category Filter Pills */}
            <div className="filter-pills">
              {categories.map((cat) => (
                <button
                  key={cat}
                  className={`filter-pill ${selectedCategory === cat ? 'active' : ''}`}
                  onClick={() => setSelectedCategory(cat)}
                >
                  {cat}
                </button>
              ))}
            </div>

            {/* Freshness Status Filter */}
            <div className="filter-pills">
              {['ALL', 'FRESH', 'EXPIRING_SOON', 'CRITICAL'].map((st) => (
                <button
                  key={st}
                  className={`filter-pill ${selectedFreshness === st ? 'active' : ''}`}
                  onClick={() => setSelectedFreshness(st)}
                >
                  {st === 'ALL' ? 'All Status' : st.replace('_', ' ')}
                </button>
              ))}
            </div>
          </div>

          {/* Batches Data Table */}
          <div className="table-card">
            <div className="table-header-title">
              <h2>
                <Layers size={20} color="#10B981" />
                Live Perishable Batch Matrix
              </h2>
              <span className="badge-pill-outline">Showing {filteredBatches.length} batches</span>
            </div>

            <div className="table-scroll">
              <table>
                <thead>
                  <tr>
                    <th>Batch & SKU</th>
                    <th>Product & Category</th>
                    <th>Store Location</th>
                    <th>Units & Threshold</th>
                    <th>Days to Expiry</th>
                    <th>Status</th>
                    <th>Unit Cost / Price</th>
                    <th>Waste Exposure</th>
                  </tr>
                </thead>
                <tbody>
                  {filteredBatches.length === 0 ? (
                    <tr>
                      <td colSpan="8" style={{ textAlign: 'center', padding: '40px', color: '#94A3B8' }}>
                        No inventory batches found matching current filters.
                      </td>
                    </tr>
                  ) : (
                    filteredBatches.map((b) => {
                      const dtePercent = Math.max(0, Math.min(100, (b.days_to_expiry / 10) * 100));
                      let progressColor = '#10B981';
                      if (b.freshness_status === 'CRITICAL') progressColor = '#F43F5E';
                      else if (b.freshness_status === 'EXPIRING_SOON') progressColor = '#F59E0B';

                      return (
                        <tr key={b.batch_id}>
                          <td>
                            <div className="batch-code">{b.batch_id}</div>
                            <div className="sku-sub">{b.sku}</div>
                          </td>
                          <td>
                            <div style={{ fontWeight: 600 }}>{b.name}</div>
                            <div style={{ fontSize: '0.78rem', color: '#94A3B8' }}>
                              {b.category} • Storage: {b.ideal_storage_temp}
                            </div>
                          </td>
                          <td>
                            <div style={{ fontSize: '0.85rem' }}>{b.store_name}</div>
                            <div style={{ fontSize: '0.75rem', color: '#64748B' }}>{b.store_id}</div>
                          </td>
                          <td>
                            <div style={{ fontWeight: 700 }}>
                              {b.quantity} {b.unit}s
                            </div>
                            <div style={{ fontSize: '0.75rem', color: b.is_stockout_risk ? '#F43F5E' : '#64748B' }}>
                              Threshold: {b.reorder_threshold} {b.is_stockout_risk && '⚠️ Risk'}
                            </div>
                          </td>
                          <td>
                            <div className="dte-bar-wrap">
                              <span className="dte-text" style={{ color: progressColor }}>
                                {b.days_to_expiry} days left
                              </span>
                              <div className="dte-progress">
                                <div
                                  className="dte-progress-fill"
                                  style={{
                                    width: `${dtePercent}%`,
                                    backgroundColor: progressColor,
                                  }}
                                />
                              </div>
                              <span style={{ fontSize: '0.7rem', color: '#64748B' }}>
                                Exp: {b.expiry_date}
                              </span>
                            </div>
                          </td>
                          <td>
                            <span
                              className={`status-badge ${
                                b.freshness_status === 'FRESH'
                                  ? 'badge-fresh'
                                  : b.freshness_status === 'EXPIRING_SOON'
                                  ? 'badge-expiring'
                                  : b.freshness_status === 'CRITICAL'
                                  ? 'badge-critical'
                                  : 'badge-expired'
                              }`}
                            >
                              {b.freshness_status.replace('_', ' ')}
                            </span>
                          </td>
                          <td>
                            <div>${b.selling_price.toFixed(2)}</div>
                            <div style={{ fontSize: '0.75rem', color: '#64748B' }}>
                              Cost: ${b.unit_cost.toFixed(2)}
                            </div>
                          </td>
                          <td>
                            <div style={{ fontWeight: 700, color: b.days_to_expiry <= 3 ? '#F43F5E' : '#F8FAFC' }}>
                              ${b.estimated_waste_cost.toFixed(2)}
                            </div>
                          </td>
                        </tr>
                      );
                    })
                  )}
                </tbody>
              </table>
            </div>
          </div>
        </main>
      )}

      {/* ==================================================================== */}
      {/* TAB 2: AI RECOMMENDATIONS */}
      {/* ==================================================================== */}
      {activeTab === 'recommendations' && (
        <main>
          <div className="toolbar-card" style={{ marginBottom: '24px' }}>
            <div>
              <h2 style={{ fontSize: '1.25rem', fontWeight: 800 }}>
                Proactive Inventory Interventions
              </h2>
              <p style={{ color: '#94A3B8', fontSize: '0.88rem' }}>
                Algorithmic actions dispatched to minimize perishability decay and maximize sell-through velocity
              </p>
            </div>
            <button
              className="btn btn-secondary"
              onClick={() => {
                setRecommendations(INITIAL_RECOMMENDATIONS);
                showToast('Reset recommendations queue to default state.');
              }}
            >
              <RefreshCw size={15} />
              <span>Reset Recommendations</span>
            </button>
          </div>

          <div className="recommendations-grid">
            {filteredRecommendations.map((rec) => {
              const typeClass =
                rec.type === 'MARKDOWN'
                  ? 'type-markdown'
                  : rec.type === 'RESTOCK'
                  ? 'type-restock'
                  : 'type-transfer';

              const isExecuted = rec.status === 'EXECUTED';

              return (
                <div key={rec.id} className="recommendation-card">
                  <div className="rec-top-row">
                    <span className={`rec-type-badge ${typeClass}`}>{rec.type}</span>
                    <span
                      className={`status-badge ${
                        rec.urgency === 'CRITICAL'
                          ? 'badge-critical'
                          : rec.urgency === 'HIGH'
                          ? 'badge-expiring'
                          : 'badge-fresh'
                      }`}
                    >
                      {rec.urgency} Urgency
                    </span>
                  </div>

                  <div>
                    <h3 className="rec-title">{rec.title}</h3>
                    <div style={{ fontSize: '0.82rem', color: '#94A3B8', marginTop: '2px' }}>
                      {rec.product_name} • {rec.store_name}
                    </div>
                  </div>

                  <p className="rec-desc">{rec.description}</p>

                  <div className="rec-action-box">
                    <strong>Recommended Action:</strong>
                    {rec.action_detail}
                  </div>

                  <div className="rec-roi-bar">
                    <div className="roi-item">
                      <span className="roi-label">Est. Financial Savings</span>
                      <span className="roi-val" style={{ color: '#10B981' }}>
                        +${rec.estimated_savings_usd.toFixed(2)}
                      </span>
                    </div>
                    {rec.waste_reduction_kg > 0 && (
                      <div className="roi-item">
                        <span className="roi-label">Waste Averted</span>
                        <span className="roi-val" style={{ color: '#06B6D4' }}>
                          {rec.waste_reduction_kg} kg
                        </span>
                      </div>
                    )}
                  </div>

                  <div className="rec-card-actions">
                    {isExecuted ? (
                      <div
                        style={{
                          display: 'flex',
                          alignItems: 'center',
                          gap: '6px',
                          color: '#10B981',
                          fontWeight: 700,
                          fontSize: '0.9rem',
                        }}
                      >
                        <CheckCircle2 size={18} />
                        <span>Action Executed & Synced to POS</span>
                      </div>
                    ) : (
                      <>
                        <button
                          className="btn btn-primary"
                          style={{ flex: 1 }}
                          onClick={() => handleExecuteRec(rec.id, rec.type)}
                        >
                          <CheckCircle2 size={16} />
                          <span>Approve & Execute</span>
                        </button>
                        <button
                          className="btn btn-secondary"
                          onClick={() => handleDismissRec(rec.id)}
                          title="Dismiss recommendation"
                        >
                          <XCircle size={16} />
                        </button>
                      </>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        </main>
      )}

      {/* ==================================================================== */}
      {/* TAB 3: TECHNICAL ARCHITECTURE SLIDE DECK EXPLORER */}
      {/* ==================================================================== */}
      {activeTab === 'slides' && (
        <main className="slides-deck-container">
          <div className="slides-deck-header">
            <div>
              <span className="slide-category-chip">Interactive Technical Presentation</span>
              <h2 style={{ fontSize: '1.4rem', fontWeight: 800 }}>
                15-Slide Architecture & System Design Specification
              </h2>
              <p style={{ color: '#94A3B8', fontSize: '0.9rem', marginTop: '4px' }}>
                Browse slides interactively or download the native .pptx PowerPoint file below.
              </p>
            </div>

            <a
              href="./FreshGuard_AI_Technical_Architecture.pptx"
              download="FreshGuard_AI_Technical_Architecture.pptx"
              className="btn btn-primary"
            >
              <Download size={16} />
              <span>Download PowerPoint (.pptx)</span>
            </a>
          </div>

          {/* Interactive Slide Viewer Canvas */}
          <div className="slide-viewer-box">
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span className="slide-category-chip">{currentSlide.category}</span>
                <span style={{ fontSize: '0.9rem', color: '#64748B', fontWeight: 600 }}>
                  Slide {currentSlide.slideNumber} of 15
                </span>
              </div>

              <h2 className="slide-heading">{currentSlide.title}</h2>
              <div className="slide-subtitle">{currentSlide.subtitle}</div>

              <ul className="slide-bullets-list">
                {currentSlide.bullets.map((bullet, i) => (
                  <li key={i} className="slide-bullet-item">
                    <span className="bullet-dot" />
                    <span>{bullet}</span>
                  </li>
                ))}
              </ul>
            </div>

            {/* Slide Navigation Controls */}
            <div className="slide-footer-bar">
              <div className="slide-controls">
                <button
                  className="btn btn-secondary"
                  disabled={currentSlideIndex === 0}
                  onClick={() => setCurrentSlideIndex((prev) => Math.max(0, prev - 1))}
                  style={{ opacity: currentSlideIndex === 0 ? 0.4 : 1 }}
                >
                  <ChevronLeft size={18} />
                  <span>Previous</span>
                </button>

                <button
                  className="btn btn-primary"
                  disabled={currentSlideIndex === SLIDES_DATA.length - 1}
                  onClick={() =>
                    setCurrentSlideIndex((prev) => Math.min(SLIDES_DATA.length - 1, prev + 1))
                  }
                  style={{ opacity: currentSlideIndex === SLIDES_DATA.length - 1 ? 0.4 : 1 }}
                >
                  <span>Next</span>
                  <ChevronRight size={18} />
                </button>
              </div>

              {/* Slide Number Dot Selector */}
              <div className="slide-number-pills">
                {SLIDES_DATA.map((s, idx) => (
                  <button
                    key={s.slideNumber}
                    className={`slide-nav-dot ${idx === currentSlideIndex ? 'active' : ''}`}
                    onClick={() => setCurrentSlideIndex(idx)}
                    title={`Slide ${s.slideNumber}: ${s.title}`}
                  >
                    {s.slideNumber}
                  </button>
                ))}
              </div>
            </div>
          </div>
        </main>
      )}

      {/* Footer */}
      <footer className="app-footer">
        <div>
          © 2026 <strong>FreshGuard.AI</strong> — Engineering Specification & Zero-Waste Retail Intelligence.
        </div>
        <div className="footer-links">
          <a
            href="./FreshGuard_AI_Technical_Architecture.pptx"
            download="FreshGuard_AI_Technical_Architecture.pptx"
          >
            Download Deck (.pptx)
          </a>
          <a href="https://github.com" target="_blank" rel="noreferrer">
            GitHub Repo
          </a>
        </div>
      </footer>
    </div>
  );
}
