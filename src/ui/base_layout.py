import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: #5865F2 !important;
            }
            .stApp div[data-testid="stColumn"]{
                background-color:#FFB6C1 !important;
                padding:2.5rem !important;
                border-radius:5rem !important;
                }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #E0E3FF !important;
            }
        </style>
    """, unsafe_allow_html=True)



def style_base_layout():
    st.markdown("""
        <style>
                
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');

            /*hide Top Bar of streamlit */
            #mainmenu , footer , header{
                visibility : hidden;
            }

            .block-container{
                padding-top: 1.5rem !important;
            }

            h1{
                font-family: 'Climate Crisis' , sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
            }

            h2{
                font-family: 'Climate Crisis' , sans-serif !important;
                font-size: 2rem !important;
                line-height:1.1 !important;
                color:#5860F2 !important;
                margin-bottom:0rem !important;
            }
            
            h3, h4, p {
                font-family: "Outfit", sans-serif;
            }

        /* ── Base Button ── */
        button {
            border-radius: 1.5rem !important;          
            background: #5865F2 !important;
            color: white !important;
            padding: 10px 24px !important;
            border: none !important;
            font-size: 0.9rem !important;
            font-weight: 600 !important;
            letter-spacing: 0.02em !important;
            cursor: pointer !important;
            box-shadow: 0 4px 14px rgba(88, 101, 242, 0.35) !important;
            transition: transform 0.25s ease-in-out,
                        box-shadow 0.25s ease-in-out !important;
        }

        /* ── Secondary — Pink ── */
        button[kind="secondary"] {                      
            border-radius: 1.5rem !important;
            background: #EB459E !important;
            color: white !important;
            padding: 10px 24px !important;
            border: none !important;
            font-size: 0.9rem !important;
            font-weight: 600 !important;
            letter-spacing: 0.02em !important;
            cursor: pointer !important;
            box-shadow: 0 4px 14px rgba(235, 69, 158, 0.35) !important;
            transition: transform 0.25s ease-in-out,
                        box-shadow 0.25s ease-in-out !important;
        }

        /* ── Tertiary — Dark ── */
        button[kind="tertiary"] {
            border-radius: 1.5rem !important;
            background: #1A1A2E !important;            
            padding: 10px 24px !important;
            border: none !important;
            font-size: 0.9rem !important;
            font-weight: 600 !important;
            letter-spacing: 0.02em !important;
            cursor: pointer !important;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25) !important;
            transition: transform 0.25s ease-in-out,
                        box-shadow 0.25s ease-in-out !important;
        }

        /* ── Hover — all buttons ── */
        button:hover {
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2) !important;
        }

        /* ── Active / Click ── */
        button:active {
            transform: scale(0.97) !important;
            box-shadow: none !important;
        }

        /* ── Camera Input Bada aur Full Width ── */
        [data-testid="stCameraInput"] {
            width: 100% !important;
        }

        [data-testid="stCameraInput"] video,
        [data-testid="stCameraInput"] img {
            width: 100% !important;
            min-height: 520px !important;
            max-height: 520px !important;
            object-fit: cover !important;
            border-radius: 20px 20px 0 0 !important;
            border: 3px solid #5865F2 !important;
        }

        [data-testid="stCameraInputButton"] {
            width: 100% !important;
            border-radius: 0 0 20px 20px !important;
            font-size: 1rem !important;
            padding: 14px !important;
        }

        /* ── Camera label WAPAS DIKHAO ── */
        [data-testid="stCameraInput"] label {
            display: block !important;
            font-family: "Outfit", sans-serif !important;
            font-size: 0.95rem !important;
            color: #444 !important;
            margin-bottom: 8px !important;
        }

        </style>
    """, unsafe_allow_html=True)