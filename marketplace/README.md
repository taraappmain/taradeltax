# Tara Marketplace

This is the monetization module inside Tara_Main.

## Structure
- `backend/`: FastAPI services
- `dashboard/`: Unified Streamlit dashboard
- `main.py`: Launches the marketplace system

## Run
1. `cd marketplace`
2. `uvicorn backend.tara_unified_backend:app --reload`
3. `streamlit run dashboard/tara_unified_dashboard.py`
