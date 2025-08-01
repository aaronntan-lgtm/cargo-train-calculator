
import streamlit as st
import pandas as pd

# Set Streamlit page config
st.set_page_config(page_title="Last War Calculators", layout="centered")

# Language selection bar at the top
language = st.selectbox("🌐 Language", ["English", "Tiếng Việt", "繁體中文"])

# Translation dictionaries
translations = {
    "English": {
        "Mega Express Train": "🚆 Mega Express Train",
        "T10 Grind": "🪖 T10 Grind",
        "Players in Queue": "Number of players in the queue",
        "Cabin": "Cabin",
        "Chance": "Chance of entry",
        "EV": "Expected Value (EV)",
        "EV Explanation": "What is EV? Expected Value (EV) estimates your average gain over time. A higher EV means a better long-term choice.",
        "Total Resources Needed": "💰 Total Resources Needed",
        "Research Cost Breakdown": "📘 Research Cost Breakdown"
    },
    "Tiếng Việt": {
        "Mega Express Train": "🚆 Tàu Tốc Hành",
        "T10 Grind": "🪖 Cày T10",
        "Players in Queue": "Số người đang xếp hàng",
        "Cabin": "Toa",
        "Chance": "Tỷ lệ vào",
        "EV": "Giá trị kỳ vọng (EV)",
        "EV Explanation": "EV ước lượng lợi ích trung bình theo thời gian. EV càng cao càng có lợi về lâu dài.",
        "Total Resources Needed": "💰 Tổng Tài Nguyên Cần",
        "Research Cost Breakdown": "📘 Chi Tiết Nghiên Cứu"
    },
    "繁體中文": {
        "Mega Express Train": "🚆 特快列車",
        "T10 Grind": "🪖 T10 升級",
        "Players in Queue": "排隊人數",
        "Cabin": "車廂",
        "Chance": "進入機率",
        "EV": "期望值 (EV)",
        "EV Explanation": "什麼是 EV？EV 估算你長期的平均收益。數值越高代表選擇越有利。",
        "Total Resources Needed": "💰 所需總資源",
        "Research Cost Breakdown": "📘 研究成本明細"
    }
}
t = translations[language]

# Tab layout
tab1, tab2 = st.tabs([t["Mega Express Train"], t["T10 Grind"]])

# ---- Mega Express Train Calculator ----
with tab1:
    st.title(t["Mega Express Train"])

    players = st.number_input(t["Players in Queue"], min_value=0, step=1)

    st.markdown("## 📊 Cabin Rankings by EV")
    st.caption(t["EV Explanation"])

    data = []
    for cabin, slots in zip(["A", "B", "C"], [1, 2, 3]):
        chance = f"{min(100, round(slots / players * 100, 1))}%" if players else f"({t['Players in Queue']})"
        ev = round(slots / players, 3) if players else "-"
        data.append((f"{t['Cabin']} {cabin}", chance, ev))

    df = pd.DataFrame(data, columns=[t["Cabin"], t["Chance"], t["EV"]])
    st.dataframe(df, use_container_width=True)

# ---- T10 Grind Calculator ----
with tab2:
    st.title(t["T10 Grind"])

    tech_tree = {
        "Advanced Protection": 10,
        "HP Boost": 10,
        "Attack Boost": 10,
        "Defense Boost": 10,
        "Unit X": 1
    }

    st.markdown("## 🧪 Select Current Research Levels")

    levels = {}
    for tech, max_level in tech_tree.items():
        label = f"{tech} Current Level"
        options = [i for i in range(0, max_level + 1)]
        if max_level == 1:
            options = [0, 1]
            format_func = lambda x: "Max" if x == 1 else "0"
        else:
            format_func = lambda x, max_level=max_level: f"{x} (Max)" if x == max_level else str(x)

        levels[tech] = st.selectbox(label, options, index=0, format_func=lambda x, m=max_level: f"{x} (Max)" if x == m else str(x), key=tech)

    # Cost Data
    rows = [
        ("Advanced Protection", [
            (31e6, 31e6, 91e6),
            (53e6, 53e6, 158e6),
            (53e6, 53e6, 158e6),
            (74e6, 74e6, 221e6),
            (74e6, 74e6, 221e6),
            (96e6, 96e6, 287e6),
            (96e6, 96e6, 287e6),
            (134e6, 134e6, 403e6),
            (134e6, 134e6, 403e6),
            (175e6, 175e6, 522e6),
        ]),
        ("HP Boost", [
            (31e6, 31e6, 91e6),
            (53e6, 53e6, 158e6),
            (53e6, 53e6, 158e6),
            (74e6, 74e6, 221e6),
            (74e6, 74e6, 221e6),
            (96e6, 96e6, 287e6),
            (96e6, 96e6, 287e6),
            (134e6, 134e6, 403e6),
            (134e6, 134e6, 403e6),
            (175e6, 175e6, 522e6),
        ]),
        ("Attack Boost", [
            (31e6, 31e6, 91e6),
            (53e6, 53e6, 158e6),
            (53e6, 53e6, 158e6),
            (74e6, 74e6, 221e6),
            (74e6, 74e6, 221e6),
            (96e6, 96e6, 287e6),
            (96e6, 96e6, 287e6),
            (134e6, 134e6, 403e6),
            (134e6, 134e6, 403e6),
            (175e6, 175e6, 522e6),
        ]),
        ("Defense Boost", [
            (31e6, 31e6, 91e6),
            (53e6, 53e6, 158e6),
            (53e6, 53e6, 158e6),
            (74e6, 74e6, 221e6),
            (74e6, 74e6, 221e6),
            (96e6, 96e6, 287e6),
            (96e6, 96e6, 287e6),
            (134e6, 134e6, 403e6),
            (134e6, 134e6, 403e6),
            (175e6, 175e6, 522e6),
        ]),
        ("Unit X", [
            (187e6, 187e6, 560e6),
        ]),
    ]

    total_iron = total_bread = total_gold = 0
    for tech, values in rows:
        current = levels[tech]
        for cost in values[current:]:
            iron, bread, gold = cost
            total_iron += iron
            total_bread += bread
            total_gold += gold

    def fmt(val):
        return f"{val/1e9:.1f}G" if val >= 1e9 else f"{val/1e6:.1f}M"

    st.markdown(f"### {t['Total Resources Needed']}")
    st.write(f"Iron: **{fmt(total_iron)}**")
    st.write(f"Bread: **{fmt(total_bread)}**")
    st.write(f"Gold: **{fmt(total_gold)}**")

    # Show full research table
    st.markdown(f"### {t['Research Cost Breakdown']}")
    flat_rows = []
    for tech, values in rows:
        for i, (iron, bread, gold) in enumerate(values, start=1):
            flat_rows.append((f"{tech} {i}", fmt(iron), fmt(bread), fmt(gold)))

    df2 = pd.DataFrame(flat_rows, columns=["Research", "Iron", "Bread", "Gold"])
    st.dataframe(df2, use_container_width=True)
