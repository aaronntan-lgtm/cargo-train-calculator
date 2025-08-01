import streamlit as st

st.set_page_config(page_title="Best Cargo Train Calculator")

# Custom CSS for green dropdown styling
st.markdown("""
    <style>
    div[data-baseweb="select"] > div {
        border-color: #28a745 !important;
        box-shadow: 0 0 0 1px #28a745 !important;
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
    "train_title": {
        "en": "🚂 Mega Express Train",
        "vi": "🚂 Tàu siêu tốc Mega Express",
        "zh": "🚂 超级快车 Mega Express"
    },
    "t10_title": {
        "en": "T10 Grind",
        "vi": "Mài T10",
        "zh": "T10 磨练"
    },
    "train_intro": {
        "en": "Select your best cabin based on current queue sizes. This assumes that Cabin D is the best, followed by Cabin A, and Cabins B & C have equal value.",
        "vi": "Chọn khoang tốt nhất dựa trên số người xếp hàng hiện tại. Khoang D có giá trị cao nhất, tiếp theo là A, còn B và C có giá trị bằng nhau.",
        "zh": "根据目前排队人数选择最佳车厢。车厢 D 为最高价值，其次为 A，B 和 C 价值相同。"
    },
    "ev_description": {
        "en": "**What is EV?** Expected Value (EV) estimates your average gain over time. A higher EV means a better long-term choice.",
        "vi": "**EV là gì?** Giá trị kỳ vọng (EV) ước tính mức lợi trung bình của bạn theo thời gian. EV càng cao thì lựa chọn càng tốt về lâu dài.",
        "zh": "**什么是 EV？** 期望值 (EV) 表示你长期平均能获得的收益。EV 越高，长期表现越好。"
    },
    "input_header": {
        "en": "📥 Input Queue Sizes for Each Cabin",
        "vi": "📥 Nhập số người đang xếp hàng tại mỗi khoang",
        "zh": "📥 输入每个车厢的排队人数"
    },
    "input_label": {
        "en": "Cabin {name} (Enter the number of passengers in the queue here)",
        "vi": "Khoang {name} (Nhập số người xếp hàng tại đây)",
        "zh": "车厢 {name}（请输入排队人数）"
    },
    "ranking_header": {
        "en": "📊 Cabin Rankings by EV",
        "vi": "📊 Xếp hạng các khoang theo EV",
        "zh": "📊 根据 EV 排名的车厢"
    },
    "t10_header": {
        "en": "Select Current Research Levels",
        "vi": "Chọn cấp độ nghiên cứu hiện tại",
        "zh": "选择当前研究等级"
    },
    "resource_total_header": {
        "en": "### Total Research Cost Remaining:",
        "vi": "### Tổng chi phí nghiên cứu còn lại:",
        "zh": "### 剩余研究总成本："
    },
    "resource_labels": {
        "en": ["Iron", "Bread", "Gold"],
        "vi": ["Sắt", "Bánh mì", "Vàng"],
        "zh": ["铁", "面包", "金币"]
    },
    "cabins_no_input": {
        "en": "(Please select number of players in the queue)",
        "vi": "(Vui lòng chọn số người trong hàng đợi)",
        "zh": "(请选择排队人数)"
    }
}

def format_number(num):
    """Format number with M or G suffix"""
    if num >= 1000:
        # Billions
        return f"{num/1000:.1f}G"
    elif num >= 1:
        # Millions
        return f"{num:.1f}M"
    else:
        return str(num)

# Main app tabs
tabs = [
    text["train_title"][lang],
    text["t10_title"][lang]
]

selected_tab = st.tabs(tabs)

with selected_tab[0]:
    # Mega Express Train Calculator
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
            return None  # None to indicate no input yet
        return (5 / queue_size) * cabin_value

    ev_list = []
    for name, data in cabins.items():
        ev = calculate_ev(data['queue'], data['value'])
        cabins[name]['ev'] = ev
        ev_list.append((name, ev))

    ev_list.sort(key=lambda x: (x[1] is not None, x[1]), reverse=True)

    st.subheader(text["ranking_header"][lang])
    st.markdown(text["ev_description"][lang])

    for rank, (name, ev) in enumerate(ev_list, start=1):
        if ev is None:
            st.markdown(f"**{rank}. Cabin {name} — {text['cabins_no_input'][lang]}**")
        else:
            st.markdown(f"**{rank}. Cabin {name} — EV = {ev:.2f}**")

with selected_tab[1]:
    # T10 Grind Calculator
    st.title(text["t10_title"][lang])
    st.subheader(text["t10_header"][lang])

    # Levels for dropdowns - all start at 0 except Advanced Protection now starts at 0
    adv_prot_levels = [str(i) for i in range(0, 11)]
    adv_prot_levels[-1] = "10 (Max)"

    hp_boost_levels = [str(i) for i in range(0, 11)]
    hp_boost_levels[-1] = "10 (Max)"

    atk_boost_levels = [str(i) for i in range(0, 11)]
    atk_boost_levels[-1] = "10 (Max)"

    def_boost_levels = [str(i) for i in range(0, 11)]
    def_boost_levels[-1] = "10 (Max)"

    unit_x_levels = ["0", "1 (Max)"]

    adv_prot = st.selectbox({
        "en": "Advanced Protection Level",
        "vi": "Cấp độ Bảo vệ nâng cao",
        "zh": "高级保护等级"
    }[lang], adv_prot_levels, index=0)

    hp_boost = st.selectbox({
        "en": "HP Boost III Level",
        "vi": "Cấp độ Tăng HP III",
        "zh": "生命提升 III 等级"
    }[lang], hp_boost_levels, index=0)

    atk_boost = st.selectbox({
        "en": "Attack Boost III Level",
        "vi": "Cấp độ Tăng Công III",
        "zh": "攻击提升 III 等级"
    }[lang], atk_boost_levels, index=0)

    def_boost = st.selectbox({
        "en": "Defense Boost III Level",
        "vi": "Cấp độ Tăng Phòng III",
        "zh": "防御提升 III 等级"
    }[lang], def_boost_levels, index=0)

    unit_x = st.selectbox({
        "en": "Unit X Level",
        "vi": "Cấp độ Unit X",
        "zh": "单位 X 等级"
    }[lang], unit_x_levels, index=0)

    def parse_level(level_str):
        return int(level_str.split()[0])

    adv_prot_level = parse_level(adv_prot)
    hp_boost_level = parse_level(hp_boost)
    atk_boost_level = parse_level(atk_boost)
    def_boost_level = parse_level(def_boost)
    unit_x_level = parse_level(unit_x)

    # Original raw costs (no longer divided by 1,000,000 here)
    iron_costs_raw = {
        "Advanced Protection": [0, 175, 175, 175, 175, 175, 175, 175, 175, 175, 175],
        "HP Boost III": [0, 96, 96, 96, 96, 96, 96, 96, 96, 96, 96],
        "Attack Boost III": [0, 96, 134, 134, 134, 175, 175, 175, 175, 175, 175],
        "Defense Boost III": [0, 96, 96, 134, 134, 175, 175, 175, 175, 175, 175],
        "Unit X": [0, 187]
    }
    bread_costs_raw = iron_costs_raw  # same as iron
    gold_costs_raw = {
        "Advanced Protection": [0, 522, 522, 522, 522, 522, 522, 522, 522, 522, 522],
        "HP Boost III": [0, 287, 287, 287, 287, 287, 287, 287, 287, 287, 287],
        "Attack Boost III": [0, 287, 403, 403, 403, 522, 522, 522, 522, 522, 522],
        "Defense Boost III": [0, 287, 287, 403, 403, 522, 522, 522, 522, 522, 522],
        "Unit X": [0, 560]
    }

    def sum_remaining(cost_list, current_level):
        # sum from next level to end
        return sum(cost_list[current_level + 1:])

    iron_total_raw = (
        sum_remaining(iron_costs_raw["Advanced Protection"], adv_prot_level)
        + sum_remaining(iron_costs_raw["HP Boost III"], hp_boost_level)
        + sum_remaining(iron_costs_raw["Attack Boost III"], atk_boost_level)
        + sum_remaining(iron_costs_raw["Defense Boost III"], def_boost_level)
        + sum_remaining(iron_costs_raw["Unit X"], unit_x_level)
    )

    bread_total_raw = (
        sum_remaining(bread_costs_raw["Advanced Protection"], adv_prot_level)
        + sum_remaining(bread_costs_raw["HP Boost III"], hp_boost_level)
        + sum_remaining(bread_costs_raw["Attack Boost III"], atk_boost_level)
        + sum_remaining(bread_costs_raw["Defense Boost III"], def_boost_level)
        + sum_remaining(bread_costs_raw["Unit X"], unit_x_level)
    )

    gold_total_raw = (
        sum_remaining(gold_costs_raw["Advanced Protection"], adv_prot_level)
        + sum_remaining(gold_costs_raw["HP Boost III"], hp_boost_level)
        + sum_remaining(gold_costs_raw["Attack Boost III"], atk_boost_level)
        + sum_remaining(gold_costs_raw["Defense Boost III"], def_boost_level)
        + sum_remaining(gold_costs_raw["Unit X"], unit_x_level)
    )

    # Convert raw totals to millions for display
    iron_total = iron_total_raw / 1_000_000
    bread_total = bread_total_raw / 1_000_000
    gold_total = gold_total_raw / 1_000_000

    st.markdown(text["resource_total_header"][lang])
    resource_labels = text["resource_labels"][lang]

    st.write(f"- {resource_labels[0]}: {format_number(iron_total)}")
    st.write(f"- {resource_labels[1]}: {format_number(bread_total)}")
    st.write(f"- {resource_labels[2]}: {format_number(gold_total)}")
