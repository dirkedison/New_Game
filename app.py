import streamlit as st

# Initialize session state
if 'mining' not in st.session_state:
    st.session_state.mining = 1
if 'woodcutting' not in st.session_state:
    st.session_state.woodcutting = 1
if 'inventory' not in st.session_state:
    st.session_state.inventory = {'copper': 0, 'silver': 0, 'wood': 0, 'oak_wood': 0}

def level_up(skill):
    st.session_state[skill] += 1

def add_to_inventory(item):
    st.session_state.inventory[item] += 1

st.title("Simple RPG Game")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Mining")
    st.write(f"Current level: {st.session_state.mining}")
    
    if st.button("Mine Copper", key="mine_copper"):
        level_up('mining')
        add_to_inventory('copper')
    
    if st.session_state.mining >= 10:
        if st.button("Mine Silver", key="mine_silver"):
            level_up('mining')
            add_to_inventory('silver')
    
    if st.session_state.mining < 10:
        st.write("You can mine copper ore.")
    else:
        st.write("You can mine copper and silver ore.")

with col2:
    st.subheader("Woodcutting")
    st.write(f"Current level: {st.session_state.woodcutting}")
    
    if st.button("Chop Normal Trees", key="chop_normal"):
        level_up('woodcutting')
        add_to_inventory('wood')
    
    if st.session_state.woodcutting >= 10:
        if st.button("Chop Oak Trees", key="chop_oak"):
            level_up('woodcutting')
            add_to_inventory('oak_wood')
    
    if st.session_state.woodcutting < 10:
        st.write("You can chop normal trees.")
    else:
        st.write("You can chop normal and oak trees.")

st.subheader("Inventory")
st.write(f"Copper: {st.session_state.inventory['copper']}")
st.write(f"Silver: {st.session_state.inventory['silver']}")
st.write(f"Wood: {st.session_state.inventory['wood']}")
st.write(f"Oak Wood: {st.session_state.inventory['oak_wood']}")