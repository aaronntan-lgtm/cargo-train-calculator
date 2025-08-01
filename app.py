import streamlit as st

# Set up the page title and layout
st.set_page_config(page_title="Last War Calculators", layout="centered")

# Create custom tabs using HTML and CSS
tabs = ['Arms Race Calculator', 'T10 Calculator', 'Train Calculator']

# Custom CSS for tabs
tab_css = """
    <style>
    .tabs {
        display: flex;
        cursor: pointer;
        background-color: #f1f1f1;
        border: 1px solid #ccc;
        margin-bottom: 1rem;
    }
    .tabs div {
        padding: 10px 20px;
        text-align: center;
        border-right: 1px solid #ccc;
        flex: 1;
    }
    .tabs div:last-child {
        border-right: none;
    }
    .tabs div.active {
        background-color: #4CAF50;
        color: white;
    }
    </style>
"""

# Inject the custom CSS into the Streamlit app
st.markdown(tab_css, unsafe_allow_html=True)

# Create a container for the tabs
tab_selection = st.selectbox("Choose a calculator", tabs, index=0)

# Function to simulate the Excel-like tab layout
def display_tabs(selected_tab):
    if selected_tab == 'Arms Race Calculator':
        st.title("Arms Race Calculator")
        # Add your Arms Race calculator code here
        st.write("This is the Arms Race Calculator. Add your code here.")
        
    elif selected_tab == 'T10 Calculator':
        st.title("T10 Calculator")
        # Add your T10 calculator code here
        st.write("This is the T10 Calculator. Add your code here.")
        
    elif selected_tab == 'Train Calculator':
        st.title("Best Cargo Train Calculator")
        # Add your Train calculator code here
        st.write("This is the Train Calculator. Add your code here.")

# Call the function to display the selected tab content
display_tabs(tab_selection)
