import streamlit as st

st.set_page_config(page_title="أثر | محقق ذكي", page_icon="🔎", layout="wide")

st.markdown("""
<style>
.stApp { background:#07111f; color:#eef4ff; }
.block-container {max-width:1100px; padding-top:2rem;}
h1,h2,h3,p,div {font-family:Arial,sans-serif;}
.hero {background:linear-gradient(135deg,#10243b,#0a1628);border:1px solid #1d3955;border-radius:24px;padding:28px;margin-bottom:20px}
.card {background:#0b1929;border:1px solid #1d344b;border-radius:20px;padding:20px;margin-bottom:18px}
.small {color:#91a8bf}
.score {color:#5eead4;font-weight:800}
.result {background:#0f2237;border:1px solid #24435f;border-radius:15px;padding:16px;margin:10px 0}
.timeline {border-right:2px solid #2b4964;padding-right:18px}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>أثــر <span style="color:#5eead4">•</span></h1>
<h2>محقق ذكي يبحث داخل تسجيلات الفيديو</h2>
<p class="small">اكتب ما تبحث عنه باللغة الطبيعية، ويحوّل أثر الطلب إلى نتائج قابلة للمراجعة مع الوقت والكاميرا والدليل.</p>
</div>
""", unsafe_allow_html=True)

query = st.text_input(
    "🔎 البحث باللغة الطبيعية",
    value="ابحث عن مركبة سوداء بين 10:30 و11:00 قرب البوابة"
)

if st.button("بحث", type="primary", use_container_width=True):
    st.session_state["searched"] = True

col1, col2 = st.columns([2,1])

with col1:
    st.markdown('<div class="card"><h2>🔎 النتائج المطابقة</h2>', unsafe_allow_html=True)
    results = [
        ("مركبة سوداء — CAM-02", "10:36:14 • بوابة الدخول • Track #17", "96%"),
        ("مركبة مشابهة — CAM-04", "10:42:51 • الممر الرئيسي • Track #17", "91%"),
        ("مركبة مشابهة — CAM-05", "10:47:08 • المخرج • Track #17", "87%"),
    ]
    for title, detail, score in results:
        st.markdown(f"""
        <div class="result">
        <b>{title}</b> <span class="score">{score}</span><br>
        <span class="small">{detail}</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h2>🕵️ محقق AI</h2>', unsafe_allow_html=True)
    st.metric("الكاميرات", "06")
    st.metric("الأحداث المفحوصة", "1,248")
    st.metric("المطابقات", "03")
    st.metric("آخر ظهور مرصود", "10:47:08")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="card"><h2>🕒 Timeline</h2><div class="timeline">', unsafe_allow_html=True)
for time, cam, place in [
    ("10:36:14","CAM-02","بوابة الدخول"),
    ("10:42:51","CAM-04","الممر الرئيسي"),
    ("10:47:08","CAM-05","المخرج"),
]:
    st.markdown(f"<p><b>{time}</b><br><span class='small'>{cam} • {place}</span></p>", unsafe_allow_html=True)
st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>🎥 الدليل المحدد</h2>
<div style="height:230px;background:linear-gradient(145deg,#172d42,#050b13);
border-radius:15px;display:flex;align-items:center;justify-content:center;
color:#8fa8bf;font-size:20px;">🎥 معاينة الدليل المرئي</div>
<p class="small">الدليل التجريبي: CAM-05 عند 10:47:08 — Track #17</p>
</div>
""", unsafe_allow_html=True)

st.caption("أثر — نموذج أولي لمفهوم منصة ذكاء التحقيق المرئي")
