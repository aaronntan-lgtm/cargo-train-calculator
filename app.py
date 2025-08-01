
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Last War Calculators", layout="centered")

# Custom CSS for green dropdown and floating language selector
st.markdown("""
    <style>
    div[data-baseweb="select"] > div {
        border-color: #28a745 !important;
        box-shadow: 0 0 0 1px #28a745 !important;
    }
    .language-bar {
        position: fixed;
        top: 10px;
        right: 10px;
        z-index: 9999;
        background: white;
        padding: 0.5em;
        border-radius: 6px;
        box-shadow: 0px 0px 5px #ccc;
    }
    </style>
""", unsafe_allow_html=True)

# Language options
languages = {
    "English": "en",
    "Tiếng Việt": "vi",
    "繁體中文": "zh"
}
lang_choice = st.selectbox("🌐 Language / Ngôn ngữ / 語言", list(languages.keys()), key="lang", help="Select your language")
lang = languages[lang_choice]

# Localized strings
text = {
    "mega_title": {
        "en": "🚂 Mega Express Train",
        "vi": "🚂 Tàu tốc hành Mega",
        "zh": "🚂 Mega 特快列車"
    },
    "t10_title": {
        "en": "🪖 T10 Grind",
        "vi": "🪖 Cày T10",
        "zh": "🪖 T10 消耗計算"
    },
    "ev_description": {
        "en": "**What is EV?** Expected Value (EV) estimates your average gain over time. A higher EV means a better long-term choice.",
        "vi": "**EV là gì?** EV (Giá trị kỳ vọng) ước tính lợi ích trung bình của bạn theo thời gian. EV càng cao thì càng có lợi.",
        "zh": "**什麼是 EV？** EV（期望值）估計你隨著時間平均的收益，越高越好。"
    },
    "input_header": {
        "en": "📥 Input Queue Sizes for Each Cabin",
        "vi": "📥 Nhập số người xếp hàng từng toa",
        "zh": "📥 輸入每節車廂的排隊人數"
    },
    "input_label": {
        "en": "Cabin {name}",
        "vi": "Toa {name}",
        "zh": "車廂 {name}"
    },
    "ranking_header": {
        "en": "📊 Cabin Rankings by EV",
        "vi": "📊 Xếp hạng toa theo EV",
        "zh": "📊 根據 EV 排名"
    },
    "placeholder": {
        "en": "(Please select number of players in the queue)",
        "vi": "(Vui lòng nhập số người trong hàng đợi)",
        "zh": "（請輸入排隊人數）"
    },
    "t10_desc": {
        "en": "Estimate the total resources required to unlock T10 using current progress.",
        "vi": "Tính tổng tài nguyên cần để mở khóa T10 dựa trên tiến độ hiện tại.",
        "zh": "根據當前進度預估解鎖 T10 所需總資源。"
    },
    "t10_header": {
        "en": "📦 Resources needed for T10",
        "vi": "📦 Tài nguyên cần thiết cho T10",
        "zh": "📦 解鎖 T10 所需資源"
    }
}

# Start tab interface
tab1, tab2 = st.tabs([text["mega_title"][lang], text["t10_title"][lang]])

# -------- Mega Express Train Tab --------
with tab1:
    st.title(text["mega_title"][lang])
    st.markdown(text["input_header"][lang])
    queue_a = st.number_input(text["input_label"][lang].format(name="A"), min_value=0, value=0)
    queue_b = st.number_input(text["input_label"][lang].format(name="B"), min_value=0, value=0)
    queue_c = st.number_input(text["input_label"][lang].format(name="C"), min_value=0, value=0)
    queue_d = st.number_input(text["input_label"][lang].format(name="D"), min_value=0, value=0)

    # Cabin values
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
        cabins[name]['ev'] = ev
        ev_list.append((name, ev))

    ev_list.sort(key=lambda x: -x[1])

    st.subheader(text["ranking_header"][lang])
    st.markdown(text["ev_description"][lang])
    for rank, (name, ev) in enumerate(ev_list, start=1):
        if cabins[name]['queue'] == 0:
            st.markdown(f"**{rank}. Cabin {name} — {text['placeholder'][lang]}**")
        else:
            st.markdown(f"**{rank}. Cabin {name} — EV = {ev:.2f}**")

# -------- T10 Grind Tab --------
with tab2:
    st.title(text["t10_title"][lang])
    st.markdown(text["t10_desc"][lang])

    st.divider()
    techs = {
        "Advanced Protection": 10,
        "HP Boost": 10,
        "Attack Boost": 10,
        "Defense Boost": 10,
        "Unit X": 1
    }

    levels = {}
    for tech, max_lv in techs.items():
        options = list(range(0, max_lv + 1))
        levels[tech] = st.selectbox(
            tech, options,
            index=0,
            format_func=lambda x, m=max_lv: "Max" if x == m else x,
            key=tech
        )

    # Full cost table
    cost_data = [
        # (Tech Name, Level, Iron, Bread, Gold)
        ("Advanced Protection", 1, 31_000_000, 31_000_000, 91_000_000),
        ("Advanced Protection", 2, 53_000_000, 53_000_000, 158_000_000),
        ("Advanced Protection", 3, 53_000_000, 53_000_000, 158_000_000),
        ("Advanced Protection", 4, 74_000_000, 74_000_000, 221_000_000),
        ("Advanced Protection", 5, 74_000_000, 74_000_000, 221_000_000),
        ("Advanced Protection", 6, 96_000_000, 96_000_000, 287_000_000),
        ("Advanced Protection", 7, 96_000_000, 96_000_000, 287_000_000),
        ("Advanced Protection", 8, 134_000_000, 134_000_000, 403_000_000),
        ("Advanced Protection", 9, 134_000_000, 134_000_000, 403_000_000),
        ("Advanced Protection", 10, 175_000_000, 175_000_000, 522_000_000),
        ("HP Boost", 1, 31_000_000, 31_000_000, 91_000_000),
        ("HP Boost", 2, 53_000_000, 53_000_000, 158_000_000),
        ("HP Boost", 3, 53_000_000, 53_000_000, 158_000_000),
        ("HP Boost", 4, 74_000_000, 74_000_000, 221_000_000),
        ("HP Boost", 5, 74_000_000, 74_000_000, 221_000_000),
        ("HP Boost", 6, 96_000_000, 96_000_000, 287_000_000),
        ("HP Boost", 7, 96_000_000, 96_000_000, 287_000_000),
        ("HP Boost", 8, 134_000_000, 134_000_000, 403_000_000),
        ("HP Boost", 9, 134_000_000, 134_000_000, 403_000_000),
        ("HP Boost", 10, 175_000_000, 175_000_000, 522_000_000),
        ("Attack Boost", 7, 96_000_000, 96_000_000, 287_000_000),
        ("Attack Boost", 8, 134_000_000, 134_000_000, 403_000_000),
        ("Attack Boost", 9, 134_000_000, 134_000_000, 403_000_000),
        ("Attack Boost", 10, 175_000_000, 175_000_000, 522_000_000),
        ("Defense Boost", 6, 96_000_000, 96_000_000, 287_000_000),
        ("Defense Boost", 7, 96_000_000, 96_000_000, 287_000_000),
        ("Defense Boost", 8, 134_000_000, 134_000_000, 403_000_000),
        ("Defense Boost", 9, 134_000_000, 134_000_000, 403_000_000),
        ("Defense Boost", 10, 175_000_000, 175_000_000, 522_000_000),
        ("Unit X", 1, 187_000_000, 187_000_000, 560_000_000)
    ]

    # Sum totals
    total_iron = 0
    total_bread = 0
    total_gold = 0
    for tech, level in levels.items():
        for row in cost_data:
            if row[0].startswith(tech) and row[1] <= level:
                total_iron += row[2]
                total_bread += row[3]
                total_gold += row[4]

    def fmt(val):
        if val >= 1_000_000_000:
            return f"{val/1e9:.1f}G"
        elif val >= 1_000_000:
            return f"{val/1e6:.1f}M"
        else:
            return str(val)

    st.subheader(text["t10_header"][lang])
    st.write(f"**Iron:** {fmt(total_iron)}")
    st.write(f"**Bread:** {fmt(total_bread)}")
    st.write(f"**Gold:** {fmt(total_gold)}")
