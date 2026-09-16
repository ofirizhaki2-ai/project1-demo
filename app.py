import streamlit as st

st.title("האפליקציה שלי")

st.subheader("ברוכים הבאים לאפליקציה!")

name = st.text_input("מה השם שלך?")
st.write("שלום ",(name),"!")

age = st.number_input("בן כמה אתה?", min_value=0, max_value=120)
st.write("נשארו לך ",(18 - age) ,"שנים עד גיל 18")

if st.button("לחץ כאן"):
    st.success("הכפתור נלחץ בהצלחה!")



st.title("Fortnite Stats")

st.subheader("בדקו כמה ניצחונות יש לכם בפורטנייט")

wins = st.number_input("כמה ניצחונות יש לך?", min_value=0)

st.write("כל הכבוד! יש לך ",(wins)," ניצחונות בפורטנייט!")

if wins >= 10:
    st.success("יש לך כבר הרבה ניצחונות!")
else:
    st.info("תמשיך לשחק ותנסה להגיע ל-10 ניצחונות!")

if st.button("בדוק את הסטטיסטיקה"):
    st.success(f"הסטטיסטיקה שלך: {wins} ניצחונות")

