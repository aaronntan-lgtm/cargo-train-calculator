
import streamlit as st

st.set_page_config(page_title="Last War Tools", layout="wide")

# Language options
languages = {
    "English": "en",
    "Tiếng Việt": "vi",
    "繁體中文": "zh"
}
lang_choice = st.selectbox("🌐 Select Language / Chọn ngôn ngữ / 選擇語言", list(languages.keys()))
lang = languages[lang_choice]

# Localized text
text = {
    "mega_title": {
        "en": "🚂 Mega Express Train",
        "vi": "🚂 Tàu Tốc Hành Mega",
        "zh": "🚂 超級特快車"
    },
    "t10_title": {
        "en": "🪖 T10 Grind",
        "vi": "🪖 Cày T10",
        "zh": "🪖 T10 肝度計算"
    },
    "ev_intro": {
        "en": "What is EV? Expected Value (EV) estimates your average gain over time. A higher EV means a better long-term choice.",
        "vi": "EV là gì? Giá trị kỳ vọng (EV) ước tính mức lợi trung bình theo thời gian. EV càng cao thì lựa chọn càng tốt.",
        "zh": "什麼是 EV？期望值（EV）表示你長期平均能獲得的收益。EV 越高，長期表現越好。"
    },
    "ranking_header": {
        "en": "📊 Cabin Rankings by EV",
        "vi": "📊 Xếp hạng các khoang theo EV",
        "zh": "📊 根據 EV 排名的車廂"
    },
    "input_header": {
        "en": "📥 Input Queue Sizes for Each Cabin",
        "vi": "📥 Nhập số người đang xếp hàng tại mỗi khoang",
        "zh": "📥 輸入每個車廂的排隊人數"
    },
    "input_label": {
        "en": "Cabin {name} (Enter the number of players in the queue)",
        "vi": "Khoang {name} (Nhập số người xếp hàng)",
        "zh": "車廂 {name}（請輸入排隊人數）"
    },
    "t10_intro": {
        "en": "📊 Resources needed for T10",
        "vi": "📊 Tài nguyên cần cho T10",
        "zh": "📊 T10 所需資源"
    }
}

tab1, tab2 = st.tabs([text["mega_title"][lang], text["t10_title"][lang]])

with tab1:
    st.title(text["mega_title"][lang])
    st.markdown(text["input_header"][lang])
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

    def calculate_ev(queue, value):
        return float("inf") if queue == 0 else (5 / queue) * value

    ev_list = [(name, calculate_ev(data['queue'], data['value'])) for name, data in cabins.items()]
    ev_list.sort(key=lambda x: -x[1])

    st.subheader(text["ranking_header"][lang])
    st.markdown(text["ev_intro"][lang])
    for i, (name, ev) in enumerate(ev_list, 1):
        if ev == float("inf"):
            st.markdown(f"**{i}. Cabin {name} — (Please select number of players in the queue)**")
        else:
            st.markdown(f"**{i}. Cabin {name} — EV = {ev:.2f}**")

with tab2:
    st.title(text["t10_title"][lang])
    st.subheader(text["t10_intro"][lang])

    research_order = [
        "Advanced Protection", "HP Boost", "Attack Boost", "Defense Boost", "Unit X"
    ]

    research_levels = {
        "Advanced Protection": 10,
        "HP Boost": 10,
        "Attack Boost": 10,
        "Defense Boost": 10,
        "Unit X": 1
    }

    levels = {}
    for tech in research_order:
        max_lv = research_levels[tech]
        levels[tech] = st.selectbox(
            tech,
            options=[str(i) if i < max_lv else "Max" for i in range(0, max_lv + 1)],
            index=0,
            key=tech
        )

    # Cost data
    cost_data = {
        "HP Boost 10": (175e6, 175e6, 522e6),
        "Attack Boost 7": (96e6, 96e6, 287e6),
        "Attack Boost 8": (134e6, 134e6, 403e6),
        "Attack Boost 9": (134e6, 134e6, 403e6),
        "Attack Boost 10": (175e6, 175e6, 522e6),
        "Defense Boost 6": (96e6, 96e6, 287e6),
        "Defense Boost 7": (96e6, 96e6, 287e6),
        "Defense Boost 8": (134e6, 134e6, 403e6),
        "Defense Boost 9": (134e6, 134e6, 403e6),
        "Defense Boost 10": (175e6, 175e6, 522e6),
        "Unit X": (187e6, 187e6, 560e6),
    }

    def format_cost(x):
        if x >= 1e9:
            return f"{x / 1e9:.1f}G"
        elif x >= 1e6:
            return f"{x / 1e6:.1f}M"
        return f"{x}"

    iron_total = bread_total = gold_total = 0
    st.markdown("### Research Costs Summary")
    for item, (iron, bread, gold) in cost_data.items():
        iron_total += iron
        bread_total += bread
        gold_total += gold
        st.markdown(f"- **{item}** — Iron: {format_cost(iron)}, Bread: {format_cost(bread)}, Gold: {format_cost(gold)}")

    st.markdown("### Total Cost")
    st.markdown(f"- 🪓 Iron: {format_cost(iron_total)}")
    st.markdown(f"- 🍞 Bread: {format_cost(bread_total)}")
    st.markdown(f"- 🪙 Gold: {format_cost(gold_total)}")
