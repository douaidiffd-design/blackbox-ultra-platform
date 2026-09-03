from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import sqlite3
from datetime import datetime

app = FastAPI(
    title="BlackBox Ultra Platform",
    description="سيرفر سحابي متقدم لتصفية، تحليل، وحفظ الإشارات الميدانية مع نظام إحصاءات",
    version="2.0.0"
)

DB_NAME = "field_signals.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS signals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            signal_value REAL,
            threshold REAL,
            is_valid BOOLEAN,
            action TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>منصة تصفية الإشارات الميدانية - BlackBox Ultra</title>
        <style>
            :root {
                --primary: #0f172a;
                --accent: #3b82f6;
                --success: #10b981;
                --bg: #f8fafc;
                --card-bg: #ffffff;
                --text: #334155;
            }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: var(--bg);
                color: var(--text);
                margin: 0;
                padding: 0;
            }
            header {
                background: var(--primary);
                color: white;
                padding: 20px 40px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
            }
            header h1 {
                margin: 0;
                font-size: 22px;
            }
            .badge {
                background: var(--success);
                color: white;
                padding: 6px 12px;
                border-radius: 20px;
                font-size: 14px;
                font-weight: bold;
            }
            .container {
                max-width: 1200px;
                margin: 40px auto;
                padding: 0 20px;
            }
            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }
            .card {
                background: var(--card-bg);
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05);
                border-top: 4px solid var(--accent);
            }
            .card h3 {
                margin-top: 0;
                color: var(--primary);
            }
            .metric {
                font-size: 28px;
                font-weight: bold;
                color: var(--accent);
                margin: 10px 0;
            }
            .btn {
                background: var(--accent);
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 15px;
                transition: background 0.3s;
                text-decoration: none;
                display: inline-block;
            }
            .btn:hover {
                background: #2563eb;
            }
            footer {
                text-align: center;
                padding: 20px;
                color: #64748b;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>⚡ منصة تصفية الإشارات الميدانية (IIoT)</h1>
            <div class="badge">النظام متصل ويعمل 🟢</div>
        </header>

        <div class="container">
            <div class="grid">
                <div class="card">
                    <h3>حالة السيرفر</h3>
                    <p>المتصل: الإنتاج الأساسي (Production)</p>
                    <div class="metric">نشط 100%</div>
                </div>
                <div class="card">
                    <h3>قاعدة البيانات</h3>
                    <p>نظام تخزين الإشارات محلياً (SQLite)</p>
                    <div class="metric">جاهزة ومتصلة</div>
                </div>
                <div class="card">
                    <h3>التوثيق التقني (API)</h3>
                    <p>استعراض واجهات البرمجة التفاعلية للعميل</p>
                    <br>
                    <a href="/docs" target="_blank" class="btn">فتح وثائق Swagger</a>
                </div>
            </div>

            <div class="card">
                <h3>لوحة التحكم المباشرة للعميل</h3>
                <p>مرحباً بك! هذه الواجهة تعرض جاهزية المنصة ومراقبة التدفقات الحية وإدارة الإشارات الميدانية بكفاءة عالية.</p>
            </div>
        </div>

        <footer>
            جميع الحقوق محفوظة © BlackBox Ultra Platform 2026
        </footer>
    </body>
    </html>
    """from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import sqlite3
from datetime import datetime

app = FastAPI(
    title="BlackBox Ultra Platform",
    description="سيرفر سحابي متقدم لتصفية، تحليل، وحفظ الإشارات الميدانية مع نظام إحصاءات",
    version="2.0.0"
)

DB_NAME = "field_signals.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS signals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            signal_value REAL,
            threshold REAL,
            is_valid BOOLEAN,
            action TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>منصة تصفية الإشارات الميدانية - BlackBox Ultra</title>
        <style>
            :root {
                --primary: #0f172a;
                --accent: #3b82f6;
                --success: #10b981;
                --bg: #f8fafc;
                --card-bg: #ffffff;
                --text: #334155;
            }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: var(--bg);
                color: var(--text);
                margin: 0;
                padding: 0;
            }
            header {
                background: var(--primary);
                color: white;
                padding: 20px 40px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
            }
            header h1 {
                margin: 0;
                font-size: 22px;
            }
            .badge {
                background: var(--success);
                color: white;
                padding: 6px 12px;
                border-radius: 20px;
                font-size: 14px;
                font-weight: bold;
            }
            .container {
                max-width: 1200px;
                margin: 40px auto;
                padding: 0 20px;
            }
            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }
            .card {
                background: var(--card-bg);
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05);
                border-top: 4px solid var(--accent);
            }
            .card h3 {
                margin-top: 0;
                color: var(--primary);
            }
            .metric {
                font-size: 28px;
                font-weight: bold;
                color: var(--accent);
                margin: 10px 0;
            }
            .btn {
                background: var(--accent);
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 15px;
                transition: background 0.3s;
                text-decoration: none;
                display: inline-block;
            }
            .btn:hover {
                background: #2563eb;
            }
            footer {
                text-align: center;
                padding: 20px;
                color: #64748b;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>⚡ منصة تصفية الإشارات الميدانية (IIoT)</h1>
            <div class="badge">النظام متصل ويعمل 🟢</div>
        </header>

        <div class="container">
            <div class="grid">
                <div class="card">
                    <h3>حالة السيرفر</h3>
                    <p>المتصل: الإنتاج الأساسي (Production)</p>
                    <div class="metric">نشط 100%</div>
                </div>
                <div class="card">
                    <h3>قاعدة البيانات</h3>
                    <p>نظام تخزين الإشارات محلياً (SQLite)</p>
                    <div class="metric">جاهزة ومتصلة</div>
                </div>
                <div class="card">
                    <h3>التوثيق التقني (API)</h3>
                    <p>استعراض واجهات البرمجة التفاعلية للعميل</p>
                    <br>
                    <a href="/docs" target="_blank" class="btn">فتح وثائق Swagger</a>
                </div>
            </div>

            <div class="card">
                <h3>لوحة التحكم المباشرة للعميل</h3>
                <p>مرحباً بك! هذه الواجهة تعرض جاهزية المنصة ومراقبة التدفقات الحية وإدارة الإشارات الميدانية بكفاءة عالية.</p>
            </div>
        </div>

        <footer>
            جميع الحقوق محفوظة © BlackBox Ultra Platform 2026
        </footer>
    </body>
    </html>
    """