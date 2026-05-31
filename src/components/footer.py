import streamlit as st 

def footer_home():
    #logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
        <div style = 'display:flex; flex-direction:column;align-items:center; justify-content:center;margin-bottom:30px;'> 
                <p style="font-weight:bold; color:white;">  Created With ❤️ by 
                <span style='color:#FFD166;'>Rahul</span>
                <span style='color:black;'>Sahu</span></p>

    </div>

    
                  """,unsafe_allow_html=True)
    

def footer_dashboard():
    #logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
        <div style = 'display:flex; flex-direction:column;align-items:center; justify-content:center;margin-bottom:30px;'> 
                <p style="font-weight:bold; color:black;">  Created With ❤️ by 
                <span style='color:#FFD166;'>Rahul</span>
                <span style='color:black;'>Sahu</span></p>

    </div>

    
                  """,unsafe_allow_html=True)