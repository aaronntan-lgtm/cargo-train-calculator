
import streamlit as st
import pandas as pd

# Language selector at the top
st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] {
        width: 250px;
    }
    .main .block-container {
        max-width: 800px;
        margin: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

languages = {
    "English": "en",
    "Tiếng Việt": "vi",
    "繁體中文": "zh"
}
lang_choice = st.selectbox("🌐 Select Language / Chọn ngôn ngữ / 選擇語言", list(languages.keys()))
lang = languages[lang_choice]

text = {
    "train_title": {
        "en": "🚂 Mega Express Train",
        "vi": "🚂 Tàu Cao Tốc Mega",
        "zh": "🚂 巨型特快列車"
    },
    "train_intro": {
        "en": "Select your best cabin based on current queue sizes. Cabin D is best, then A, while B & C are equal.",
        "vi": "Chọn khoang tốt nhất dựa trên số người xếp hàng. D tốt nhất, tiếp theo là A, B và C ngang nhau.",
        "zh": "根據排隊人數選擇最佳車廂。D 最佳，其次是 A，B 和 C 相等。"
    },
    "train_input_header": {
        "en": "📥 Input Queue Sizes for Each Cabin",
        "vi": "📥 Nhập số hàng đợi cho từng khoang",
        "zh": "📥 輸入各車廂的排隊人數"
    },
    "train_input_label": {
        "en": "Cabin {name} (Enter the number of passengers in the queue here)",
        "vi": "Khoang {name} (Nhập số người xếp hàng tại đây)",
        "zh": "車廂 {name}（請輸入排隊人數）"
    },
    "train_ranking_header": {
        "en": "📊 Cabin Rankings by EV",
        "vi": "📊 Xếp hạng các khoang theo EV",
        "zh": "📊 根據 EV 排名的車廂"
    },
    "ev_description": {
        "en": "**What is EV?** Expected Value (EV) estimates your average gain over time. A higher EV means a better long-term choice.",
        "vi": "**EV là gì?** EV (Giá trị kỳ vọng) ước tính lợi ích trung bình theo thời gian. EV cao hơn nghĩa là lựa chọn dài hạn tốt hơn.",
        "zh": "**什麼是 EV？** EV（期望值）表示長期平均收益。EV 越高，表示更佳的長期選擇。"
    },
    "t10_title": {
        "en": "🪖 T10 Grind",
        "vi": "🪖 Leo T10",
        "zh": "🪖 T10 研究"
    },
    "t10_input_header": {
        "en": "📥 Select Current Research Levels",
        "vi": "📥 Chọn cấp độ nghiên cứu hiện tại",
        "zh": "📥 選擇目前研究等級"
    },
    "t10_total": {
        "en": "💰 Total Resources Needed",
        "vi": "💰 Tổng tài nguyên cần thiết",
        "zh": "💰 所需總資源"
    },
    "t10_table": {
        "en": "📋 Research Cost Breakdown",
        "vi": "📋 Chi tiết chi phí nghiên cứu",
        "zh": "📋 研究成本明細"
    }
}

tab1, tab2 = st.tabs([text["train_title"][lang], text["t10_title"][lang]])

# Mega Express Train Tab
with tab1:
    st.title(text["train_title"][lang])
    st.markdown(text["train_intro"][lang])
    st.subheader(text["train_input_header"][lang])

    queue_a = st.number_input(text["train_input_label"][lang].format(name="A"), min_value=0, value=0)
    queue_b = st.number_input(text["train_input_label"][lang].format(name="B"), min_value=0, value=0)
    queue_c = st.number_input(text["train_input_label"][lang].format(name="C"), min_value=0, value=0)
    queue_d = st.number_input(text["train_input_label"][lang].format(name="D"), min_value=0, value=0)

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

    st.subheader(text["train_ranking_header"][lang])
    st.markdown(text["ev_description"][lang])
    for rank, (name, ev) in enumerate(ev_list, start=1):
        if ev == float('inf'):
            st.markdown(f"**{rank}. Cabin {name} — (Please select number of players in the queue)**")
        else:
            st.markdown(f"**{rank}. Cabin {name} — EV = {ev:.2f}**")

# T10 Grind Tab
with tab2:
    st.title(text["t10_title"][lang])
    st.subheader(text["t10_input_header"][lang])

    tech_data = {
        "Advanced Protection": 10,
        "HP Boost": 10,
        "Attack Boost": 10,
        "Defense Boost": 10
    }

    cost_data = {
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

    def format_mg(n):
        if n >= 1_000:
            return f"{n / 1000:.1f}G"
        else:
            return f"{n:.1f}M"

    levels = {}
    for tech, max_level in tech_data.items():
        label = f"{tech} Current Level"
        options = list(range(0, max_level + 1))
        format_func = lambda x, m=max_level: "Max" if x == m else x
        levels[tech] = st.selectbox(label, options, index=0, format_func=format_func, key=tech)

    if all(levels[tech] == tech_data[tech] for tech in tech_data):
        include_unitx = True
    else:
        include_unitx = False

    total_iron = total_bread = total_gold = 0
    rows = []

    for tech in tech_data:
        current_level = levels[tech]
        for lvl in range(current_level, tech_data[tech]):
            iron, bread, gold = cost_data[tech][lvl]
            total_iron += iron
            total_bread += bread
            total_gold += gold
            rows.append((f"{tech} {lvl + 1}", f"{iron:.0f}M", f"{bread:.0f}M", f"{gold:.0f}M"))

    if include_unitx:
        iron, bread, gold = cost_data["Unit X"][0]
        total_iron += iron
        total_bread += bread
        total_gold += gold
        rows.append(("Unit X", f"{iron:.0f}M", f"{bread:.0f}M", f"{gold:.0f}M"))

    st.subheader(text["t10_total"][lang])
    st.markdown(f"- Iron: **{format_mg(total_iron)}**")
    st.markdown(f"- Bread: **{format_mg(total_bread)}**")
    st.markdown(f"- Gold: **{format_mg(total_gold)}**")

    st.subheader(text["t10_table"][lang])
    df = pd.DataFrame(rows, columns=["Item", "Iron (M)", "Bread (M)", "Gold (M)"])
    st.dataframe(df, use_container_width=True)
