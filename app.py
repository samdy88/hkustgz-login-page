import streamlit as st

# 1. 初始化全屏配置
st.set_page_config(
    page_title="HKUST(GZ) Portal", 
    page_icon="🎓", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. 注入全局样式：隐藏 Streamlit 原生组件，同时定制我们自己的精美网页组件
st.markdown("""
    <style>
        /* 隐藏 Streamlit 自带导航和底部 */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
        
        /* ==================== 页面 1：登录页样式 ==================== */
        .login-bg {
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: url('https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1920&q=80') no-repeat center center;
            background-size: cover;
            position: relative;
        }
        .login-bg::before {
            content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(255, 255, 255, 0.4); backdrop-filter: blur(2px); z-index: 1;
        }
        .login-box {
            position: relative; z-index: 2; background: rgba(255, 255, 255, 0.98);
            width: 420px; padding: 35px 40px; border-radius: 4px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        }
        .brand-header { display: flex; align-items: center; justify-content: center; margin-bottom: 25px; }
        .logo-placeholder {
            width: 24px; height: 32px; background: #b38728; border-radius: 2px; margin-right: 10px; position: relative;
        }
        .logo-placeholder::before {
            content: ''; position: absolute; top: -6px; left: 6px; width: 12px; height: 12px; background: #112e51; border-radius: 50%;
        }
        .brand-text { font-size: 11px; color: #112e51; font-weight: bold; line-height: 1.3; letter-spacing: 0.5px; text-align: left; }
        .login-box h2 { font-size: 22px; color: #333333; margin-bottom: 20px; font-weight: 500; }
        
        /* 强制覆盖修改 Streamlit 输入框和按钮的统一样式 */
        div.stTextInput > div > div > input {
            border: 1px solid #dcdfe6 !important;
            border-radius: 4px !important;
            padding: 10px 12px !important;
        }
        
        /* 统一样式的金色主按钮 */
        div.stButton > button {
            background-color: #946912 !important;
            color: white !important;
            border: none !important;
            padding: 12px 0px !important;
            font-size: 14px !important;
            border-radius: 4px !important;
            font-weight: 600 !important;
            width: 100% !important;
            cursor: pointer !important;
            box-shadow: 0 2px 6px rgba(148, 105, 18, 0.2) !important;
        }
        div.stButton > button:hover {
            background-color: #7d580f !important;
            color: white !important;
        }
        
        /* ==================== 页面 2 & 3 共用：复刻深蓝色页眉 ==================== */
        .header-bar {
            background-color: #004b93; 
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 30px;
            color: white;
            width: 100%;
        }
        .left-section { display: flex; align-items: center; }
        .logo-container { display: flex; align-items: center; }
        .mini-crest {
            width: 20px; height: 26px; background: white; border-radius: 1px; margin-right: 8px; position: relative;
        }
        .mini-crest::before {
            content: ''; position: absolute; top: -4px; left: 5px; width: 10px; height: 10px; background: #b38728; border-radius: 50%;
        }
        .uni-title-en { font-size: 10px; font-weight: bold; line-height: 1.15; letter-spacing: 0.1px; color: #ffffff; text-align: left; }
        .vertical-divider { width: 1px; height: 30px; background-color: rgba(255,255,255,0.3); margin: 0 18px; }
        .sys-title-en { font-size: 16px; font-weight: 600; letter-spacing: 0.2px; }
        .right-section { display: flex; align-items: center; gap: 24px; font-size: 13px; font-weight: 500; }
        
        /* 页面内容布局容器 */
        .main-content { padding: 50px 40px; max-width: 900px; margin: 0 auto; width: 100%; }
        .page-title { font-size: 22px; color: #111; margin-bottom: 30px; font-weight: 600; display: flex; align-items: center; gap: 10px; }
        .page-title::before { content: ''; display: inline-block; width: 4px; height: 20px; background-color: #004b93; border-radius: 2px; }
        
        /* 表格样式 */
        .table-container { background: white; border-radius: 6px; box-shadow: 0 2px 12px rgba(0,0,0,0.04); border: 1px solid #eef2f5; overflow: hidden; margin-bottom: 35px; width: 100%; }
        table { width: 100%; border-collapse: collapse; text-align: left; font-size: 14px; }
        th { background-color: #f8fafc; color: #475569; font-weight: 600; padding: 16px 24px; border-bottom: 1px solid #eef2f5; font-size: 13px; text-transform: uppercase; }
        td { padding: 18px 24px; border-bottom: 1px solid #f1f5f9; color: #334155; }
        
        /* 页面 3：二维码名片卡 */
        .payment-card { background: white; border-radius: 8px; width: 100%; padding: 40px; box-shadow: 0 4px 16px rgba(0,0,0,0.05); border: 1px solid #eef2f5; text-align: center; margin: 0 auto 40px auto; max-width: 650px; }
        .section-title { font-size: 20px; color: #111; font-weight: 600; margin-bottom: 24px; }
        .info-row { display: flex; justify-content: space-between; padding: 12px 0; border-bottom: 1px dashed #e2e8f0; font-size: 14px; color: #475569; }
        .info-value { font-weight: 600; color: #111; }
        .info-value.amount { color: #946912; font-size: 18px; }
        .qr-container { background-color: #f8fafc; border: 1px solid #e2e8f0; padding: 20px; border-radius: 6px; display: inline-block; margin: 15px 0; width: 100%; }
        .qr-code { width: 180px; height: 180px; display: flex; align-items: center; justify-content: center; background: #fff; border: 1px solid #cbd5e1; position: relative; margin: 0 auto; }
        .qr-code::before { content: 'QR CODE'; font-size: 11px; color: #94a3b8; font-weight: 600; }
        .qr-tip { font-size: 12px; color: #64748b; margin-top: 10px; }
        .support-footer { font-size: 13px; color: #64748b; text-align: center; margin-top: 20px; line-height: 1.5; width: 100%; }
        .support-footer a { color: #004b93; text-decoration: none; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

# 3. 完美的 Python 原生状态机路由管理
if 'page' not in st.session_state:
    st.session_state.page = 'login'

# --- 提取出来的公共深蓝色页眉 HTML ---
header_html = """
<div class="header-bar">
    <div class="left-section">
        <div class="logo-container">
            <div class="mini-crest"></div>
            <div class="uni-title-en">THE HONG KONG<br>UNIVERSITY OF SCIENCE AND<br>TECHNOLOGY (GUANGZHOU)</div>
        </div>
        <div class="vertical-divider"></div>
        <div class="sys-title-en">Student Finance System</div>
    </div>
    <div class="right-section">
        <span style="cursor:pointer;">🏠</span>
        <span style="cursor:pointer;">📄</span>
        <span>Sabrina Li ▾</span>
    </div>
</div>
"""

# ==================== 路由控制逻辑 ====================

if st.session_state.page == 'login':
    # --- 渲染页面 1：高保真登录框 ---
    st.markdown('<div class="login-bg">', unsafe_allow_html=True)
    
    # 用 Streamlit 列控组件将登录框挤到中间，形成完美的卡片居中
    _, col_center, _ = st.columns([1, 2.2, 1])
    with col_center:
        st.markdown("""
            <div class="login-box">
                <div class="brand-header">
                    <div class="logo-placeholder"></div>
                    <div class="brand-text">
                        THE HONG KONG UNIVERSITY OF SCIENCE<br>
                        AND TECHNOLOGY (GUANGZHOU)
                    </div>
                </div>
                <h2>Login</h2>
            </div>
        """, unsafe_allow_html=True)
        
        # 使用原生输入组件，100% 捕获键盘输入
        user_input = st.text_input("GZ campus username", placeholder="without(@hkust-gz.edu.cn)", key="user")
        pass_input = st.text_input("Password", type="password", key="pass")
        
        st.markdown('<div style="margin-top:15px;"></div>', unsafe_allow_html=True)
        
        # 核心原生按钮：点击直接触发 Python 后端状态切换，绝不失效！
        if st.button("Sign in"):
            if user_input.strip() == "11760523" and pass_input == "tg-hkust2027":
                st.session_state.page = 'finance'
                st.rerun()
            else:
                st.error("Invalid username or password! Please check your credentials.")
                
        st.markdown("""
            <div style="display:flex; justify-content:between; font-size:13px; color:#606266; margin-top:15px;">
                <span style="flex:1;">🔲 Remember my login</span>
                <span style="color:#946912; cursor:pointer;">Forget My Password</span>
            </div>
            <div style="text-align:center; margin: 20px 0 15px 0; color:#909399; font-size:12px;">─── Other login methods ───</div>
            <div style="text-align:center;"><span style="background:#a0b2cb; color:white; padding:5px 12px; border-radius:3px; font-size:12px; cursor:pointer;">@ust.hk</span></div>
        """, unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'finance':
    # --- 渲染页面 2：财务学报信息表 ---
    st.markdown(header_html, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="main-content">
            <div class="page-title">Admission Fee & Deposit Statements</div>
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>Student Name</th>
                            <th>Fee Description</th>
                            <th>Due Date</th>
                            <th>Amount</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="font-weight: 500;">Sabrina Li</td>
                            <td>Admission Deposit</td>
                            <td style="color: #d9534f; font-weight: 500;">June 30, 2026</td>
                            <td style="font-weight: 600; color: #111;">¥ 20,000.00</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # 放出原生 Python 跳转按钮，点击后 100% 能够进入二维码页面
    _, btn_col, _ = st.columns([1, 0.4, 1])
    with btn_col:
        if st.button("Pay Now"):
            st.session_state.page = 'payment'
            st.rerun()

elif st.session_state.page == 'payment':
    # --- 渲染页面 3：二维码缴费中心与 adimt 脚注 ---
    st.markdown(header_html, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="main-content" style="max-width: 750px;">
            <div class="payment-card">
                <div class="section-title">Payment Information</div>
                <div class="info-row">
                    <span>Student Name:</span>
                    <span class="info-value">Sabrina Li</span>
                </div>
                <div class="info-row">
                    <span>Fee Type:</span>
                    <span class="info-value">Admission Deposit</span>
                </div>
                <div class="info-row" style="border-bottom:none;">
                    <span>Amount Due:</span>
                    <span class="info-value amount">¥ 20,000.00</span>
                </div>
                <div class="qr-container">
                    <div class="qr-code">
                        <div style="position: absolute; top:0; left:0; width:25px; height:25px; border-bottom:4px solid #004b93; border-right:4px solid #004b93;"></div>
                        <div style="position: absolute; bottom:0; right:0; width:25px; height:25px; border-top:4px solid #004b93; border-left:4px solid #004b93;"></div>
                    </div>
                    <p class="qr-tip">Please scan this QR code to complete your payment transaction securely.</p>
                </div>
            </div>
            <div class="support-footer">
                If you have any questions regarding your payment, please contact us at: <br>
                <a href="mailto:admit@hkust.com"><strong>admit@hkust.com</strong></a>
            </div>
        </div>
    """, unsafe_allow_html=True)
