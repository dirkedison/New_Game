import streamlit as st

# Initialize session state
if 'state' not in st.session_state:
    st.session_state.state = {
        'mining': 1,
        'woodcutting': 1,
        'blacksmithing': 1,
        'inventory': {'copper': 0, 'silver': 0, 'wood': 0, 'oak_wood': 0, 'copper_sword': 0, 'silver_sword': 0},
        'show_blacksmith_unlock': False
    }

def level_up_and_gather(skill, item):
    st.session_state.state[skill] += 1
    st.session_state.state['inventory'][item] += 1
    if skill == 'mining' and st.session_state.state[skill] == 10:
        st.session_state.state['show_blacksmith_unlock'] = True

def craft_item(item, resource):
    if st.session_state.state['inventory'][resource] > 0:
        st.session_state.state['inventory'][resource] -= 1
        st.session_state.state['inventory'][item] += 1
        st.session_state.state['blacksmithing'] += 1
        return True
    return False

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

if st.session_state.state['mining'] >= 10:
    st.subheader("Blacksmithing")
    st.write(f"Current level: {st.session_state.state['blacksmithing']}")
    
    if st.session_state.state['show_blacksmith_unlock']:
        st.success("You unlocked blacksmithing!")
        st.session_state.state['show_blacksmith_unlock'] = False
    
    if st.button("Make Copper Sword", key="make_copper_sword", disabled=st.session_state.state['inventory']['copper'] == 0):
        if craft_item('copper_sword', 'copper'):
            st.success("Crafted a Copper Sword!")
        else:
            st.error("Not enough copper!")
    
    if st.session_state.state['blacksmithing'] > 9:
        if st.button("Make Silver Sword", key="make_silver_sword", disabled=st.session_state.state['inventory']['silver'] == 0):
            if craft_item('silver_sword', 'silver'):
                st.success("Crafted a Silver Sword!")
            else:
                st.error("Not enough silver!")

st.subheader("Inventory")
for item, amount in st.session_state.state['inventory'].items():
    st.write(f"{item.capitalize().replace('_', ' ')}: {amount}")