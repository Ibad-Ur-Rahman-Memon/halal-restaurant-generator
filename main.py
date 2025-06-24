import streamlit as st
import langchain_helper

# ----------------- Page Configuration -----------------
st.set_page_config(page_title="Halal Restaurant Name Generator", page_icon="🍽️")
st.title("🍛 Halal Restaurant Name Generator")

st.markdown("""
Welcome to the Halal Restaurant Generator powered by AI! 🌍  
Select an Islamic country from the sidebar and get an AI-generated unique restaurant name along with a traditional Halal menu.  
""")

# ----------------- Sidebar: Islamic Countries -----------------
st.sidebar.header("🌐 Choose a Country")
islamic_countries = [
    "Pakistan", "Turkey", "Indonesia", "Saudi Arabia", "Morocco",
    "Egypt", "Malaysia", "Iran", "Iraq", "Bangladesh", "Algeria",
    "Qatar", "Jordan", "United Arab Emirates", "Afghanistan"
]
selected_country = st.sidebar.selectbox("Select an Islamic Country", islamic_countries)

# ----------------- Generate Restaurant Name & Menu -----------------
if selected_country:
    st.subheader(f"🕌 Inspired by: **{selected_country}**")

    response = langchain_helper.generate_restaurant_name_and_items(selected_country)

    restaurant_name = response.get("restaurant_name", "Unnamed Halal Bistro").strip()
    menu_items = response.get("menu_items", "").strip().split(",")

    st.success(f"🏷️ **Restaurant Name**: {restaurant_name}")
    st.markdown("### 🧾 Menu Highlights:")
    for item in menu_items:
        st.write(f"• {item.strip()}")
else:
    st.warning("👈 Please select a country from the sidebar to get started.")
