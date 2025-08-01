import streamlit as st

# Enable dark mode by default
st.set_page_config(page_title="Last War Calculators", layout="centered", page_icon="🚂", theme="dark")

# Create a container for the tabs with custom CSS
tabs = ['Arms Race Calculator', 'T10 Calculator', 'Train Calculator']

# Custom CSS for tabs (Excel-style tabs layout in dark mode)
tab_css = """
    <style>
    /* Tabs layout and styling */
    .tabs {
        display: flex;
        cursor: pointer;
        background-color: #333;
        border: 1px solid #444;
        margin-bottom: 1rem;
        font-weight: bold;
        color: #bbb;
    }
    .tabs div {
        padding: 12px 20px;
        text-align: center;
        border-right: 1px solid #444;
        flex: 1;
        color: #bbb;
        transition: background-color 0.3s ease;
        cursor: pointer;
    }
    .tabs div:last-child {
        border-right: none;
    }
    .tabs div:hover {
        background-color: #444;
    }
    .tabs div.active {
        background-color: #4CAF50;
        color: white;
    }

    /* Streamlit's default button color */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }

    /* Fix some styling issues with certain elements in dark mode */
    .stRadio>label, .stSelectbox>label, .stNumberInput>label, .stMarkdown {
        color: white;
    }
    </style>
"""

# Inject the custom CSS into the Streamlit app
st.markdown(tab_css, unsafe_allow_html=True)

# Create the tab navigation
selected_tab = st.radio("Select Calculator", tabs, index=0, horizontal=True)

# Create the content for each tab
def display_tabs(selected_tab):
    if selected_tab == 'Arms Race Calculator':
        st.title("Arms Race Calculator")
        # Add your Arms Race calculator code here
        st.write("This is the Arms Race Calculator. Implement the required code here.")
        
    elif selected_tab == 'T10 Calculator':
        st.title("T10 Calculator")
        # Add your T10 calculator code here
        st.write("This is the T10 Calculator. Implement the required code here.")
        
    elif selected_tab == 'Train Calculator':
        st.title("Best Cargo Train Calculator")

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
                "en": "**What is**
