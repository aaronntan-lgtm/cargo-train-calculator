
import streamlit as st

st.set_page_config(page_title="Last War Calculators", layout="centered")

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
        "train": {
            "en": "🚂 Mega Express Train",
            "vi": "🚂 Tàu tốc hành",
            "zh": "🚂 特快列車"
        },
        "t10": {
            "en": "🪖 T10 Grind",
            "vi": "🪖 Cày T10",
            "zh": "🪖 T10 肝帝"
        },
    },
    "train_intro": {
        "en": "Select the best cabin to queue for maximum rewards.",
        "vi": "Chọn khoang tốt nhất để nhận phần thưởng tối đa.",
        "zh": "選擇最佳車廂以獲得最大獎勵。"
    },
    "ev_description": {
        "en": "**What is EV?** Expected Value (EV) estimates your average gain over time. A higher EV means a better long-term choice.",
        "vi": "**EV là gì?** Giá trị kỳ vọng (EV) ước tính lợi nhuận trung bình của bạn theo thời gian. EV càng cao thì lựa chọn càng tốt.",
        "zh": "**什麼是 EV？** 期望值 (EV) 表示你長期平均能獲得的收益。EV 越高，長期表現越好。"
    },
    "input_header": {
        "en": "📥 Input Queue Sizes for Each Cabin",
        "vi": "📥 Nhập số người xếp hàng tại mỗi khoang",
        "zh": "📥 輸入每個車廂的排隊人數"
    },
    "input_label": {
        "en": "Cabin {name} (Enter number in queue)",
        "vi": "Khoang {name} (Nhập số người xếp hàng)",
        "zh": "車廂 {name}（請輸入排隊人數）"
    },
    "ranking_header": {
        "en": "📊 Cabin Rankings by EV",
        "vi": "📊 Xếp hạng khoang theo EV",
        "zh": "📊 根據 EV 排名的車廂"
    },
    "t10_header": {
        "en": "🪖 T10 Grind",
        "vi": "🪖 Cày T10",
        "zh": "🪖 T10 肝帝"
    },
    "level_header": {
        "en": "Current Level",
        "vi": "Cấp hiện tại",
        "zh": "目前等級"
    },
    "total_cost": {
        "en": "Total Resources Needed",
        "vi": "Tổng tài nguyên cần thiết",
        "zh": "所需資源總數"
    },
    "summary_header": {
        "en": "Research Cost Breakdown",
        "vi": "Chi tiết chi phí nghiên cứu",
        "zh": "研究成本明細"
    }
}

tab1, tab2 = st.tabs([text["tabs"]["train"][lang], text["tabs"]["t10"][lang]])

with tab1:
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
        cabins[name]['ev'] = ev
        ev_list.append((name, ev))

    ev_list.sort(key=lambda x: -x[1])

    st.subheader(text["ranking_header"][lang])
    st.markdown(text["ev_description"][lang])
    for rank, (name, ev) in enumerate(ev_list, start=1):
        if ev == float('inf'):
            st.markdown(f"**{rank}. Cabin {name} — (Please select number of players in the queue)**")
        else:
            st.markdown(f"**{rank}. Cabin {name} — EV = {ev:.2f}**")

with tab2:
    st.markdown(f"### {text['t10_header'][lang]}")
    st.write("Select your current level for each tech tree below to see the remaining resources needed.")

    tech_trees = {
        "Advanced Protection": 10,
        "HP Boost": 10,
        "Attack Boost": 10,
        "Defense Boost": 10
    }

    # Define cost table
    cost_data = {
        "Advanced Protection": [
            (31, 31, 91), (53, 53, 158), (53, 53, 158), (74, 74, 221),
            (74, 74, 221), (96, 96, 287), (96, 96, 287), (134, 134, 403),
            (134, 134, 403), (175, 175, 522)
        ],
        "HP Boost": [
            (31, 31, 91), (53, 53, 158), (53, 53, 158), (74, 74, 221),
            (74, 74, 221), (96, 96, 287), (96, 96, 287), (134, 134, 403),
            (134, 134, 403), (175, 175, 522)
        ],
        "Attack Boost": [
            (31, 31, 91), (53, 53, 158), (53, 53, 158), (74, 74, 221),
            (74, 74, 221), (96, 96, 287), (96, 96, 287), (134, 134, 403),
            (134, 134, 403), (175, 175, 522)
        ],
        "Defense Boost": [
            (31, 31, 91), (53, 53, 158), (53, 53, 158), (74, 74, 221),
            (74, 74, 221), (96, 96, 287), (96, 96, 287), (134, 134, 403),
            (134, 134, 403), (175, 175, 522)
        ],
        "Unit X": [
            (187, 187, 560)
        ]
    }

    def format_number(n):
        if n >= 1_000:
            return f"{n / 1000:.1f}G"
        else:
            return f"{n:.1f}M"

    total_iron = total_bread = total_gold = 0
    levels = {}

    for tech, max_level in tech_trees.items():
        label = f"{tech} Current Level"
        options = [str(i) for i in range(0, max_level + 1)]
        index = 0
        levels[tech] = int(st.selectbox(label, options, index=index, key=tech))

    # Check if all 4 tech trees are maxed before showing Unit X
    if all(levels[tech] == 10 for tech in tech_trees):
        show_unit_x = True
        levels["Unit X"] = 0
        unit_options = ["0", "Max"]
        unit_selection = st.selectbox("Unit X Research Level", unit_options, index=0, key="unitx")
        if unit_selection == "Max":
            levels["Unit X"] = 1
    else:
        show_unit_x = False

    # Sum costs
    for tech, level in levels.items():
        for step in cost_data[tech][level:]:
            iron, bread, gold = step
            total_iron += iron
            total_bread += bread
            total_gold += gold

    st.subheader(text["total_cost"][lang])
    st.markdown(f"- **Iron:** {format_number(total_iron)}")
    st.markdown(f"- **Bread:** {format_number(total_bread)}")
    st.markdown(f"- **Gold:** {format_number(total_gold)}")

    st.subheader(text["summary_header"][lang])
    st.write("Coming soon: full breakdown table.")

