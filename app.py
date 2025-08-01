
import streamlit as st

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
text_train = {
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

# Tabs
tab1, tab2 = st.tabs(["🪖 T10 Grind", "🚂 Mega Express Train"])

# T10 Calculator Tab
with tab1:
    st.markdown("## 🪖 T10 Grind")
    st.markdown("Coming soon... (previous code inserted here by script)")

# Train Calculator Tab
with tab2:
    st.title(text_train["title"][lang])
    st.markdown(text_train["intro"][lang])

    # Input section
    st.subheader(text_train["input_header"][lang])
    queue_a = st.number_input(text_train["input_label"][lang].format(name="A"), min_value=0, value=11)
    queue_b = st.number_input(text_train["input_label"][lang].format(name="B"), min_value=0, value=9)
    queue_c = st.number_input(text_train["input_label"][lang].format(name="C"), min_value=0, value=13)
    queue_d = st.number_input(text_train["input_label"][lang].format(name="D"), min_value=0, value=22)

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

    st.subheader(text_train["ranking_header"][lang])
    for rank, (name, ev) in enumerate(ev_list, start=1):
        if ev == float('inf'):
            st.markdown(f"**{rank}. Cabin {name} — 100% chance of entry**")
        else:
            st.markdown(f"**{rank}. Cabin {name} — EV = {ev:.2f}**")

    st.markdown("---")
    st.markdown(text_train["ev_description"][lang])
