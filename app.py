import streamlit as st
import pandas as pd

# 1. 页面基本配置
st.set_page_config(page_title="Student Finance System - HKUST(GZ)", page_icon="💳", layout="wide")

# 初始化登录状态
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# =========================================================================
# 样式 A：登录页面样式 (屏幕截图_20260602_185502.jpg)
# =========================================================================
login_css = """
<style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .stApp {
        background: url('https://images.unsplash.com/photo-1541339907198-e08756dedf3f?q=80&w=1920') no-repeat center center fixed;
        background-size: cover;
    }
    .login-container {
        background-color: rgba(255, 255, 255, 0.98);
        padding: 40px;
        border-radius: 4px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.15);
        max-width: 450px;
        margin: 80px auto 20px auto;
        font-family: -apple-system, sans-serif;
    }
    .logo-text {
        color: #003366;
        font-weight: bold;
        font-size: 14px;
        text-align: center;
        margin-bottom: 25px;
        line-height: 1.4;
    }
    .login-title { font-size: 24px; font-weight: 500; color: #333; margin-bottom: 20px; }
    .input-label { font-size: 14px; color: #555; margin-bottom: 5px; margin-top: 15px; }
    
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
</style>
"""

# =========================================================================
# 样式 B：学生财务系统样式 (屏幕截图_20260602_185242.png)
# =========================================================================
dashboard_css = """
<style>
    /* 顶部深蓝色导航栏 */
    .finance-header {
        background-color: #003366;
        padding: 15px 30px;
        margin: -85px -5rem 30px -5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
        font-family: -apple-system, sans-serif;
    }
    .header-left { display: flex; align-items: center; }
    .brand-title {
        border-left: 1px solid rgba(255,255,255,0.4);
        margin-left: 15px;
        padding-left: 15px;
        font-size: 16px;
        line-height: 1.2;
    }
    .brand-title .en { font-weight: bold; font-size: 18px; }
    .brand-title .zh { font-size: 13px; opacity: 0.9; }
    .header-right { display: flex; align-items: center; gap: 20px; font-size: 14px; }
    .header-right a { color: white; text-decoration: none; opacity: 0.9; }
    
    /* 用户基础信息卡片 */
    .profile-card {
        background-color: white;
        padding: 20px 25px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border: 1px solid #eef2f5;
    }
    .profile-card h2 { margin: 0 0 15px 0; color: #333; font-size: 22px; }
    .info-grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 15px;
    }
    .info-item .label { font-size: 12px; color: #888; margin-bottom: 4px; }
    .info-item .value { font-size: 13px; font-weight: bold; color: #333; }

    /* 蓝色强提醒横幅 (Alert Banner) */
    .alert-banner {
        background-color: #0d529a;
        color: white;
        padding: 18px 25px;
        border-radius: 6px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 30px;
    }
    .alert-left { display: flex; align-items: center; gap: 12px; font-size: 14px; }
    .alert-left a { color: white; text-transform: underline; }
    .alert-icon {
        background: white; color: #0d529a; border-radius: 50%;
        width: 20px; height: 20px; display: inline-flex;
        align-items: center; justify-content: center; font-weight: bold; font-size: 13px;
    }
    .setup-btn {
        background-color: white; color: #0d529a;
        padding: 8px 30px; border-radius: 4px;
        font-weight: 500; font-size: 14px; text-decoration: none;
        border: 1px solid white; transition: all 0.2s;
    }
    .setup-btn:hover { background-color: #eef2f5; }

    /* 模块标题 */
    .section-title {
        font-size: 18px; font-weight: bold; color: #333;
        margin-bottom: 15px; padding-bottom: 5px;
    }
</style>
"""

# =========================================================================
# 页面路由控制逻辑
# =========================================================================

if not st.session_state["logged_in"]:
    # 展示登录界面
    st.markdown(login_css, unsafe_allow_html=True)
    
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
        # 这里默认任意输入即可登录成功，用于复刻演示
        if username and password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.rerun()  # 刷新状态，进入后台
        else:
            st.error("Please enter both username and password.")
            
    # 底部链接样式还原
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

else:
    # 展示已经登录后的学生财务系统后台
    st.markdown(dashboard_css, unsafe_allow_html=True)
    
    # 1. 顶部深蓝导航条
    st.markdown("""
    <div class="finance-header">
        <div class="header-left">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="opacity:0.9;"><path d="M22 10v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V10M22 6H2v4h20V6zM12 14v4M6 14v4M18 14v4"/></svg>
            <div class="brand-title">
                <div class="en">Student Finance System</div>
                <div class="zh">学生财务系统</div>
            </div>
        </div>
        <div class="header-right">
            <a href="#">🏠</a>
            <a href="#">📄</a>
            <span style="font-weight:500; cursor:pointer;">XXXXX PENG 彭某某 ▾</span>
            <a href="#" id="logout-link" style="opacity:0.7; font-size:12px;">[Logout]</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 退出登录的暗门按钮（Streamlit原生组件处理状态更稳定）
    if st.button("← 模拟退出系统 (Logout)", key="logout_btn"):
        st.session_state["logged_in"] = False
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. 个人基础数据面板卡片
    st.markdown("""
    <div class="profile-card">
        <h2>XXXXX PENG 彭某某</h2>
        <div class="info-grid">
            <div class="info-item"><div class="label">Student Id</div><div class="value">60000046</div></div>
            <div class="info-item"><div class="label">Study Year</div><div class="value">02</div></div>
            <div class="info-item"><div class="label">Academic Load</div><div class="value">Full-Time</div></div>
            <div class="info-item"><div class="label">Hub</div><div class="value">Function Hub</div></div>
            <div class="info-item"><div class="label">Thrust</div><div class="value">Advanced Materials</div></div>
            <div class="info-item"><div class="label">Program</div><div class="value">PhD(AMAT)</div></div>
            <div class="info-item"><div class="label">Self-financed</div><div class="value">N</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 3. 蓝色核心强提醒 Banner
    st.markdown("""
    <div class="alert-banner">
        <div class="alert-left">
            <span class="alert-icon">i</span>
            <div>
                <strong>Please set your default payment method first to complete subsequent payments</strong><br>
                Click to <a href="#" style="color: white; text-decoration: underline;">see guidance for payment methods</a>
            </div>
        </div>
        <a class="setup-btn" href="#">Set Up</a>
    </div>
    """, unsafe_allow_html=True)

    # 4. Current Due 费用表格模块
    st.markdown('<div class="section-title">Current Due</div>', unsafe_allow_html=True)
    
    # 严格按照原图数据组装表格
    fee_data = {
        "Bill Period": ["Year 2023/24", "Sep 2023", "Oct 2023", "Nov 2023", "Dec 2023", "Jan 2024", "Feb 2024", "Mar 2024"],
        "Item": ["Tuition Fees", "Accommodation Fees", "Accommodation Fees", "Accommodation Fees", "Accommodation Fees", "Accommodation Fees", "Accommodation Fees", "Accommodation Fees"],
        "Outstanding Charges & Deposits": ["￥ 40000.00", "￥ 250.00", "￥ 250.00", "￥ 250.00", "￥ 250.00", "￥ 250.00", "￥ 250.00", "￥ 250.00"],
        "Payment Deadline": ["2023-09-10", "2023-09-30", "2023-10-31", "2023-11-30", "2023-12-31", "2024-01-31", "2024-02-29", "2024-03-31"],
        "Remark": ["", "", "", "", "", "", "", ""]
    }
    df = pd.DataFrame(fee_data)
    
    # 渲染为漂亮的交互式大宽表
    st.dataframe(df, use_container_width=True, hide_index=True)
