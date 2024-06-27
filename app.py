import streamlit as st

# Initialize session state
if 'state' not in st.session_state:
    st.session_state.state = {
        'mining': 1,
        'woodcutting': 1,
        'inventory': {'copper': 0, 'silver': 0, 'wood': 0, 'oak_wood': 0}
    }

def level_up_and_gather(skill, item):
    st.session_state.state[skill] += 1
    st.session_state.state['inventory'][item] += 1

st.title("Simple RPG Game")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Mining")
    st.write(f"Current level: {st.session_state.state['mining']}")
    
    if st.button("Mine Copper", key="mine_copper"):
        level_up_and_gather('mining', 'copper')
    
    if st.session_state.state['mining'] > 9:
        if st.button("Mine Silver", key="mine_silver"):
            level_up_and_gather('mining', 'silver')
    
    if st.session_state.state['mining'] < 10:
        st.write("You can mine copper ore.")
    else:
        st.write("You can mine copper and silver ore.")

with col2:
    st.subheader("Woodcutting")
    st.write(f"Current level: {st.session_state.state['woodcutting']}")
    
    if st.button("Chop Normal Trees", key="chop_normal"):
        level_up_and_gather('woodcutting', 'wood')
    
    if st.session_state.state['woodcutting'] > 9:
        if st.button("Chop Oak Trees", key="chop_oak"):
            level_up_and_gather('woodcutting', 'oak_wood')
    
    if st.session_state.state['woodcutting'] < 10:
        st.write("You can chop normal trees.")
    else:
        st.write("You can chop normal and oak trees.")

st.subheader("Inventory")
for item, amount in st.session_state.state['inventory'].items():
    st.write(f"{item.capitalize()}: {amount}")