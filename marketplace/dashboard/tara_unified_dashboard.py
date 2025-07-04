

import sys
import os
import streamlit as st
import pandas as pd
import logging

# --- Plugin Imports ---
# Stock and Crypto plugins (optional)
try:
    from tara_skills import stock_plugin
except ImportError:
    stock_plugin = None
try:
    from tera.marketplace.crypto.crypto_agent_module import CryptoAgent, crypto_agent_ui
except ImportError:
    # Fallback for relative paths
    dashboard_dir = os.path.dirname(os.path.abspath(__file__))
    crypto_path = os.path.abspath(os.path.join(dashboard_dir, '..', 'crypto'))
    if crypto_path not in sys.path:
        sys.path.append(crypto_path)
    try:
        from crypto_agent_module import CryptoAgent, crypto_agent_ui
    except ImportError:
        CryptoAgent = None
        crypto_agent_ui = None

try:
    from tara_skills import crypto_plugin  # keep existing crypto_plugin if needed
except ImportError:
    crypto_plugin = None

try:
    from tara_voice.voice_toggle import toggle_voice_mode
except ImportError:
    def toggle_voice_mode():
        st.warning("Voice module not found.")

# --- Logging Setup ---
logging.basicConfig(
    filename='tara_dashboard.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# --- Init Streamlit ---
st.set_page_config(page_title="Tara Delta Monetization Dashboard", layout="wide")
st.title("🧠 Tara Delta Monetization Control Center")

# --- Initialize Agents ---
if 'tara_agents_df' not in st.session_state:
    st.session_state.tara_agents_df = pd.DataFrame([
        {"Agent ID": "A001", "Agent Name": "Tara Stock Plugin", "Category": "Finance", "Weekly Earnings": 600, "Monthly Profit": 200, "Monetizing": False, "Status": "Inactive"},
        {"Agent ID": "A002", "Agent Name": "YouTube Engine", "Category": "Content AI", "Weekly Earnings": 400, "Monthly Profit": 120, "Monetizing": False, "Status": "Inactive"},
        {"Agent ID": "A003", "Agent Name": "Affiliate Agent", "Category": "Marketing", "Weekly Earnings": 320, "Monthly Profit": 80, "Monetizing": False, "Status": "Inactive"},
        {"Agent ID": "A004", "Agent Name": "Dropshipping Agent", "Category": "E-commerce", "Weekly Earnings": 480, "Monthly Profit": 160, "Monetizing": False, "Status": "Inactive"},
        {"Agent ID": "A005", "Agent Name": "Crypto Agent", "Category": "Crypto", "Weekly Earnings": 800, "Monthly Profit": 280, "Monetizing": False, "Status": "Inactive"},
    ])

# --- Auto-Activate on First Load ---
if not st.session_state.get("agents_activated", False):
    st.session_state.tara_agents_df["Status"] = "Live"
    st.session_state.tara_agents_df["Monetizing"] = True
    st.session_state["agents_activated"] = True
    logging.info("All agents auto-activated on dashboard start.")

# --- Status Indicator ---
def status_dot(status):
    return "🟢 Live" if status.lower() == "live" else "⚫ Inactive"

# --- Agent Command Parser ---
def execute_dang_task(task_name):
    task = task_name.strip().lower()
    df = st.session_state.tara_agents_df
    if task == "activate all agents":
        df["Status"] = "Live"
        df["Monetizing"] = True
        logging.info("All agents activated and monetizing!")
        return True
    elif task.startswith("activate agent"):
        aid = task.split()[-1].upper()
        if aid in df["Agent ID"].values:
            df.loc[df["Agent ID"] == aid, ["Status", "Monetizing"]] = ["Live", True]
            logging.info(f"Agent {aid} activated.")
            return True
    elif task.startswith("deactivate agent"):
        aid = task.split()[-1].upper()
        if aid in df["Agent ID"].values:
            df.loc[df["Agent ID"] == aid, ["Status", "Monetizing"]] = ["Inactive", False]
            logging.info(f"Agent {aid} deactivated.")
            return True
    return False

# --- Dashboard Tabs ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview",
    "🧠 Agents",
    "💸 Crypto",
    "📈 Stocks",
    "🏦 Withdrawals"
])

# --- Overview Tab ---
with tab1:
    st.header("🧭 System Status")
    st.success("Tara Delta is online.")
    modules = {
        "Core Intelligence": "🟢",
        "Voice Engine": "🟡"
        if toggle_voice_mode else "⚫",
        "Cyber Core": "🟢",
        "Vision System": "🟢",
    }
    st.table(pd.DataFrame(modules.items(), columns=["Module", "Status"]))
    st.subheader("🎙️ Voice")
    if st.button("Toggle Voice Mode"):
        toggle_voice_mode()

# --- Agents Tab ---
with tab2:
    st.header("🧠 Agent Control & Earnings")
    df = st.session_state.tara_agents_df.copy()
    df["Daily Earnings"] = (df["Weekly Earnings"] / 7).round(2)
    df["Monetizing"] = df["Monetizing"].apply(lambda x: "Yes" if x else "No")
    df["Status"] = df["Status"].apply(status_dot)
    st.dataframe(
        df[["Agent ID", "Agent Name", "Category", "Daily Earnings", "Weekly Earnings", "Monthly Profit", "Monetizing", "Status"]]
    )

    st.subheader("🛠️ Agent Commands")
    cmd = st.text_input("Enter task (e.g., Activate Agent A002, Deactivate Agent A003)")
    if st.button("Execute Command"):
        if execute_dang_task(cmd):
            st.success(f"Executed: {cmd}")
        else:
            st.error("Unknown agent or command")

# --- Crypto Tab (Updated) ---
with tab3:
    st.header("💸 Crypto Agent Dashboard")
    if CryptoAgent and crypto_agent_ui:
        try:
            agent = CryptoAgent("A001")
            crypto_agent_ui(agent)
        except Exception as e:
            st.error(f"Error loading Crypto Agent UI: {e}")
    else:
        st.warning("Crypto Agent module not available.")

# --- Stock Tab ---
with tab4:
    st.header("📈 Stock Screener")
    if stock_plugin:
        try:
            stock_data = stock_plugin.get_market_snapshot()
            st.dataframe(stock_data)
        except Exception as e:
            st.error(f"Stock plugin error: {e}")
    else:
        st.warning("Stock plugin not available.")

# --- Withdrawals Tab ---
with tab5:
    st.header("🏦 Withdrawal Panel")
    st.write("💵 Fiat Available: $1000.00")
    st.write("🪙 Crypto Available: 2.5 BTC")
    col1, col2 = st.columns(2)
    with col1:
        withdrawal_type = st.radio("Type", ["Fiat", "Crypto"], horizontal=True)
        amount = st.number_input("Amount", min_value=0.01, step=0.01)
        wallet_id = st.text_input("Wallet ID (crypto only)") if withdrawal_type == "Crypto" else None
        pin = st.text_input("Enter 4-digit PIN", type="password")
        if st.button("Submit Withdrawal"):
            if len(pin) == 4 and pin.isdigit():
                if withdrawal_type == "Crypto" and not wallet_id:
                    st.error("Wallet ID required for crypto withdrawals.")
                else:
                    logging.info(f"Withdrawal requested: {amount} {withdrawal_type}")
                    st.success("Withdrawal submitted.")
            else:
                st.error("Invalid PIN.")

    with col2:
        st.subheader("📜 Recent Logs")
        try:
            with open("tara_dashboard.log") as f:
                logs = f.readlines()[-10:]
                for line in logs:
                    st.write(line.strip())
        except FileNotFoundError:
            st.info("No logs yet.")