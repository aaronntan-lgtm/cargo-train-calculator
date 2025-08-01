import streamlit as st
import pandas as pd

st.set_page_config(page_title="Last War Calculators", layout="centered")

# Language bar on top
lang_options = {"English": "en", "Tiếng Việt": "vi", "繁體中文": "zh"}
lang_choice = st.selectbox("🌐 Select Language / Chọn ngôn ngữ / 選擇語言", list(lang_options.keys()))
lang = lang_options[lang_choice]

# Text dictionary
text = {
    "mega_title": {"en": "🚂 Mega Express Train", "vi": "🚂 Tàu siêu tốc Mega", "zh": "🚂 超級快車"},
    "t10_title": {"en": "🪖 T10 Grind", "vi": "🪖 Hành trình T10", "zh": "🪖 T10 鍛鍊"},
    "ev_intro": {
        "en": "**What is EV?** Expected Value (EV) estimates your average gain over time. A higher EV means a better long-term choice.",
        "vi": "**EV là gì?** EV (Giá trị kỳ vọng) ước lượng lợi ích trung bình bạn nhận được theo thời gian. EV càng cao thì lựa chọn càng tốt.",
        "zh": "**什麼是 EV？** EV（期望值）估計你隨時間獲得的平均收益。EV 越高，長期效果越好。"
    },
    "train_intro": {
        "en": "Select your best cabin based on current queue sizes.",
        "vi": "Chọn khoang tốt nhất dựa trên số người xếp hàng hiện tại.",
        "zh": "根據目前排隊人數選擇最佳車廂。"
    },
    "t10_intro": {
        "en": "Estimate how much Iron, Bread, and Gold you need to unlock T10.",
        "vi": "Ước tính số Sắt, Bánh mì và Vàng bạn cần để mở khóa T10.",
        "zh": "估算解鎖 T10 所需的鐵、麵包和黃金數量。"
    },
    "input_queue": {
        "en": "Enter the number of players in queue for Cabin {}",
        "vi": "Nhập số người xếp hàng ở Khoang {}",
        "zh": "輸入車廂 {} 的排隊人數"
    },
    "ranking_header": {"en": "📊 Cabin Rankings by EV", "vi": "📊 Xếp hạng khoang theo EV", "zh": "📊 根據 EV 排名的車廂"},
    "total_cost": {"en": "💰 Total Resources Needed", "vi": "💰 Tổng tài nguyên cần thiết", "zh": "💰 所需資源總量"},
    "summary_header": {"en": "📘 Research Cost Breakdown", "vi": "📘 Chi tiết chi phí nghiên cứu", "zh": "📘 研究成本明細"},
    "unit_x_info": {
        "en": "🔒 Unit X will only be unlocked after completing all other techs.",
        "vi": "🔒 Unit X chỉ có thể nghiên cứu sau khi hoàn thành các công nghệ khác.",
        "zh": "🔒 完成所有其他科技後才能解鎖 Unit X。"
    }
}

tab1, tab2 = st.tabs([text["mega_title"][lang], text["t10_title"][lang]])

# --- Mega Express Train ---
with tab1:
    st.title(text["mega_title"][lang])
    st.markdown(text["train_intro"][lang])
    st.subheader(text["ranking_header"][lang])
    st.markdown(text["ev_intro"][lang])

    values = {"A": 2, "B": 1, "C": 1, "D": 4}
    queues = {}
    for cabin in ["A", "B", "C", "D"]:
        queues[cabin] = st.number_input(text["input_queue"][lang].format(cabin), min_value=0, value=0)

    def calc_ev(q, val):
        return float('inf') if q == 0 else (5 / q) * val

    evs = [(cabin, calc_ev(queues[cabin], val)) for cabin, val in values.items()]
    evs.sort(key=lambda x: -x[1])

    for i, (cabin, ev) in enumerate(evs, 1):
        if ev == float('inf') and queues[cabin] == 0:
            st.markdown(f"**{i}. Cabin {cabin} — (Please select number of players in the queue)**")
        else:
            st.markdown(f"**{i}. Cabin {cabin} — EV = {ev:.2f}**")

# --- T10 Grind ---
with tab2:
    st.title(text["t10_title"][lang])
    st.markdown(text["t10_intro"][lang])

    tech_tree = {
        "Advanced Protection Current Level": 10,
        "HP Boost Current Level": 10,
        "Attack Boost Current Level": 10,
        "Defense Boost Current Level": 10
    }

    levels = {}
    for tech, max_level in tech_tree.items():
        def format_option(x, max_level=max_level):
            return "Max" if x == max_level else x
        levels[tech] = st.selectbox(f"{tech}", list(range(0, max_level + 1)), index=0,
                                    format_func=format_option, key=tech)

    st.markdown(text["unit_x_info"][lang])

    research_data = {
        "Advanced Protection Current Level": ([31,53,53,74,74,96,96,134,134,175],)*3,
        "HP Boost Current Level": ([31,53,53,74,74,96,96,134,134,175],)*3,
        "Attack Boost Current Level": ([31,53,53,74,74,96,96,134,134,175],)*3,
        "Defense Boost Current Level": ([31,53,53,74,74,96,96,134,134,175],)*3,
        "Unit X": ([187], [187], [560])
    }

    total_iron = total_bread = total_gold = 0
    rows = []

    for tech, (iron_list, bread_list, gold_list) in research_data.items():
        if tech == "Unit X":
            if all(levels[t] == 10 for t in tech_tree):
                total_iron += iron_list[0]
                total_bread += bread_list[0]
                total_gold += gold_list[0]
                rows.append({"Item": "Unit X", "Iron": f"{iron_list[0]/1000:.1f}M", "Bread": f"{bread_list[0]/1000:.1f}M", "Gold": f"{gold_list[0]/1000:.1f}M"})
            continue

        current_lvl = levels[tech]
        for i in range(current_lvl, 10):
            total_iron += iron_list[i]
            total_bread += bread_list[i]
            total_gold += gold_list[i]
            rows.append({
                "Item": f"{tech.replace(' Current Level', '')} {i+1}",
                "Iron": f"{iron_list[i]/1000:.1f}M",
                "Bread": f"{bread_list[i]/1000:.1f}M",
                "Gold": f"{gold_list[i]/1000:.1f}M"
            })

    # Total cost above summary
    st.subheader(text["total_cost"][lang])
    st.write(f"**Iron:** {total_iron/1000:.1f}M")
    st.write(f"**Bread:** {total_bread/1000:.1f}M")
    st.write(f"**Gold:** {total_gold/1000:.1f}M")

    st.subheader(text["summary_header"][lang])
    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True)
