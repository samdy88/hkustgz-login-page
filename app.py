import streamlit as st

# 1. Page Configuration (Ensure wide layout and hide standard headers)
st.set_page_config(page_title="Student Finance System - HKUST(GZ)", page_icon="💳", layout="wide")

# Initialize session state for navigation tracking
if "page_state" not in st.session_state:
    st.session_state["page_state"] = "LOGIN"

# =========================================================================
# Flawless Premium CSS (Replicating the exact layout from image_4a927e.png)
# =========================================================================
common_css = """
<style>
    /* Hide Streamlit framework headers and menus */
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .block-container { padding-top: 1.5rem !important; padding-bottom: 0rem !important; }

    /* Login Page Background - 100% viewport coverage */
    .login-bg {
        background: url('https://images.unsplash.com/photo-1541339907198-e08756dedf3f?q=80&w=1920') no-repeat center center fixed;
        background-size: cover;
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -2;
    }
    
    /* Login Centered Card Box */
    .login-wrapper {
        background-color: rgba(255, 255, 255, 0.98);
        padding: 40px; border-radius: 4px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.15);
        max-width: 450px; margin: 80px auto 10px auto;
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    }
    .logo-text {
        color: #003366; font-weight: bold; font-size: 13px; text-align: center;
        margin-bottom: 25px; line-height: 1.5; letter-spacing: 0.5px;
    }
    .login-title { font-size: 24px; font-weight: 500; color: #333; margin-bottom: 20px; }
    .input-label { font-size: 14px; color: #555; margin-bottom: 2px; margin-top: 12px; font-weight: 500;}
    
    /* Neutralize Streamlit's native Form container design */
    div[data-testid="stForm"] {
        border: none !important; background: transparent !important; padding: 0 !important; margin: 0 !important;
    }
    div[data-testid="stTextInput"] div[col-name] {  background-color: transparent !important; }
    div[data-testid="stTextInput"] input {
        border: 1px solid #ccc !important; border-radius: 4px !important;
        padding: 8px 12px !important; background-color: #fff !important; color: #333 !important;
    }
    
    /* Elegant Gold Button Style for Form Submission and Pay action */
    div.stButton > button:first-child {
        background-color: #A37012 !important; color: white !important;
        border: none !important; border-radius: 4px !important;
        width: 100% !important; padding: 12px 0px !important;
        font-size: 16px !important; font-weight: bold !important; margin-top: 15px !important;
    }
    div.stButton > button:first-child:hover { background-color: #855a0e !important; }
    
    /* Top Navigation bar for Portal Pages (Solid Blue Bar) */
    .finance-header {
        background-color: #003366; padding: 15px 30px;
        margin: -1.5rem -5rem 0 -5rem;
        display: flex; justify-content: space-between; align-items: center;
        color: white; font-family: -apple-system, sans-serif;
    }
    .header-left { display: flex; align-items: center; }
    .brand-title {
        border-left: 1px solid rgba(255,255,255,0.4);
        margin-left: 15px; padding-left: 15px; font-size: 18px; line-height: 1.2; font-weight: bold;
    }
    .header-right { display: flex; align-items: center; gap: 20px; font-size: 14px; }

    /* Main Dashboard Multi-Column Layout Grid */
    .portal-container {
        display: flex; margin: 0 -5rem; font-family: -apple-system, sans-serif;
        min-height: calc(100vh - 150px);
    }
    
    /* LEFT SIDEBAR NAVIGATION MENU */
    .portal-sidebar {
        width: 240px; background-color: #f8f9fa; border-right: 1px solid #dee2e6;
        padding-top: 20px; display: flex; flex-direction: column;
    }
    .sidebar-item {
        padding: 14px 25px; color: #495057; font-size: 14px; font-weight: 500;
        text-decoration: none; border-left: 4px solid transparent;
    }
    .sidebar-item.active {
        background-color: #e9ecef; color: #003366; font-weight: bold;
        border-left: 4px solid #003366;
    }
    .sidebar-item:hover { background-color: #edf0f2; color: #003366; }

    /* MAIN CONTENT AREA CONTAINER */
    .portal-main {
        flex: 1; padding: 30px 40px; background-color: #ffffff;
    }
    
    /* Profile Card Box */
    .profile-card {
        background-color: white; padding: 20px 25px; border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08); margin-bottom: 25px;
        border: 1px solid #eef2f5;
    }
    .profile-card h2 { margin: 0 0 15px 0; color: #333; font-size: 22px; font-weight: 600; }
    .info-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; }
    .info-item .label { font-size: 12px; color: #888; margin-bottom: 4px; }
    .info-item .value { font-size: 14px; font-weight: bold; color: #333; }

    /* Section Title */
    .section-title {
        font-size: 18px; font-weight: bold; color: #003366;
        margin-bottom: 15px; padding-bottom: 5px; border-bottom: 2px solid #eef2f5;
    }

    /* Information Table Structure */
    .custom-table {
        width: 100%; border-collapse: collapse; margin-bottom: 30px;
        background: #fff; border: 1px solid #dee2e6; border-radius: 4px; overflow: hidden;
    }
    .custom-table th { background-color: #f8f9fa; color: #003366; padding: 12px 15px; text-align: left; border-bottom: 2px solid #dee2e6; font-size: 14px;}
    .custom-table td { padding: 14px 15px; border-bottom: 1px solid #dee2e6; color: #333; font-size: 14px;}
    
    /* Payment QR Code Box layout */
    .payment-box {
        background: white; border: 1px solid #dee2e6; border-radius: 8px;
        max-width: 500px; margin: 10px auto; padding: 35px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); text-align: center;
    }
    .payment-box h3 { color: #003366; margin-top: 0; margin-bottom: 25px; font-size: 22px;}
    .qr-placeholder {
        width: 200px; height: 200px; margin: 20px auto;
        background: url('https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://soch.hkust-gz.edu.cn/') no-repeat center;
        border: 1px solid #ddd; padding: 5px; border-radius: 4px;
    }
    .detail-row { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #f5f5f5; font-size: 14px;}
    .detail-row .lbl { color: #666; }
    .detail-row .val { font-weight: bold; color: #333; }

    /* Footer English Contact Text style */
    .footer-notice {
        text-align: center; margin-top: 50px; margin-bottom: 20px;
        font-size: 14px; font-family: -apple-system, sans-serif; color: #333;
        width: 100%; clear: both; position: relative; z-index: 10;
    </div>
</style>
"""
st.markdown(common_css, unsafe_allow_html=True)

# Fixed Global Student Metadata (English Only)
student_name = "XXXXX PENG"
student_id = "60000046"
deposit_amount = "HKD $15,000.00"
deadline_date = "2026-06-30"

# Reusable footer notice function (Fully English & Bold)
def show_footer_notice():
    st.markdown("""
    <div class="footer-notice">
        <strong>If you have any questions regarding payment, please contact: <a href="mailto:hkust@hkust.com" style="color: #A37012; text-decoration: none;">hkust@hkust.com</a></strong>
    </div>
    """, unsafe_allow_html=True)


# =========================================================================
# ROUTE 1: LOGIN PAGE
# =========================================================================
if st.session_state["page_state"] == "LOGIN":
    st.markdown('<div class="login-bg"></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="login-wrapper">
        <div class="logo-text">
            THE HONG KONG UNIVERSITY OF SCIENCE<br>
            AND TECHNOLOGY (GUANGZHOU)
        </div>
        <div class="login-title">Login</div>
    """, unsafe_allow_html=True)

    with st.form(key="login_form"):
        st.markdown('<p class="input-label">GZ campus username</p>', unsafe_allow_html=True)
        username = st.text_input("username", placeholder="without(@hkust-gz.edu.cn)", label_visibility="collapsed")
        
        st.markdown('<p class="input-label">Password</p>', unsafe_allow_html=True)
        password = st.text_input("password", type="password", label_visibility="collapsed")
        
        submit = st.form_submit_button("Sign in")

    if submit:
        if username and password:
            st.session_state["page_state"] = "DASHBOARD"
            st.rerun()
        else:
            st.error("Please enter both username and password.")
            
    st.markdown("""
        <div class="flex-container">
            <label style="color:#555;"><input type="checkbox"> Remember my login</label>
            <a class="forgot-pwd" href="#">Forget My Password</a>
        </div>
        <div class="divider"><span>Other login methods</span></div>
        <div class="ust-btn-container">
            <a class="ust-btn" href="#">@ust.hk</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    show_footer_notice()


# =========================================================================
# ROUTE 2: DASHBOARD (STUDENT FINANCE SYSTEM SYSTEM METADATA)
# =========================================================================
elif st.session_state["page_state"] == "DASHBOARD":
    # Top Solid Blue Navigation Bar
    st.markdown(f"""
    <div class="finance-header">
        <div class="header-left">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="opacity:0.9;"><path d="M22 10v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V10M22 6H2v4h20V6zM12 14v4M6 14v4M18 14v4"/></svg>
            <div class="brand-title">Student Finance System</div>
        </div>
        <div class="header-right">
            <span style="font-weight:500;">🏠 Home &nbsp;&nbsp;|&nbsp;&nbsp; {student_name} ▾</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Core Two-Column Screen Container Injector
    st.markdown("""
    <div class="portal-container">
        <div class="portal-sidebar">
            <a class="sidebar-item" href="#">Dashboard</a>
            <a class="sidebar-item" href="#">Student Center</a>
            <a class="sidebar-item" href="#">Housing Application</a>
            <a class="sidebar-item active" href="#">Finance</a>
            <a class="sidebar-item" href="#">Profile Settings</a>
        </div>
        
        <div class="portal-main">
    """, unsafe_allow_html=True)
    
    # Inside Main Layout Area: Profile info header block
    st.markdown(f"""
            <div class="profile-card">
                <h2>{student_name}</h2>
                <div class="info-grid">
                    <div class="info-item"><div class="label">Student ID</div><div class
