# XAUUSD Phone Scalper

Phone-first demo dashboard for an XAUUSD scalping strategy.

## Deploy backend on Render
- Runtime: Python
- Root Directory: `backend`
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`

## Frontend
The `frontend/index.html` is a standalone phone dashboard and can be hosted on GitHub Pages.

## Important
This build is DEMO/SIMULATION only. It does not place Headway orders.
Headway MT5 automation requires an MT5 execution environment/EA or another supported execution bridge.
Do not put your Headway password into this demo site.
