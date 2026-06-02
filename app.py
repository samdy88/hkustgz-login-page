import streamlit as st
import streamlit.components.v1 as components

# 1. Setup clean seamless page layout
st.set_page_config(
    page_title="HKUST(GZ) Portal", 
    page_icon="🎓", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. Inject global CSS to completely hide Streamlit headers/footers for a pure native web feel
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
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

# 3. Simple State Routing Management
if 'page' not in st.session_state:
    st.session_state.page = 'login'

# Read query parameters from iframe redirect trigger
query_params = st.query_params
if 'view' in query_params:
    st.session_state.page = query_params['view']

# --- View Routing Engine ---
if st.session_state.page == 'login':
    # --- VIEW A: REPLICATED LOGIN PAGE ---
    login_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login - HKUST(GZ)</title>
        <style>
            * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
            body {
                height: 100vh; display: flex; justify-content: center; align-items: center;
                background: url('https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1920&q=80') no-repeat center center;
                background-size: cover; position: relative; overflow: hidden;
            }
            body::before {
                content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
                background: rgba(255, 255, 255, 0.4); backdrop-filter: blur(2px); z-index: 1;
            }
            .login-container {
                position: relative; z-index: 2; background: rgba(255, 255, 255, 0.98);
                width: 420px; padding: 35px 40px; border-radius: 4px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            }
            .brand-header { display: flex; align-items: center; justify-content: center; margin-bottom: 30px; }
            .logo-placeholder {
                width: 24px; height: 32px; background: #b38728; border-radius: 2px; margin-right: 10px; position: relative;
            }
            .logo-placeholder::before {
                content: ''; position: absolute; top: -6px; left: 6px; width: 12px; height: 12px; background: #112e51; border-radius: 50%;
            }
            .brand-text { font-size: 11px; color: #112e51; font-weight: bold; line-height: 1.3; letter-spacing: 0.5px; }
            h2 { font-size: 22px; color: #333333; margin-bottom: 24px; font-weight: 500; }
            .form-group { margin-bottom: 20px; }
            label { display: block; font-size: 13px; color: #555555; margin-bottom: 8px; }
            input[type="text"], input[type="password"] {
                width: 100%; padding: 10px 12px; border: 1px solid #dcdfe6; border-radius: 4px; font-size: 14px; color: #333; outline: none;
            }
            input[type="text"]:focus, input[type="password"]:focus { border-color: #b38728; }
            input::placeholder { color: #a8abb2; font-size: 13px; }
            .btn-submit {
                width: 100%; background-color: #946912; color: white; border: none; padding: 12px; font-size: 14px; border-radius: 4px; cursor: pointer; margin-top: 4px;
            }
            .btn-submit:hover { background-color: #7d580f; }
            .options-bar { display: flex; justify-content: space-between; align-items: center; margin-top: 16px; font-size: 13px; }
            .remember-me { display: flex; align-items: center; color: #606266; cursor: pointer; }
            .remember-me input { margin-right: 6px; }
            .forgot-password { color: #946912; text-decoration: none; }
            .forgot-password:hover { text-decoration: underline; }
            .divider { margin: 30px 0 20px 0; position: relative; text-align: center; }
            .divider::before { content: ""; position: absolute; left: 0; top: 50%; width: 100%; height: 1px; background-color: #e4e7ed; z-index: 1; }
            .divider span { position: relative; z-index: 2; background-color: #fff; padding: 0 15px; font-size: 12px; color: #909399; }
            .other-login-methods { display: flex; justify-content: center; }
            .btn-ust-hk { background-color: #a0b2cb; color: #ffffff; border: none; padding: 6px 12px; font-size: 11px; border-radius: 3px; cursor: pointer; }
        </style>
    </head>
    <body>
        <div class="login-container">
            <div class="brand-header">
                <div class="logo-placeholder"></div>
                <div class="brand-text">
                    THE HONG KONG UNIVERSITY OF SCIENCE<br>
                    AND TECHNOLOGY (GUANGZHOU)
                </div>
            </div>
            <h2>Login</h2>
            <form id="loginForm">
                <div class="form-group">
                    <label for="username">GZ campus username</label>
                    <input type="text" id="username" placeholder="without(@hkust-gz.edu.cn)" required autocomplete="off">
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" required autocomplete="off">
                </div>
                <button type="submit" class="btn-submit">Sign in</button>
                <div class="options-bar">
                    <label class="remember-me"><input type="checkbox"> Remember my login</label>
                    <a href="#" class="forgot-password">Forget My Password</a>
                </div>
            </form>
            <div class="divider"><span>Other login methods</span></div>
            <div class="other-login-methods"><button class="btn-ust-hk" type="button">@ust.hk</button></div>
        </div>
        <script>
            document.getElementById('loginForm').addEventListener('submit', function(e) {
                e.preventDefault();
                window.top.location.href = window.top.location.pathname + "?view=finance";
            });
        </script>
    </body>
    </html>
    """
    components.html(login_html, height=1000, scrolling=False)

else:
    # --- VIEW B: STUDENT FINANCE SYSTEM PAGE ---
    finance_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Student Finance System</title>
        <style>
            * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
            body { background-color: #f4f6f9; min-height: 100vh; display: flex; flex-direction: column; }
            
            /* High Fidelity Header matching screenshot */
            .header-bar {
                background-color: #004b93; 
                height: 60px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0 30px;
                color: white;
            }
            .left-section { display: flex; align-items: center; }
            .logo-container { display: flex; align-items: center; }
            .mini-crest {
                width: 20px; height: 26px; background: white; border-radius: 1px; margin-right: 8px; position: relative;
            }
            .mini-crest::before {
                content: ''; position: absolute; top: -4px; left: 5px; width: 10px; height: 10px; background: #b38728; border-radius: 50%;
            }
            .uni-title-en { font-size: 10px; font-weight: bold; line-height: 1.15; letter-spacing: 0.1px; color: #ffffff; }
            .vertical-divider { width: 1px; height: 30px; background-color: rgba(255,255,255,0.3); margin: 0 18px; }
            .sys-title-container { display: flex; flex-direction: column; }
            .sys-title-en { font-size: 16px; font-weight: 600; letter-spacing: 0.2px; }
            
            .right-section { display: flex; align-items: center; gap: 24px; }
            .nav-icon { fill: white; width: 18px; height: 18px; opacity: 0.95; cursor: pointer; }
            .user-profile { display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 500; cursor: pointer; }
            .caret-down { border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 4px solid white; margin-left: 2px; }

            /* Dashboard Main Content Area */
            .main-content { padding: 50px 40px; max-width: 1000px; margin: 0 auto; width: 100%; flex: 1; }
            .page-title { font-size: 22px; color: #111; margin-bottom: 30px; font-weight: 600; display: flex; align-items: center; gap: 10px; }
            .page-title::before { content: ''; display: inline-block; width: 4px; height: 20px; background-color: #004b93; border-radius: 2px; }
            
            /* Clean Table Container */
            .table-container { background: white; border-radius: 6px; box-shadow: 0 2px 12px rgba(0,0,0,0.04); border: 1px solid #eef2f5; overflow: hidden; margin-bottom: 35px; }
            table { width: 100%; border-collapse: collapse; text-align: left; font-size: 14px; }
            th { background-color: #f8fafc; color: #475569; font-weight: 600; padding: 16px 24px; border-bottom: 1px solid #eef2f5; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; }
            td { padding: 18px 24px; border-bottom: 1px solid #f1f5f9; color: #334155; font-size: 14px; }
            tr:last-child td { border-bottom: none; }
            
            /* Action Button Centering and Styling */
            .action-area { display: flex; justify-content: center; margin-top: 10px; }
            .btn-pay {
                background-color: #946912; /* Golden Amber Theme Color */
                color: white; 
                border: none; 
                padding: 14px 45px; 
                font-size: 15px; 
                border-radius: 4px; 
                cursor: pointer; 
                font-weight: 600;
                box-shadow: 0 2px 6px rgba(148, 105, 18, 0.2);
                transition: background 0.2s, transform 0.1s;
            }
            .btn-pay:hover { background-color: #7d580f; }
            .btn-pay:active { transform: scale(0.98); }

            .logout-btn { font-size: 11px; opacity: 0.6; text-decoration: none; color: white; margin-left: 5px;}
            .logout-btn:hover { opacity: 1; text-decoration: underline;}
        </style>
    </head>
    <body>
        <div class="header-bar">
            <div class="left-section">
                <div class="logo-container">
                    <div class="mini-crest"></div>
                    <div class="uni-title-en">THE HONG KONG<br>UNIVERSITY OF SCIENCE AND<br>TECHNOLOGY (GUANGZHOU)</div>
                </div>
                <div class="vertical-divider"></div>
                <div class="sys-title-container">
                    <div class="sys-title-en">Student Finance System</div>
                </div>
            </div>
            <div class="right-section">
                <svg class="nav-icon" viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-
