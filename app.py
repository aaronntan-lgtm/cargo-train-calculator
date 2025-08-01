
import streamlit as st

st.set_page_config(page_title="Cargo Tools", layout="centered")

# ----------------- Shared Styling -------------------
st.markdown("""
    <style>
    div[data-baseweb="select"] > div {
        border-color: #28a745 !important;
        box-shadow: 0 0 0 1px #28a745 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- Language Bar -------------------
languages = {
    "English": "en",
    "Tiếng Việt": "vi",
    "繁體中文": "zh"
}

lang_choice = st.selectbox("🌐 Select Language / Chọn ngôn ngữ / 選擇語言", list(languages.keys()))
lang = languages[lang_choice]

# ----------------- Train Calculator -------------------
def render_train_calculator():
    text = {
        "title": {
            "en": "🚂 Best Cargo Train Calculator",
            "vi": "🚂 Trình tính khoang tàu tốt nhất",
            "zh": "🚂 最佳貨運列車計算器"
        },
        "intro": {
            "en": "Select your best cabin based on current queue sizes. This assumes that Cabin D is the best, followed by Cabin A, and Cabins B & C have equal value.",
            "vi": "Chọn khoang tốt nhất dựa trên số người xếp hàng hiện tại. Khoang D có giá trị cao nhất, tiếp theo là A, còn B và C có giá trị bằng nhau.",
            "zh": "根據目前排隊人數選擇最佳車廂。車廂 D 為最高價值，其次為 A，B 和 C 價值相同。"
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
    }

    st.title(text["title"][lang])
    st.markdown(text["intro"][lang])
    st.subheader(text["input_header"][lang])

    queue_a = st.number_input(text["input_label"][lang].format(name="A"), min_value=0, value=11)
    queue_b = st.number_input(text["input_label"][lang].format(name="B"), min_value=0, value=9)
    queue_c = st.number_input(text["input_label"][lang].format(name="C"), min_value=0, value=13)
    queue_d = st.number_input(text["input_label"][lang].format(name="D"), min_value=0, value=22)

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
    for rank, (name, ev) in enumerate(ev_list, start=1):
        if ev == float('inf'):
            st.markdown(f"**{rank}. Cabin {name} — 100% chance of entry**")
        else:
            st.markdown(f"**{rank}. Cabin {name} — EV = {ev:.2f}**")

    st.markdown("---")
    st.markdown(text["ev_description"][lang])

# ----------------- T10 Calculator -------------------
def render_t10_calculator():
    st.title("🪖 T10 Research Calculator")
    st.write("Select your current level for each technology to calculate how much resources are needed to complete T10 requirements.")

    tech_trees = {
        "Advanced Protection": 10,
        "HP Boost": 10,
        "Attack Boost": 10,
        "Defense Boost": 10,
        "Unit X": 1
    }

    levels = {}
    for tech, max_level in tech_trees.items():
        if tech == "Unit X":
            levels[tech] = st.selectbox(f"{tech}", ["Not Researched", "Researched"], index=0, key=tech)
        else:
            label = f"{tech} Current Level"
            options = list(range(0, max_level + 1))
            format_func = lambda x: "10 (Max)" if x == 10 else x
            levels[tech] = st.selectbox(label, options, index=0, format_func=format_func, key=tech)

    cost_data = {
        "Advanced Protection": [
            (31e6, 31e6, 91e6), (53e6, 53e6, 158e6), (53e6, 53e6, 158e6),
            (74e6, 74e6, 221e6), (74e6, 74e6, 221e6), (96e6, 96e6, 287e6),
            (96e6, 96e6, 287e6), (134e6, 134e6, 403e6), (134e6, 134e6, 403e6),
            (175e6, 175e6, 522e6)
        ],
        "HP Boost": [
            (31e6, 31e6, 91e6), (53e6, 53e6, 158e6), (53e6, 53e6, 158e6),
            (74e6, 74e6, 221e6), (74e6, 74e6, 221e6), (96e6, 96e6, 287e6),
            (96e6, 96e6, 287e6), (134e6, 134e6, 403e6), (134e6, 134e6, 403e6),
            (175e6, 175e6, 522e6)
        ],
        "Attack Boost": [
            (31e6, 31e6, 91e6), (53e6, 53e6, 158e6), (53e6, 53e6, 158e6),
            (74e6, 74e6, 221e6), (74e6, 74e6, 221e6), (96e6, 96e6, 287e6),
            (96e6, 96e6, 287e6), (134e6, 134e6, 403e6), (134e6, 134e6, 403e6),
            (175e6, 175e6, 522e6)
        ],
        "Defense Boost": [
            (31e6, 31e6, 91e6), (53e6, 53e6, 158e6), (53e6, 53e6, 158e6),
            (74e6, 74e6, 221e6), (74e6, 74e6, 221e6), (96e6, 96e6, 287e6),
            (96e6, 96e6, 287e6), (134e6, 134e6, 403e6), (134e6, 134e6, 403e6),
            (175e6, 175e6, 522e6)
        ],
        "Unit X": [(187e6, 187e6, 560e6)]
    }

    total_iron = total_bread = total_gold = 0
    breakdown_rows = []

    for tech, level in levels.items():
        if tech == "Unit X":
            if level == "Researched":
                continue
            cost = cost_data[tech][0]
            total_iron += cost[0]
            total_bread += cost[1]
            total_gold += cost[2]
            breakdown_rows.append((tech, *cost))
        else:
            current_level = int(level)
            for idx in range(current_level, 10):
                cost = cost_data[tech][idx]
                total_iron += cost[0]
                total_bread += cost[1]
                total_gold += cost[2]
                breakdown_rows.append((f"{tech} {idx + 1}", *cost))

    def format_number(n):
        return f"{n/1e9:.1f}G" if n >= 1e9 else f"{n/1e6:.1f}M"

    st.subheader("Total Resources Needed")
    st.markdown(f"- 🪙 Iron: **{format_number(total_iron)}**")
    st.markdown(f"- 🍞 Bread: **{format_number(total_bread)}**")
    st.markdown(f"- 🪙 Gold: **{format_number(total_gold)}**")

    st.subheader("Research Cost Breakdown")
    for row in breakdown_rows:
        tech, iron, bread, gold = row
        st.markdown(f"- **{tech}** → 🪙 {format_number(iron)}, 🍞 {format_number(bread)}, 🪙 {format_number(gold)}")

# ----------------- Main App Layout -------------------
tab1, tab2 = st.tabs(["🚂 Train Calculator", "🪖 T10 Calculator"])
with tab1:
    render_train_calculator()
with tab2:
    render_t10_calculator()
