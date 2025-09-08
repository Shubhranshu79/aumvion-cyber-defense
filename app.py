import streamlit as st
import random
import time
from datetime import datetime
import pandas as pd

# ==========================
# CONFIG
# ==========================
st.set_page_config(page_title="AUMVION Cyber Defense Demo", layout="wide")
st.markdown("""
    <style>
    body { background-color: #0d0d0d; color: #e0e0e0; font-family: 'Consolas', monospace; }
    .stApp { background-color: #0d0d0d; }
    .big-title { font-size: 38px; font-weight: bold; color: #00ffea; text-shadow: 0px 0px 15px #00ffea; }
    .sub-title { font-size: 22px; color: #ff007f; text-shadow: 0px 0px 10px #ff007f; }
    .threat   { font-size: 20px; color: #ff4d4d; font-weight: bold; }
    .defense  { font-size: 20px; color: #00ff00; font-weight: bold; }
    .safe     { font-size: 20px; color: #00ffe1; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# ==========================
# DATA
# ==========================
threats = [
    "Malware Attack", "Phishing Attempt", "DDoS Attack", "Ransomware Infection",
    "Data Breach", "SQL Injection", "Zero-Day Exploit", "Insider Threat"
]
defenses = {
    "Malware Attack": "Antivirus Scan & Quarantine",
    "Phishing Attempt": "Firewall + Email Filter Blocked",
    "DDoS Attack": "Traffic Filtering & Load Balancing",
    "Ransomware Infection": "System Backup Restored + Isolation",
    "Data Breach": "Intrusion Prevention & Security Patch",
    "SQL Injection": "Database Firewall & Query Sanitization",
    "Zero-Day Exploit": "AI Heuristic Patch + Rollback",
    "Insider Threat": "User Monitoring & Access Revoked"
}

def generate_threat():
    return random.choice(threats)
def defend(threat):
    return defenses.get(threat, "General Defense Protocol Applied")

def run_attack_cycle():
    threat = generate_threat()
    defense = defend(threat)
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.ledger.append(
        {"time": timestamp, "threat": threat, "defense": defense}
    )
    status_placeholder.markdown(f"<p class='threat'>🟥 ALERT! {timestamp}: {threat}</p>", unsafe_allow_html=True)
    time.sleep(1.2)
    status_placeholder.markdown(f"<p class='defense'>🟨 Defense in Progress: {defense}</p>", unsafe_allow_html=True)
    time.sleep(1.2)
    status_placeholder.markdown(f"<p class='safe'>🟩 System Safe & Self-Healed ✅</p>", unsafe_allow_html=True)
    # Update Ledger (latest 10, reversed order)
    with ledger_placeholder:
        st.markdown("<h3 style='color:#00ffea;'>📑 Defense Ledger</h3>", unsafe_allow_html=True)
        df = pd.DataFrame(list(reversed(st.session_state.ledger[-10:])))
        st.dataframe(df, use_container_width=True)

if "ledger" not in st.session_state:
    st.session_state.ledger = []
if "auto_mode" not in st.session_state:
    st.session_state.auto_mode = False

# ==========================
# UI HEADER
# ==========================
st.markdown("<p class='big-title'>🛡️ AUMVION: Self-Healing Cyber Defense</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Futuristic AI-Powered Protection Simulation ⚡</p>", unsafe_allow_html=True)

# ==========================
# SIDEBAR CONTROLS
# ==========================
st.sidebar.header("⚙️ Controls")
speed = st.sidebar.slider("Attack Speed (seconds)", 2, 8, 4)
st.session_state.auto_mode = st.sidebar.checkbox("Enable Auto Mode (Continuous Attacks)", value=False)

# ==========================
# PLACEHOLDERS
# ==========================
status_placeholder = st.empty()
ledger_placeholder = st.container()

# ==========================
# MANUAL ATTACK BUTTON
# ==========================
if st.button("🚀 Launch Manual Attack"):
    run_attack_cycle()

# ==========================
# AUTO MODE LOOP
# ==========================
if st.session_state.auto_mode:
    placeholder = st.empty()
    iteration = 0
    while True:
        iteration += 1
        with placeholder.container():
            st.markdown(f"<h4 style='color:#ff007f;'>🔄 Cycle #{iteration}</h4>", unsafe_allow_html=True)
        run_attack_cycle()
        time.sleep(speed)
