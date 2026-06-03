import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# 1. 初始化全屏配置
st.set_page_config(
    page_title="HKUST(GZ) Portal", 
    page_icon="🎓", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. 全局注入 CSS 确保 iframe 铺满全屏
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

# ⚙️ 核心修复：现在图片移到了外面，我们直接在根目录下读取 "logo_white.png"
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
            ext = image_path.split(".")[-1].lower()
            if ext in ["jpg", "jpeg"]:
                return f"data:image/jpeg;base64,{encoded}"
            else:
                return f"data:image/png;base64,{encoded}"
    else:
        # 如果找不到本地图片，返回一个在线备用提示图，确保系统不崩溃
        return "https://via.placeholder.com/150x38/004b93/ffffff?text=Logo+Not+Found"

# 🔍 路径已更新：直接读取根目录下的文件名
logo_path = "logo_white.png" 
logo_base64 = get_base64_image(logo_path)

# 3. 将所有页面写在同一个 HTML 中，通过 JS 实现纯前端页面无感切换
monolithic_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HKUST(GZ) Portal</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        
        /* ==================== 页面 1：高保真登录页样式 ==================== */
        #login-page {
            height: 100vh; display: flex; justify-content: center; align-items: center;
            background: url('https://cdn.i-scmp.com/sites/default/files/styles/1200x800/public/d8/images/methode/2021/05/19/eac9bf90-b7e2-11eb-9461-e80e43f535ad_image_hires_163959.jpg?itok=ZKnOYwta&v=1621413607') no-repeat center center;
            background-size: cover; position: relative; overflow: hidden;
        }
        #login-page::before {
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
        .brand-text { font-size: 11px; color: #112e51; font-weight: bold; line-height: 1.3; letter-spacing: 0.5px; text-align: left; }
        .login-container h2 { font-size: 22px; color: #333333; margin-bottom: 24px; font-weight: 500; }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; font-size: 13px; color: #555555; margin-bottom: 8px; text-align: left; }
        .form-group input {
            width: 100%; padding: 10px 12px; border: 1px solid #dcdfe6; border-radius: 4px; font-size: 14px; color: #333; outline: none; transition: border-color 0.2s;
        }
        .form-group input:focus { border-color: #b38728; }
        .form-group input::placeholder { color: #a8abb2; font-size: 13px; }
        .btn-submit {
            width: 100%; background-color: #946912; color: white; border: none; padding: 12px; font-size: 14px; border-radius: 4px; cursor: pointer; margin-top: 4px; font-weight: 600;
        }
        .btn-submit:hover { background-color: #7d580f; }
        .options-bar { display: flex; justify-content: space-between; align-items: center; margin-top: 16px; font-size: 13px; color: #606266; }
        .divider { margin: 30px 0 20px 0; position: relative; text-align: center; }
        .divider::before { content: ""; position: absolute; left: 0; top: 50%; width: 100%; height: 1px; background-color: #e4e7ed; z-index: 1; }
        .divider span { position: relative; z-index: 2; background-color: #fff; padding: 0 15px; font-size: 12px; color: #909399; }
        .btn-ust-hk { background-color: #a0b2cb; color: #ffffff; border: none; padding: 6px 12px; font-size: 11px; border-radius: 3px; cursor: pointer; display: block; margin: 0 auto; }

        /* ==================== 页面 2 & 3：公用深蓝色页眉 ==================== */
        body { background-color: #f4f6f9; min-height: 100vh; }
        .header-bar {
            background-color: #004b93; height: 60px; display: flex; align-items: center; justify-content: space-between; padding: 0 30px; color: white;
        }
        .left-section { display: flex; align-items: center; }
        
        /* 学校真实 Logo 的自适应样式 */
        .uni-logo {
            height: 36px;
            width: auto;
            display: block;
            object-fit: contain;
        }
        
        .vertical-divider { width: 1px; height: 30px; background-color: rgba(255,255,255,0.3); margin: 0 18px; }
        .sys-title-en { font-size: 16px; font-weight: 600; letter-spacing: 0.2px; }
        .right-section { display: flex; align-items: center; gap: 24px; }
        .nav-icon { fill: white; width: 18px; height: 18px; opacity: 0.95; cursor: pointer; }
        .user-profile { display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 500; }
        .caret-down { border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 4px solid white; margin-left: 2px; }

        /* ==================== 页面 2：财务报表页样式 ==================== */
        .main-content { padding: 50px 40px; max-width: 900px; margin: 0 auto; width: 100%; text-align: left; }
        .page-title { font-size: 22px; color: #111; margin-bottom: 30px; font-weight: 600; display: flex; align-items: center; gap: 10px; }
        .page-title::before { content: ''; display: inline-block; width: 4px; height: 20px; background-color: #004b93; border-radius: 2px; }
        .table-container { background: white; border-radius: 6px; box-shadow: 0 2px 12px rgba(0,0,0,0.04); border: 1px solid #eef2f5; overflow: hidden; margin-bottom: 35px; }
        table { width: 100%; border-collapse: collapse; text-align: left; font-size: 14px; }
        th { background-color: #f8fafc; color: #475569; font-weight: 600; padding: 16px 24px; border-bottom: 1px solid #eef2f5; font-size: 13px; text-transform: uppercase; }
        td { padding: 18px 24px; border-bottom: 1px solid #f1f5f9; color: #334155; }
        tr:last-child td { border-bottom: none; }
        .action-area { display: flex; justify-content: center; margin-top: 10px; }
        .btn-pay {
            background-color: #946912; color: white; border: none; padding: 14px 55px; font-size: 15px; border-radius: 4px; cursor: pointer; font-weight: 600; box-shadow: 0 2px 6px rgba(148, 105, 18, 0.2);
        }
        .btn-pay:hover { background-color: #7d580f; }

        /* ==================== 页面 3：二维码缴费页样式 ==================== */
        .payment-card { background: white; border-radius: 8px; width: 100%; padding: 40px; box-shadow: 0 4px 16px rgba(0,0,0,0.05); border: 1px solid #eef2f5; text-align: center; margin-bottom: 40px; }
        .section-title { font-size: 20px; color: #111; font-weight: 600; margin-bottom: 24px; }
        .info-row { display: flex; justify-content: space-between; padding: 12px 0; border-bottom: 1px dashed #e2e8f0; font-size: 14px; color: #475569; }
        .info-row:last-of-type { border-bottom: none; margin-bottom: 20px; }
        .info-value { font-weight: 600; color: #111; }
        .info-value.amount { color: #946912; font-size: 18px; }
        .qr-container { background-color: #f8fafc; border: 1px solid #e2e8f0; padding: 20px; border-radius: 6px; display: inline-block; margin: 15px 0; }
        .qr-code { width: 180px; height: 180px; display: flex; align-items: center; justify-content: center; background: #fff; border: 1px solid #cbd5e1; position: relative; margin: 0 auto; }
        .qr-code::before { content: 'QR CODE'; font-size: 11px; color: #94a3b8; font-weight: 600; }
        .qr-tip { font-size: 12px; color: #64748b; margin-top: 10px; line-height: 1.4; }
        .support-footer { font-size: 13px; color: #64748b; text-align: center; margin-top: auto; padding-bottom: 20px; line-height: 1.5; width: 100%; }
        .support-footer a { color: #004b93; text-decoration: none; font-weight: 500; }
        .support-footer a:hover { text-decoration: underline; }
    </style>
</head>
<body>

    <div id="login-page">
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
                    <label>Campus username</label>
                    <input type="text" id="username" placeholder="Payment Number" required autocomplete="off">
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <input type="password" id="password" required autocomplete="off">
                </div>
                <button type="submit" class="btn-submit">Sign in</button>
                <div class="options-bar">
                    <label><input type="checkbox" style="margin-right: 5px;"> Remember my login</label>
                    <a href="#" style="color: #946912; text-decoration: none;">Forget My Password</a>
                </div>
            </form>
        </div>
    </div>

    <div id="finance-page" style="display: none;">
        <div class="header-bar">
            <div class="left-section">
                <img class="uni-logo" src="THE_LOGO_WILL_BE_INJECTED_HERE_A" alt="HKUST(GZ) Logo">
                
                <div class="vertical-divider"></div>
                
                <div class="sys-title-container">
                    <div class="sys-title-en">Student Finance System</div>
                </div>
            </div>
            <div class="right-section">
                <svg class="nav-icon" viewBox="0 0 24 24" onclick="showPage('finance-page')"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
                <svg class="nav-icon" viewBox="0 0 24 24" onclick="showPage('finance-page')"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
                <div class="user-profile">
                    <span>Tao Ge</span>
                    <span class="caret-down"></span>
                </div>
            </div>
        </div>

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
                            <td style="font-weight: 500;">Tao Ge</td>
                            <td>Admission Deposit</td>
                            <td style="color: #d9534f; font-weight: 500;">June 30, 2026</td>
                            <td style="font-weight: 600; color: #111;">¥ 20,000.00</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="action-area">
                <button class="btn-pay" id="payNowBtn">Pay Now</button>
            </div>
        </div>
    </div>

    <div id="payment-page" style="display: none;">
        <div class="header-bar">
            <div class="left-section">
                <img class="uni-logo" src="THE_LOGO_WILL_BE_INJECTED_HERE_B" alt="HKUST(GZ) Logo">
                <div class="vertical-divider"></div>
                <div class="sys-title-container">
                    <div class="sys-title-en">Student Finance System</div>
                </div>
            </div>
            <div class="right-section">
                <svg class="nav-icon" viewBox="0 0 24 24" onclick="showPage('finance-page')"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
                <svg class="nav-icon" viewBox="0 0 24 24" onclick="showPage('finance-page')"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
                <div class="user-profile">
                    <span>Tao Ge</span>
                    <span class="caret-down"></span>
                </div>
            </div>
        </div>

        <div class="main-content" style="max-width: 700px;">
            <div class="payment-card">
                <div class="section-title">Payment Information</div>
                <div class="info-row">
                    <span>Student Name:</span>
                    <span class="info-value">Tao Ge</span>
                </div>
                <div class="info-row">
                    <span>Fee Type:</span>
                    <span class="info-value">Admission Deposit</span>
                </div>
                <div class="info-row">
                    <span>Amount Due:</span>
                    <span class="info-value amount">¥ 20,000.00</span>
                </div>
                <div class="qr-container">
                    <div class="qr-code">
                        <div style="position: absolute; top:0; left:0; width:30px; height:30px; border-bottom:4px solid #004b93; border-right:4px solid #004b93;"></div>
                        <div style="position: absolute; bottom:0; right:0; width:30px; height:30px; border-top:4px solid #004b93; border-left:4px solid #004b93;"></div>
                    </div>
                    <p class="qr-tip">Please scan this QR code to complete your payment transaction securely.</p>
                </div>
            </div>
            <div class="support-footer">
                If you have any questions regarding your payment, please contact us at: <br>
                <a href="mailto:admit@hkust.com">admit@hkust.com</a>
            </div>
        </div>
    </div>

    <script>
        function showPage(pageId) {
            document.getElementById('login-page').style.display = 'none';
            document.getElementById('finance-page').style.display = 'none';
            document.getElementById('payment-page').style.display = 'none';
            
            if(pageId === 'login-page') {
                document.getElementById('login-page').style.display = 'flex';
            } else {
                document.getElementById(pageId).style.display = 'block';
            }
        }

        document.getElementById('loginForm').addEventListener('submit', function(e) {
            e.preventDefault();
            var userVal = document.getElementById('username').value.trim();
            var passVal = document.getElementById('password').value;

            if (userVal === "11760523" && passVal === "tg-hkust2027") {
                showPage('finance-page');
            } else {
                alert("Invalid username or password! Please check your credentials.");
            }
        });

        document.getElementById('payNowBtn').addEventListener('click', function() {
            showPage('payment-page');
        });
    </script>
</body>
</html>
"""

# 安全替换占位符
monolithic_html = monolithic_html.replace("THE_LOGO_WILL_BE_INJECTED_HERE_A", logo_base64)
monolithic_html = monolithic_html.replace("THE_LOGO_WILL_BE_INJECTED_HERE_B", logo_base64)

components.html(monolithic_html, height=1200, scrolling=False)
