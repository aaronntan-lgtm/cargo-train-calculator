
import streamlit as st

st.set_page_config(page_title="Last War Tools Suite")

# =================== Language Setup ===================
languages = {
    "English": "en",
    "Tiếng Việt": "vi",
    "繁體中文": "zh"
}

lang_choice = st.selectbox("🌐 Select Language / Chọn ngôn ngữ / 選擇語言", list(languages.keys()))
lang = languages[lang_choice]

# =================== Localized Text ===================
text = {
    "train_title": {
        "en": "🚂 Best Cargo Train Calculator",
        "vi": "🚂 Trình tính khoang tàu tốt nhất",
        "zh": "🚂 最佳貨運列車計算器"
    },
    "train_intro": {
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
    "t10_title": {
        "en": "🪖 T10 Research Calculator",
        "vi": "🪖 Trình tính nghiên cứu T10",
        "zh": "🪖 T10 研究計算器"
    }
}

# =================== T10 Data and Functions ===================
t10_data = {
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
        (175_000_000, 175_000_000, 522_000_000)
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
        (175_000_000, 175_000_000, 522_000_000)
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
        (175_000_000, 175_000_000, 522_000_000)
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
        (175_000_000, 175_000_000, 522_000_000)
    ],
    "Unit X": (187_000_000, 187_000_000, 560_000_000)
}

def format_number(n):
    if n >= 1_000_000_000:
        return f"{n / 1_000_000_000:.1f}G"
    elif n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    return str(n)
