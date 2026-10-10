# 🌱 FreshGuard.AI

> **Zero-Waste Perishable Demand & Shelf-Life Management Engine**  
> Proactive FEFO (First-Expired, First-Out) inventory tracking, decay analytics, and autonomous retail markdown intelligence.

---

## 🚀 Key Highlights & Features

- **Dynamic FEFO State Machine**: Real-time batch shelf-life tracking across `FRESH`, `EXPIRING_SOON`, `CRITICAL`, and `EXPIRED` status.
- **3-Pillar Decision Intelligence**:
  1. 🏷️ **Dynamic Markdowns**: Timed discount triggers based on days-to-expiry and sales velocity.
  2. 📦 **Predictive Replenishment**: Automated restock alerts before stockout thresholds trip.
  3. 🔄 **Inter-Store Transfers**: Balances surplus perishable batches from slow stores to high-demand locations.
- **Store-Centric Telemetry**: Unified network overview with granular multi-store switching (San Francisco, Oakland).
- **Interactive Technical Slide Deck**: Embedded 15-slide technical architecture explorer and direct downloadable `.pptx` presentation file.
- **Full-Stack or Serverless Edge**: Runs with the FastAPI backend or seamlessly standalone on **GitHub Pages** with embedded telemetry simulation.

---

## 📊 Technical Presentation (.pptx)

The complete 15-slide editable technical architecture deck is included in this repository:
- 📁 **File Location**: [`FreshGuard_AI_Technical_Architecture.pptx`](./FreshGuard_AI_Technical_Architecture.pptx)
- 🌐 **Web Download**: Click the **"Download Deck (.pptx)"** button directly inside the web application navbar or presentation tab.

### Slide Deck Summary
1. **Title & Overview**: System Design & Mission
2. **System Context**: Perishable Grocery Problem Domain & FIFO Failure
3. **System Topology**: 3-Tier Layered Architecture
4. **Data Modeling**: Pydantic v2 Batch Entities & Inventory Schemas
5. **API Specification**: RESTful FastAPI OpenAPI Endpoints
6. **Degradation Modeling**: Deterministic State Machine Transitions
7. **Predictive Analytics**: Spoilage Velocity & Revenue at Risk Formulas
8. **Decision Intelligence**: 3-Pillar Action Engine (Markdown / Restock / Transfer)
9. **Data Engineering**: In-Memory Vectorization & TimescaleDB Roadmap
10. **Client Architecture**: React 18 + Vite SPA & Reactive State Flow
11. **Distributed Logistics**: Multi-Store Rebalancing Graph
12. **Performance SLAs**: Sub-50ms Latency & High-Concurrency Uvicorn Loop
13. **Security & Governance**: Multi-Role RBAC & Food Safety Compliance
14. **DevOps & QA**: Pytest Suites & Docker Deployment
15. **Strategic Roadmap**: Milestones 1 through 3 (IoT Sensors & Autonomous AI)

---

## 🌐 Deploying to GitHub Pages (Step-by-Step)

This repository includes a pre-configured automated GitHub Actions workflow at [`.github/workflows/deploy.yml`](./.github/workflows/deploy.yml).

### Step 1: Initialize Git and Push to GitHub

Open PowerShell or your terminal in this project folder and run:

```bash
# 1. Initialize git repository
git init

# 2. Stage all project files
git add .

# 3. Create your initial commit
git commit -m "feat: FreshGuard.AI website, backend, and technical architecture PPT"

# 4. Set default branch to main
git branch -M main

# 5. Link your GitHub remote repository (replace with your GitHub repository URL)
git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY_NAME>.git

# 6. Push code to GitHub
git push -u origin main
```

### Step 2: Enable GitHub Pages

1. Navigate to your repository on **GitHub**: `https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY_NAME>`
2. Click **Settings** (top navigation tab).
3. In the left sidebar, click **Pages** (under the "Code and automation" section).
4. Under **Build and deployment**:
   - Change **Source** to: `GitHub Actions`
5. That's it! GitHub Actions will automatically trigger the deployment workflow.
6. Once completed (usually 1-2 minutes), your live website will be accessible at:
   `https://<YOUR_USERNAME>.github.io/<YOUR_REPOSITORY_NAME>/`

---

## 💻 Running Locally

### 1. Frontend (React 18 + Vite)

```bash
cd frontend
npm install
npm run dev
```

Open your browser at `http://localhost:3000` (or the port displayed in your terminal).

To test the production build:
```bash
npm run build
npm run preview
```

### 2. Backend (FastAPI Microservice)

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000
```

- API Base URL: `http://localhost:8000`
- Interactive OpenAPI Docs: `http://localhost:8000/docs`
- Health Check: `http://localhost:8000/api/health`

---

## 📁 Repository Structure

```
FreshGuard.AI/
├── .github/
│   └── workflows/
│       └── deploy.yml              # Automated GitHub Pages CI/CD workflow
├── backend/
│   ├── app/
│   │   ├── config.py               # Path configurations & demo date anchor
│   │   ├── data_loader.py          # Vectorized Pandas dataset joiner
│   │   ├── main.py                 # FastAPI application & route endpoints
│   │   └── models.py               # Pydantic v2 schemas
│   ├── data/
│   │   ├── inventory_batches.csv   # Physical batches & expiration dates
│   │   ├── products.csv            # Perishable catalog & unit costs
│   │   ├── sample_recommendations.csv # Prescriptive actions dataset
│   │   └── stores.csv              # Retail store locations & managers
│   └── requirements.txt            # Python dependencies
├── frontend/
│   ├── public/
│   │   └── FreshGuard_AI_Technical_Architecture.pptx # Downloadable presentation asset
│   ├── src/
│   │   ├── data/
│   │   │   └── mockData.js         # Embedded telemetry datasets & state engine
│   │   ├── App.jsx                 # Main React UI component
│   │   ├── index.css               # Design system & dark theme tokens
│   │   └── main.jsx                # React DOM entry point
│   ├── index.html                  # HTML entry point with SEO tags
│   ├── package.json                # Frontend dependencies
│   └── vite.config.js              # Vite build config with relative base path
├── FreshGuard_AI_Technical_Architecture.pptx # Master 15-slide PowerPoint deck
├── .gitignore                      # Git exclusion rules
└── README.md                       # Documentation & deployment guide
```

---

## 📄 License

MIT License. Built for zero-waste grocery innovation.
