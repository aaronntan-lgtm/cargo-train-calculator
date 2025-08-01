
import streamlit as st
import pandas as pd

# Utility function
def format_number(value):
    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.1f}G"
    elif value >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    return str(value)

# Sidebar Language Toggle
lang = st.sidebar.selectbox("🌐 Language", ["English", "Vietnamese", "Traditional Chinese"])

# Tab Layout
tab1, tab2 = st.tabs(["🚂 Mega Express Train", "🪖 T10 Grind"])

# ------------- Mega Express Train (Original) -------------
with tab1:
    st.header("🚂 Mega Express Train")
    num_players = st.number_input("How many players are in the queue?", min_value=0, value=0, step=1)
    train_options = {
        "Cabin A": 1.0,
        "Cabin B": 0.8,
        "Cabin C": 0.6,
        "Cabin D": 0.4,
    }

    if num_players == 0:
        st.write("Cabin A — (Please select number of players in the queue)")
    else:
        st.subheader("📊 Cabin Rankings by EV")
        st.markdown(
            "What is EV? Expected Value (EV) estimates your average gain over time. A higher EV means a better long-term choice."
        )
        ev_results = {k: round(v / (num_players + 1), 4) for k, v in train_options.items()}
        sorted_cabins = sorted(ev_results.items(), key=lambda x: x[1], reverse=True)

        for cabin, ev in sorted_cabins:
            st.write(f"{cabin} — EV: {ev}")

# ------------- T10 Grind Calculator -------------
with tab2:
    st.header("🪖 T10 Grind")
    st.markdown("Select your current level for each tech branch:")

    tech_tree = {
        "Advanced Protection": 10,
        "HP Boost": 10,
        "Attack Boost": 10,
        "Defense Boost": 10,
        "Unit X": 1
    }

    # Full cost data
    cost_data = {
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
            (175_000_000, 175_000_000, 522_000_000),
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
            (175_000_000, 175_000_000, 522_000_000),
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
            (175_000_000, 175_000_000, 522_000_000),
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
            (175_000_000, 175_000_000, 522_000_000),
        ],
        "Unit X": [
            (187_000_000, 187_000_000, 560_000_000),
        ],
    }

    levels = {}
    for tech, max_level in tech_tree.items():
        label = f"{tech} Current Level"
        options = list(range(0, max_level + 1))
        format_func = lambda x: f"{x} (Max)" if x == max_level else str(x)
        levels[tech] = st.selectbox(label, options, index=0, format_func=format_func, key=tech)

    # Calculate remaining research cost
    total_iron = total_bread = total_gold = 0
    rows = []

    for tech, current_level in levels.items():
        for lvl in range(current_level, len(cost_data[tech])):
            iron, bread, gold = cost_data[tech][lvl]
            total_iron += iron
            total_bread += bread
            total_gold += gold
            rows.append({
                "Research": f"{tech} {lvl + 1}",
                "Iron": format_number(iron),
                "Bread": format_number(bread),
                "Gold": format_number(gold),
            })

    st.subheader("📦 Total Resources Needed")
    st.write(f"**Iron:** {format_number(total_iron)}")
    st.write(f"**Bread:** {format_number(total_bread)}")
    st.write(f"**Gold:** {format_number(total_gold)}")

    st.subheader("📊 Research Cost Breakdown")
    if rows:
        df = pd.DataFrame(rows)
        st.dataframe(df, use_container_width=True)
    else:
        st.write("🎉 All research complete!")
