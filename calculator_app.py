import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")


st.markdown("""
<style>
 
.calc-container {
    width: 360px;
    margin: auto;
    padding: 20px;
    border: 4px solid black;  /* <-- thick border around whole calculator */
    border-radius: 15px;
    background-color: #f8f8f8;
}

/* Yellow Display */
.stTextInput > div > div > input {
    background-color: yellow;
    color: black;
    font-size: 28px;
    text-align: right;
    padding: 10px;
    border-radius: 8px;
    border: 2px solid black;
}

/* Buttons */
button {
    height: 50px;
    font-size: 18px !important;
    border-radius: 8px !important;
}
</style>
            
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:black;'> Simple Calculator</h1>", unsafe_allow_html=True)


# start div
st.markdown("<div class='calculator' border: 2px solid black !important;;> ", unsafe_allow_html=True)


# st.text_input("Calculator", key="expr", label_visibility="collapsed")

        




buttons = [
    ["7","8","9","÷"],
    ["4","5","6","x"],
    ["1","2","3","-"],
    ["C","0","⌫","+"],
    ["="]
]




# -------------------
# Functions
# -------------------
def press(x):
    st.session_state.expr += str(x)

def backspace():
    st.session_state.expr = st.session_state.expr[:-1]

def clear():
    st.session_state.expr = ""

def calculate():
    try:
        expr = st.session_state.expr.replace("x", "*").replace("÷", "/")
        st.session_state.expr = str(eval(expr))
    except:
        st.session_state.expr = "Error"



# Display (Enter key triggers calculate)
st.text_input(
    "Calculator",
    key="expr",
    label_visibility="collapsed",
    on_change=calculate   # 🔥 Enter key support
)



for row in buttons:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        if btn == "C":
            cols[i].button(btn, on_click=clear, use_container_width=True)
        elif btn == "=":
            cols[i].button(btn, on_click=calculate, use_container_width=True)
        elif btn == "⌫":
            cols[i].button(btn, on_click=backspace, use_container_width=True)
        else:
            cols[i].button(btn, on_click=press, args=(btn,), use_container_width=True)


st.markdown("</div>", unsafe_allow_html=True)