import streamlit as st 

def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px;">
            <img src="{logo_url}" style="height:100px;"/>
        </div>
        <h1 style="text-align:center; color:#E0E3FF;">SNAP<br/>CLASS</h1>
    """, unsafe_allow_html=True)
    

def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
        <div style='display:flex; flex-direction:row; align-items:center; 
                    justify-content:center; gap:12px; margin-bottom:10px;'> 
            <img src='{logo_url}' style='height:60px;'/>
            <h2 style='color:#262638; margin:0; font-size:1.8rem;'>SNAP<br/>CLASS</h2>
        </div>
    """, unsafe_allow_html=True)