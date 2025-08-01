import streamlit as st
import pandas as pd

st.set_page_config(page_title="Last War Calculators", layout="centered")

# Language selection at the top
languages = {
    "English": "en",
    "Tiếng Việt": "vi",
    "繁體中文": "zh"
}
lang_choice = st.selectbox("🌐 Select Language / Chọn ngôn ngữ / 選擇語言", list(languages.keys()))
lang = languages[lang_choice]

# Translations
text = {
    "train_title": {
        "en": "🚂 Mega Express Train",
        "vi": "🚂 Tàu cao tốc Mega",
        "zh": "🚂 超級快車"
    },
    "train_intro": {
        "en": "Choose your best cabin based on current queue. Cabin D is best, A second, B and C equal.",
        "vi": "Chọn khoang tốt nhất dựa trên hàng chờ. Khoang D tốt nhất, sau đó là A, B và C bằng nhau.",
        "zh": "根據排隊人數選擇最佳車廂。D 最佳，其次 A，B 與 C 相同。"
    },
    "input_header": {
        "en": "📥 Enter Queue for Each Cabin",
        "vi": "📥 Nhập hàng chờ cho mỗi khoang",
        "zh": "📥 輸入每個車廂的排隊人數"
    },
    "input_label": {
        "en": "Cabin {name} (passengers in queue)",
        "vi": "Khoang {name} (số người đang chờ)",
        "zh": "車廂 {name}（排隊人數）"
    },
    "ranking_header": {
        "en": "📊 Cabin Rankings by EV",
        "vi": "📊 Xếp hạng khoang theo EV",
        "zh": "📊 車廂 EV 排名"
    },
    "ev_note": {
        "en": "What is EV? Expected Value (EV) estimates your average gain over time. A higher EV means a better long-term choice.",
        "vi": "EV là gì? Giá trị kỳ vọng (EV) là mức lợi nhuận trung bình theo thời gian. EV càng cao càng tốt.",
        "zh": "什麼是 EV？期望值表示長期平均收益。EV 越高，越好。"
    },
    "t10_title": {
        "en": "🪖 T10 Grind",
        "vi": "🪖 Cày T10",
        "zh": "🪖 T10 升級"
    },
    "t10_header": {
        "en": "🧮 Select Your Current Research Levels",
        "vi": "🧮 Chọn cấp độ nghiên cứu hiện tại",
        "zh": "🧮 選擇目前研究等級"
    },
    "t10_table_header": {
        "en": "📦 Resources Needed for T10",
        "vi": "📦 Tài nguyên cần thiết cho T10",
        "zh": "📦 T10 所需資源"
    }
}

tab1, tab2 = st.tabs([text["train_title"][lang], text["t10_title"][lang]])

# --------------------- Mega Express Train Calculator ---------------------
with tab1:
    st.title(text["train_title"][lang])
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
            return float('inf')
        return (5 / queue_size) * cabin_value

    ev_list = []
    for name, data in cabins.items():
        ev = calculate_ev(data['queue'], data['value'])
        ev_list.append((name, ev))

    ev_list.sort(key=lambda x: -x[1])

    st.subheader(text["ranking_header"][lang])
    st.markdown(text["ev_note"][lang])

    for rank, (name, ev) in enumerate(ev_list, start=1):
        if cabins[name]['queue'] == 0:
            st.markdown(f"**{rank}. Cabin {name} — (Please select number of players in the queue)**")
        else:
            st.markdown(f"**{rank}. Cabin {name} — EV = {ev:.2f}**")

# --------------------- T10 Calculator ---------------------
with tab2:
    st.title(text["t10_title"][lang])
    st.subheader(text["t10_header"][lang])

    def format_large_number(n):
        if n >= 1_000_000_000:
            return f"{n / 1_000_000_000:.1f}G"
        elif n >= 1_000_000:
            return f"{n / 1_000_000:.1f}M"
        else:
            return str(n)

    # Full cost table
    t10_data = {
        "Advanced Protection": [
            (31_000_000, 31_000_000, 91_000_000),
            (53_000_000, 53_000_000, 158_000_000),
            (53_000_000, 53_000_000, 158_000_000),
            (74_000_000, 74_000_000, 221_000_000),
            (74_000_000, 74_000_000, 221_000_000),
            (96_000_000, 96_000_000, 287_000_000),
            (96_000_000, 96_000_000, 287_000_000),
            (134_000_000, 134_000_000, 403_000_000),
            (134_000_000, 134_000_000, 403_000_000),
            (175_000_000, 175_000_000, 522_000_000),
        ],
        "HP Boost": [
            (31_000_000, 31_000_000, 91_000_000),
            (53_000_000, 53_000_000, 158_000_000),
            (53_000_000, 53_000_000, 158_000_000),
            (74_000_000, 74_000_000, 221_000_000),
            (74_000_000, 74_000_000, 221_000_000),
            (96_000_000, 96_000_000, 287_000_000),
            (96_000_000, 96_000_000, 287_000_000),
            (134_000_000, 134_000_000, 403_000_000),
            (134_000_000, 134_000_000, 403_000_000),
            (175_000_000, 175_000_000, 522_000_000),
        ],
        "Attack Boost": [
            (31_000_000, 31_000_000, 91_000_000),
            (53_000_000, 53_000_000, 158_000_000),
            (53_000_000, 53_000_000, 158_000_000),
            (74_000_000, 74_000_000, 221_000_000),
            (74_000_000, 74_000_000, 221_000_000),
            (96_000_000, 96_000_000, 287_000_000),
            (96_000_000, 96_000_000, 287_000_000),
            (134_000_000, 134_000_000, 403_000_000),
            (134_000_000, 134_000_000, 403_000_000),
            (175_000_000, 175_000_000, 522_000_000),
        ],
        "Defense Boost": [
            (31_000_000, 31_000_000, 91_000_000),
            (53_000_000, 53_000_000, 158_000_000),
            (53_000_000, 53_000_000, 158_000_000),
            (74_000_000, 74_000_000, 221_000_000),
            (74_000_000, 74_000_000, 221_000_000),
            (96_000_000, 96_000_000, 287_000_000),
            (96_000_000, 96_000_000, 287_000_000),
            (134_000_000, 134_000_000, 403_000_000),
            (134_000_000, 134_000_000, 403_000_000),
            (175_000_000, 175_000_000, 522_000_000),
        ],
        "Unit X": [(187_000_000, 187_000_000, 560_000_000)]
    }

    levels = {}
    for tech in ["Advanced Protection", "HP Boost", "Attack Boost", "Defense Boost"]:
        levels[tech] = st.selectbox(
            tech,
            list(range(0, 11)),
            index=0,
            format_func=lambda x: "Max" if x == 10 else x
        )
    levels["Unit X"] = st.selectbox("Unit X", [0, 1], index=0, format_func=lambda x: "Max" if x == 1 else x)

    total_iron = total_bread = total_gold = 0
    for tech, level in levels.items():
        for i in range(level):
            iron, bread, gold = t10_data[tech][i]
            total_iron += iron
            total_bread += bread
            total_gold += gold

    st.subheader(text["t10_table_header"][lang])
    st.markdown(f"**Iron**: {format_large_number(total_iron)}")
    st.markdown(f"**Bread**: {format_large_number(total_bread)}")
    st.markdown(f"**Gold**: {format_large_number(total_gold)}")
