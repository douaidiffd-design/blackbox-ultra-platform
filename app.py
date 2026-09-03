from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from datetime import datetime

# إنشاء تطبيق السيرفر مع وصف للمشروع
app = FastAPI(
    title="Field Signal Filter API",
    description="سيرفر سحابي متقدم لتصفية، تحليل، وحفظ الإشارات الميدانية مع نظام إحصاءات",
    version="2.0.0"
)

# إعداد قاعدة البيانات المحلية (SQLite)
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

# تشغيل قاعدة البيانات عند بدء السيرفر
init_db()

# هيكل البيانات الواردة
class SignalData(BaseModel):
    signal_value: float
    threshold: float = 5.0

# 1. مسار ترحيبي تجريبي
@app.get("/")
def read_root():
    return {
        "status": "success",
        "message": "مرحباً بك! سيرفر تصفية الإشارات الميدانية يعمل بكامل ميزاته المتقدمة."
    }

# 2. مسار لتصفية وتحليل الإشارة وحفظها في قاعدة البيانات
@app.post("/filter-signal")
def filter_signal(data: SignalData):
    # تصنيف متقدم للإشارة
    if data.signal_value >= data.threshold * 1.5:
        action = "قبول الإشارة (قوية جداً وممتازة)"
    elif data.signal_value >= data.threshold:
        action = "قبول الإشارة (مقبولة)"
    else:
        action = "رفض الإشارة (ضعيفة)"
        
    is_valid = data.signal_value >= data.threshold
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # حفظ السجل في قاعدة البيانات
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO signals (signal_value, threshold, is_valid, action, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (data.signal_value, data.threshold, is_valid, action, timestamp))
        conn.commit()
        conn.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"خطأ في حفظ البيانات: {str(e)}")

    return {
        "status": "success",
        "signal_value": data.signal_value,
        "threshold": data.threshold,
        "is_valid": is_valid,
        "action": action,
        "timestamp": timestamp
    }

# 3. مسار الإحصاءات الفورية
@app.get("/stats")
def get_statistics():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM signals")
    total_signals = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM signals WHERE is_valid = 1")
    accepted_signals = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM signals WHERE is_valid = 0")
    rejected_signals = cursor.fetchone()[0]
    
    conn.close()
    
    return {
        "total_scans": total_signals,
        "accepted_signals": accepted_signals,
        "rejected_signals": rejected_signals,
        "system_status": "يعمل بكفاءة عالية"
    }

# 4. مسار لعرض سجلات الإشارات المحفوظة مسبقاً
@app.get("/history")
def get_history():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # لجلب النتائج على شكل قاموس مرتب
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM signals ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    
    return {
        "recent_signals": [dict(row) for row in rows]
    }