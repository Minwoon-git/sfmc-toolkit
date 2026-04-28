import streamlit as st

st.set_page_config(
    page_title="SFMC Toolkit",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', system-ui, sans-serif;
}

.stApp {
    background-color: #f8fafc;
    color: #1e293b;
}

/* ── 사이드바 ── */
section[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 0.5px solid #e2e8f0;
}
section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] label {
    color: #64748b;
    font-size: 11px;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}
section[data-testid="stSidebar"] input {
    color: #1e293b !important;
    background-color: #f8fafc !important;
    border: 0.5px solid #e2e8f0 !important;
    border-radius: 8px !important;
    font-size: 13px !important;
}
section[data-testid="stSidebar"] .stRadio label {
    color: #1e293b !important;
    font-size: 13px !important;
    text-transform: none !important;
    letter-spacing: 0 !important;
    font-weight: 400 !important;
}
section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label p {
    color: #1e293b !important;
    font-size: 13px !important;
    text-transform: none !important;
    letter-spacing: 0 !important;
}
section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label[data-baseweb="radio"] {
    padding: 6px 8px !important;
    border-radius: 8px !important;
}

/* ── 사이드바 커스텀 클래스 ── */
.sidebar-title {
    font-size: 15px;
    font-weight: 600;
    color: #0f172a;
    letter-spacing: -0.01em;
    margin-bottom: 2px;
}
.sidebar-sub {
    font-size: 11px;
    color: #94a3b8;
    margin-bottom: 24px;
}
.status-ok {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 12px;
    color: #15803d;
    background: #f0fdf4;
    border: 0.5px solid #bbf7d0;
    border-radius: 6px;
    padding: 5px 10px;
    margin-top: 4px;
    margin-bottom: 12px;
}

/* ── 페이지 헤더 ── */
.page-header {
    margin-bottom: 24px;
    padding-bottom: 18px;
    border-bottom: 0.5px solid #e2e8f0;
}
.page-title {
    font-size: 22px;
    font-weight: 600;
    color: #0f172a;
    letter-spacing: -0.02em;
    margin-bottom: 4px;
}
.page-desc {
    font-size: 13px;
    color: #94a3b8;
    line-height: 1.6;
}

/* ── 결과 박스 ── */
.result-box {
    background: #f8fafc;
    border: 0.5px solid #e2e8f0;
    border-left: 3px solid #2563eb;
    border-radius: 0 8px 8px 0;
    padding: 16px 18px;
    margin-top: 12px;
    font-size: 13px;
    line-height: 1.8;
    color: #334155;
    white-space: pre-wrap;
}
.result-label {
    font-size: 10px;
    font-weight: 600;
    color: #2563eb;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 8px;
}

/* ── 태그/배지 ── */
.tag { display:inline-block;font-size:10px;padding:2px 8px;border-radius:4px;font-weight:500;letter-spacing:0.04em;text-transform:uppercase; }
.tag-blue  { background:#eff6ff;color:#1d4ed8;border:0.5px solid #bfdbfe; }
.tag-green { background:#f0fdf4;color:#15803d;border:0.5px solid #bbf7d0; }
.tag-amber { background:#fffbeb;color:#b45309;border:0.5px solid #fde68a; }
.tag-red   { background:#fef2f2;color:#b91c1c;border:0.5px solid #fecaca; }

/* ── 입력 요소 ── */
div[data-testid="stTextArea"] textarea {
    background: #ffffff !important;
    border: 0.5px solid #e2e8f0 !important;
    border-radius: 8px !important;
    color: #1e293b !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 13px !important;
    line-height: 1.6 !important;
}
div[data-testid="stTextArea"] textarea:focus {
    border-color: #2563eb !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.08) !important;
}
div[data-testid="stTextInput"] input {
    background: #ffffff !important;
    border: 0.5px solid #e2e8f0 !important;
    border-radius: 8px !important;
    color: #1e293b !important;
    font-size: 13px !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color: #2563eb !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.08) !important;
}
div[data-testid="stSelectbox"] > div {
    background: #ffffff !important;
    border: 0.5px solid #e2e8f0 !important;
    border-radius: 8px !important;
    color: #1e293b !important;
    font-size: 13px !important;
}

/* ── 버튼 ── */
.stButton > button {
    background: #2563eb !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    font-size: 13px !important;
    padding: 7px 16px !important;
    transition: background 0.15s !important;
    box-shadow: none !important;
}
.stButton > button:hover {
    background: #1d4ed8 !important;
}
.stButton > button[data-testid="baseButton-secondary"] {
    background: #f1f5f9 !important;
    color: #475569 !important;
    border: 0.5px solid #e2e8f0 !important;
    font-size: 12px !important;
    padding: 6px 12px !important;
}
.stButton > button[data-testid="baseButton-secondary"]:hover {
    background: #e2e8f0 !important;
    color: #1e293b !important;
}

/* ── 탭 ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 0;
    border-bottom: 0.5px solid #e2e8f0;
    background: transparent;
}
.stTabs [data-baseweb="tab"] {
    font-size: 13px !important;
    color: #94a3b8 !important;
    padding: 8px 16px !important;
    background: transparent !important;
    border-bottom: 2px solid transparent !important;
    font-weight: 400 !important;
}
.stTabs [aria-selected="true"] {
    color: #1d4ed8 !important;
    border-bottom-color: #2563eb !important;
    font-weight: 500 !important;
    background: transparent !important;
}
.stTabs [data-baseweb="tab-highlight"] { display: none !important; }
.stTabs [data-baseweb="tab-border"] { display: none !important; }

/* ── 익스팬더 ── */
.stExpander {
    border: 0.5px solid #e2e8f0 !important;
    border-radius: 10px !important;
    background: #fff !important;
    margin-bottom: 8px !important;
}
.stExpander summary {
    font-size: 13px !important;
    font-weight: 500 !important;
    color: #1e293b !important;
}

/* ── 체크박스 ── */
.stCheckbox label {
    font-size: 13px !important;
    color: #475569 !important;
}

/* ── 라벨 ── */
label[data-testid="stWidgetLabel"] {
    color: #64748b !important;
    font-size: 11px !important;
    font-weight: 500 !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase !important;
}

/* ── 스피너 ── */
.stSpinner > div { border-top-color: #2563eb !important; }

/* ── 점검탭 버튼 소형화 ── */
button[key="chk_sel_all"], button[key="chk_sel_all2"],
button[key="chk_bulk_del"], button[key="chk_sel_none"], button[key="chk_sel_none2"] {
    padding: 5px 12px !important;
    font-size: 12px !important;
    white-space: nowrap !important;
}
button[key^="toggle_"] {
    padding: 2px 8px !important;
    font-size: 11px !important;
    background: transparent !important;
    border: none !important;
    color: inherit !important;
}

/* ── 구분선 ── */
hr { border-color: #e2e8f0 !important; margin: 16px 0 !important; }

/* ── 메모 카드 ── */
.memo-card {
    background: #ffffff;
    border: 0.5px solid #e2e8f0;
    border-left: 2px solid #2563eb;
    border-radius: 0 8px 8px 0;
    padding: 14px 16px;
    margin-bottom: 10px;
}
.memo-meta { font-size: 11px; color: #94a3b8; margin-bottom: 6px; }
.memo-content { font-size: 13px; color: #475569; line-height: 1.6; }
.memo-summary {
    font-size: 12px; color: #2563eb; margin-top: 8px;
    padding-top: 8px; border-top: 0.5px solid #e2e8f0; line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# ── JWT 자동 연결 (Cloudflare Worker에서 전달된 경우) ───────────────────────
import requests as _req

def _jwt_auto_connect():
    """URL 파라미터로 전달된 JWT로 SFMC 자동 연결"""
    if st.session_state.get("sfmc_token"):
        return  # 이미 연결됨

    params = st.query_params
    jwt_token = params.get("jwt", "")
    if not jwt_token:
        return

    try:
        import base64, json as _json

        # JWT 디코딩 (페이로드 부분)
        parts = jwt_token.split(".")
        if len(parts) < 2:
            return

        payload_b64 = parts[1]
        # base64 패딩 맞추기
        payload_b64 += "=" * (4 - len(payload_b64) % 4)
        payload = _json.loads(base64.b64decode(payload_b64).decode("utf-8"))

        # JWT에서 필요한 정보 추출
        rest_base = payload.get("rest", "") or payload.get("restInstanceUrl", "")
        soap_base = payload.get("soap", "") or payload.get("soapInstanceUrl", "")
        org_id = payload.get("org", "") or payload.get("organizationId", "")

        # access_token이 JWT 자체인 경우
        if rest_base:
            st.session_state["sfmc_token"] = jwt_token
            st.session_state["sfmc_rest_base"] = rest_base.rstrip("/")
            # subdomain 추출 (rest_base에서)
            import re
            m = re.search(r'https://([^.]+)\.rest\.', rest_base)
            if m:
                st.session_state["sfmc_subdomain"] = m.group(1)
            st.session_state["sfmc_web_url"] = ""
            st.session_state["sfmc_jwt_auto"] = True

    except Exception:
        pass  # JWT 파싱 실패 시 수동 입력으로 fallback

_jwt_auto_connect()

# ── Streamlit Secrets 자동 연결 ─────────────────────────────────────────────
def _secrets_auto_connect():
    """Streamlit Cloud Secrets에 SFMC 정보가 있으면 자동 연결"""
    if st.session_state.get("sfmc_token"):
        return
    try:
        client_id     = st.secrets.get("SFMC_CLIENT_ID", "")
        client_secret = st.secrets.get("SFMC_CLIENT_SECRET", "")
        subdomain     = st.secrets.get("SFMC_SUBDOMAIN", "")
        web_url       = st.secrets.get("SFMC_WEB_URL", "")

        if not (client_id and client_secret and subdomain):
            return

        auth_url = f"https://{subdomain}.auth.marketingcloudapis.com/v2/token"
        resp = _req.post(auth_url, json={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret
        }, timeout=10)

        if resp.status_code == 200:
            data = resp.json()
            st.session_state["sfmc_token"]         = data["access_token"]
            st.session_state["sfmc_rest_base"]     = f"https://{subdomain}.rest.marketingcloudapis.com"
            st.session_state["sfmc_subdomain"]     = subdomain
            st.session_state["sfmc_client_id"]     = client_id
            st.session_state["sfmc_client_secret"] = client_secret
            st.session_state["sfmc_web_url"]       = web_url.rstrip("/") if web_url else ""
            st.session_state["sfmc_auto_secret"]   = True
    except Exception:
        pass

_secrets_auto_connect()

# ── Sidebar ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-title">⚡ SFMC Toolkit</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-sub">by AI · v1.0</div>', unsafe_allow_html=True)

    ai_provider = st.selectbox(
        "AI 제공사",
        ["Anthropic", "OpenAI", "Gemini"],
        label_visibility="collapsed"
    )

    api_key, openai_key, gemini_key = "", "", ""

    if ai_provider == "Anthropic":
        api_key = st.text_input(
            "Anthropic API Key",
            type="password",
            placeholder="sk-ant-...",
            help="console.anthropic.com에서 발급"
        )
    elif ai_provider == "OpenAI":
        openai_key = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="sk-...",
            help="platform.openai.com에서 발급 (gpt-4o-mini)"
        )
    elif ai_provider == "Gemini":
        gemini_key = st.text_input(
            "Gemini API Key",
            type="password",
            placeholder="AIza...",
            help="aistudio.google.com에서 발급 (무료 티어 지원)"
        )

    # 활성 키 감지
    active_ai = None
    if api_key:
        active_ai = "anthropic"
    elif openai_key:
        active_ai = "openai"
    elif gemini_key:
        active_ai = "gemini"

    if active_ai:
        label = {"anthropic":"Anthropic","openai":"OpenAI","gemini":"Gemini"}[active_ai]
        st.markdown(f'<div class="status-ok">● {label} 연결됨</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**도구 선택**")

    menu = st.radio(
        "",
        ["🗂️ Journey 관리", "💾 Query 생성기", "🔍 Error 분석기"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("**SFMC 연동**")
    sfmc_client_id = st.text_input("Client ID", placeholder="7r72av...", type="password")
    sfmc_client_secret = st.text_input("Client Secret", placeholder="SFMC_...", type="password")
    sfmc_subdomain = st.text_input("Subdomain", placeholder="mc82m0sycp8ynx4fqynw-63lx470")
    sfmc_web_url = st.text_input(
        "SFMC 웹 URL (선택)",
        placeholder="https://mc.s10.exacttarget.com",
        help="브라우저에서 SFMC 로그인 후 주소창의 https://mc.sXX.exacttarget.com 부분만 복사해서 입력하세요. Journey 바로가기 링크에 사용됩니다."
    )

    if st.button("🔗 SFMC 연결"):
        if not sfmc_client_id or not sfmc_client_secret or not sfmc_subdomain:
            st.error("Client ID, Secret, Subdomain을 모두 입력해주세요.")
        else:
            try:
                auth_url = f"https://{sfmc_subdomain}.auth.marketingcloudapis.com/v2/token"
                resp = _req.post(auth_url, json={
                    "grant_type": "client_credentials",
                    "client_id": sfmc_client_id,
                    "client_secret": sfmc_client_secret
                })
                if resp.status_code == 200:
                    data = resp.json()
                    st.session_state["sfmc_token"] = data["access_token"]
                    st.session_state["sfmc_rest_base"] = f"https://{sfmc_subdomain}.rest.marketingcloudapis.com"
                    st.session_state["sfmc_subdomain"] = sfmc_subdomain
                    st.session_state["sfmc_client_id"] = sfmc_client_id
                    st.session_state["sfmc_client_secret"] = sfmc_client_secret
                    st.session_state["sfmc_web_url"] = sfmc_web_url.rstrip("/") if sfmc_web_url else ""
                    st.session_state["sfmc_jwt_auto"] = False
                    st.success("SFMC 연결 성공!")
                else:
                    st.error(f"연결 실패: {resp.status_code}")
            except Exception as e:
                st.error(f"오류: {e}")

    if st.session_state.get("sfmc_token"):
        if st.session_state.get("sfmc_jwt_auto"):
            st.markdown('<div class="status-ok">⚡ SFMC 자동 연결됨</div>', unsafe_allow_html=True)
        elif st.session_state.get("sfmc_auto_secret"):
            st.markdown('<div class="status-ok">🔒 SFMC 자동 연결됨</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-ok">● SFMC 연결됨</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style="font-size:11px; color:#475569; line-height:1.8;">
    SFMC Toolkit v1.1<br>AI + SFMC 연동 버전
    </div>
    """, unsafe_allow_html=True)

# ── AI 호출 함수 ────────────────────────────────────────────────────────────
def call_ai(system_prompt: str, user_message: str) -> str:
    """active_ai 기준으로 정확한 프로바이더 호출"""
    if active_ai == "anthropic" and api_key:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=2000,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}]
        )
        return message.content[0].text
    elif active_ai == "openai" and openai_key:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=openai_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                max_tokens=2000,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ]
            )
            return response.choices[0].message.content
        except ImportError:
            return "❌ openai 패키지가 설치되지 않았습니다. pip install openai 를 실행하세요."
    elif active_ai == "gemini" and gemini_key:
        try:
            import google.generativeai as genai
            genai.configure(api_key=gemini_key)
            model = genai.GenerativeModel(
                "gemini-2.5-flash",
                system_instruction=system_prompt
            )
            response = model.generate_content(user_message)
            return response.text
        except ImportError:
            return "❌ google-generativeai 패키지가 설치되지 않았습니다. pip install google-generativeai 를 실행하세요."
    return "❌ API 키를 입력해주세요."

def call_claude(api_key: str, system_prompt: str, user_message: str) -> str:
    """하위 호환용 — call_ai로 위임"""
    return call_ai(system_prompt, user_message)


def call_claude_with_search(api_key: str, system_prompt: str, user_message: str) -> str:
    """웹 검색 기능이 포함된 호출 - 에러 분석기 전용
    Anthropic: 웹 검색 툴 사용 / OpenAI·Gemini: 웹 검색 없이 일반 호출"""

    if active_ai == "anthropic" and api_key:
        # Anthropic — 웹 검색 툴 사용
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        tools = [{"type": "web_search_20250305", "name": "web_search"}]
        messages = [{"role": "user", "content": user_message}]
        full_text = ""
        while True:
            response = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=3000,
                system=system_prompt,
                tools=tools,
                messages=messages
            )
            messages.append({"role": "assistant", "content": response.content})
            for block in response.content:
                if hasattr(block, "text"):
                    full_text += block.text
            if response.stop_reason != "tool_use":
                break
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": []
                    })
            messages.append({"role": "user", "content": tool_results})
        return full_text

    elif active_ai == "openai" and openai_key:
        # OpenAI — 웹 검색 없이 일반 호출
        try:
            from openai import OpenAI
            client = OpenAI(api_key=openai_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                max_tokens=3000,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ]
            )
            return response.choices[0].message.content
        except ImportError:
            return "❌ openai 패키지가 설치되지 않았습니다. pip install openai 를 실행하세요."

    elif active_ai == "gemini" and gemini_key:
        # Gemini — 웹 검색 없이 일반 호출
        try:
            import google.generativeai as genai
            genai.configure(api_key=gemini_key)
            model = genai.GenerativeModel(
                "gemini-2.5-flash",
                system_instruction=system_prompt
            )
            response = model.generate_content(user_message)
            return response.text
        except ImportError:
            return "❌ google-generativeai 패키지가 설치되지 않았습니다. pip install google-generativeai 를 실행하세요."

    return "❌ API 키를 입력해주세요."


def require_key():
    st.markdown("""
    <div style="background:#fee2e2; border:1px solid #fecaca; border-radius:8px;
    padding:20px; color:#dc2626; font-size:13px; line-height:1.8;">
    ⚠️ 왼쪽 사이드바에서 API Key를 먼저 입력해주세요.<br>
    <span style="color:#64748b; font-size:12px;">Anthropic / OpenAI / Gemini 중 하나만 입력하면 됩니다.</span>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 1. 에러 분석기
# ══════════════════════════════════════════════════════════════════════════════
if menu == "🔍 Error 분석기":
    st.markdown("""
    <div class="page-header">
        <div class="page-title">Error 분석기</div>
        <div class="page-desc">SFMC에서 발생한 에러 메시지를 붙여넣으면 원인과 해결법을 한국어로 알려드립니다.</div>
    </div>
    """, unsafe_allow_html=True)

    error_input = st.text_area(
        "에러 메시지",
        placeholder="예: An error has occurred. Please contact your administrator.\n\n또는 Automation Studio, Journey Builder, Query Activity 등에서 발생한 에러 전체를 붙여넣으세요.",
        height=180
    )

    col1, col2 = st.columns([2, 1])
    with col1:
        context = st.text_input("에러 발생 위치 (선택)", placeholder="예: Automation Studio > SQL Query Activity")
    with col2:
        severity = st.selectbox("심각도 추정", ["모름", "운영 중단", "일부 오류", "경고"])

    if api_key:
        st.markdown("""<div style="background:#eff6ff;border:1px solid #bfdbfe;border-radius:6px;
        padding:10px 14px;font-size:12px;color:#1d4ed8;margin:12px 0;">
        🔍 웹 검색 활성화 — Salesforce 공식 문서를 실시간 검색해서 참고 링크를 함께 제공합니다.
        </div>""", unsafe_allow_html=True)

    if st.button("🔍 에러 분석하기", type="primary"):
        if not active_ai:
            require_key()
        elif not error_input.strip():
            st.warning("에러 메시지를 입력해주세요.")
        else:
            with st.spinner("분석 중..."):
                system = """당신은 Salesforce Marketing Cloud(SFMC) 전문가입니다.
에러를 분석하고 반드시 아래 JSON 형식으로만 응답하세요. JSON 외 텍스트는 절대 포함하지 마세요.

{
  "summary": "에러 한 줄 요약",
  "badge": "에러 유형 (예: Time Out, API Error, Query Error 등)",
  "causes": ["원인1", "원인2", "원인3"],
  "solutions": ["해결방법1", "해결방법2", "해결방법3"],
  "official_docs": [{"title": "문서 제목", "url": "https://help.salesforce.com/..."}],
  "other_docs": [{"title": "문서 제목", "url": "https://..."}]
}

- official_docs: help.salesforce.com 또는 developer.salesforce.com URL만 포함
- other_docs: Trailblazer 커뮤니티, 블로그, 기타 참고 자료
- 실제 존재하는 URL만 제공. 모르면 빈 배열 []로 두세요."""

                user_msg = f"에러 발생 위치: {context or '미입력'}\n심각도: {severity}\n\n에러 메시지:\n{error_input}"
                raw = call_claude_with_search(api_key, system, user_msg)

            # JSON 파싱
            import json, re
            try:
                json_match = re.search(r'\{.*\}', raw, re.DOTALL)
                data = json.loads(json_match.group()) if json_match else {}
            except:
                data = {}

            if not data:
                st.markdown(f'<div class="result-box">{raw}</div>', unsafe_allow_html=True)
            else:
                summary = data.get("summary","")
                badge = data.get("badge","")
                causes = data.get("causes", [])
                solutions = data.get("solutions", [])
                official_docs = data.get("official_docs", [])
                other_docs = data.get("other_docs", [])

                # 에러 요약 카드
                st.markdown(f"""<div style="background:#fff;border:1px solid #e2e8f0;border-radius:10px;
                padding:16px 20px;margin:12px 0;display:flex;align-items:center;gap:12px;">
                <span style="background:#fee2e2;color:#dc2626;font-size:12px;font-weight:600;
                padding:4px 12px;border-radius:99px;border:1px solid #fecaca;white-space:nowrap;">{badge}</span>
                <span style="font-size:14px;color:#1e293b;font-weight:500;">{summary}</span>
                </div>""", unsafe_allow_html=True)

                # 원인 / 해결방법 2단 카드
                c1, c2 = st.columns(2)
                with c1:
                    causes_html = "".join([f"""<div style="display:flex;gap:8px;align-items:flex-start;margin-bottom:8px;">
                    <span style="min-width:7px;height:7px;border-radius:50%;background:#ef4444;margin-top:5px;display:inline-block;flex-shrink:0;"></span>
                    <span style="font-size:13px;color:#374151;">{c}</span></div>""" for c in causes])
                    st.markdown(f"""<div style="background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:16px;height:100%;">
                    <div style="font-size:11px;font-weight:600;color:#94a3b8;letter-spacing:0.05em;text-transform:uppercase;margin-bottom:12px;">발생 원인</div>
                    {causes_html}</div>""", unsafe_allow_html=True)
                with c2:
                    solutions_html = "".join([f"""<div style="display:flex;gap:8px;align-items:flex-start;margin-bottom:8px;">
                    <span style="min-width:20px;height:20px;border-radius:50%;background:#dcfce7;color:#15803d;
                    font-size:10px;font-weight:600;display:flex;align-items:center;justify-content:center;flex-shrink:0;">{i+1}</span>
                    <span style="font-size:13px;color:#374151;">{s}</span></div>""" for i,s in enumerate(solutions)])
                    st.markdown(f"""<div style="background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:16px;height:100%;">
                    <div style="font-size:11px;font-weight:600;color:#94a3b8;letter-spacing:0.05em;text-transform:uppercase;margin-bottom:12px;">해결 방법</div>
                    {solutions_html}</div>""", unsafe_allow_html=True)

                # 참고 문서
                if official_docs or other_docs:
                    st.markdown("<div style='margin-top:12px;'></div>", unsafe_allow_html=True)
                    d1, d2 = st.columns(2)
                    with d1:
                        if official_docs:
                            links = "".join([f'<a href="{d["url"]}" target="_blank" style="display:block;font-size:13px;color:#3b82f6;text-decoration:none;margin-bottom:6px;">→ {d["title"]}</a>' for d in official_docs])
                            st.markdown(f"""<div style="background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:16px;">
                            <div style="font-size:11px;font-weight:600;color:#94a3b8;letter-spacing:0.05em;text-transform:uppercase;margin-bottom:10px;">공식 문서</div>
                            {links}</div>""", unsafe_allow_html=True)
                    with d2:
                        if other_docs:
                            links2 = "".join([f'<a href="{d["url"]}" target="_blank" style="display:block;font-size:13px;color:#3b82f6;text-decoration:none;margin-bottom:6px;">→ {d["title"]}</a>' for d in other_docs])
                            st.markdown(f"""<div style="background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:16px;">
                            <div style="font-size:11px;font-weight:600;color:#94a3b8;letter-spacing:0.05em;text-transform:uppercase;margin-bottom:10px;">기타 문서</div>
                            {links2}</div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 2. SQL 생성기
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "💾 Query 생성기":
    st.markdown("""
    <div class="page-header">
        <div class="page-title">Query 생성기</div>
        <div class="page-desc">SFMC Data Extension 목록을 불러와서 원하는 조건을 입력하면 SFMC 전용 SQL을 자동 생성합니다.</div>
    </div>
    """, unsafe_allow_html=True)

    import requests

    # ── SFMC DE 목록 불러오기 ──────────────────────────────────────────────
    de_load_col, de_search_col = st.columns([1, 2])
    with de_load_col:
        if st.button("🔄 DE 목록 불러오기"):
            if not st.session_state.get("sfmc_token"):
                st.error("먼저 사이드바에서 SFMC 연결을 해주세요.")
            else:
                with st.spinner("DE 목록 불러오는 중..."):
                    try:
                        token = st.session_state["sfmc_token"]
                        sfmc_subdomain = st.session_state["sfmc_subdomain"]
                        soap_url = f"https://{sfmc_subdomain}.soap.marketingcloudapis.com/Service.asmx"

                        all_des = []
                        request_id = None

                        while True:
                            if request_id:
                                # 페이지 계속 요청
                                body = f"""<?xml version="1.0" encoding="UTF-8"?>
<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope"
            xmlns:a="http://schemas.xmlsoap.org/ws/2004/08/addressing"
            xmlns:u="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
  <s:Header>
    <fueloauth xmlns="http://exacttarget.com">{token}</fueloauth>
  </s:Header>
  <s:Body>
    <RetrieveRequestMsg xmlns="http://exacttarget.com/wsdl/partnerAPI">
      <RetrieveRequest>
        <ContinueRequest>{request_id}</ContinueRequest>
      </RetrieveRequest>
    </RetrieveRequestMsg>
  </s:Body>
</s:Envelope>"""
                            else:
                                body = f"""<?xml version="1.0" encoding="UTF-8"?>
<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope"
            xmlns:a="http://schemas.xmlsoap.org/ws/2004/08/addressing"
            xmlns:u="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
  <s:Header>
    <fueloauth xmlns="http://exacttarget.com">{token}</fueloauth>
  </s:Header>
  <s:Body>
    <RetrieveRequestMsg xmlns="http://exacttarget.com/wsdl/partnerAPI">
      <RetrieveRequest>
        <ObjectType>DataExtension</ObjectType>
        <Properties>Name</Properties>
        <Properties>CustomerKey</Properties>
        <Properties>Description</Properties>
      </RetrieveRequest>
    </RetrieveRequestMsg>
  </s:Body>
</s:Envelope>"""

                            soap_resp = requests.post(
                                soap_url,
                                data=body.encode("utf-8"),
                                headers={
                                    "Content-Type": "text/xml; charset=utf-8",
                                    "SOAPAction": "Retrieve"
                                }
                            )

                            if soap_resp.status_code != 200:
                                st.error(f"SOAP API 오류: {soap_resp.status_code} — {soap_resp.text[:300]}")
                                break

                            import xml.etree.ElementTree as ET
                            root = ET.fromstring(soap_resp.text)
                            ns = {"ns": "http://exacttarget.com/wsdl/partnerAPI"}

                            results = root.findall(".//ns:Results", ns)
                            for r in results:
                                name_el = r.find("ns:Name", ns)
                                key_el  = r.find("ns:CustomerKey", ns)
                                desc_el = r.find("ns:Description", ns)
                                if name_el is not None:
                                    all_des.append({
                                        "name": name_el.text or "",
                                        "key":  key_el.text if key_el is not None else "",
                                        "desc": desc_el.text if desc_el is not None else ""
                                    })

                            # 페이지 더 있는지 확인
                            overall_status = root.findtext(".//{http://exacttarget.com/wsdl/partnerAPI}OverallStatus", "")
                            req_id_el = root.find(".//{http://exacttarget.com/wsdl/partnerAPI}RequestID")
                            if overall_status == "MoreDataAvailable" and req_id_el is not None:
                                request_id = req_id_el.text
                            else:
                                break

                        if all_des:
                            all_des.sort(key=lambda x: x["name"].lower())
                            st.session_state["sfmc_des"] = all_des
                            st.success(f"✅ {len(all_des)}개 DE 불러옴")
                        else:
                            st.warning("불러온 DE가 없습니다.")
                    except Exception as e:
                        st.error(f"오류: {e}")

    # ── DE 선택 및 컬럼 조회 ──────────────────────────────────────────────
    des = st.session_state.get("sfmc_des", [])

    if des:
        de_names = [d["name"] for d in des]
        st.markdown("---")
        st.markdown("**📂 쿼리에 사용할 DE 선택** (여러 개 가능)")

        # DE 검색 필터
        de_search = ""
        filtered_des = des

        selected_de_names = st.multiselect(
            "DE 선택",
            [d["name"] for d in filtered_des],
            placeholder="DE를 선택하세요..."
        )

        # 선택된 DE의 컬럼 자동 조회 (SOAP)
        de_schemas = {}
        if selected_de_names and st.session_state.get("sfmc_token"):
            token = st.session_state["sfmc_token"]
            sfmc_subdomain = st.session_state["sfmc_subdomain"]
            soap_url = f"https://{sfmc_subdomain}.soap.marketingcloudapis.com/Service.asmx"

            for de_name in selected_de_names:
                de_obj = next((d for d in des if d["name"] == de_name), None)
                if not de_obj:
                    continue
                cache_key = f"de_cols_{de_name}"
                if cache_key in st.session_state:
                    de_schemas[de_name] = st.session_state[cache_key]
                else:
                    try:
                        de_key = de_obj.get("key", "")
                        soap_body = f"""<?xml version="1.0" encoding="UTF-8"?>
<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope">
  <s:Header>
    <fueloauth xmlns="http://exacttarget.com">{token}</fueloauth>
  </s:Header>
  <s:Body>
    <RetrieveRequestMsg xmlns="http://exacttarget.com/wsdl/partnerAPI">
      <RetrieveRequest>
        <ObjectType>DataExtensionField</ObjectType>
        <Properties>Name</Properties>
        <Properties>FieldType</Properties>
        <Properties>IsPrimaryKey</Properties>
        <Properties>IsRequired</Properties>
        <Filter xsi:type="SimpleFilterPart" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <Property>DataExtension.CustomerKey</Property>
          <SimpleOperator>equals</SimpleOperator>
          <Value>{de_key}</Value>
        </Filter>
      </RetrieveRequest>
    </RetrieveRequestMsg>
  </s:Body>
</s:Envelope>"""
                        soap_resp = requests.post(
                            soap_url,
                            data=soap_body.encode("utf-8"),
                            headers={"Content-Type": "text/xml; charset=utf-8", "SOAPAction": "Retrieve"}
                        )
                        if soap_resp.status_code == 200:
                            import xml.etree.ElementTree as ET
                            root = ET.fromstring(soap_resp.text)
                            ns = {"ns": "http://exacttarget.com/wsdl/partnerAPI"}
                            fields = []
                            for r in root.findall(".//ns:Results", ns):
                                n = r.findtext("ns:Name", "", ns)
                                t = r.findtext("ns:FieldType", "", ns)
                                pk = r.findtext("ns:IsPrimaryKey", "false", ns)
                                if n:
                                    fields.append({"name": n, "type": t, "pk": pk == "true"})
                            if fields:
                                de_schemas[de_name] = fields
                                st.session_state[cache_key] = fields
                            else:
                                de_schemas[de_name] = []
                        else:
                            de_schemas[de_name] = []
                    except Exception as e:
                        de_schemas[de_name] = []

            # 컬럼 미리보기
            if de_schemas:
                for de_name, fields in de_schemas.items():
                    if fields:
                        col_tags = ""
                        for f in fields:
                            pk_badge = "<span style='font-size:9px;font-weight:500;color:#185FA5;background:#E6F1FB;padding:1px 5px;border-radius:3px;margin-left:2px;'>PK</span>" if f["pk"] else ""
                            col_tags += (
                                f'<span style="display:inline-flex;align-items:center;gap:4px;'
                                f'padding:4px 10px;border-radius:6px;border:0.5px solid #e2e8f0;'
                                f'background:#f8fafc;font-size:12px;margin:3px;">'
                                f'<span style="font-weight:500;color:#1e293b;">{f["name"]}</span>'
                                f'<span style="font-size:10px;color:#94a3b8;">{f["type"]}</span>'
                                f'{pk_badge}'
                                f'</span>'
                            )
                        st.markdown(f"""
                        <div style="background:#fff;border:0.5px solid #e2e8f0;border-radius:10px;
                        padding:14px 16px;margin:8px 0;">
                        <div style="font-size:11px;font-weight:500;color:#94a3b8;text-transform:uppercase;
                        letter-spacing:0.05em;margin-bottom:8px;">조회된 컬럼 정보</div>
                        <div style="font-size:13px;font-weight:500;color:#1e293b;margin-bottom:10px;">
                        {de_name} <span style="font-size:11px;color:#94a3b8;font-weight:400;">· {len(fields)}개 컬럼</span></div>
                        <div style="display:flex;flex-wrap:wrap;gap:4px;">{col_tags}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div style="background:#fef2f2;border:0.5px solid #fecaca;border-radius:10px;
                        padding:12px 16px;margin:8px 0;font-size:12px;color:#b91c1c;">
                        {de_name}: 컬럼 조회 실패 — CustomerKey를 확인하세요
                        </div>
                        """, unsafe_allow_html=True)

    # ── SQL 프롬프트 입력 ──────────────────────────────────────────────────
    st.markdown("---")
    st.markdown("**💬 원하는 쿼리를 설명하세요**")

    query_desc = st.text_area(
        "쿼리 설명",
        value=st.session_state.get("sql_desc_input", ""),
        placeholder="예: 최근 7일 이내에 이메일을 열어봤지만 클릭은 하지 않은 고객 목록을 뽑아줘. SubscriberKey, EmailAddress, EventDate 컬럼이 필요해.",
        height=120,
        key="sql_query_desc"
    )

    if st.button("⚡ SQL 생성", type="primary"):
        if not active_ai:
            require_key()
        elif not query_desc.strip():
            st.warning("쿼리 설명을 입력해주세요.")
        else:
            with st.spinner("SQL 생성 중..."):
                schema_context = ""
                if de_schemas:
                    schema_lines = []
                    for de_name, fields in de_schemas.items():
                        if fields:
                            col_info = ", ".join([
                                f'{f["name"]}({f["type"]}{"*PK" if f["pk"] else ""})'
                                for f in fields
                            ])
                            schema_lines.append(f"- [{de_name}]: {col_info}")
                        else:
                            schema_lines.append(f"- [{de_name}]: (컬럼 미확인)")
                    schema_context = "사용 가능한 DE 스키마:\n" + "\n".join(schema_lines)
                elif selected_de_names:
                    schema_context = f"사용 DE: {', '.join(selected_de_names)} (컬럼 정보 없음 — 추정해서 작성)"
                else:
                    schema_context = "DE 정보 없음 — 요청 내용 기반으로 추정해서 작성"

                system = f"""당신은 Salesforce Marketing Cloud(SFMC) SQL 전문가입니다.
SFMC Automation Studio의 Query Activity에서 실행되는 SQL을 작성하세요.

{schema_context}

[절대 금지 사항 — 위반 시 틀린 SQL]
- INTO 절 절대 사용 금지. SELECT ... INTO ... FROM ... 형식 절대 불가
- ORDER BY 사용 금지 (SFMC Query Activity 미지원)
- LIMIT 사용 금지 (TOP 사용)
- 존재하지 않는 컬럼이나 함수 사용 금지
- 주석(-- 또는 /* */) 절대 사용 금지

[SFMC SQL 규칙]
- 올바른 형식: SELECT 컬럼 FROM [테이블] WHERE 조건
- Target DE는 Query Activity UI에서 별도 설정하므로 SQL에 포함하지 않음
- 날짜 함수: GETDATE(), DATEADD(DAY, -7, GETDATE()), DATEDIFF()
- 서브쿼리, JOIN, GROUP BY, HAVING 모두 사용 가능

출력 형식:
SQL 코드만 출력하세요. 마크다운 코드펜스(```), 주석, 설명 텍스트 일절 포함하지 마세요.
반드시 아래 들여쓰기 형식을 따르세요:

SELECT
        컬럼1,
        컬럼2,
        컬럼3
FROM
        [테이블명]
WHERE
        조건1
        AND 조건2"""

                result = call_ai(system, f"요청:\n{query_desc}")

            # 코드펜스/설명 제거 — 순수 SQL만
            sql_part = result.strip()
            for fence in ["```sql", "```SQL", "```"]:
                sql_part = sql_part.replace(fence, "")
            if "[설명]" in sql_part:
                sql_part = sql_part.split("[설명]")[0]
            sql_part = "\n".join(
                l for l in sql_part.splitlines()
                if "INTO [" not in l and "INTO[" not in l
            ).strip()
            st.session_state["generated_sql"] = sql_part

    # ── 생성된 SQL 표시 ────────────────────────────────────────────────────
    if st.session_state.get("generated_sql"):
        sql = st.session_state["generated_sql"]
        st.markdown('<div class="result-label">● 생성된 SQL</div>', unsafe_allow_html=True)
        st.code(sql, language="sql")

        if st.button("💡 AI 검토", key="sql_review_btn"):
            if active_ai:
                with st.spinner("SQL 검토 중..."):
                    review = call_ai(
                        "당신은 SFMC SQL 전문가입니다. 주어진 SQL의 문제점, 성능 이슈, 개선점을 한국어로 알려주세요. 번호 목록 없이 짧고 명확하게 작성하세요.",
                        f"다음 SFMC SQL을 검토해주세요:\n\n{sql}"
                    )
                st.markdown(f"""<div style="background:#f8fafc;border-left:3px solid #3b82f6;
                border-radius:0 8px 8px 0;padding:14px 18px;font-size:13px;
                color:#1e293b;line-height:1.8;margin-top:8px;width:100%;">{review}</div>""",
                unsafe_allow_html=True)





# ══════════════════════════════════════════════════════════════════════════════
# 3. AMPscript 어시스턴트

elif menu == "🗂️ Journey 관리":
    st.markdown("""
    <div class="page-header">
        <div class="page-title">Journey 관리</div>
        <div class="page-desc">Journey 목록 조회, 상태 관리, 점검을 한 곳에서 확인합니다.</div>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.get("sfmc_token"):
        st.markdown("""
        <div style="background:#fee2e2; border:1px solid #fecaca; border-radius:8px;
        padding:20px; color:#ff5555; font-size:13px; line-height:1.8;">
        ⚠️ 왼쪽 사이드바에서 <strong>SFMC 연결</strong>을 먼저 해주세요.
        </div>
        """, unsafe_allow_html=True)
    else:
        import requests

        token = st.session_state["sfmc_token"]
        rest_base = st.session_state["sfmc_rest_base"]

        ACTIVE_STATUSES = {"Published"}

        def journey_action(action, journey_id, journey_version, token, rest_base):
            try:
                if action == "pause":
                    url = f"{rest_base}/interaction/v1/interactions/pause/{journey_id}?versionNumber={journey_version}"
                    resp = requests.post(url, headers={"Authorization": f"Bearer {token}"})
                elif action == "resume":
                    url = f"{rest_base}/interaction/v1/interactions/resume/{journey_id}?versionNumber={journey_version}"
                    resp = requests.post(url, headers={"Authorization": f"Bearer {token}"})
                elif action == "stop":
                    url = f"{rest_base}/interaction/v1/interactions/stop/{journey_id}?versionNumber={journey_version}"
                    resp = requests.post(url, headers={"Authorization": f"Bearer {token}"})
                elif action == "delete":
                    url = f"{rest_base}/interaction/v1/interactions/{journey_id}?versionNumber={journey_version}"
                    resp = requests.delete(url, headers={"Authorization": f"Bearer {token}"})
                return resp.status_code, resp.text
            except Exception as e:
                return 0, str(e)

        def action_error_msg(code, msg):
            if code == 403:
                return "403 권한 없음 — Installed Package에서 Journey Builder 쓰기 권한을 확인하세요."
            elif code == 409:
                return "409 충돌 — Journey 상태가 변경 중입니다. 잠시 후 다시 시도해주세요."
            return f"실패: {code} — {msg[:200]}"

        # ── 탭 ────────────────────────────────────────────────────────────────
        tab_j, tab_check, tab_dash = st.tabs(["🗺️ Journey 목록", "⚠️ Journey 점검", "📊 대시보드"])

        # ════════════════════════════════════════════════════════════════════
        # JOURNEY 탭
        # ════════════════════════════════════════════════════════════════════
        with tab_j:
            if st.button("🔄 Journey 불러오기", key="load_journey"):
                try:
                    all_journeys = []
                    page = 1
                    progress = st.progress(0, text="Journey 불러오는 중...")
                    while True:
                        params = {"$pageSize": 50, "$page": page}
                        resp = requests.get(
                            f"{rest_base}/interaction/v1/interactions",
                            headers={"Authorization": f"Bearer {token}"},
                            params=params
                        )
                        if resp.status_code == 401:
                            st.error("토큰 만료 — 다시 연결해주세요.")
                            break
                        if resp.status_code != 200:
                            st.error(f"오류: {resp.status_code}")
                            break
                        data = resp.json()
                        items = data.get("items", [])
                        all_journeys.extend(items)
                        total_count = data.get("count", 0)
                        progress.progress(min(len(all_journeys)/max(total_count,1), 1.0),
                                          text=f"{len(all_journeys)} / {total_count}개 로드 중...")
                        if len(items) < 50 or len(all_journeys) >= total_count:
                            break
                        page += 1
                    progress.empty()
                    st.session_state["journeys_all"] = all_journeys
                    st.session_state["selected_journeys"] = set()
                    st.session_state["chk_version"] = 0
                    st.success(f"✅ 총 {len(all_journeys)}개 Journey 불러옴")
                except Exception as e:
                    st.error(f"오류: {e}")

            journeys_all = st.session_state.get("journeys_all", [])

            if journeys_all:
                # 상태 집계 카드
                from collections import Counter
                status_counts = Counter(j.get("status","Unknown") for j in journeys_all)
                known = {"Published","Draft","Paused","Stopped"}
                etc_statuses = [k for k in status_counts if k not in known]
                etc_count = sum(status_counts[k] for k in etc_statuses)
                etc_labels = " · ".join(f"{k} {status_counts[k]}" for k in etc_statuses) if etc_statuses else ""

                m1, m2, m3, m4, m5, m6 = st.columns(6)
                with m1:
                    st.markdown(f"""<div style="background:#f1f5f9;border:1px solid #e2e8f0;border-radius:8px;padding:14px 16px;">
                    <div style="font-size:11px;color:#94a3b8;margin-bottom:6px;">Total</div>
                    <div style="font-size:28px;font-weight:600;color:#1e293b;">{len(journeys_all)}</div></div>""", unsafe_allow_html=True)
                with m2:
                    st.markdown(f"""<div style="background:#dcfce7;border:1px solid #bbf7d0;border-radius:8px;padding:14px 16px;">
                    <div style="font-size:11px;color:#15803d;margin-bottom:6px;">Published</div>
                    <div style="font-size:28px;font-weight:600;color:#15803d;">{status_counts.get("Published",0)}</div></div>""", unsafe_allow_html=True)
                with m3:
                    st.markdown(f"""<div style="background:#fef9c3;border:1px solid #fde68a;border-radius:8px;padding:14px 16px;">
                    <div style="font-size:11px;color:#92400e;margin-bottom:6px;">Draft</div>
                    <div style="font-size:28px;font-weight:600;color:#92400e;">{status_counts.get("Draft",0)}</div></div>""", unsafe_allow_html=True)
                with m4:
                    st.markdown(f"""<div style="background:#dbeafe;border:1px solid #bfdbfe;border-radius:8px;padding:14px 16px;">
                    <div style="font-size:11px;color:#1d4ed8;margin-bottom:6px;">Paused</div>
                    <div style="font-size:28px;font-weight:600;color:#1d4ed8;">{status_counts.get("Paused",0)}</div></div>""", unsafe_allow_html=True)
                with m5:
                    st.markdown(f"""<div style="background:#fee2e2;border:1px solid #fecaca;border-radius:8px;padding:14px 16px;">
                    <div style="font-size:11px;color:#dc2626;margin-bottom:6px;">Stopped</div>
                    <div style="font-size:28px;font-weight:600;color:#dc2626;">{status_counts.get("Stopped",0)}</div></div>""", unsafe_allow_html=True)
                with m6:
                    st.markdown(f"""<div style="background:#e2e8f0;border:1px solid #cbd5e1;border-radius:8px;padding:14px 16px;">
                    <div style="font-size:11px;color:#64748b;margin-bottom:6px;">Others</div>
                    <div style="font-size:28px;font-weight:600;color:#334155;">{etc_count}</div></div>""", unsafe_allow_html=True)

                st.markdown("---")

                # 선택 상태 초기화 (필터보다 먼저)
                if "selected_journeys" not in st.session_state:
                    st.session_state["selected_journeys"] = set()
                if "chk_version" not in st.session_state:
                    st.session_state["chk_version"] = 0
                sel = st.session_state["selected_journeys"]
                chk_v = st.session_state["chk_version"]

                # 검색 & 필터
                filter_options = ["전체","Published","Draft","Paused","Stopped"] + etc_statuses
                fc1, fc2, fc3, fc4 = st.columns([3, 1.2, 1.2, 1.2])
                with fc1:
                    search_query = st.text_input("검색", placeholder="Journey 이름 검색...", label_visibility="collapsed")
                with fc2:
                    status_filter = st.selectbox("상태", filter_options, label_visibility="collapsed")
                with fc3:
                    sort_order = st.selectbox("정렬", ["최신순","오래된순","수정일순","이름순"], label_visibility="collapsed")
                with fc4:
                    page_size_opt = st.selectbox("표시", ["전체","10개","25개","50개","100개"], label_visibility="collapsed")
                    page_size = len(journeys_all) if page_size_opt == "전체" else int(page_size_opt.replace("개",""))

                # 선택 버튼 — 필터 아래 별도 작은 행
                sel_row1, sel_row2, sel_row3, _ = st.columns([0.8, 0.8, 0.8, 7])
                with sel_row1:
                    st.markdown(f"<div style='font-size:12px;color:#94a3b8;padding-top:6px;'>{len(sel)}개 선택</div>", unsafe_allow_html=True)
                with sel_row2:
                    if st.button("전체선택", key="sel_all"):
                        st.session_state["selected_journeys"] = {j.get("id") for j in journeys_all}
                        st.session_state["chk_version"] += 1
                        st.rerun()
                with sel_row3:
                    if st.button("선택해제", key="sel_none"):
                        st.session_state["selected_journeys"] = set()
                        st.session_state["chk_version"] += 1
                        st.rerun()

                # 필터 적용
                journeys = journeys_all[:]
                if search_query:
                    journeys = [j for j in journeys if search_query.lower() in j.get("name","").lower()]
                if status_filter != "전체":
                    journeys = [j for j in journeys if j.get("status") == status_filter]

                def safe_date(j, key):
                    return j.get(key) or "1970-01-01"

                if sort_order == "최신순":
                    journeys = sorted(journeys, key=lambda j: safe_date(j,"createdDate"), reverse=True)
                elif sort_order == "오래된순":
                    journeys = sorted(journeys, key=lambda j: safe_date(j,"createdDate"))
                elif sort_order == "수정일순":
                    journeys = sorted(journeys, key=lambda j: safe_date(j,"modifiedDate"), reverse=True)
                elif sort_order == "이름순":
                    journeys = sorted(journeys, key=lambda j: j.get("name","").lower())

                filtered_total = len(journeys)
                journeys = journeys[:page_size]
                st.session_state["journeys"] = journeys

                # 선택 개수 + 일괄 작업
                if sel:
                    sel_data = [j for j in journeys if j.get("id") in sel]
                    sel_statuses = set(j.get("status","") for j in sel_data)

                    # 상태별 가능한 액션 계산
                    can_pause  = bool(sel_statuses & ACTIVE_STATUSES)
                    can_resume = "Paused" in sel_statuses
                    can_stop   = bool(sel_statuses & (ACTIVE_STATUSES | {"Paused"}))
                    can_delete = bool(sel_statuses & {"Draft","Stopped","Paused"})

                    # 보여줄 버튼 수에 따라 컬럼 동적 생성
                    btn_labels = []
                    if can_pause:  btn_labels.append("pause")
                    if can_resume: btn_labels.append("resume")
                    if can_stop:   btn_labels.append("stop")
                    if can_delete: btn_labels.append("delete")

                    col_widths = [1.5] + [0.9] * len(btn_labels) + [4]
                    act_cols = st.columns(col_widths)

                    with act_cols[0]:
                        st.markdown(f"<div style='font-size:12px;color:#64748b;padding-top:8px;'>{len(sel)}개 선택됨</div>", unsafe_allow_html=True)

                    btn_idx = 1
                    if can_pause:
                        with act_cols[btn_idx]:
                            if st.button("⏸ Pause", key="bulk_pause"):
                                ok, fail = 0, 0
                                for j in sel_data:
                                    if j.get("status") in ACTIVE_STATUSES:
                                        c, m = journey_action("pause", j["id"], j.get("version",1), token, rest_base)
                                        if c in [200,201,202]:
                                            ok+=1
                                            for item in st.session_state["journeys_all"]:
                                                if item.get("id") == j["id"]: item["status"] = "Paused"
                                        else: fail+=1
                                st.success(f"Pause {ok}개 완료" + (f", {fail}개 실패" if fail else ""))
                                st.session_state["selected_journeys"] = set()
                                st.session_state["chk_version"] += 1
                                st.rerun()
                        btn_idx += 1

                    if can_resume:
                        with act_cols[btn_idx]:
                            if st.button("▶ Resume", key="bulk_resume"):
                                ok, fail = 0, 0
                                for j in sel_data:
                                    if j.get("status") == "Paused":
                                        c, m = journey_action("resume", j["id"], j.get("version",1), token, rest_base)
                                        if c in [200,201,202]:
                                            ok+=1
                                            for item in st.session_state["journeys_all"]:
                                                if item.get("id") == j["id"]: item["status"] = "Published"
                                        else: fail+=1
                                st.success(f"Resume {ok}개 완료" + (f", {fail}개 실패" if fail else ""))
                                st.session_state["selected_journeys"] = set()
                                st.session_state["chk_version"] += 1
                                st.rerun()
                        btn_idx += 1

                    if can_stop:
                        with act_cols[btn_idx]:
                            if st.button("⏹ Stop", key="bulk_stop"):
                                ok, fail = 0, 0
                                for j in sel_data:
                                    if j.get("status") in ACTIVE_STATUSES | {"Paused"}:
                                        c, m = journey_action("stop", j["id"], j.get("version",1), token, rest_base)
                                        if c in [200,201,202]:
                                            ok+=1
                                            for item in st.session_state["journeys_all"]:
                                                if item.get("id") == j["id"]: item["status"] = "Stopped"
                                        else: fail+=1
                                st.success(f"Stop {ok}개 완료" + (f", {fail}개 실패" if fail else ""))
                                st.session_state["selected_journeys"] = set()
                                st.session_state["chk_version"] += 1
                                st.rerun()
                        btn_idx += 1

                    if can_delete:
                        with act_cols[btn_idx]:
                            if st.button("🗑 Delete", key="bulk_delete"):
                                ok, fail = 0, 0
                                deleted_ids = set()
                                for j in sel_data:
                                    if j.get("status") in ["Draft","Stopped","Paused"]:
                                        c, m = journey_action("delete", j["id"], j.get("version",1), token, rest_base)
                                        if c in [200,201,202,204]:
                                            ok+=1
                                            deleted_ids.add(j["id"])
                                        else: fail+=1
                                if deleted_ids:
                                    st.session_state["journeys_all"] = [
                                        item for item in st.session_state["journeys_all"]
                                        if item.get("id") not in deleted_ids
                                    ]
                                st.success(f"Delete {ok}개 완료" + (f", {fail}개 실패" if fail else ""))
                                st.session_state["selected_journeys"] = set()
                                st.session_state["chk_version"] += 1
                                st.rerun()
                else:
                    pass

                st.markdown(f"<div style='font-size:12px;color:#64748b;margin:6px 0;'>{len(journeys)}개 표시 중 (필터 결과 {filtered_total}개 / 전체 {len(journeys_all)}개)</div>", unsafe_allow_html=True)

                # 상태별 색상 & 배지
                STATUS_COLORS = {
                    "Published":"#15803d","Draft":"#92400e",
                    "Paused":"#1d4ed8","Stopped":"#dc2626","Deleted":"#64748b"
                }
                STATUS_BG = {
                    "Published":"#dcfce7","Draft":"#fef9c3",
                    "Paused":"#dbeafe","Stopped":"#fee2e2","Deleted":"#f1f5f9"
                }
                sfmc_web_url = st.session_state.get("sfmc_web_url","")

                # 헤더 — Streamlit 컬럼으로 통일
                hc1, hc2, hc3, hc4a, hc4b, hc4c, hc5 = st.columns([0.5, 4.5, 1.5, 1.2, 1.2, 1.2, 1.2])
                with hc1: st.markdown("<div style='font-size:11px;color:#64748b;'></div>", unsafe_allow_html=True)
                with hc2: st.markdown("<div style='font-size:11px;font-weight:500;color:#64748b;letter-spacing:0.05em;text-transform:uppercase;'>이름 / ID</div>", unsafe_allow_html=True)
                with hc3: st.markdown("<div style='font-size:11px;font-weight:500;color:#64748b;letter-spacing:0.05em;text-transform:uppercase;'>상태</div>", unsafe_allow_html=True)
                with hc4a: st.markdown("<div style='font-size:11px;font-weight:500;color:#64748b;letter-spacing:0.05em;text-transform:uppercase;'>일시정지</div>", unsafe_allow_html=True)
                with hc4b: st.markdown("<div style='font-size:11px;font-weight:500;color:#64748b;letter-spacing:0.05em;text-transform:uppercase;'>중단</div>", unsafe_allow_html=True)
                with hc4c: st.markdown("<div style='font-size:11px;font-weight:500;color:#64748b;letter-spacing:0.05em;text-transform:uppercase;'>삭제</div>", unsafe_allow_html=True)
                with hc5: st.markdown("<div style='font-size:11px;font-weight:500;color:#64748b;letter-spacing:0.05em;text-transform:uppercase;'>바로가기</div>", unsafe_allow_html=True)
                st.markdown("<div style='height:1px;background:#e2e8f0;margin:4px 0 8px 0;'></div>", unsafe_allow_html=True)

                for idx, j in enumerate(journeys):
                    status = j.get("status","Unknown")
                    color = STATUS_COLORS.get(status,"#8888aa")
                    bg = STATUS_BG.get(status,"#111111")
                    name = j.get("name","이름 없음")
                    version = j.get("version",1)
                    created = j.get("createdDate","")[:10] if j.get("createdDate") else "-"
                    modified = j.get("modifiedDate","")[:10] if j.get("modifiedDate") else "-"
                    jid = j.get("id","")
                    jkey = j.get("key","")
                    is_selected = jid in sel

                    if sfmc_web_url:
                        base = sfmc_web_url.strip()
                        if not base.startswith("http"):
                            base = "https://" + base
                        sfmc_link = f"{base}/cloud/#app/Journey%20Builder/%23{jid}/{version}"
                    else:
                        sfmc_link = ""

                    chk_col, info_col, badge_col, bcol_pause, bcol_stop, bcol_del, link_col = st.columns(
                        [0.5, 4.5, 1.5, 1.2, 1.2, 1.2, 1.2], vertical_alignment="center"
                    )
                    with chk_col:
                        checked = st.checkbox("", key=f"jchk_{idx}_v{chk_v}", value=is_selected)
                        if checked and jid not in sel:
                            st.session_state["selected_journeys"].add(jid)
                            st.rerun()
                        elif not checked and jid in sel:
                            st.session_state["selected_journeys"].discard(jid)
                            st.rerun()

                    with info_col:
                        st.markdown(f"""
                        <div>
                        <div style="font-size:13px;font-weight:500;color:#1e293b;">{name}</div>
                        <div style="font-size:11px;color:#64748b;margin-top:3px;">v{version} &nbsp;·&nbsp; 생성: {created} &nbsp;·&nbsp; 수정: {modified}</div>
                        </div>
                        """, unsafe_allow_html=True)

                    with badge_col:
                        st.markdown(f"""
                        <span style="display:inline-flex;align-items:center;gap:4px;font-size:12px;font-weight:500;
                        padding:4px 10px;border-radius:99px;background:{bg};color:{color};">
                        <span style="width:6px;height:6px;border-radius:50%;background:{color};display:inline-block;flex-shrink:0;"></span>
                        {status}
                        </span>
                        """, unsafe_allow_html=True)

                    with bcol_pause:
                        if status in ACTIVE_STATUSES:
                            if st.button("II", key=f"pause_{idx}", help="일시정지"):
                                c, m = journey_action("pause", jid, version, token, rest_base)
                                if c in [200,201,202]:
                                    for item in st.session_state["journeys_all"]:
                                        if item.get("id") == jid: item["status"] = "Paused"
                                    st.rerun()
                                else:
                                    st.error(action_error_msg(c, m))
                        if status == "Paused":
                            if st.button("▶", key=f"resume_{idx}", help="재개"):
                                c, m = journey_action("resume", jid, version, token, rest_base)
                                if c in [200,201,202]:
                                    for item in st.session_state["journeys_all"]:
                                        if item.get("id") == jid: item["status"] = "Published"
                                    st.rerun()
                                else:
                                    st.error(action_error_msg(c, m))

                    with bcol_stop:
                        if status in ACTIVE_STATUSES:
                            if st.button("■", key=f"stop_{idx}", help="중단"):
                                c, m = journey_action("stop", jid, version, token, rest_base)
                                if c in [200,201,202]:
                                    for item in st.session_state["journeys_all"]:
                                        if item.get("id") == jid: item["status"] = "Stopped"
                                    st.rerun()
                                else:
                                    st.error(action_error_msg(c, m))
                        if status == "Paused":
                            if st.button("■", key=f"stop_p_{idx}", help="중단"):
                                c, m = journey_action("stop", jid, version, token, rest_base)
                                if c in [200,201,202]:
                                    for item in st.session_state["journeys_all"]:
                                        if item.get("id") == jid: item["status"] = "Stopped"
                                    st.rerun()
                                else:
                                    st.error(action_error_msg(c, m))

                    with bcol_del:
                        if status in ["Draft","Stopped","Paused"]:
                            if st.button("🗑", key=f"del_{idx}", help="삭제"):
                                c, m = journey_action("delete", jid, version, token, rest_base)
                                if c in [200,201,202,204]:
                                    st.session_state["journeys_all"] = [
                                        item for item in st.session_state["journeys_all"]
                                        if item.get("id") != jid
                                    ]
                                    st.session_state["selected_journeys"].discard(jid)
                                    st.rerun()
                                else:
                                    st.error(action_error_msg(c, m))

                    with link_col:
                        if sfmc_link:
                            st.link_button("↗", sfmc_link)

                    st.markdown("<div style='height:1px;background:#f1f5f9;margin:2px 0;'></div>", unsafe_allow_html=True)

                # AI 분석
                if active_ai and journeys:
                    st.markdown("---")
                    if st.button("🤖 AI Journey 현황 분석", key="ai_j"):
                        with st.spinner("분석 중..."):
                            summary_text = "\n".join([
                                f"- {j.get('name','?')} | {j.get('status','?')} | v{j.get('version',1)} | 수정:{j.get('modifiedDate','')[:10]}"
                                for j in journeys
                            ])
                            result = call_ai(
                                """SFMC Journey Builder 전문가로서 Journey 목록을 분석하세요.
Draft 미배포, 오래된 Published Journey, 버전 이슈 등을 파악하고 개선 제안을 한국어로 해주세요.""",
                                f"Journey 목록:\n{summary_text}")
                        st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)

        # ════════════════════════════════════════════════════════════════════
        # JOURNEY 점검 탭
        # ════════════════════════════════════════════════════════════════════
        with tab_check:
            journeys_all = st.session_state.get("journeys_all", [])

            if not journeys_all:
                st.markdown("""
                <div style="background:#fef9c3;border:1px solid #fde68a;border-radius:8px;
                padding:16px 20px;font-size:13px;color:#92400e;">
                ⚠️ 먼저 <strong>Journey 목록</strong> 탭에서 Journey를 불러와주세요.
                </div>
                """, unsafe_allow_html=True)
            else:
                from datetime import datetime

                def days_ago(date_str):
                    if not date_str:
                        return 9999
                    try:
                        return (datetime.now() - datetime.fromisoformat(date_str[:19])).days
                    except:
                        return 9999

                # ── 필터 ──────────────────────────────────────────────────
                ff1, ff2, ff3 = st.columns([1.5, 1.5, 1.5])
                with ff1:
                    filter_category = st.selectbox("점검 항목", ["전체","방치된 Draft","중복 이름","오래된 Published","미사용 Stopped"], label_visibility="collapsed")
                with ff2:
                    filter_status = st.selectbox("상태 필터", ["전체","Draft","Published","Stopped","Paused"], label_visibility="collapsed")
                with ff3:
                    filter_days = st.selectbox("방치 기준", ["30일+","60일+","90일+","180일+"], label_visibility="collapsed")
                    threshold = int(filter_days.replace("일+",""))

                # ── 점검 항목 계산 ─────────────────────────────────────────
                from collections import Counter
                issues = {"방치된 Draft":[], "중복 이름":[], "오래된 Published":[], "미사용 Stopped":[]}

                for j in journeys_all:
                    if j.get("status") == "Draft" and days_ago(j.get("modifiedDate","")) >= threshold:
                        issues["방치된 Draft"].append(j)

                name_counts = Counter(j.get("name","").strip().lower() for j in journeys_all)
                dup_names = {n for n, c in name_counts.items() if c > 1}
                seen_dups = set()
                for j in journeys_all:
                    name_lower = j.get("name","").strip().lower()
                    if name_lower in dup_names and name_lower not in seen_dups:
                        dups = [x for x in journeys_all if x.get("name","").strip().lower() == name_lower]
                        issues["중복 이름"].extend(dups)
                        seen_dups.add(name_lower)

                for j in journeys_all:
                    if j.get("status") in ["Published","Active"] and days_ago(j.get("modifiedDate","")) >= threshold:
                        issues["오래된 Published"].append(j)

                for j in journeys_all:
                    if j.get("status") == "Stopped" and days_ago(j.get("modifiedDate","")) >= threshold:
                        issues["미사용 Stopped"].append(j)

                if filter_status != "전체":
                    for k in issues:
                        issues[k] = [j for j in issues[k] if j.get("status") == filter_status]

                # ── 상세 내역 자동 생성 ────────────────────────────────────
                def get_detail(j, category):
                    d = days_ago(j.get("modifiedDate",""))
                    d_str = f"{d}일" if d < 9999 else "-"
                    if category == "방치된 Draft":
                        return f"{d_str} 동안 미수정 Draft"
                    elif category == "중복 이름":
                        cnt = name_counts.get(j.get("name","").strip().lower(), 1)
                        return f"동일 이름 {cnt}개 존재"
                    elif category == "오래된 Published":
                        return f"{d_str} 동안 미수정 운영 중"
                    elif category == "미사용 Stopped":
                        return f"{d_str} 동안 방치된 Stopped"
                    return "-"

                # ── 일괄 선택/삭제 ─────────────────────────────────────────
                if "chk_issues" not in st.session_state:
                    st.session_state["chk_issues"] = set()
                if "chk_issues_v" not in st.session_state:
                    st.session_state["chk_issues_v"] = 0
                if "section_open" not in st.session_state:
                    st.session_state["section_open"] = {"방치된 Draft":True,"중복 이름":True,"오래된 Published":True,"미사용 Stopped":True}

                sel_issues = st.session_state["chk_issues"]
                chk_v = st.session_state["chk_issues_v"]
                sfmc_web_url = st.session_state.get("sfmc_web_url","")

                all_deletable_ids = set()
                for cat in ["방치된 Draft","중복 이름","미사용 Stopped"]:
                    for j in issues[cat]:
                        if j.get("status") in ["Draft","Stopped"]:
                            all_deletable_ids.add(j.get("id"))

                # ── 요약 카드 ──────────────────────────────────────────────
                ic1, ic2, ic3, ic4 = st.columns(4)
                card_data = [
                    (ic1, "방치된 Draft",     "#fef9c3","#fde68a","#92400e", f"{threshold}일+ 미수정"),
                    (ic2, "중복 이름",        "#fee2e2","#fecaca","#dc2626", "동일 이름 Journey"),
                    (ic3, "오래된 Published", "#dbeafe","#bfdbfe","#1d4ed8", f"{threshold}일+ 미수정 운영 중"),
                    (ic4, "미사용 Stopped",   "#f1f5f9","#e2e8f0","#64748b", f"{threshold}일+ 방치"),
                ]
                for col, label, bg, border, color, sub in card_data:
                    with col:
                        st.markdown(f"""<div style="background:{bg};border:1px solid {border};
                        border-radius:8px;padding:12px 16px;">
                        <div style="font-size:11px;color:{color};margin-bottom:4px;font-weight:500;">{label}</div>
                        <div style="font-size:26px;font-weight:700;color:{color};">{len(issues[label])}</div>
                        <div style="font-size:10px;color:{color};opacity:0.7;margin-top:2px;">{sub}</div>
                        </div>""", unsafe_allow_html=True)

                st.markdown("<div style='margin:12px 0;'></div>", unsafe_allow_html=True)

                # ── 상태 + 일괄 버튼 ───────────────────────────────────────
                total_issues = sum(len(v) for v in issues.values())
                if total_issues == 0:
                    st.markdown("""<div style="background:#dcfce7;border:1px solid #bbf7d0;border-radius:8px;
                    padding:14px 16px;font-size:13px;color:#15803d;">
                    ✅ 점검 결과 이상 없음</div>""", unsafe_allow_html=True)
                else:
                    st.markdown(f"""<div style="background:#fee2e2;border:1px solid #fecaca;border-radius:8px;
                    padding:10px 16px;font-size:13px;color:#dc2626;margin-bottom:8px;">
                    ⚠️ 총 {total_issues}건의 점검 항목이 발견됐습니다.</div>""", unsafe_allow_html=True)

                # 선택 개수에 따라 버튼 구성 변경
                if len(sel_issues) > 0:
                    # 선택된 항목 있을 때 — 선택개수 + 전체선택 + 선택해제 + 일괄삭제
                    chk_ba1, chk_ba2, chk_ba3, chk_ba4, _ = st.columns([0.8, 0.8, 0.8, 0.8, 5])
                    with chk_ba1:
                        st.markdown(f"<div style='font-size:12px;color:#94a3b8;padding-top:6px;'>{len(sel_issues)}개 선택</div>", unsafe_allow_html=True)
                    with chk_ba2:
                        if st.button("전체선택", key="chk_sel_all"):
                            st.session_state["chk_issues"] = set(all_deletable_ids)
                            st.session_state["chk_issues_v"] += 1
                            st.rerun()
                    with chk_ba3:
                        if st.button("선택해제", key="chk_sel_none"):
                            st.session_state["chk_issues"] = set()
                            st.session_state["chk_issues_v"] += 1
                            st.rerun()
                    with chk_ba4:
                        if st.button("일괄삭제", key="chk_bulk_del"):
                            ok, fail = 0, 0
                            deleted_ids = set()
                            all_items = [j for cat in issues.values() for j in cat if j.get("id") in sel_issues]
                            seen = set()
                            unique_items = [j for j in all_items if j.get("id") not in seen and not seen.add(j.get("id"))]
                            for j in unique_items:
                                c, m = journey_action("delete", j["id"], j.get("version",1), token, rest_base)
                                if c in [200,201,202,204]:
                                    ok += 1; deleted_ids.add(j["id"])
                                else:
                                    fail += 1
                            if deleted_ids:
                                st.session_state["journeys_all"] = [x for x in st.session_state.get("journeys_all",[]) if x.get("id") not in deleted_ids]
                            st.session_state["chk_issues"] = set()
                            st.session_state["chk_issues_v"] += 1
                            st.success(f"삭제 완료 {ok}개" + (f", 실패 {fail}개" if fail else ""))
                            st.rerun()
                else:
                    # 선택 없을 때 — 선택개수 + 전체선택 + 선택해제
                    chk_ba1, chk_ba2, chk_ba3, _ = st.columns([0.8, 0.8, 0.8, 7])
                    with chk_ba1:
                        st.markdown(f"<div style='font-size:12px;color:#94a3b8;padding-top:6px;'>{len(sel_issues)}개 선택</div>", unsafe_allow_html=True)
                    with chk_ba2:
                        if st.button("전체선택", key="chk_sel_all2"):
                            st.session_state["chk_issues"] = set(all_deletable_ids)
                            st.session_state["chk_issues_v"] += 1
                            st.rerun()
                    with chk_ba3:
                        if st.button("선택해제", key="chk_sel_none2"):
                            st.session_state["chk_issues"] = set()
                            st.session_state["chk_issues_v"] += 1
                            st.rerun()
                # ── 섹션 렌더링 ────────────────────────────────────────────
                SECTION_CONFIG = {
                    "방치된 Draft":      ("#fef9c3","#fde68a","#92400e","⚠️"),
                    "중복 이름":         ("#fee2e2","#fecaca","#dc2626","🔴"),
                    "오래된 Published":  ("#dbeafe","#bfdbfe","#1d4ed8","🔵"),
                    "미사용 Stopped":    ("#f1f5f9","#e2e8f0","#64748b","⬜"),
                }

                STATUS_COLORS_CHK = {"Published":"#15803d","Draft":"#92400e","Paused":"#1d4ed8","Stopped":"#64748b","Active":"#15803d"}
                STATUS_BG_CHK    = {"Published":"#dcfce7","Draft":"#fef9c3","Paused":"#dbeafe","Stopped":"#f1f5f9","Active":"#dcfce7"}

                for cat, (bg, border, color, icon) in SECTION_CONFIG.items():
                    if filter_category != "전체" and filter_category != cat:
                        continue
                    items = issues[cat]

                    with st.expander(f"{icon} {cat}  ({len(items)}건)", expanded=True):
                        if not items:
                            st.markdown("<div style='font-size:12px;color:#94a3b8;padding:4px 0;'>해당 없음</div>", unsafe_allow_html=True)
                        else:
                            # 테이블 헤더
                            h0, h1, h2, h3, h4, h5 = st.columns([0.35, 4, 1.2, 2.2, 0.6, 0.6])
                            with h1: st.markdown("<div style='font-size:10px;font-weight:600;color:#94a3b8;letter-spacing:0.06em;text-transform:uppercase;padding:6px 0;'>Journey Name</div>", unsafe_allow_html=True)
                            with h2: st.markdown("<div style='font-size:10px;font-weight:600;color:#94a3b8;letter-spacing:0.06em;text-transform:uppercase;padding:6px 0;'>Status</div>", unsafe_allow_html=True)
                            with h3: st.markdown("<div style='font-size:10px;font-weight:600;color:#94a3b8;letter-spacing:0.06em;text-transform:uppercase;padding:6px 0;'>상세 내역</div>", unsafe_allow_html=True)
                            with h4: st.markdown("<div style='font-size:10px;font-weight:600;color:#94a3b8;letter-spacing:0.06em;text-transform:uppercase;padding:6px 0;'>바로가기</div>", unsafe_allow_html=True)
                            with h5: st.markdown("<div style='font-size:10px;font-weight:600;color:#94a3b8;letter-spacing:0.06em;text-transform:uppercase;padding:6px 0;'>삭제</div>", unsafe_allow_html=True)
                            st.markdown("<div style='height:1px;background:#e2e8f0;margin-bottom:4px;'></div>", unsafe_allow_html=True)

                            for i, j in enumerate(items):
                                status = j.get("status","")
                                sc = STATUS_COLORS_CHK.get(status,"#64748b")
                                sb = STATUS_BG_CHK.get(status,"#f1f5f9")
                                name = j.get("name","이름 없음")
                                jid = j.get("id","")
                                version = j.get("version",1)
                                can_delete = status in ["Draft","Stopped"]
                                is_selected = jid in sel_issues
                                detail = get_detail(j, cat)

                                if sfmc_web_url:
                                    base = sfmc_web_url.strip()
                                    if not base.startswith("http"):
                                        base = "https://" + base
                                    sfmc_link = f"{base}/cloud/#app/Journey%20Builder/%23{jid}/{version}"
                                else:
                                    sfmc_link = ""

                                row_key = f"issue_{cat}_{i}"
                                chk_col, info_col, badge_col, detail_col, link_col, del_col = st.columns(
                                    [0.35, 4, 1.2, 2.2, 0.6, 0.6], vertical_alignment="center"
                                )
                                with chk_col:
                                    if can_delete:
                                        checked = st.checkbox("", key=f"{row_key}_v{chk_v}", value=is_selected)
                                        if checked and jid not in sel_issues:
                                            st.session_state["chk_issues"].add(jid)
                                            st.rerun()
                                        elif not checked and jid in sel_issues:
                                            st.session_state["chk_issues"].discard(jid)
                                            st.rerun()
                                with info_col:
                                    st.markdown(f"""<div>
                                    <span style="font-size:13px;font-weight:500;color:#1e293b;">{name}</span>
                                    <div style="font-size:10px;color:#94a3b8;margin-top:2px;">v{version}</div>
                                    </div>""", unsafe_allow_html=True)
                                with badge_col:
                                    st.markdown(f"""<span style="display:inline-flex;align-items:center;gap:4px;
                                    font-size:11px;font-weight:600;padding:3px 10px;border-radius:99px;
                                    background:{sb};color:{sc};">
                                    <span style="width:5px;height:5px;border-radius:50%;background:{sc};display:inline-block;"></span>
                                    {status}</span>""", unsafe_allow_html=True)
                                with detail_col:
                                    st.markdown(f"""<span style="display:inline-block;font-size:11px;
                                    color:{color};background:{bg};border:1px solid {border};
                                    border-radius:99px;padding:2px 10px;">{detail}</span>""", unsafe_allow_html=True)
                                with link_col:
                                    if sfmc_link:
                                        st.link_button("↗", sfmc_link)
                                with del_col:
                                    if can_delete:
                                        if st.button("🗑", key=f"{row_key}_del", help="삭제"):
                                            c, m = journey_action("delete", jid, version, token, rest_base)
                                            if c in [200,201,202,204]:
                                                st.session_state["journeys_all"] = [
                                                    x for x in st.session_state.get("journeys_all",[]) if x.get("id") != jid
                                                ]
                                                st.session_state["chk_issues"].discard(jid)
                                                st.success(f"삭제: {name}")
                                                st.rerun()
                                            else:
                                                st.error(action_error_msg(c, m))


        # ════════════════════════════════════════════════════════════════════
        # 대시보드 탭
        # ════════════════════════════════════════════════════════════════════
        with tab_dash:
            st.markdown("""
            <div class="page-header">
                <div class="page-title">대시보드</div>
                <div class="page-desc">Journey 이메일 발송 성과 및 바운스 현황을 한눈에 확인합니다.</div>
            </div>
            """, unsafe_allow_html=True)

            import requests as _req

            if not st.session_state.get("sfmc_token"):
                st.markdown("""<div style="background:#fee2e2;border:1px solid #fecaca;border-radius:8px;
                padding:20px;font-size:13px;color:#dc2626;">
                ⚠️ 왼쪽 사이드바에서 <strong>SFMC 연결</strong>을 먼저 해주세요.</div>""", unsafe_allow_html=True)
            else:
                token = st.session_state["sfmc_token"]
                rest_base = st.session_state["sfmc_rest_base"]

                # 필터 행
                fc1, fc2, fc3 = st.columns([1.2, 1.2, 1.2])
                with fc1:
                    show_only_sent = st.checkbox("발송 있는 Journey만 보기", value=True, key="dash_filter_sent")
                with fc2:
                    bounce_filter = st.selectbox("바운스 기준", ["전체","2% 이상","5% 이상","10% 이상"], key="dash_bounce_filter", label_visibility="collapsed")
                with fc3:
                    pass

                load_col, _ = st.columns([1.5, 8])
                with load_col:
                    load_btn = st.button("🔄 대시보드 불러오기", key="load_dashboard")

                if load_btn:
                    import time
                    from datetime import datetime, timezone
                    date_end = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                    date_start = "2023-01-01T00:00:00Z"

                    with st.spinner("데이터 불러오는 중..."):
                        journeys_all = st.session_state.get("journeys_all", [])
                        if not journeys_all:
                            r = _req.get(f"{rest_base}/interaction/v1/interactions",
                                headers={"Authorization": f"Bearer {token}"},
                                params={"$pageSize": 200, "status": "Published"})
                            if r.status_code == 200:
                                journeys_all = r.json().get("items", [])

                        published = sorted(
                            [j for j in journeys_all if j.get("status") in ["Published","Active"]],
                            key=lambda j: j.get("modifiedDate","1970-01-01"), reverse=True
                        )[:10]

                        journey_stats = []
                        for j in published:
                            jid = j.get("id","")
                            try:
                                r1 = _req.get(f"{rest_base}/interaction/v1/interactions/{jid}",
                                    headers={"Authorization": f"Bearer {token}"})
                                if r1.status_code != 200: continue
                                version_id = r1.json().get("versionId") or r1.json().get("id","")
                                modified = j.get("modifiedDate","")[:10] if j.get("modifiedDate") else "-"
                                time.sleep(0.15)

                                r_fail = _req.post(
                                    f"{rest_base}/interaction/v1/interactions/journeyhistory/download?columns=ContactKey",
                                    headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "x-direct-pipe": "true"},
                                    json={"definitionIds": [version_id], "activityTypes": ["emailv2"], "statuses": ["Failed"], "start": date_start, "end": date_end})
                                r_ok = _req.post(
                                    f"{rest_base}/interaction/v1/interactions/journeyhistory/download?columns=ContactKey",
                                    headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "x-direct-pipe": "true"},
                                    json={"definitionIds": [version_id], "activityTypes": ["emailv2"], "statuses": ["Complete"], "start": date_start, "end": date_end})

                                failed = max(0, len(r_fail.text.strip().split("\n")) - 1) if r_fail.status_code == 200 and r_fail.text.strip() else 0
                                complete = max(0, len(r_ok.text.strip().split("\n")) - 1) if r_ok.status_code == 200 and r_ok.text.strip() else 0
                                total = failed + complete
                                bounce_rate = round(failed / total * 100, 1) if total > 0 else 0.0

                                journey_stats.append({
                                    "name": j.get("name",""),
                                    "version": j.get("version",1),
                                    "id": jid,
                                    "modified": modified,
                                    "sends": total,
                                    "bounces": failed,
                                    "bounce_rate": bounce_rate,
                                })
                            except: pass
                            time.sleep(0.15)

                        st.session_state["dashboard_stats"] = journey_stats
                        # rerun 제거 — 탭이 바뀌는 문제 방지

                stats = st.session_state.get("dashboard_stats", [])
                if stats:
                    # 필터 적용
                    display_stats = stats[:]
                    if show_only_sent:
                        display_stats = [s for s in display_stats if s["sends"] > 0]
                    if bounce_filter == "2% 이상":
                        display_stats = [s for s in display_stats if s["bounce_rate"] >= 2]
                    elif bounce_filter == "5% 이상":
                        display_stats = [s for s in display_stats if s["bounce_rate"] >= 5]
                    elif bounce_filter == "10% 이상":
                        display_stats = [s for s in display_stats if s["bounce_rate"] >= 10]

                    total_sends = sum(s["sends"] for s in stats)
                    total_bounces = sum(s["bounces"] for s in stats)
                    avg_bounce = round(total_bounces / total_sends * 100, 1) if total_sends > 0 else 0.0
                    danger_count = sum(1 for s in stats if s["bounce_rate"] >= 10)
                    warning_count = sum(1 for s in stats if 5 <= s["bounce_rate"] < 10)

                    # 요약 카드
                    mc1, mc2, mc3, mc4 = st.columns(4)
                    with mc1:
                        st.markdown(f"""<div style="background:#f1f5f9;border:1px solid #e2e8f0;border-radius:8px;padding:14px 16px;">
                        <div style="font-size:11px;color:#64748b;margin-bottom:4px;">조회된 Journey</div>
                        <div style="font-size:26px;font-weight:600;color:#1e293b;">{len(stats)}</div>
                        <div style="font-size:11px;color:#94a3b8;margin-top:4px;">Published 최근 10개</div></div>""", unsafe_allow_html=True)
                    with mc2:
                        st.markdown(f"""<div style="background:#dbeafe;border:1px solid #bfdbfe;border-radius:8px;padding:14px 16px;">
                        <div style="font-size:11px;color:#1d4ed8;margin-bottom:4px;">총 발송</div>
                        <div style="font-size:26px;font-weight:600;color:#1d4ed8;">{total_sends:,}</div>
                        <div style="font-size:11px;color:#1d4ed8;margin-top:4px;">바운스 {total_bounces:,}건</div></div>""", unsafe_allow_html=True)
                    with mc3:
                        rc = "#dc2626" if avg_bounce >= 5 else "#92400e" if avg_bounce >= 2 else "#15803d"
                        rb = "#fee2e2" if avg_bounce >= 5 else "#fef9c3" if avg_bounce >= 2 else "#dcfce7"
                        rbd = "#fecaca" if avg_bounce >= 5 else "#fde68a" if avg_bounce >= 2 else "#bbf7d0"
                        st.markdown(f"""<div style="background:{rb};border:1px solid {rbd};border-radius:8px;padding:14px 16px;">
                        <div style="font-size:11px;color:{rc};margin-bottom:4px;">평균 바운스율</div>
                        <div style="font-size:26px;font-weight:600;color:{rc};">{avg_bounce}%</div>
                        <div style="font-size:11px;color:{rc};margin-top:4px;">업계 권장: 5% 미만</div></div>""", unsafe_allow_html=True)
                    with mc4:
                        st.markdown(f"""<div style="background:#fee2e2;border:1px solid #fecaca;border-radius:8px;padding:14px 16px;">
                        <div style="font-size:11px;color:#dc2626;margin-bottom:4px;">주의 필요</div>
                        <div style="font-size:26px;font-weight:600;color:#dc2626;">{danger_count + warning_count}</div>
                        <div style="font-size:11px;color:#dc2626;margin-top:4px;">위험 {danger_count} / 주의 {warning_count}</div></div>""", unsafe_allow_html=True)

                    st.markdown("<div style='margin:16px 0;'></div>", unsafe_allow_html=True)

                    # 차트 — 발송 있는 것만
                    chart_stats = [s for s in stats if s["sends"] > 0]
                    import json as _json

                    st.markdown("<div style='margin:16px 0;'></div>", unsafe_allow_html=True)

                    chart_col, donut_col = st.columns([2, 1])
                    chart_height = max(220, len(chart_stats) * 50 + 80) if chart_stats else 220
                    donut_height = chart_height

                    with chart_col:
                        st.markdown(f"""<div style="background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:16px;height:{chart_height+80}px;">
                        <div style="font-size:13px;font-weight:500;color:#1e293b;margin-bottom:4px;">Journey별 발송 현황</div>""", unsafe_allow_html=True)
                        if chart_stats:
                            import plotly.graph_objects as go
                            names = [s["name"][:22]+"…" if len(s["name"])>22 else s["name"] for s in chart_stats]
                            ok_data     = [s["sends"]-s["bounces"] for s in chart_stats]
                            bounce_data = [s["bounces"] for s in chart_stats]
                            fig_bar = go.Figure()
                            fig_bar.add_trace(go.Bar(name="정상 발송", y=names, x=ok_data,     orientation='h', marker_color='#bfdbfe'))
                            fig_bar.add_trace(go.Bar(name="바운스",    y=names, x=bounce_data, orientation='h', marker_color='#fecaca'))
                            fig_bar.update_layout(
                                barmode='stack', margin=dict(l=0,r=0,t=10,b=40),
                                height=chart_height,
                                legend=dict(orientation='h', y=-0.2, x=0),
                                plot_bgcolor='#fff', paper_bgcolor='#fff',
                                xaxis=dict(gridcolor='#f1f5f9', tickfont=dict(size=10, color='#94a3b8')),
                                yaxis=dict(tickfont=dict(size=11, color='#475569'), autorange='reversed')
                            )
                            st.plotly_chart(fig_bar, use_container_width=True)
                        else:
                            st.markdown("<div style='font-size:13px;color:#94a3b8;padding:20px 0;text-align:center;'>발송 데이터가 있는 Journey가 없습니다.</div>", unsafe_allow_html=True)
                        st.markdown("</div>", unsafe_allow_html=True)

                    with donut_col:
                        normal = sum(1 for s in stats if s["bounce_rate"] < 2)
                        watch  = sum(1 for s in stats if 2 <= s["bounce_rate"] < 5)
                        warn   = sum(1 for s in stats if 5 <= s["bounce_rate"] < 10)
                        danger = sum(1 for s in stats if s["bounce_rate"] >= 10)
                        st.markdown(f"""<div style="background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:16px;height:{chart_height+80}px;">
                        <div style="font-size:13px;font-weight:500;color:#1e293b;margin-bottom:4px;">바운스율 분포</div>""", unsafe_allow_html=True)
                        import plotly.graph_objects as go
                        fig_donut = go.Figure(go.Pie(
                            labels=["정상 (0-2%)", "관찰 (2-5%)", "주의 (5-10%)", "위험 (10%+)"],
                            values=[max(normal,0), max(watch,0), max(warn,0), max(danger,0)],
                            hole=0.6,
                            marker_colors=["#dcfce7","#dbeafe","#fef9c3","#fee2e2"],
                            marker_line=dict(color=["#bbf7d0","#bfdbfe","#fde68a","#fecaca"], width=1),
                            textinfo='none',
                            showlegend=False
                        ))
                        fig_donut.update_layout(
                            margin=dict(l=0,r=0,t=10,b=0), height=int(chart_height*0.65),
                            plot_bgcolor='#fff', paper_bgcolor='#fff'
                        )
                        st.plotly_chart(fig_donut, use_container_width=True)
                        st.markdown(f"""<div style="display:flex;flex-direction:column;gap:5px;font-size:11px;padding-bottom:12px;">
                        <span style="color:#15803d;">● 정상 (0-2%): {normal}개</span>
                        <span style="color:#1d4ed8;">● 관찰 (2-5%): {watch}개</span>
                        <span style="color:#92400e;">● 주의 (5-10%): {warn}개</span>
                        <span style="color:#dc2626;">● 위험 (10%+): {danger}개</span>
                        </div></div>""", unsafe_allow_html=True)

                    st.markdown("<div style='margin:16px 0;'></div>", unsafe_allow_html=True)

                    # Journey 성과 테이블
                    st.markdown("""<div style="background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:16px;">
                    <div style="font-size:13px;font-weight:500;color:#1e293b;margin-bottom:12px;">Journey별 상세 현황</div>""", unsafe_allow_html=True)

                    th1,th2,th3,th4,th5,th6 = st.columns([3.5,1,1,1,1.8,0.7])
                    for col, label in zip([th1,th2,th3,th4,th5,th6],["Journey Name","최근 수정일","발송","바운스","바운스율","바로가기"]):
                        with col:
                            col.markdown(f"<div style='font-size:10px;font-weight:600;color:#94a3b8;text-transform:uppercase;padding:4px 0;'>{label}</div>", unsafe_allow_html=True)
                    st.markdown("<div style='height:1px;background:#e2e8f0;margin-bottom:4px;'></div>", unsafe_allow_html=True)

                    sfmc_web_url_d = st.session_state.get("sfmc_web_url","")
                    sorted_stats = sorted(display_stats, key=lambda x: x["bounce_rate"], reverse=True)

                    for s in sorted_stats:
                        rate = s["bounce_rate"]
                        is_zero = s["sends"] == 0
                        if is_zero:
                            bc,bb,bt = "#94a3b8","#f8fafc","데이터없음"
                        elif rate >= 10: bc,bb,bt = "#dc2626","#fee2e2","위험"
                        elif rate >= 5:  bc,bb,bt = "#92400e","#fef9c3","주의"
                        elif rate >= 2:  bc,bb,bt = "#1d4ed8","#dbeafe","관찰"
                        else:            bc,bb,bt = "#15803d","#dcfce7","정상"

                        if sfmc_web_url_d:
                            base = sfmc_web_url_d.strip()
                            if not base.startswith("http"): base = "https://" + base
                            link = f"{base}/cloud/#app/Journey%20Builder/%23{s['id']}/{s['version']}"
                        else:
                            link = ""

                        text_alpha = "opacity:0.4;" if is_zero else ""
                        rc1,rc2,rc3,rc4,rc5,rc6 = st.columns([3.5,1,1,1,1.8,0.7], vertical_alignment="center")
                        with rc1:
                            st.markdown(f"""<div style="{text_alpha}">
                            <span style="font-size:13px;font-weight:500;color:#1e293b;">{s['name']}</span>
                            <div style="font-size:10px;color:#94a3b8;">v{s['version']}</div></div>""", unsafe_allow_html=True)
                        with rc2:
                            st.markdown(f"<div style='font-size:11px;color:#64748b;{text_alpha}'>{s['modified']}</div>", unsafe_allow_html=True)
                        with rc3:
                            st.markdown(f"<div style='font-size:13px;color:#1e293b;{text_alpha}'>{s['sends']:,}</div>", unsafe_allow_html=True)
                        with rc4:
                            st.markdown(f"<div style='font-size:13px;color:#dc2626;font-weight:500;{text_alpha}'>{s['bounces']:,}</div>", unsafe_allow_html=True)
                        with rc5:
                            st.markdown(f"""<span style="display:inline-block;font-size:12px;font-weight:500;
                            padding:3px 12px;border-radius:99px;background:{bb};color:{bc};">
                            {'' if is_zero else str(rate)+'% '}{bt}</span>""", unsafe_allow_html=True)
                        with rc6:
                            if link:
                                st.link_button("↗", link)
                        st.markdown("<div style='height:1px;background:#f1f5f9;'></div>", unsafe_allow_html=True)

                    st.markdown("</div>", unsafe_allow_html=True)

                    if not display_stats:
                        st.markdown("""<div style="background:#dcfce7;border:1px solid #bbf7d0;border-radius:8px;
                        padding:14px 16px;font-size:13px;color:#15803d;">
                        ✅ 현재 필터 조건에 해당하는 Journey가 없습니다.</div>""", unsafe_allow_html=True)
