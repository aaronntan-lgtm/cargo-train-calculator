
# --- Streamlit App Code for Mega Express Train and T10 Grind Calculators ---

import streamlit as st

# Set page config
st.set_page_config(page_title="Last War Calculators", layout="centered")

# Language selection (at top)
languages = {
    "English": "en",
    "Tiếng Việt": "vi",
    "繁體中文": "zh"
}
lang_choice = st.selectbox("🌐 Select Language / Chọn ngôn ngữ / 選擇語言", list(languages.keys()))
lang = languages[lang_choice]

# Localized text
text = {
    "train_title": {
        "en": "🚂 Mega Express Train",
        "vi": "🚂 Tàu tốc hành Mega",
        "zh": "🚂 超級特快列車"
    },
    "train_intro": {
        "en": "Choose the best cabin to queue for to maximize long-term rewards.",
        "vi": "Chọn khoang tốt nhất để xếp hàng nhằm tối đa hóa phần thưởng lâu dài.",
        "zh": "選擇最佳車廂排隊以最大化長期獎勵。"
    },
    "train_input_header": {
        "en": "📥 Input Queue Sizes",
        "vi": "📥 Nhập số hàng chờ",
        "zh": "📥 輸入排隊人數"
    },
    "input_label": {
        "en": "Cabin {name}",
        "vi": "Khoang {name}",
        "zh": "車廂 {name}"
    },
    "train_ranking_header": {
        "en": "📊 Cabin Rankings by EV",
        "vi": "📊 Xếp hạng khoang theo EV",
        "zh": "📊 根據 EV 排名的車廂"
    },
    "ev_explainer": {
        "en": "What is EV? Expected Value (EV) estimates your average gain over time. A higher EV means a better long-term choice.",
        "vi": "EV là gì? Giá trị kỳ vọng (EV) ước tính mức lợi trung bình theo thời gian. EV càng cao thì lựa chọn càng tốt.",
        "zh": "什麼是 EV？期望值 (EV) 表示你長期平均能獲得的收益。EV 越高越好。"
    },
    "t10_title": {
        "en": "🪖 T10 Grind",
        "vi": "🪖 Cày T10",
        "zh": "🪖 T10 肝法"
    },
    "t10_intro": {
        "en": "Calculate the total resources needed to complete your T10 research.",
        "vi": "Tính tổng tài nguyên cần thiết để hoàn thành nghiên cứu T10.",
        "zh": "計算完成 T10 研究所需的總資源。"
    },
    "total_cost_header": {
        "en": "📦 Total Resources Needed",
        "vi": "📦 Tổng tài nguyên cần",
        "zh": "📦 所需總資源"
    },
    "research_cost_breakdown": {
        "en": "🔍 Research Cost Breakdown",
        "vi": "🔍 Chi tiết chi phí nghiên cứu",
        "zh": "🔍 研究成本明細"
    },
    "tech_level_label": {
        "en": "{name} Current Level",
        "vi": "{name} Cấp hiện tại",
        "zh": "{name} 當前等級"
    }
}

# === Mega Express Train Calculator ===
st.title(text["train_title"][lang])
st.markdown(text["train_intro"][lang])
st.subheader(text["train_input_header"][lang])

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

# Calculate EVs
ev_list = []
for name, data in cabins.items():
    ev = calculate_ev(data['queue'], data['value'])
    cabins[name]['ev'] = ev
    ev_list.append((name, ev))

ev_list.sort(key=lambda x: -x[1])

# Display rankings
st.subheader(text["train_ranking_header"][lang])
st.markdown(text["ev_explainer"][lang])
for rank, (name, ev) in enumerate(ev_list, start=1):
    if cabins[name]['queue'] == 0:
        st.markdown(f"**{rank}. Cabin {name} — (Please select number of players in the queue)**")
    elif ev == float('inf'):
        st.markdown(f"**{rank}. Cabin {name} — 100% chance of entry**")
    else:
        st.markdown(f"**{rank}. Cabin {name} — EV = {ev:.2f}**")

# === T10 Grind Calculator ===
st.title(text["t10_title"][lang])
st.markdown(text["t10_intro"][lang])

# Define research paths
research_paths = {
    "Advanced Protection": 10,
    "HP Boost": 10,
    "Attack Boost": 10,
    "Defense Boost": 10,
}

# Input levels
levels = {}
for tech, max_level in research_paths.items():
    label = text["tech_level_label"][lang].format(name=tech)
    levels[tech] = st.selectbox(label, list(range(0, max_level + 1)), index=0,
                                format_func=lambda x: "Max" if x == max_level else x,
                                key=tech)

# Unit X is only added after all research complete
include_unit_x = all(lvl == 10 for lvl in levels.values())

# Define costs
cost_data = {
    "Advanced Protection": [(31, 31, 91), (53, 53, 158), (53, 53, 158), (74, 74, 221), (74, 74, 221),
                            (96, 96, 287), (96, 96, 287), (134, 134, 403), (134, 134, 403), (175, 175, 522)],
    "HP Boost": [(31, 31, 91), (53, 53, 158), (53, 53, 158), (74, 74, 221), (74, 74, 221),
                 (96, 96, 287), (96, 96, 287), (134, 134, 403), (134, 134, 403), (175, 175, 522)],
    "Attack Boost": [(31, 31, 91), (53, 53, 158), (53, 53, 158), (74, 74, 221), (74, 74, 221),
                     (96, 96, 287), (96, 96, 287), (134, 134, 403), (134, 134, 403), (175, 175, 522)],
    "Defense Boost": [(31, 31, 91), (53, 53, 158), (53, 53, 158), (74, 74, 221), (74, 74, 221),
                      (96, 96, 287), (96, 96, 287), (134, 134, 403), (134, 134, 403), (175, 175, 522)],
    "Unit X": [(187, 187, 560)]
}

def format_number(n):
    if n >= 1_000:
        return f"{n/1_000:.1f}G"
    return f"{n:.1f}M"

# Calculate costs
total_iron = total_bread = total_gold = 0
breakdown = []

for tech, level in levels.items():
    costs = cost_data[tech][:level]
    for i, (iron, bread, gold) in enumerate(costs, start=1):
        total_iron += iron
        total_bread += bread
        total_gold += gold
        breakdown.append((f"{tech} {i}", iron, bread, gold))

if include_unit_x:
    ux = cost_data["Unit X"][0]
    total_iron += ux[0]
    total_bread += ux[1]
    total_gold += ux[2]
    breakdown.append(("Unit X", *ux))

# Total Resources
st.subheader(f"📦 {text['total_cost_header'][lang]}")
st.markdown(f"- Iron: **{format_number(total_iron)}**")
st.markdown(f"- Bread: **{format_number(total_bread)}**")
st.markdown(f"- Gold: **{format_number(total_gold)}**")

# Breakdown Table
st.subheader(f"🔍 {text['research_cost_breakdown'][lang]}")
import pandas as pd
df = pd.DataFrame(breakdown, columns=["Item", "Iron", "Bread", "Gold"])
df["Iron"] = df["Iron"].apply(lambda x: format_number(x))
df["Bread"] = df["Bread"].apply(lambda x: format_number(x))
df["Gold"] = df["Gold"].apply(lambda x: format_number(x))
st.dataframe(df, use_container_width=True)
