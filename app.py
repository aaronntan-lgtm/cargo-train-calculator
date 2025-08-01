import streamlit as st
import pandas as pd

st.set_page_config(page_title="Last War Calculators")

# Custom CSS for green dropdown styling in train tab
st.markdown("""
    <style>
    div[data-baseweb="select"] > div {
        border-color: #28a745 !important;
        box-shadow: 0 0 0 1px #28a745 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Language options ---
languages = {
    "English": "en",
    "Tiếng Việt": "vi",
    "繁體中文": "zh"
}

# Tabs
tab = st.tabs(["Best Cargo Train Calculator", "T10 Calculator"])

### --- Tab 1: Best Cargo Train Calculator ---
with tab[0]:
    lang_choice = st.selectbox("🌐 Select Language / Chọn ngôn ngữ / 選擇語言", list(languages.keys()))
    lang = languages[lang_choice]

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

    ev_list.sort(key=lambda x: (x[1] is None, -(x[1] or 0)))

    st.subheader(text["ranking_header"][lang])
    st.markdown(text["ev_description"][lang])

    for rank, (name, ev) in enumerate(ev_list, start=1):
        if ev is None:
            st.markdown(f"**{rank}. Cabin {name} — (Please select number of players in the queue)**")
        else:
            st.markdown(f"**{rank}. Cabin {name} — EV = {ev:.2f}**")

### --- Tab 2: T10 Calculator (Arms Race) ---
with tab[1]:
    st.title("T10 Calculator")

    st.markdown("""
    This calculator helps estimate the total Iron, Bread, and Gold costs needed to reach your desired research levels in the Arms Race tech tree.
    """)

    # Research tech list in order
    techs = [
        ("HP Boost 10", 175, 175, 522),
        ("Attack Boost 7", 96, 96, 287),
        ("Attack Boost 8", 134, 134, 403),
        ("Attack Boost 9", 134, 134, 403),
        ("Attack Boost 10", 175, 175, 522),
        ("Defense Boost 6", 96, 96, 287),
        ("Defense Boost 7", 96, 96, 287),
        ("Defense Boost 8", 134, 134, 403),
        ("Defense Boost 9", 134, 134, 403),
        ("Defense Boost 10", 175, 175, 522),
        ("Unit X", 187, 187, 560),
    ]

    # Current level inputs for each tech (except Unit X which can only be done if all others completed)
    st.subheader("Set current research level for each tech (0 = not researched)")

    current_levels = {}
    max_level = 1  # Each tech is either done or not done here (binary)

    for tech_name, iron_cost, bread_cost, gold_cost in techs[:-1]:  # skip Unit X for now
        current_levels[tech_name] = st.slider(f"{tech_name}", 0, max_level, 0)

    # Check if all techs done except Unit X
    all_done_except_unitx = all(level == max_level for level in current_levels.values())

    unitx_done = st.checkbox("Unit X research completed", value=False)

    # Calculate total remaining cost
    total_iron = 0
    total_bread = 0
    total_gold = 0

    for tech_name, iron_cost, bread_cost, gold_cost in techs[:-1]:
        if current_levels[tech_name] < max_level:
            total_iron += iron_cost
            total_bread += bread_cost
            total_gold += gold_cost

    # Unit X can only be researched if others completed
    if all_done_except_unitx and not unitx_done:
        total_iron += techs[-1][1]
        total_bread += techs[-1][2]
        total_gold += techs[-1][3]

    # Show total costs
    st.subheader("Total Remaining Cost to Research")
    st.write(f"Iron: {total_iron}")
    st.write(f"Bread: {total_bread}")
    st.write(f"Gold: {total_gold}")

    # Bonus: Show full cost table for reference
    st.subheader("Full Research Cost Table")
    df = pd.DataFrame(techs, columns=["Research", "Iron", "Bread", "Gold"])
    st.dataframe(df)
