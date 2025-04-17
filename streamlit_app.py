import streamlit as st
from Graph.graph_builder import SupplyChainGraph

st.set_page_config(page_title="Supply Chain Acharya", page_icon="📦")
st.title("📦 Supply Chain Acharya")

if "state" not in st.session_state:
    st.session_state.state = {
        "user_query": "",
        "valid_stores": [],
        "valid_items": [],
        "generated_sql": "",
        "executed_results": "",
        "root_cause_summary": "",
        "needs_user_input": True,
        "clarification_attempts": 0
    }

if "graph" not in st.session_state:
    st.session_state.graph = SupplyChainGraph().build()

chat_input = st.chat_input("What supply chain issue can I help with?")
if chat_input:
    st.session_state.state["user_query"] = chat_input
    result = st.session_state.graph.invoke(st.session_state.state)

    with st.chat_message("user"):
        st.write(chat_input)
    with st.chat_message("ai"):
        st.write(result.get("manager_response") or result.get("root_cause_summary"))
