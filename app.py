import streamlit as st
from PIL import Image

# Initialize session state
if 'state' not in st.session_state:
    st.session_state.state = {
        'mining': 0,
        'woodcutting': 0,
        'blacksmithing': 0,
        'inventory': {'copper': 0, 'silver': 0, 'wood': 0, 'oak_wood': 0, 'copper_sword': 0, 'silver_sword': 0},
        'copper_coins': 0,
        'silver_coins': 0,
        'gold_coins': 0,
        'show_blacksmith_unlock': False,
        'residence': None
    }

prices = {
    'copper': 1,
    'silver': 2,
    'wood': 1,
    'oak_wood': 2,
    'copper_sword': 4,
    'silver_sword': 6
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

def sell_item(item):
    if st.session_state.state['inventory'][item] > 0:
        st.session_state.state['inventory'][item] -= 1
        st.session_state.state['copper_coins'] += prices[item]
        convert_currency()
        return True
    return False

def convert_currency():
    while st.session_state.state['copper_coins'] >= 100:
        st.session_state.state['copper_coins'] -= 100
        st.session_state.state['silver_coins'] += 1
    
    while st.session_state.state['silver_coins'] >= 100:
        st.session_state.state['silver_coins'] -= 100
        st.session_state.state['gold_coins'] += 1

def buy_item(item, cost):
    if st.session_state.state['copper_coins'] >= cost:
        st.session_state.state['copper_coins'] -= cost
        st.session_state.state['residence'] = item
        convert_currency()
        return True
    return False

# Currency display at the top
st.markdown("### Currency")
currency_display = f"🟤 {st.session_state.state['copper_coins']} | ⚪ {st.session_state.state['silver_coins']} | 🟡 {st.session_state.state['gold_coins']}"
st.markdown(currency_display)

st.title("Simple RPG Game")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Mining")
    st.write(f"Current level: {st.session_state.state['mining']}")
    
    if st.button("Mine Copper", key="mine_copper"):
        level_up_and_gather('mining', 'copper')
    
    if st.session_state.state['mining'] >= 10:
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
    
    if st.session_state.state['woodcutting'] >= 10:
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
    
    if st.session_state.state['blacksmithing'] >= 10:
        if st.button("Make Silver Sword", key="make_silver_sword", disabled=st.session_state.state['inventory']['silver'] == 0):
            if craft_item('silver_sword', 'silver'):
                st.success("Crafted a Silver Sword!")
            else:
                st.error("Not enough silver!")

st.subheader("Inventory")
for item, amount in st.session_state.state['inventory'].items():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"{item.capitalize().replace('_', ' ')}: {amount}")
    with col2:
        if st.button(f"Sell (+ {prices[item]} copper)", key=f"sell_{item}", disabled=amount == 0):
            if sell_item(item):
                st.success(f"Sold 1 {item.replace('_', ' ')} for {prices[item]} copper coins!")
            else:
                st.error(f"No {item.replace('_', ' ')} to sell!")

st.subheader("Store")
if st.button("Buy Old Tent (40 copper)", disabled=st.session_state.state['copper_coins'] < 40):
    if buy_item("old_tent", 40):
        st.success("You bought an old tent!")
    else:
        st.error("Not enough copper coins!")

if st.session_state.state['residence']:
    st.subheader("Current Residence")
    if st.session_state.state['residence'] == "old_tent":
        tent_image = Image.open("path_to_your_tent_image.jpg")  # Replace with the actual path to your image
        st.image(tent_image, caption="Your Old Tent", use_column_width=True)