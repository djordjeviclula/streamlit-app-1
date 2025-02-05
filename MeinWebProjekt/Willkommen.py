import streamlit as st

# Seiten-Konfiguration
st.set_page_config(page_title="👋 Willkommen", page_icon="👋")

# 🎨 Einheitliches Sidebar-Design mit Farbverlauf und dunkler Schrift
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(to bottom, #7C9ED3, #C6DC8B);
        color: black !important;
    }
    [data-testid="stSidebar"] * {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎉 Hauptinhalt der Seite
st.title("👋 Hey, schön, dass du hier bist!")

st.divider()

st.write("Liebes Peopleware-Team, hier habe ich euch ein paar Dinge vorbereitet.")
st.write(
    "Ich hoffe, euch gefällt es, und ich kann damit zeigen, wie viel Spaß ich am Lernen habe. "
    "Gleichzeitig möchte ich meine Begeisterung für IT, Software und digitale Prozesse mit euch teilen!"
)

st.divider()
st.write(
    "Diese gesamte Web-App habe ich mit **Python & Streamlit** erstellt. Weiter unten könnt ihr mehr dazu erfahren.")

st.divider()

# 🖥️ UI Design & Blender
st.subheader("🖥️ UI Design & Blender")
if st.button("➡️ mehr erfahren", use_container_width=True, key="blender"):
    st.switch_page("pages/UI_Design_&_Blender.py")

st.divider()

# ❓ Fragen & Antworten (FAQ)
st.subheader("❓ Fragen & Antworten")
if st.button("➡️ mehr erfahren", use_container_width=True, key="faq"):
    st.switch_page("pages/FAQ.py")

st.divider()

# 📄 Bewerbungsunterlagen
st.subheader("📄 Bewerbungsunterlagen")
if st.button("➡️ mehr erfahren", use_container_width=True, key="bewerbung"):
    st.switch_page("pages/Bewerbung.py")

st.divider()

# 🐍 Python & Streamlit
st.subheader("🐍 Python & Streamlit")
if st.button("➡️ mehr erfahren", use_container_width=True, key="python"):
    st.switch_page("pages/Python_&_Streamlit.py")

st.divider()

# Abschluss
st.write("Danke fürs Vorbeischauen! 😊")