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
        background: white; border: 1px solid #dee2e6; border-radius: 8px;
        max-width: 500px; margin: 40px auto; padding: 35px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); text-align: center;
        font-family: -apple-system, sans-serif;
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

    /* Footer Contact Notice Style */
    .footer-notice {
        text-align: center; margin-top: 50px; margin-bottom: 20px;
        font-size: 14px; font-family: -apple-system, sans-serif; color: #333;
    }
</style>
"""
st.markdown(common_css, unsafe_allow_html=True)

# Fixed Student Metadata
student_name = "XXXXX PENG"
student_id = "60000046"
deposit_amount = "HKD $15,000.00"
deadline_date = "2026-06-30"

# Reusable footer function (Updated to English)
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
    # Background Injector
    st.markdown('<div class="login-bg"></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="login-container">
        <div class="logo-text">
            香港科技大学（广州）<br>
            THE HONG KONG UNIVERSITY OF SCIENCE<br>
            AND TECHNOLOGY (GUANGZHOU)
        </div>
        <div class="login-title">Login</div>
    </div>
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
    <div style="max-width: 450px; margin: 0 auto; background: #fff; padding: 0 40px 40px 40px; margin-top: -20px; border-bottom-left-radius: 4px; border-bottom-right-radius: 4px; box-shadow: 0px 10px 20px rgba(0,0,0,0.05);">
        <div class="flex-container">
            <label><input type="checkbox"> Remember my login</label>
            <a class="forgot-pwd" href="#">Forget My Password</a>
        </div>
        <div class="divider"><span>Other login methods</span></div>
        <div class="ust-btn-container">
            <a class="ust-btn" href="#">@ust.hk</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Bottom contact text for login screen
    show_footer_notice()


# =========================================================================
# ROUTE 2: DASHBOARD (STUDENT FINANCE SYSTEM - DEPOSIT FEE)
# =========================================================================
elif st.session_state["page_state"] == "DASHBOARD":
    # Global System Top Bar Header
    st.markdown(f"""
    <div class="finance-header">
        <div class="header-left">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="opacity:0.9;"><path d="M22 10v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V10M22 6H2v4h20V6zM12 14v4M6 14v4M18 14v4"/></svg>
            <div class="brand-title">
                <div class="en">Student Finance System</div>
                <div class="zh">学生财务系统</div>
            </div>
        </div>
        <div class="header-right">
            <span>🏠 Home</span>
            <span style="font-weight:500;">{student_name} ▾</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Profile Card Box
    st.markdown(f"""
    <div class="profile-card">
        <h2>{student_name}</h2>
        <div class="info-grid">
            <div class="info-item"><div class="label">Student ID</div><div class="value">{student_id}</div></div>
            <div class="info-item"><div class="label">Academic Load</div><div class="value">Full-Time</div></div>
            <div class="info-item"><div class="label">Hub</div><div class="value">Function Hub</div></div>
            <div class="info-item"><div class="label">Program</div><div class="value">PhD(AMAT)</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Deposit Fee Section Title
    st.markdown('<div class="section-title">Outstanding Admission Deposit Fee</div>', unsafe_allow_html=True)
    
    # HTML Native Table Construction for Admission Fee
    st.markdown(f"""
    <table class="custom-table">
        <thead>
            <tr>
                <th>Academic Year</th>
                <th>Fee Description</th>
                <th>Amount Outstanding</th>
                <th>Payment Deadline</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Year 2026/27</td>
                <td>Admission Deposit Fee (留位费)</td>
                <td style="color:#A37012; font-weight:bold;">{deposit_amount}</td>
                <td>{deadline_date}</td>
            </tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)
    
    # Custom Trigger Grid layout for the operational Streamlit Action Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Proceed to Pay", key="pay_action_btn"):
            st.session_state["page_state"] = "PAYMENT"
            st.rerun()
            
    # Bottom contact text for system portal
    show_footer_notice()


# =========================================================================
# ROUTE 3: ASSOCIATED GATEWAY PAGE (PAYMENT STATUS / QR CODE)
# =========================================================================
elif st.session_state["page_state"] == "PAYMENT":
    # System Top Bar Header (Kept for interface consistency)
    st.markdown(f"""
    <div class="finance-header">
        <div class="header-left">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="opacity:0.9;"><path d="M22 10v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V10M22 6H2v4h20V6zM12 14v4M6 14v4M18 14v4"/></svg>
            <div class="brand-title">
                <div class="en">Payment Gateway</div>
                <div class="zh">支付网关</div>
            </div>
        </div>
        <div class="header-right">
            <span style="font-weight:500;">{student_name}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Standard Interactive Info Payment Container Block
    st.markdown(f"""
    <div class="payment-box">
        <h3>Scan QR Code to Pay</h3>
        <p style="color: #666; font-size:13px; margin-top:-15px; margin-bottom: 25px;">Please use authorized banking apps or WeChat Pay / Alipay to finish transactions.</p>
        
        <div class="qr-placeholder"></div>
        
        <div style="margin-top: 30px; text-align: left;">
            <div class="detail-row">
                <span class="lbl">Student Full Name</span>
                <span class="val">{student_name}</span>
            </div>
            <div class="detail-row">
                <span class="lbl">Student ID</span>
                <span class="val">{student_id}</span>
            </div>
            <div class="detail-row">
                <span class="lbl">Payment Deadline</span>
                <span class="val" style="color: #c92a2a;">{deadline_date}</span>
            </div>
            <div class="detail-row" style="border-bottom: 2px solid #003366;">
                <span class="lbl" style="font-weight: bold; color: #003366;">Total Amount Due</span>
                <span class="val" style="color: #A37012; font-size: 18px;">{deposit_amount}</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Back operation layout handler 
    c1, c2, c3 = st.columns([2, 1, 2])
    with c2:
        if st.button("← Back to System", key="back_dashboard_btn"):
            st.session_state["page_state"] = "DASHBOARD"
            st.rerun()
            
    # Bottom contact text for QR Code invoice page
    show_footer_notice()
