from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import random

app = FastAPI(title="XAUUSD Phone Scalper Demo")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

state = {"running": False, "trades": [], "price": 2650.0, "max_trades": 3}

@app.get("/")
def root():
    return {"ok": True, "service": "XAUUSD Phone Scalper Demo", "mode": "DEMO"}

@app.get("/status")
def status():
    return {"ok": True, **state}

@app.post("/start")
def start():
    state["running"] = True
    return {"ok": True, "running": True}

@app.post("/stop")
def stop():
    state["running"] = False
    return {"ok": True, "running": False}

@app.post("/demo-signal")
def demo_signal():
    state["price"] += random.uniform(-2.0, 2.0)
    side = random.choice(["BUY","SELL"])
    entry = state["price"]
    risk = 1.8
    sl = entry-risk if side=="BUY" else entry+risk
    tp = entry+risk*1.2 if side=="BUY" else entry-risk*1.2
    signal = {"time": datetime.utcnow().isoformat(), "side": side, "entry": round(entry,2), "sl": round(sl,2), "tp": round(tp,2)}
    if state["running"] and len(state["trades"]) < state["max_trades"]:
        state["trades"].append(signal)
    return signal
