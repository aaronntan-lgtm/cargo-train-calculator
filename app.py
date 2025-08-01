import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Last War Tools", layout="wide")

# Custom CSS for dropdown styling
st.markdown("""
    <style>
    div[data-baseweb="select"] > div {
        border-color: #28a745 !important;
        box-shadow: 0 0 0 1px #28a745 !important;
    }
    .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Language options
languages = {
    "English": "en",
    "Tiếng Việt": "vi",
    "繁體中文": "zh"
}
lang_choice = st.selectbox("🌐 Select Language / Chọn ngôn ngữ / 選擇語言", list(languages.keys()))
lang = languages[lang_choice]

# Localized content
text = {
    "tabs": {
        "en": ["🚂 Mega Express Train", "🪖 T10 Grind"],
        "vi": ["🚂 Tàu Cao Tốc", "🪖 Cày T10"],
        "zh": ["🚂 特快列車", "🪖 T10 升級"]
    },
    "train_title": {
        "en": "🚂 Mega Express Train",
        "vi": "🚂 Tàu Cao Tốc",
        "zh": "🚂 特快列車"
    },
    "train_intro": {
        "en": "Select your best cabin based on current queue sizes.",
        "vi": "Chọn khoang tốt nhất dựa trên số người xếp hàng hiện tại.",
        "zh": "根據目前排隊人數選擇最佳車廂。"
    },
    "ev_description": {
        "en": "**What is EV?** Expected Value (EV) estimates your average gain over time. A higher EV means a better long-term choice.",
        "vi": "**EV là gì?** Giá trị kỳ vọng (EV) ước tính mức lợi trung bình theo thời gian. EV càng cao càng tốt.",
        "zh": "**什麼是 EV？** EV（期望值）表示長期平均收益。EV 越高，選擇越優。"
    },
    "input_header": {
        "en": "📥 Input Queue Sizes for Each Cabin",
        "vi": "📥 Nhập số người đang xếp hàng tại mỗi khoang",
        "zh": "📥 輸入每個車廂的排隊人數"
    },
    "input_label": {
        "en": "Cabin {name} (Enter number of players)",
        "vi": "Khoang {name} (Nhập số người chơi)",
        "zh": "車廂 {name}（輸入玩家數）"
    },
    "ranking_header": {
        "en": "📊 Cabin Rankings by EV",
        "vi": "📊 Xếp hạng theo EV",
        "zh": "📊 EV 排名"
    },
    "t10_title": {
        "en": "🪖 T10 Grind",
        "vi": "🪖 Cày T10",
        "zh": "🪖 T10 升級"
    },
    "t10_intro": {
        "en": "Select your current research level to calculate remaining costs.",
        "vi": "Chọn cấp độ nghiên cứu hiện tại để tính chi phí còn lại.",
        "zh": "選擇你當前的研究等級以計算剩餘資源。"
    },
    "t10_table_header": {
        "en": "📋 Resources needed for T10",
        "vi": "📋 Tài nguyên cần để mở T10",
        "zh": "📋 解鎖 T10 所需資源"
    }
}

# Tabs
tabs = st.tabs(text["tabs"][lang])

# ------------------------ Train Calculator ------------------------
with tabs[0]:
    st.title(text["train_title"][lang])
    st.markdown(text["train_intro"][lang])
    st.subheader(text["ranking_header"][lang])
    st.markdown(text["ev_description"][lang])

    st.subheader(text["input_header"][lang])
    queue_a = st.number_input(text["input_label"][lang].format(name="A"), min_value=0, value=0)
    queue_b = st.number_input(text["input_label"][lang].format(name="B"), min_value=0, value=0)
    queue_c = st.number_input(text["input_label"][lang].format(name="C"), min_value=0, value=0)
    queue_d = st.number_input(text["input_label"][lang].format(name="D"), min_value=0, value=0)

    cabins = {
        'A': {'queue': queue_a, 'value': 2},
        'B': {'queue': queue_b, 'value': 1},
        'C': {'queue': queue_c, 'value': 1},
        'D': {'queue': queue_d, 'value': 4}
    }

    def calculate_ev(queue_size, cabin_value):
        if queue_size == 0:
            return float('inf')
        return (5 / queue_size) * cabin_value

    ev_list = []
    for name, data in cabins.items():
        ev = calculate_ev(data['queue'], data['value'])
        ev_list.append((name, ev))

    ev_list.sort(key=lambda x: -x[1])

    for rank, (name, ev) in enumerate(ev_list, start=1):
        if cabins[name]['queue'] == 0:
            st.markdown(f"**{rank}. Cabin {name} — (Please select number of players in the queue)**")
        else:
            st.markdown(f"**{rank}. Cabin {name} — EV = {ev:.2f}**")

# ------------------------ T10 Calculator ------------------------
with tabs[1]:
    st.title(text["t10_title"][lang])
    st.markdown(text["t10_intro"][lang])

    # Cost data
    t10_data = {
        "Advanced Protection": [
            (31, 31, 91), (53, 53, 158), (53, 53, 158), (74, 74, 221), (74, 74, 221),
            (96, 96, 287), (96, 96, 287), (134, 134, 403), (134, 134, 403), (175, 175, 522)
        ],
        "HP Boost": [
            (31, 31, 91), (53, 53, 158), (53, 53, 158), (74, 74, 221), (74, 74, 221),
            (96, 96, 287), (96, 96, 287), (134, 134, 403), (134, 134, 403), (175, 175, 522)
        ],
        "Attack Boost": [
            (31, 31, 91), (53, 53, 158), (53, 53, 158), (74, 74, 221), (74, 74, 221),
            (96, 96, 287), (96, 96, 287), (134, 134, 403), (134, 134, 403), (175, 175, 522)
        ],
        "Defense Boost": [
            (31, 31, 91), (53, 53, 158), (53, 53, 158), (74, 74, 221), (74, 74, 221),
            (96, 96, 287), (96, 96, 287), (134, 134, 403), (134, 134, 403), (175, 175, 522)
        ],
        "Unit X": [(187, 187, 560)]
    }

    # Dropdowns for each category
    levels = {}
    col1, col2 = st.columns(2)
    with col1:
        levels["Advanced Protection"] = st.selectbox("Advanced Protection", list(range(0, 11)), index=0, format_func=lambda x: "Max" if x == 10 else x)
        levels["Attack Boost"] = st.selectbox("Attack Boost III", list(range(0, 11)), index=0, format_func=lambda x: "Max" if x == 10 else x)
    with col2:
        levels["HP Boost"] = st.selectbox("HP Boost III", list(range(0, 11)), index=0, format_func=lambda x: "Max" if x == 10 else x)
        levels["Defense Boost"] = st.selectbox("Defense Boost III", list(range(0, 11)), index=0, format_func=lambda x: "Max" if x == 10 else x)

    levels["Unit X"] = st.selectbox("Unit X", [0, 1], index=0, format_func=lambda x: "Max" if x == 1 else x)

    # Calculate remaining cost
    iron_total = bread_total = gold_total = 0
    for category, level in levels.items():
        steps = t10_data[category][level:]
        for iron, bread, gold in steps:
            iron_total += iron
            bread_total += bread
            gold_total += gold

    def format_number(val):
        if val >= 1_000:
            return f"{val/1000:.1f}G"
        return f"{val:.1f}M"

    st.subheader(text["t10_table_header"][lang])
    df = pd.DataFrame([
        {"Resource": "Iron", "Amount": format_number(iron_total)},
        {"Resource": "Bread", "Amount": format_number(bread_total)},
        {"Resource": "Gold", "Amount": format_number(gold_total)}
    ])
    st.table(df.set_index("Resource"))
