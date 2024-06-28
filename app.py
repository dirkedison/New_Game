import streamlit as st

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
        'show_blacksmith_unlock': False
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

# Currency display in header
st.markdown("""
    <style>
    .header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #f0f2f6;
        padding: 10px;
        z-index: 999;
    }
    .content {
        margin-top: 60px;
    }
    </style>
    """, unsafe_allow_html=True)

currency_display = f"🥇 {st.session_state.state['gold_coins']} | 🥈 {st.session_state.state['silver_coins']} | 🥉 {st.session_state.state['copper_coins']}"
st.markdown(f'<div class="header">Currency: {currency_display}</div>', unsafe_allow_html=True)

st.markdown('<div class="content">', unsafe_allow_html=True)

st.title("Simple RPG Game")

# ... (rest of the game code remains the same)

st.markdown('</div>', unsafe_allow_html=True)