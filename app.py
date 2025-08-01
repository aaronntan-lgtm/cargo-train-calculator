
import streamlit as st
import pandas as pd

# Set up page config
st.set_page_config(page_title="Last War Tools", layout="wide")

# Custom CSS to float the language selector at the top right
st.markdown("""
    <style>
        .css-18e3th9 {
            padding-top: 1rem;
        }
        .css-1d391kg {
            padding-top: 1rem;
        }
        div[data-testid="stSidebarNav"] {
            display: none;
        }
        div[data-testid="stSidebar"] {
            background-color: #f0f2f6;
        }
    </style>
""", unsafe_allow_html=True)

# Language selector pinned to top
language = st.selectbox("🌐 Language", ["English", "Tiếng Việt", "繁體中文"])

# Translation dictionary
translations = {
    "Mega Express Train": {
        "English": "🚂 Mega Express Train",
        "Tiếng Việt": "🚂 Tàu cao tốc",
        "繁體中文": "🚂 特快列車"
    },
    "T10 Grind": {
        "English": "🪖 T10 Grind",
        "Tiếng Việt": "🪖 Cày T10",
        "繁體中文": "🪖 T10 肝度"
    },
    "Resources needed for T10": {
        "English": "📦 Resources needed for T10",
        "Tiếng Việt": "📦 Tài nguyên cần thiết cho T10",
        "繁體中文": "📦 T10 所需資源"
    }
}

def format_number(n):
    if n >= 1_000_000_000:
        return f"{n / 1_000_000_000:.1f}G"
    elif n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    else:
        return str(n)

# Tab setup
tab1, tab2 = st.tabs([
    translations["Mega Express Train"][language],
    translations["T10 Grind"][language]
])

# ========== MEGA EXPRESS TRAIN ==========
with tab1:
    st.markdown("### 📥 Input Queue Sizes for Each Cabin")

    queue_a = st.number_input("Cabin A", min_value=0, value=0)
    queue_b = st.number_input("Cabin B", min_value=0, value=0)
    queue_c = st.number_input("Cabin C", min_value=0, value=0)
    queue_d = st.number_input("Cabin D", min_value=0, value=0)

    cabins = {
        'A': {'queue': queue_a, 'value': 2},
        'B': {'queue': queue_b, 'value': 1},
        'C': {'queue': queue_c, 'value': 1},
        'D': {'queue': queue_d, 'value': 4}
    }

    def calculate_ev(queue, value):
        if queue == 0:
            return float('inf')
        return (5 / queue) * value

    for name in cabins:
        cabins[name]['ev'] = calculate_ev(cabins[name]['queue'], cabins[name]['value'])

    sorted_cabins = sorted(cabins.items(), key=lambda x: -x[1]['ev'])

    st.markdown("### 📊 Cabin Rankings by EV")
    st.markdown("**What is EV?** Expected Value (EV) estimates your average gain over time. A higher EV means a better long-term choice.")

    for rank, (name, data) in enumerate(sorted_cabins, 1):
        if data['ev'] == float('inf'):
            st.markdown(f"**{rank}. Cabin {name} — (Please select number of players in the queue)**")
        else:
            st.markdown(f"**{rank}. Cabin {name} — EV = {data['ev']:.2f}**")

# ========== T10 GRIND ==========
with tab2:
    st.markdown("### 🪖 T10 Grind Calculator")

    # Levels input
    col1, col2 = st.columns(2)
    with col1:
        ap_lvl = st.selectbox("Advanced Protection", list(range(0, 11)), index=0, format_func=lambda x: f"{x}" if x < 10 else "Max")
        hp_lvl = st.selectbox("HP Boost III", list(range(0, 11)), index=0, format_func=lambda x: f"{x}" if x < 10 else "Max")
    with col2:
        atk_lvl = st.selectbox("Attack Boost III", list(range(0, 11)), index=0, format_func=lambda x: f"{x}" if x < 10 else "Max")
        def_lvl = st.selectbox("Defence Boost III", list(range(0, 11)), index=0, format_func=lambda x: f"{x}" if x < 10 else "Max")

    unitx = st.selectbox("Unit X", [0, 1], index=0, format_func=lambda x: "0" if x == 0 else "Max")

    # Cost table (updated)
    t10_data = [
        ["Advanced Protection", [
            (31, 31, 91), (53, 53, 158), (53, 53, 158), (74, 74, 221), (74, 74, 221),
            (96, 96, 287), (96, 96, 287), (134, 134, 403), (134, 134, 403), (175, 175, 522)
        ]],
        ["HP Boost III", [
            (31, 31, 91), (53, 53, 158), (53, 53, 158), (74, 74, 221), (74, 74, 221),
            (96, 96, 287), (96, 96, 287), (134, 134, 403), (134, 134, 403), (175, 175, 522)
        ]],
        ["Attack Boost III", [
            (31, 31, 91), (53, 53, 158), (53, 53, 158), (74, 74, 221), (74, 74, 221),
            (96, 96, 287), (96, 96, 287), (134, 134, 403), (134, 134, 403), (175, 175, 522)
        ]],
        ["Defence Boost III", [
            (31, 31, 91), (53, 53, 158), (53, 53, 158), (74, 74, 221), (74, 74, 221),
            (96, 96, 287), (96, 96, 287), (134, 134, 403), (134, 134, 403), (175, 175, 522)
        ]]
    ]

    unit_x_cost = (187, 187, 560) if unitx == 1 else (0, 0, 0)

    # Accumulate totals
    iron_total = bread_total = gold_total = 0

    for (name, levels), lvl in zip(t10_data, [ap_lvl, hp_lvl, atk_lvl, def_lvl]):
        for i in range(lvl):
            iron_total += levels[i][0] * 1_000_000
            bread_total += levels[i][1] * 1_000_000
            gold_total += levels[i][2] * 1_000_000

    iron_total += unit_x_cost[0] * 1_000_000
    bread_total += unit_x_cost[1] * 1_000_000
    gold_total += unit_x_cost[2] * 1_000_000

    st.markdown("### 📦 " + translations["Resources needed for T10"][language])
    st.write(f"**Iron:** {format_number(iron_total)}")
    st.write(f"**Bread:** {format_number(bread_total)}")
    st.write(f"**Gold:** {format_number(gold_total)}")
