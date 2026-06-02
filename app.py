import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Student Finance System - HKUST(GZ)", page_icon="💳", layout="wide")

# Initialize session state for navigation tracking
if "page_state" not in st.session_state:
    st.session_state["page_state"] = "LOGIN"  # Available states: LOGIN, DASHBOARD, PAYMENT

# =========================================================================
# Custom CSS Styles
# =========================================================================
common_css = """
<style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    
    /* Login Page Background */
    .login-bg {
        background: url('https://images.unsplash.com/photo-1541339907198-e08756dedf3f?q=80&w=1920') no-repeat center center fixed;
        background-size: cover;
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1;
    }
    
    /* Login Card Container */
    .login-container {
        background-color: rgba(255, 255, 255, 0.98);
        padding: 40px; border-radius: 4px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.15);
        max-width: 450px; margin: 80px auto 20px auto;
        font-family: -apple-system, sans-serif;
    }
    .logo-text {
        color: #003366; font-weight: bold; font-size: 14px; text-align: center;
        margin-bottom: 25px; line-height: 1.4;
    }
    .login-title { font-size: 24px; font-weight: 500; color: #333; margin-bottom: 20px; }
    .input-label { font-size: 14px; color: #555; margin-bottom: 5px; margin-top: 15px; }
    
    /* Primary Gold Button for Streamlit */
    div.stButton > button:first-child {
        background-color: #A37012 !important; color: white !important;
        border: none !important; border-radius: 4px !important;
        width: 100% !important; padding: 10px 0px !important;
        font-size: 16px !important; font-weight: bold !important;
    }
    div.stButton > button:first-child:hover { background-color: #855a0e !important; }
    
    .flex-container { display: flex; justify-content: space-between; font-size: 14px; margin-top: 15px;}
    .forgot-pwd { color: #A37012; text-decoration: none; }
    .divider { margin: 30px 0 20px 0; text-align: center; border-bottom: 1px solid #e0e0e0; line-height: 0.1em; }
    .divider span { background: #fff; padding: 0 10px; color: #777; font-size: 13px; }
    .ust-btn-container { text-align: center; }
    .ust-btn { background-color: #94A6B8; color: white; padding: 6px 12px; border-radius: 4px; font-size: 12px; text-decoration: none; }

    /* Top Blue Navigation Bar */
    .finance-header {
        background-color: #003366; padding: 15px 30px;
        margin: -85px -5rem 30px -5rem;
        display: flex; justify-content: space-between; align-items: center;
        color: white; font-family: -apple-system, sans-serif;
    }
    .header-left { display: flex; align-items: center; }
    .brand-title {
        border-left: 1px solid rgba(255,255,255,0.4);
        margin-left: 15px; padding-left: 15px; font-size: 16px; line-height: 1.2;
    }
    .brand-title .en { font-weight: bold; font-size: 18px; }
    .brand-title .zh { font-size: 13px; opacity: 0.9; }
    .header-right { display: flex; align-items: center; gap: 20px; font-size: 14px; }
    .header-right a { color: white; text-decoration: none; opacity: 0.9; }
    
    /* Student Profile Card */
    .profile-card {
        background-color: white; padding: 20px 25px; border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 25px;
        border: 1px solid #eef2f5; font-family: -apple-system, sans-serif;
    }
    .profile-card h2 { margin: 0 0 15px 0; color: #333; font-size: 22px; }
    .info-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; }
    .info-item .label { font-size: 12px; color: #888; margin-bottom: 4px; }
    .info-item .value { font-size: 14px; font-weight: bold; color: #333; }

    /* Section Header */
    .section-title {
        font-size: 18px; font-weight: bold; color: #003366;
        margin-bottom: 15px; padding-bottom: 5px;
        border-bottom: 2px solid #eef2f5;
        font-family: -apple-system, sans-serif;
    }

    /* Financial Custom Table */
    .custom-table {
        width: 100%; border-collapse: collapse; margin-bottom: 25px;
        font-family: -apple-system, sans-serif; background: #fff;
        border: 1px solid #dee2e6; border-radius: 4px; overflow: hidden;
    }
    .custom-table th { background-color: #f8f9fa; color: #003366; padding: 12px; text-align: left; border-bottom: 2px solid #dee2e6; font-size: 14px;}
    .custom-table td { padding: 12px; border-bottom: 1px solid #dee2e6; color: #333; font-size: 14px;}
    
    /* Payment Result Box */
    .payment-box {
        background
