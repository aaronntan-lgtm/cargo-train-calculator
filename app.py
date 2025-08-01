
import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Last War Tools", layout="wide")

# Language options
languages = {
    "English": "en",
    "Tiếng Việt": "vi",
    "繁體中文": "zh"
}

lang_choice = st.sidebar.selectbox("🌐 Language", list(languages.keys()))
lang = languages[lang_choice]

# Text dictionary
text = {
    "mega_train_title": {
        "en": "🚂 Mega Express Train",
        "vi": "🚂 Tàu tốc hành Mega",
        "zh": "🚂 巨無霸特快車"
    },
    "train_intro": {
        "en": "Choose the best cabin based on queue sizes.",
        "vi": "Chọn khoang tốt nhất dựa trên hàng chờ.",
        "zh": "根據排隊人數選擇最佳車廂。"
    },
    "input_header": {
        "en": "📥 Enter Queue Sizes",
        "vi": "📥 Nhập số người xếp hàng",
        "zh": "📥 輸入排隊人數"
    },
    "input_label": {
        "en": "Cabin {name}",
        "vi": "Khoang {name}",
        "zh": "車廂 {name}"
    },
    "ranking_header": {
        "en": "📊 Cabin Rankings by EV",
        "vi": "📊 Xếp hạng khoang theo EV",
        "zh": "📊 根據 EV 排名的車廂"
    },
    "ev_desc": {
        "en": "What is EV? Expected Value (EV) estimates your average gain over time. A higher EV means a better long-term choice.",
        "vi": "EV là gì? Giá trị kỳ vọng (EV) ước tính mức lợi trung bình. EV càng cao thì lựa chọn càng tốt.",
        "zh": "什麼是 EV？期望值 (EV) 表示你平均獲得的收益，越高越好。"
    },
    "t10_title": {
        "en": "🛡️ T10 Grind",
        "vi": "🛡️ Cày T10",
        "zh": "🛡️ T10 辛勞"
    },
    "t10_intro": {
        "en": "Select your current research levels to calculate remaining resources needed to unlock Unit X.",
        "vi": "Chọn cấp nghiên cứu hiện tại để tính toán tài nguyên cần thiết.",
        "zh": "選擇目前研究等級來計算剩餘資源。"
    },
    "resources_needed": {
        "en": "📦 Resources needed for T10",
        "vi": "📦 Tài nguyên cần thiết cho T10",
        "zh": "📦 T10 所需資源"
    }
}

# Tabs
tab1, tab2 = st.tabs([text["mega_train_title"][lang], text["t10_title"][lang]])

# --------------- MEGA TRAIN CALCULATOR ---------------
with tab1:
    st.header(text["mega_train_title"][lang])
    st.markdown(text["train_intro"][lang])

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
            return None
        return (5 / queue_size) * cabin_value

    ev_list = []
    for name, data in cabins.items():
        ev = calculate_ev(data['queue'], data['value'])
        cabins[name]['ev'] = ev
        ev_list.append((name, ev))

    ev_list.sort(key=lambda x: -x[1] if x[1] else -1)

    st.subheader(text["ranking_header"][lang])
    st.markdown(text["ev_desc"][lang])
    for rank, (name, ev) in enumerate(ev_list, start=1):
        if ev is None:
            st.markdown(f"**{rank}. Cabin {name} — (Please select number of players in the queue)**")
        else:
            st.markdown(f"**{rank}. Cabin {name} — EV = {ev:.2f}**")

# --------------- T10 CALCULATOR ---------------
with tab2:
    st.header(text["t10_title"][lang])
    st.markdown(text["t10_intro"][lang])

    level_options = [f"{i}" for i in range(0, 10)] + ["Max"]
    unitx_option = ["0", "Max"]

    col1, col2 = st.columns(2)
    with col1:
        adv = st.selectbox("Advanced Protection", level_options, index=0)
        hp = st.selectbox("HP Boost III", level_options, index=0)
    with col2:
        atk = st.selectbox("Attack Boost III", level_options, index=0)
        defn = st.selectbox("Defence Boost III", level_options, index=0)
    unitx = st.selectbox("Unit X", unitx_option, index=0)

    def parse_level(val):
        return 10 if val == "Max" else int(val)

    level_data = {
        "Advanced Protection": parse_level(adv),
        "HP Boost III": parse_level(hp),
        "Attack Boost III": parse_level(atk),
        "Defence Boost III": parse_level(defn),
        "Unit X": parse_level(unitx)
    }

    # Cost per level in raw numbers
    cost_table = {
        "Advanced Protection": [
            (31,31,91),(53,53,158),(53,53,158),(74,74,221),(74,74,221),
            (96,96,287),(96,96,287),(134,134,403),(134,134,403),(175,175,522)
        ],
        "HP Boost III": [
            (31,31,91),(53,53,158),(53,53,158),(74,74,221),(74,74,221),
            (96,96,287),(96,96,287),(134,134,403),(134,134,403),(175,175,522)
        ],
        "Attack Boost III": [
            (31,31,91),(53,53,158),(53,53,158),(74,74,221),(74,74,221),
            (96,96,287),(96,96,287),(134,134,403),(134,134,403),(175,175,522)
        ],
        "Defence Boost III": [
            (31,31,91),(53,53,158),(53,53,158),(74,74,221),(74,74,221),
            (96,96,287),(96,96,287),(134,134,403),(134,134,403),(175,175,522)
        ],
        "Unit X": [
            (187,187,560)
        ]
    }

    # Accumulate cost
    total_iron, total_bread, total_gold = 0,0,0
    for cat, level in level_data.items():
        for i in range(level):
            iron, bread, gold = cost_table[cat][i]
            total_iron += iron
            total_bread += bread
            total_gold += gold

    def fmt(x):
        return f"{x/1000:.1f}G" if x >= 1000 else f"{x:.1f}M"

    st.subheader(text["resources_needed"][lang])
    df = pd.DataFrame({
        "Resource": ["Iron", "Bread", "Gold"],
        "Amount": [fmt(total_iron), fmt(total_bread), fmt(total_gold)]
    })

    st.table(df)
