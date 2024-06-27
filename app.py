import streamlit as st

# Initialize session state
if 'mining' not in st.session_state:
    st.session_state.mining = 1
if 'woodcutting' not in st.session_state:
    st.session_state.woodcutting = 1

def level_up(skill):
    if st.session_state[skill] < 100:
        st.session_state[skill] += 1

st.title("Simple RPG Game")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Mining")
    st.write(f"Current level: {st.session_state.mining}")
    if st.button("Mine", key="mine"):
        level_up('mining')
    
    if st.session_state.mining < 10:
        st.write("You can mine copper ore.")
    else:
        st.write("You can mine copper and silver ore.")

with col2:
    st.subheader("Woodcutting")
    st.write(f"Current level: {st.session_state.woodcutting}")
    if st.button("Chop", key="chop"):
        level_up('woodcutting')
    
    if st.session_state.woodcutting < 10:
        st.write("You can chop normal trees.")
    else:
        st.write("You can chop normal and oak trees.")