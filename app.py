
import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Last War Tools", layout="centered")

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
    "mega_train_title": {
        "en": "🚂 Mega Express Train Calculator",
        "vi": "🚂 Trình tính Mega Express Train",
        "zh": "🚂 Mega Express 火車計算器"
    },
    "train_intro": {
        "en": "Choose the best cabin based on queue size.",
        "vi": "Chọn khoang tốt nhất dựa trên số người xếp hàng.",
        "zh": "根據排隊人數選擇最佳車廂。"
    },
    "input_label": {
        "en": "Cabin {name} (number of players in queue)",
        "vi": "Khoang {name} (số người xếp hàng)",
        "zh": "車廂 {name}（排隊人數）"
    },
    "ranking_header": {
        "en": "📊 Cabin Rankings by EV",
        "vi": "📊 Xếp hạng các khoang theo EV",
        "zh": "📊 車廂 EV 排名"
    },
    "ev_description": {
        "en": "What is EV? Expected Value (EV) estimates your average gain over time. A higher EV means a better long-term choice.",
        "vi": "EV là gì? Giá trị kỳ vọng (EV) ước tính lợi ích trung bình. EV càng cao càng tốt về lâu dài.",
        "zh": "什麼是 EV？期望值 (EV) 估算長期平均收益。EV 越高越好。"
    },
    "t10_title": {
        "en": "🪖 T10 Grind Calculator",
        "vi": "🪖 Trình tính T10 Grind",
        "zh": "🪖 T10 計算器"
    },
    "t10_header": {
        "en": "Advanced Protection Current Level",
        "vi": "Cấp hiện tại của Advanced Protection",
        "zh": "Advanced Protection 當前等級"
    },
    "total_cost_header": {
        "en": "Total Resources Needed",
        "vi": "Tổng tài nguyên cần thiết",
        "zh": "所需總資源"
    },
    "breakdown_header": {
        "en": "Research Cost Breakdown",
        "vi": "Chi tiết chi phí nghiên cứu",
        "zh": "研究成本明細"
    }
}

# Mega Train Calculator
st.title(text["mega_train_title"][lang])
st.markdown(text["train_intro"][lang])

st.subheader("📥 " + text["input_label"][lang].format(name=""))

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
