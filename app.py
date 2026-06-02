import streamlit as st
import streamlit.components.v1 as components

# 1. 设置页面配置（标题和图标）
st.set_page_config(
    page_title="Login - HKUST(GZ)", 
    page_icon="🎓", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. 隐藏 Streamlit 默认的组件（页眉、页脚、主容器边距），实现真正的全屏纯净网页
st.markdown("""
    <style>
        /* 隐藏顶部彩虹条和菜单按钮 */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* 移除 Streamlit 默认给主页面的内边距 */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        
        /* 让 iframe 强制撑满全屏，消除滚动条 */
        iframe {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw !important;
            height: 100vh !important;
            border: none;
            z-index: 999999;
        }
    </style>
""", unsafe_allow_html=True)

# 3. 嵌入复刻好的完整 HTML/CSS 代码
html_code = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }

        body {
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: url('https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1920&q=80') no-repeat center center;
            background-size: cover;
            position: relative;
            overflow: hidden;
        }

        body::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(255, 255, 255, 0.4);
            backdrop-filter: blur(2px);
            z-index: 1;
        }

        .login-container {
            position: relative;
            z-index: 2;
            background: rgba(255, 255, 255, 0.98);
            width: 420px;
            padding: 35px 40px;
            border-radius: 4px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        }

        .brand-header {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 30px;
        }

        .logo-placeholder {
            width: 24px;
            height: 32px;
            background: #b38728;
            border-radius: 2px;
            margin-right: 10px;
            position: relative;
        }
        .logo-placeholder::before {
            content: '';
            position: absolute;
            top: -6px;
            left: 6px;
            width: 12px;
            height: 12px;
            background: #112e51;
            border-radius: 50%;
        }

        .brand-text {
            font-size: 11px;
            color: #112e51;
            font-weight: bold;
            line-height: 1.3;
            letter-spacing: 0.5px;
        }

        h2 {
            font-size: 22px;
            color: #333333;
            margin-bottom: 24px;
            font-weight: 500;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            font-size: 13px;
            color: #555555;
            margin-bottom: 8px;
        }

        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 10px 12px;
            border: 1px solid #dcdfe6;
            border-radius: 4px;
            font-size: 14px;
            color: #333;
            outline: none;
            transition: border-color 0.2s;
        }

        input[type="text"]:focus,
        input[type="password"]:focus {
            border-color: #b38728;
        }

        input::placeholder {
            color: #a8abb2;
            font-size: 13px;
        }

        .btn-submit {
            width: 100%;
            background-color: #946912;
            color: white;
            border: none;
            padding: 12px;
            font-size: 14px;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 4px;
            transition: background-color 0.2s;
        }

        .btn-submit:hover {
            background-color: #7d580f;
        }

        .options-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 16px;
            font-size: 13px;
        }

        .remember-me {
            display: flex;
            align-items: center;
            color: #606266;
            cursor: pointer;
        }

        .remember-me input {
            margin-right: 6px;
            cursor: pointer;
        }

        .forgot-password {
            color: #946912;
            text-decoration: none;
        }

        .forgot-password:hover {
            text-decoration: underline;
        }

        .divider {
            margin: 30px 0 20px 0;
            position: relative;
            text-align: center;
        }

        .divider::before {
            content: "";
            position: absolute;
            left: 0;
            top: 50%;
            width: 100%;
            height: 1px;
            background-color: #e4e7ed;
            z-index: 1;
        }

        .divider span {
            position: relative;
            z-index: 2;
            background-color: #fff;
            padding: 0 15px;
            font-size: 12px;
            color: #909399;
        }

        .other-login-methods {
            display: flex;
            justify-content: center;
        }

        .btn-ust-hk {
            background-color: #a0b2cb;
            color: #ffffff;
            border: none;
            padding: 6px 12px;
            font-size: 11px;
            border-radius: 3px;
            cursor: pointer;
            transition: background-color 0.2s;
        }

        .btn-ust-hk:hover {
            background-color: #899db8;
        }
    </style>
</head>
<body>

    <div class="login-container">
        <div class="brand-header">
            <div class="logo-placeholder"></div>
            <div class="brand-text">
                香港科技大学（广州）<br>
                THE HONG KONG UNIVERSITY OF SCIENCE<br>
                AND TECHNOLOGY (GUANGZHOU)
            </div>
        </div>

        <h2>Login</h2>

        <form onsubmit="event.preventDefault(); alert('Sign in clicked!');">
            <div class="form-group">
                <label for="username">GZ campus username</label>
                <input type="text" id="username" placeholder="without(@hkust-gz.edu.cn)" autocomplete="off">
            </div>

            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" autocomplete="off">
            </div>

            <button type="submit" class="btn-submit">Sign in</button>

            <div class="options-bar">
                <label class="remember-me">
                    <input type="checkbox"> Remember my login
                </label>
                <a href="#" class="forgot-password">Forget My Password</a>
            </div>
        </form>

        <div class="divider">
            <span>Other login methods</span>
        </div>

        <div class="other-login-methods">
            <button class="btn-ust-hk" onclick="alert('Redirecting to @ust.hk login...');">@ust.hk</button>
        </div>
    </div>

</body>
</html>
"""

# 使用 components.v1.html 将写好的前端页面无缝渲染出来
components.html(html_code, height=1000, scrolling=False)
