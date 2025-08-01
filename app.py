import streamlit as st

st.set_page_config(page_title="Best Cargo Train Calculator")

# Move language selector to the top
languages = {
    "English": "en",
    "Tiếng Việt": "vi",
    "繁體中文": "zh"
}
lang_choice = st.selectbox("🌐 Select Language / Chọn ngôn ngữ / 選擇語言", list(languages.keys()))
lang = languages[lang_choice]

# Custom CSS for green dropdown styling
st.markdown("""
    <style>
    div[data-baseweb="select"] > div {
        border-color: #28a745 !important;
        box-shadow: 0 0 0 1px #28a745 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Localized content
text = {
    "title_train": {
        "en": "🚂 Mega Express Train",
        "vi": "🚂 Tàu cao tốc Mega",
        "zh": "🚂 超級特快列車"
    },
    "title_t10": {
        "en": "🪖 T10 Grind",
        "vi": "🪖 Cày T10",
        "zh": "🪖 T10 升級"
    },
    "ev_description": {
        "en": "**What is EV?** Expected Value (EV) estimates your average gain over time. A higher EV means a better long-term choice.",
        "vi": "**EV là gì?** Giá trị kỳ vọng (EV) ước tính mức lợi trung bình của bạn theo thời gian. EV càng cao thì lựa chọn càng tốt về lâu dài.",
        "zh": "**什麼是 EV？** 期望值 (EV) 表示你長期平均能獲得的收益。EV 越高，長期表現越好。"
    },
    "input_header": {
        "en": "📥 Input Queue Sizes for Each Cabin",
        "vi": "📥 Nhập số người đang xếp hàng tại mỗi khoang",
        "zh": "📥 輸入每個車廂的排隊人數"
    },
    "input_label": {
        "en": "Cabin {name} (Enter the number of passengers in the queue here)",
        "vi": "Khoang {name} (Nhập số người xếp hàng tại đây)",
        "zh": "車廂 {name}（請輸入排隊人數）"
    },
    "ranking_header": {
        "en": "📊 Cabin Rankings by EV",
        "vi": "📊 Xếp hạng các khoang theo EV",
        "zh": "📊 根據 EV 排名的車廂"
    },
    "resources_header": {
        "en": "📦 Resources needed for T10",
        "vi": "📦 Tài nguyên cần thiết cho T10",
        "zh": "📦 T10 所需資源"
    }
}

tab1, tab2 = st.tabs([text["title_train"][lang], text["title_t10"][lang]])

with tab1:
    st.title(text["title_train"][lang])
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

    st.subheader(text["ranking_header"][lang])
    for rank, (name, ev) in enumerate(ev_list, start=1):
        if ev == float('inf'):
            st.markdown(f"**{rank}. Cabin {name} — (Please select number of players in the queue)**")
        else:
            st.markdown(f"**{rank}. Cabin {name} — EV = {ev:.2f}**")

with tab2:
    st.title(text["title_t10"][lang])

    def format_number(n):
        if n >= 1_000_000_000:
            return f"{n / 1_000_000_000:.1f}G"
        elif n >= 1_000_000:
            return f"{n / 1_000_000:.1f}M"
        return str(n)

    research_data = {
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
    for name, steps in research_data.items():
        max_level = len(steps)
        label = name
        levels[name] = st.selectbox(
            label,
            list(range(0, max_level + 1)),
            index=0,
            format_func=lambda x: "Max" if x == max_level else str(x)
        )

    total_iron = 0
    total_bread = 0
    total_gold = 0

    for name, level in levels.items():
        steps = research_data[name]
        for i in range(level):
            iron, bread, gold = steps[i]
            total_iron += iron
            total_bread += bread
            total_gold += gold

    st.markdown("### " + text["resources_header"][lang])
    st.markdown(f"- **Iron**: {format_number(total_iron)}")
    st.markdown(f"- **Bread**: {format_number(total_bread)}")
    st.markdown(f"- **Gold**: {format_number(total_gold)}")
