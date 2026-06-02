import streamlit as st

# 1. 设置页面标题和配置
st.set_page_config(page_title="HKUST(GZ) Login", page_icon="🎓", layout="centered")

# 2. 注入自定义 CSS 样式来复刻视觉效果
st.markdown("""
    <style>
    /* 隐藏 Streamlit 默认的头部和尾部 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 整体背景图与布局 */
    .stApp {
        background: url('https://images.unsplash.com/photo-1541339907198-e08756dedf3f?q=80&w=1920') no-repeat center center fixed;
        background-size: cover;
    }
    
    /* 登录卡片容器 */
    .login-container {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 40px;
        border-radius: 4px;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
        max-width: 450px;
        margin: 60px auto;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* 校徽和标题 */
    .logo-text {
        color: #003366;
        font-weight: bold;
        font-size: 14px;
        text-align: center;
        margin-bottom: 25px;
        line-height: 1.3;
    }
    .login-title {
        font-size: 24px;
        font-weight: 500;
        color: #333333;
        margin-bottom: 20px;
    }
    
    /* 输入框标签样式 */
    .input-label {
        font-size: 14px;
        color: #555555;
        margin-bottom: 5px;
        margin-top: 15px;
    }
    
    /* 覆盖 Streamlit 默认按钮样式（港科大金黄色） */
    div.stButton > button:first-child {
        background-color: #A37012 !important;
        color: white !important;
        border: none !important;
        border-radius: 4px !important;
        width: 100% !important;
        padding: 10px 0px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        transition: background-color 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: #855a0e !important;
    }
    
    /* 底部辅助链接 */
    .flex-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 15px;
        font-size: 14px;
    }
    .forgot-pwd {
        color: #A37012;
        text-decoration: none;
    }
    
    /* 其他登录方式分割线 */
    .divider {
        margin: 30px 0 20px 0;
        text-align: center;
        border-bottom: 1px solid #e0e0e0;
        line-height: 0.1em;
    }
    .divider span {
        background: #fff;
        padding: 0 10px;
        color: #777;
        font-size: 13px;
    }
    
    /* @ust.hk 按钮样式 */
    .ust-btn-container {
        text-align: center;
    }
    .ust-btn {
        background-color: #94A6B8;
        color: white;
        padding: 6px 12px;
        border-radius: 4px;
        font-size: 12px;
        text-decoration: none;
        display: inline-block;
    }
    </style>
""", unsafe_index=True)

# 3. 构建页面结构
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

# 使用 Streamlit 表单接收输入
with st.form(key="login_form", clear_on_submit=False):
    st.markdown('<p class="input-label">GZ campus username</p>', unsafe_allow_html=True)
    username = st.text_input(label="username", placeholder="without(@hkust-gz.edu.cn)", label_visibility="collapsed")
    
    st.markdown('<p class="input-label">Password</p>', unsafe_allow_html=True)
    password = st.text_input(label="password", type="password", label_visibility="collapsed")
    
    # 提交按钮
    submit_button = st.form_submit_button(label="Sign in")

# 底部附加组件
col1, col2 = st.columns([1, 1])
with col1:
    remember = st.checkbox("Remember my login")
with col2:
    st.markdown('<div style="text-align: right; margin-top: 5px;"><a class="forgot-pwd" href="#">Forget My Password</a></div>', unsafe_allow_html=True)

st.markdown("""
    <div class="divider"><span>Other login methods</span></div>
    <div class="ust-btn-container">
        <a class="ust-btn" href="#">@ust.hk</a>
    </div>
""", unsafe_allow_html=True)

# 4. 后台简单逻辑验证
if submit_button:
    if username and password:
        st.success(f"正在尝试登录: {username}")
    else:
        st.error("请输入用户名和密码")
