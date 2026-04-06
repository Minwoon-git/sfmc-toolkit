import streamlit as st

st.set_page_config(
    page_title="SFMC Toolkit",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'IBM Plex Sans', sans-serif;
}

.stApp {
    background-color: #0a0a0f;
    color: #e8e8f0;
}

section[data-testid="stSidebar"] {
    background-color: #0f0f1a;
    border-right: 1px solid #1e1e2e;
}

section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] label {
    color: #8888aa;
    font-size: 12px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.sidebar-title {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 18px;
    font-weight: 500;
    color: #e8e8f0;
    letter-spacing: -0.02em;
    margin-bottom: 4px;
}

.sidebar-sub {
    font-size: 11px;
    color: #4444666;
    letter-spacing: 0.05em;
    margin-bottom: 32px;
}

.page-header {
    margin-bottom: 32px;
    padding-bottom: 20px;
    border-bottom: 1px solid #1e1e2e;
}

.page-title {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 26px;
    font-weight: 500;
    color: #e8e8f0;
    letter-spacing: -0.03em;
    margin-bottom: 6px;
}

.page-desc {
    font-size: 14px;
    color: #6666888;
    line-height: 1.6;
}

.result-box {
    background-color: #0f0f1a;
    border: 1px solid #1e1e2e;
    border-radius: 8px;
    padding: 20px;
    margin-top: 16px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 13px;
    line-height: 1.7;
    color: #c8c8e0;
    white-space: pre-wrap;
}

.result-label {
    font-size: 11px;
    font-weight: 500;
    color: #4a9eff;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.tag {
    display: inline-block;
    font-size: 10px;
    padding: 3px 10px;
    border-radius: 4px;
    font-weight: 500;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

.tag-blue { background: #0a2040; color: #4a9eff; border: 1px solid #1a4070; }
.tag-green { background: #0a2015; color: #3acc7a; border: 1px solid #1a4030; }
.tag-amber { background: #201500; color: #f0a030; border: 1px solid #402a00; }
.tag-red { background: #200a0a; color: #ff5555; border: 1px solid #401010; }

.memo-card {
    background-color: #0f0f1a;
    border: 1px solid #1e1e2e;
    border-left: 3px solid #4a9eff;
    border-radius: 6px;
    padding: 16px 18px;
    margin-bottom: 12px;
}

.memo-meta {
    font-size: 11px;
    color: #555577;
    font-family: 'IBM Plex Mono', monospace;
    margin-bottom: 8px;
}

.memo-content {
    font-size: 13px;
    color: #a0a0c0;
    line-height: 1.6;
}

.memo-summary {
    font-size: 12px;
    color: #4a9eff;
    margin-top: 10px;
    padding-top: 10px;
    border-top: 1px solid #1e1e2e;
    line-height: 1.6;
}

div[data-testid="stTextArea"] textarea {
    background-color: #0f0f1a !important;
    border: 1px solid #1e1e2e !important;
    border-radius: 6px !important;
    color: #e8e8f0 !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 13px !important;
}

div[data-testid="stTextInput"] input {
    background-color: #0f0f1a !important;
    border: 1px solid #1e1e2e !important;
    border-radius: 6px !important;
    color: #e8e8f0 !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
}

div[data-testid="stSelectbox"] > div {
    background-color: #0f0f1a !important;
    border: 1px solid #1e1e2e !important;
    color: #e8e8f0 !important;
}

.stButton > button {
    background-color: #4a9eff !important;
    color: #000 !important;
    border: none !important;
    border-radius: 6px !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    letter-spacing: 0.03em !important;
    padding: 8px 20px !important;
    transition: all 0.15s !important;
}

.stButton > button:hover {
    background-color: #6ab0ff !important;
    transform: translateY(-1px);
}

.stSpinner > div {
    border-top-color: #4a9eff !important;
}

label[data-testid="stWidgetLabel"] {
    color: #8888aa !important;
    font-size: 12px !important;
    font-weight: 500 !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase !important;
}

.status-ok {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 12px;
    color: #3acc7a;
    background: #0a2015;
    border: 1px solid #1a4030;
    border-radius: 4px;
    padding: 4px 10px;
    margin-bottom: 16px;
}

.stRadio label {
    color: #8888aa !important;
    font-size: 13px !important;
}

hr {
    border-color: #1e1e2e !important;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-title">⚡ SFMC Toolkit</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-sub">by AI · v1.0</div>', unsafe_allow_html=True)

    api_key = st.text_input(
        "Anthropic API Key",
        type="password",
        placeholder="sk-ant-...",
        help="Anthropic API 키를 입력하세요"
    )

    if api_key:
        st.markdown('<div class="status-ok">● API 연결됨</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**도구 선택**")

    menu = st.radio(
        "",
        ["🗂️ Journey / Automation 관리", "💾 SQL 생성기", "🔧 AMPscript 어시스턴트", "🔍 에러 분석기"],
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
                import requests
                auth_url = f"https://{sfmc_subdomain}.auth.marketingcloudapis.com/v2/token"
                resp = requests.post(auth_url, json={
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
                    st.success("SFMC 연결 성공!")
                else:
                    st.error(f"연결 실패: {resp.status_code}")
            except Exception as e:
                st.error(f"오류: {e}")

    if st.session_state.get("sfmc_token"):
        st.markdown('<div class="status-ok">● SFMC 연결됨</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style="font-size:11px; color:#333355; line-height:1.8;">
    SFMC Toolkit v1.1<br>AI + SFMC 연동 버전
    </div>
    """, unsafe_allow_html=True)

# ── AI 호출 함수 ────────────────────────────────────────────────────────────
def call_claude(api_key: str, system_prompt: str, user_message: str) -> str:
    import anthropic
    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}]
    )
    return message.content[0].text


def call_claude_with_search(api_key: str, system_prompt: str, user_message: str) -> str:
    """웹 검색 기능이 포함된 Claude 호출 - 에러 분석기 전용"""
    import anthropic
    client = anthropic.Anthropic(api_key=api_key)

    tools = [{"type": "web_search_20250305", "name": "web_search"}]
    messages = [{"role": "user", "content": user_message}]
    full_text = ""

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=3000,
            system=system_prompt,
            tools=tools,
            messages=messages
        )

        # assistant 메시지를 히스토리에 추가 (tool_use 블록 포함)
        messages.append({"role": "assistant", "content": response.content})

        # 텍스트 블록 수집
        for block in response.content:
            if hasattr(block, "text"):
                full_text += block.text

        # 툴 사용이 없으면 종료
        if response.stop_reason != "tool_use":
            break

        # tool_use 블록에서 실제 검색 결과를 tool_result로 반환
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                # web_search 툴은 결과를 block.input이 아닌 서버 측에서 처리함
                # tool_result를 빈 content로 보내면 Claude가 자체 검색 결과를 이미 갖고 있음
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": []  # web_search는 서버 측 처리 — 빈 배열로 응답해야 정상 작동
                })

        messages.append({"role": "user", "content": tool_results})

    return full_text


def require_key():
    st.markdown("""
    <div style="background:#200a0a; border:1px solid #401010; border-radius:8px;
    padding:20px; color:#ff5555; font-size:13px; line-height:1.8;">
    ⚠️ 왼쪽 사이드바에서 <strong>Anthropic API Key</strong>를 먼저 입력해주세요.<br>
    <span style="color:#555577; font-size:12px;">키는 저장되지 않으며 세션 중에만 사용됩니다.</span>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 1. 에러 분석기
# ══════════════════════════════════════════════════════════════════════════════
if menu == "🔍 에러 분석기":
    st.markdown("""
    <div class="page-header">
        <div class="page-title">에러 분석기</div>
        <div class="page-desc">SFMC의 불친절한 에러 메시지를 붙여넣으면 원인과 해결법을 한국어로 알려드립니다.</div>
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

    st.markdown("""
    <div style="background:#0a1a2a; border:1px solid #1a3a5a; border-radius:6px;
    padding:10px 14px; font-size:12px; color:#4a9eff; margin: 12px 0;">
    🔍 웹 검색 활성화 — Salesforce 공식 문서를 실시간 검색해서 참고 링크를 함께 제공합니다.
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔍 에러 분석하기"):
        if not api_key:
            require_key()
        elif not error_input.strip():
            st.warning("에러 메시지를 입력해주세요.")
        else:
            with st.spinner("Salesforce 공식 문서 검색 중... (10~20초 소요)"):
                system = """당신은 Salesforce Marketing Cloud(SFMC) 10년차 전문가입니다.
사용자가 SFMC에서 발생한 에러 메시지를 분석할 때 반드시 웹 검색을 사용하여
Salesforce 공식 문서(help.salesforce.com), Salesforce 개발자 문서(developer.salesforce.com),
Trailblazer 커뮤니티를 검색한 후 다음 형식으로 한국어로 답변하세요:

[에러 요약]
한 줄로 이 에러가 무엇인지 설명

[발생 원인]
- 가능한 원인들을 구체적으로 설명

[해결 방법]
1. 단계별 해결 방법을 번호로 설명

[예방 팁]
- 재발 방지를 위한 팁

[참고 공식 문서]
- 문서 제목: URL 형식으로 실제 검색된 링크 제공
- 관련 Trailblazer 커뮤니티 링크도 포함

반드시 실제 검색을 수행하고 실제 존재하는 URL만 제공하세요."""

                user_msg = f"에러 발생 위치: {context or '미입력'}\n심각도: {severity}\n\n에러 메시지:\n{error_input}"
                result = call_claude_with_search(api_key, system, user_msg)

            st.markdown('<div class="result-label">● 분석 결과 (Salesforce 공식 문서 기반)</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 2. SQL 생성기
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "💾 SQL 생성기":
    st.markdown("""
    <div class="page-header">
        <div class="page-title">SQL 생성기</div>
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
        de_search = st.text_input("DE 이름 검색", placeholder="이름 일부 입력...", key="de_search_filter")
        filtered_des = [d for d in des if de_search.lower() in d["name"].lower()] if de_search else des

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
                st.markdown("**조회된 컬럼 정보**")
                for de_name, fields in de_schemas.items():
                    if fields:
                        col_tags = " &nbsp;".join([
                            f'<span style="color:{"#f0a030" if f["pk"] else "#8888aa"}">{f["name"]}</span>'
                            f'<span style="color:#333355; font-size:10px;">({f["type"]})</span>'
                            for f in fields
                        ])
                        st.markdown(f"""
                        <div style="background:#0a1a0a; border:1px solid #1a4a1a; border-radius:6px;
                        padding:10px 14px; margin:6px 0; font-size:12px; line-height:2;">
                        <span style="color:#3acc7a; font-weight:600;">{de_name}</span>
                        <span style="color:#333355; font-size:10px; margin-left:6px;">({len(fields)}개 컬럼)</span><br>
                        {col_tags}
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div style="background:#1a0a0a; border:1px solid #4a1a1a; border-radius:6px;
                        padding:10px 14px; margin:6px 0; font-size:12px; color:#ff5555;">
                        {de_name}: 컬럼 조회 실패 — CustomerKey를 확인하세요
                        </div>
                        """, unsafe_allow_html=True)

    # ── SQL 프롬프트 입력 ──────────────────────────────────────────────────
    st.markdown("---")
    st.markdown("**💬 원하는 쿼리를 설명하세요**")

    query_desc = st.text_area(
        "쿼리 설명",
        value=st.session_state.get("sql_desc_input", ""),
        placeholder="예: 최근 7일 이내에 이메일을 열어봤지만 클릭은 하지 않은 고객 목록을 뽑아서 결과 DE에 넣어줘. SubscriberKey, EmailAddress, EventDate 컬럼이 필요해.",
        height=120,
        key="sql_query_desc"
    )

    # 추가 옵션
    opt_col1, opt_col2, opt_col3 = st.columns(3)
    with opt_col1:
        target_de = st.text_input("결과 저장 DE 이름", placeholder="예: Result_OpenNotClick")
    with opt_col2:
        top_n = st.number_input("TOP N (0=전체)", min_value=0, max_value=100000, value=0, step=100)
    with opt_col3:
        add_comment = st.checkbox("SQL 주석 포함", value=True)

    if st.button("⚡ SQL 생성", type="primary"):
        if not api_key:
            require_key()
        elif not query_desc.strip():
            st.warning("쿼리 설명을 입력해주세요.")
        else:
            with st.spinner("SQL 생성 중..."):
                # DE 스키마 컨텍스트 구성
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

                top_clause = f"TOP {top_n} " if top_n > 0 else ""
                target_clause = f"INTO [{target_de}]" if target_de.strip() else "INTO [결과_DE명]"
                comment_instruction = "각 구문마다 한국어 주석을 달아주세요." if add_comment else "주석 없이 SQL만 작성하세요."

                system = f"""당신은 Salesforce Marketing Cloud(SFMC) SQL 전문가입니다.
SFMC Automation Studio의 Query Activity에서 실행되는 SQL을 작성하세요.

{schema_context}

SFMC SQL 규칙:
- SELECT {top_clause}... {target_clause} FROM [...] WHERE ... 형식
- ANSI SQL 기반이지만 일부 함수 제한 있음
- 날짜 함수: GETDATE(), DATEADD(DAY, -7, GETDATE()), DATEDIFF()
- 서브쿼리, JOIN, GROUP BY, HAVING 모두 사용 가능
- 존재하지 않는 함수 사용 금지 (TOP 대신 LIMIT 사용 불가)
- {comment_instruction}

출력 형식:
[SQL 코드만 출력]

[설명]
이 쿼리가 하는 일을 마케터도 이해할 수 있게 2~3문장으로"""

                result = call_claude(api_key, system, f"요청:\n{query_desc}")

            # SQL과 설명 분리
            parts = result.split("[설명]")
            sql_part = parts[0].strip()
            desc_part = parts[1].strip() if len(parts) > 1 else ""

            st.session_state["generated_sql"] = sql_part
            if desc_part:
                st.markdown(f"""
                <div style="background:#0a1a2a; border:1px solid #1a3a5a; border-radius:6px;
                padding:12px 16px; margin:12px 0; font-size:13px; color:#6ab0ff; line-height:1.7;">
                💡 {desc_part}
                </div>
                """, unsafe_allow_html=True)

    # ── 생성된 SQL 표시 ────────────────────────────────────────────────────
    if st.session_state.get("generated_sql"):
        st.markdown('<div class="result-label">● 생성된 SQL</div>', unsafe_allow_html=True)
        edited = st.text_area(
            "SQL (수정 가능)",
            value=st.session_state["generated_sql"],
            height=280,
            key="sql_edit_area"
        )
        st.session_state["generated_sql"] = edited

        btn1, btn2, btn3, _ = st.columns([1, 1, 1, 3])
        with btn1:
            st.code(edited, language="sql")
        with btn2:
            if st.button("🔁 재생성"):
                st.session_state.pop("generated_sql", None)
                st.rerun()
        with btn3:
            if st.button("💡 AI 검토"):
                if api_key:
                    with st.spinner("SQL 검토 중..."):
                        review = call_claude(
                            api_key,
                            "당신은 SFMC SQL 전문가입니다. 주어진 SQL의 문제점, 성능 이슈, 개선점을 한국어로 간결하게 알려주세요.",
                            f"다음 SFMC SQL을 검토해주세요:\n\n{edited}"
                        )
                    st.markdown(f'<div class="result-box">{review}</div>', unsafe_allow_html=True)





# ══════════════════════════════════════════════════════════════════════════════
# 3. AMPscript 어시스턴트

# ══════════════════════════════════════════════════════════════════════════════
# 3. AMPscript 어시스턴트
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "🔧 AMPscript 어시스턴트":
    st.markdown("""
    <div class="page-header">
        <div class="page-title">AMPscript 어시스턴트</div>
        <div class="page-desc">자연어로 설명하면 AMPscript 코드를 생성합니다. 기존 코드 해석 및 디버깅도 가능합니다.</div>
    </div>
    """, unsafe_allow_html=True)

    mode2 = st.radio("모드", ["자연어 → AMPscript", "코드 해석", "디버깅"], horizontal=True)
    st.markdown("---")

    if mode2 == "자연어 → AMPscript":
        amp_desc = st.text_area(
            "원하는 로직 설명",
            placeholder="예: 고객의 성별이 남성이면 '안녕하세요 {이름}님', 여성이면 '안녕하세요 {이름}님'으로 인사하고, 둘 다 아니면 그냥 '안녕하세요'라고 출력하고 싶어요.",
            height=160
        )
        if st.button("⚡ AMPscript 생성"):
            if not api_key:
                require_key()
            elif not amp_desc.strip():
                st.warning("설명을 입력해주세요.")
            else:
                with st.spinner("AMPscript 생성 중..."):
                    system = """당신은 SFMC AMPscript 전문가입니다.
사용자의 요구사항에 맞는 AMPscript 코드를 작성하세요.

규칙:
- 올바른 AMPscript 문법 사용 (%%[ ]%%, %%=...=%%)
- 각 블록에 한국어 주석 추가
- 코드 작성 후 [사용 방법]을 한국어로 설명
- 이메일 HTML에 어디에 넣어야 하는지 안내"""

                    result = call_claude(api_key, system, amp_desc)
                st.markdown('<div class="result-label">● 생성된 AMPscript</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)

    elif mode2 == "코드 해석":
        amp_code = st.text_area("AMPscript 코드", placeholder="%%[ ... ]%%", height=220)
        if st.button("📖 코드 해석"):
            if not api_key:
                require_key()
            elif not amp_code.strip():
                st.warning("코드를 입력해주세요.")
            else:
                with st.spinner("해석 중..."):
                    system = """당신은 SFMC AMPscript 전문가입니다.
입력받은 AMPscript 코드를 비개발자도 이해할 수 있게 한국어로 해석하세요.

형식:
[한 줄 요약] 이 코드가 하는 일

[단계별 설명] 각 블록이 무엇을 하는지

[실제 출력 예시] 특정 조건에서 어떻게 렌더링되는지 예시

[개선 제안] 더 효율적으로 만들 수 있다면 제안"""

                    result = call_claude(api_key, system, f"다음 AMPscript를 해석해주세요:\n\n{amp_code}")
                st.markdown('<div class="result-label">● 해석 결과</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)

    else:
        amp_bug = st.text_area("오류가 있는 AMPscript 코드", placeholder="%%[ ... ]%%", height=180)
        error_msg = st.text_input("발생한 에러 메시지 (선택)", placeholder="예: Variable @name is undefined")
        if st.button("🐛 디버깅"):
            if not api_key:
                require_key()
            elif not amp_bug.strip():
                st.warning("코드를 입력해주세요.")
            else:
                with st.spinner("디버깅 중..."):
                    system = """당신은 SFMC AMPscript 디버깅 전문가입니다.
코드의 문제를 찾아내고 수정된 버전을 제공하세요.

형식:
[발견된 문제] 어떤 오류가 있는지

[원인 설명] 왜 이 오류가 발생하는지

[수정된 코드] 올바르게 수정된 전체 코드

[설명] 무엇을 어떻게 고쳤는지"""

                    result = call_claude(api_key, system,
                        f"코드:\n{amp_bug}\n\n에러 메시지: {error_msg or '없음'}")
                st.markdown('<div class="result-label">● 디버깅 결과</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)



# ══════════════════════════════════════════════════════════════════════════════
# 4. Journey / Automation 관리
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "🗂️ Journey / Automation 관리":
    st.markdown("""
    <div class="page-header">
        <div class="page-title">Journey / Automation 관리</div>
        <div class="page-desc">Journey와 Automation의 실시간 현황을 한 곳에서 확인하고 관리합니다.</div>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.get("sfmc_token"):
        st.markdown("""
        <div style="background:#200a0a; border:1px solid #401010; border-radius:8px;
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
        tab_j, tab_a = st.tabs(["🗺️ Journey", "⚙️ Automation"])

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
                m1, m2, m3, m4, m5 = st.columns(5)
                with m1:
                    st.metric("전체", len(journeys_all))
                with m2:
                    st.metric("Published", status_counts.get("Published",0))
                with m3:
                    st.metric("Draft", status_counts.get("Draft",0))
                with m4:
                    st.metric("Paused", status_counts.get("Paused",0))
                with m5:
                    st.metric("Stopped", status_counts.get("Stopped",0))

                st.markdown("---")

                # 검색 & 필터
                fc1, fc2, fc3, fc4 = st.columns([2, 1, 1, 1])
                with fc1:
                    search_query = st.text_input("검색", placeholder="Journey 이름 검색...", label_visibility="collapsed")
                with fc2:
                    status_filter = st.selectbox("상태", ["전체","Published","Draft","Paused","Stopped"], label_visibility="collapsed")
                with fc3:
                    sort_order = st.selectbox("정렬", ["최신순","오래된순","수정일순","이름순"], label_visibility="collapsed")
                with fc4:
                    page_size_opt = st.selectbox("표시", ["전체","10개","25개","50개","100개"], label_visibility="collapsed")
                    page_size = len(journeys_all) if page_size_opt == "전체" else int(page_size_opt.replace("개",""))

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

                # 선택 상태
                if "selected_journeys" not in st.session_state:
                    st.session_state["selected_journeys"] = set()
                if "chk_version" not in st.session_state:
                    st.session_state["chk_version"] = 0
                sel = st.session_state["selected_journeys"]
                chk_v = st.session_state["chk_version"]

                # 일괄 작업 바
                ba1, ba2, ba3, ba4, ba5, ba6, ba7 = st.columns([1,1,1,1,1,1,1])
                with ba1:
                    st.markdown(f"<div style='font-size:12px;color:var(--color-text-secondary);padding-top:6px;'>{len(sel)}개 선택</div>", unsafe_allow_html=True)
                with ba2:
                    if st.button("전체선택", key="sel_all"):
                        st.session_state["selected_journeys"] = {j.get("id") for j in journeys}
                        st.session_state["chk_version"] += 1
                        st.rerun()
                with ba3:
                    if st.button("선택해제", key="sel_none"):
                        st.session_state["selected_journeys"] = set()
                        st.session_state["chk_version"] += 1
                        st.rerun()

                if sel:
                    sel_data = [j for j in journeys if j.get("id") in sel]
                    with ba4:
                        if st.button("⏸ Pause", key="bulk_pause"):
                            ok, fail = 0, 0
                            for j in sel_data:
                                if j.get("status") in ACTIVE_STATUSES:
                                    c, m = journey_action("pause", j["id"], j.get("version",1), token, rest_base)
                                    if c in [200,201]:
                                        ok+=1
                                        for item in st.session_state["journeys_all"]:
                                            if item.get("id") == j["id"]: item["status"] = "Paused"
                                    else: fail+=1
                            st.success(f"Pause {ok}개 완료" + (f", {fail}개 실패" if fail else ""))
                            st.session_state["selected_journeys"] = set()
                            st.session_state["chk_version"] += 1
                            st.rerun()
                    with ba5:
                        if st.button("▶ Resume", key="bulk_resume"):
                            ok, fail = 0, 0
                            for j in sel_data:
                                if j.get("status") == "Paused":
                                    c, m = journey_action("resume", j["id"], j.get("version",1), token, rest_base)
                                    if c in [200,201]:
                                        ok+=1
                                        for item in st.session_state["journeys_all"]:
                                            if item.get("id") == j["id"]: item["status"] = "Published"
                                    else: fail+=1
                            st.success(f"Resume {ok}개 완료" + (f", {fail}개 실패" if fail else ""))
                            st.session_state["selected_journeys"] = set()
                            st.session_state["chk_version"] += 1
                            st.rerun()
                    with ba6:
                        if st.button("⏹ Stop", key="bulk_stop"):
                            ok, fail = 0, 0
                            for j in sel_data:
                                if j.get("status") in ACTIVE_STATUSES | {"Paused"}:
                                    c, m = journey_action("stop", j["id"], j.get("version",1), token, rest_base)
                                    if c in [200,201]:
                                        ok+=1
                                        for item in st.session_state["journeys_all"]:
                                            if item.get("id") == j["id"]: item["status"] = "Stopped"
                                    else: fail+=1
                            st.success(f"Stop {ok}개 완료" + (f", {fail}개 실패" if fail else ""))
                            st.session_state["selected_journeys"] = set()
                            st.session_state["chk_version"] += 1
                            st.rerun()
                    with ba7:
                        if st.button("🗑 Delete", key="bulk_delete"):
                            ok, fail = 0, 0
                            deleted_ids = set()
                            for j in sel_data:
                                if j.get("status") in ["Draft","Stopped","Paused"]:
                                    c, m = journey_action("delete", j["id"], j.get("version",1), token, rest_base)
                                    if c in [200,201,204]:
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

                st.markdown(f"<div style='font-size:12px;color:var(--color-text-secondary);margin:6px 0;'>{len(journeys)}개 표시 중 (필터 결과 {filtered_total}개 / 전체 {len(journeys_all)}개)</div>", unsafe_allow_html=True)

                # 상태별 색상 & 배지
                STATUS_COLORS = {
                    "Published":"#3acc7a","Draft":"#f0a030",
                    "Paused":"#4a9eff","Stopped":"#ff5555","Deleted":"#555577"
                }
                STATUS_BG = {
                    "Published":"#0a2015","Draft":"#201500",
                    "Paused":"#0a1a30","Stopped":"#200a0a","Deleted":"#111111"
                }
                sfmc_web_url = st.session_state.get("sfmc_web_url","")

                # 헤더 — Streamlit 컬럼으로 통일
                hc1, hc2, hc3, hc4a, hc4b, hc4c, hc5 = st.columns([0.5, 4.5, 1.5, 1.2, 1.2, 1.2, 1.2])
                with hc1: st.markdown("<div style='font-size:11px;color:#555577;'></div>", unsafe_allow_html=True)
                with hc2: st.markdown("<div style='font-size:11px;font-weight:500;color:#555577;letter-spacing:0.05em;text-transform:uppercase;'>이름 / ID</div>", unsafe_allow_html=True)
                with hc3: st.markdown("<div style='font-size:11px;font-weight:500;color:#555577;letter-spacing:0.05em;text-transform:uppercase;'>상태</div>", unsafe_allow_html=True)
                with hc4a: st.markdown("<div style='font-size:11px;font-weight:500;color:#555577;letter-spacing:0.05em;text-transform:uppercase;'>일시정지</div>", unsafe_allow_html=True)
                with hc4b: st.markdown("<div style='font-size:11px;font-weight:500;color:#555577;letter-spacing:0.05em;text-transform:uppercase;'>중단</div>", unsafe_allow_html=True)
                with hc4c: st.markdown("<div style='font-size:11px;font-weight:500;color:#555577;letter-spacing:0.05em;text-transform:uppercase;'>삭제</div>", unsafe_allow_html=True)
                with hc5: st.markdown("<div style='font-size:11px;font-weight:500;color:#555577;letter-spacing:0.05em;text-transform:uppercase;'>바로가기</div>", unsafe_allow_html=True)
                st.markdown("<div style='height:1px;background:#1e1e2e;margin:4px 0 8px 0;'></div>", unsafe_allow_html=True)

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
                        <div style="font-size:13px;font-weight:500;color:#e8e8f0;">{name}</div>
                        <div style="font-size:11px;color:#444466;margin-top:3px;">v{version} &nbsp;·&nbsp; 생성: {created} &nbsp;·&nbsp; 수정: {modified}</div>
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
                            if st.button("⏸", key=f"pause_{idx}", help="일시정지"):
                                c, m = journey_action("pause", jid, version, token, rest_base)
                                if c in [200,201]:
                                    for item in st.session_state["journeys_all"]:
                                        if item.get("id") == jid: item["status"] = "Paused"
                                    st.rerun()
                                else:
                                    st.error(action_error_msg(c, m))
                        if status == "Paused":
                            if st.button("▶", key=f"resume_{idx}", help="재개"):
                                c, m = journey_action("resume", jid, version, token, rest_base)
                                if c in [200,201]:
                                    for item in st.session_state["journeys_all"]:
                                        if item.get("id") == jid: item["status"] = "Published"
                                    st.rerun()
                                else:
                                    st.error(action_error_msg(c, m))

                    with bcol_stop:
                        if status in ACTIVE_STATUSES:
                            if st.button("⏹", key=f"stop_{idx}", help="중단"):
                                c, m = journey_action("stop", jid, version, token, rest_base)
                                if c in [200,201]:
                                    for item in st.session_state["journeys_all"]:
                                        if item.get("id") == jid: item["status"] = "Stopped"
                                    st.rerun()
                                else:
                                    st.error(action_error_msg(c, m))
                        if status == "Paused":
                            if st.button("⏹", key=f"stop_p_{idx}", help="중단"):
                                c, m = journey_action("stop", jid, version, token, rest_base)
                                if c in [200,201]:
                                    for item in st.session_state["journeys_all"]:
                                        if item.get("id") == jid: item["status"] = "Stopped"
                                    st.rerun()
                                else:
                                    st.error(action_error_msg(c, m))

                    with bcol_del:
                        if status in ["Draft","Stopped","Paused"]:
                            if st.button("🗑", key=f"del_{idx}", help="삭제"):
                                c, m = journey_action("delete", jid, version, token, rest_base)
                                if c in [200,201,204]:
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

                    st.markdown("<div style='height:1px;background:#1a1a2e;margin:2px 0;'></div>", unsafe_allow_html=True)

                # AI 분석
                if api_key and journeys:
                    st.markdown("---")
                    if st.button("🤖 AI Journey 현황 분석", key="ai_j"):
                        with st.spinner("분석 중..."):
                            summary_text = "\n".join([
                                f"- {j.get('name','?')} | {j.get('status','?')} | v{j.get('version',1)} | 수정:{j.get('modifiedDate','')[:10]}"
                                for j in journeys
                            ])
                            result = call_claude(api_key,
                                """SFMC Journey Builder 전문가로서 Journey 목록을 분석하세요.
Draft 미배포, 오래된 Published Journey, 버전 이슈 등을 파악하고 개선 제안을 한국어로 해주세요.""",
                                f"Journey 목록:\n{summary_text}")
                        st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)

        # ════════════════════════════════════════════════════════════════════
        # AUTOMATION 탭
        # ════════════════════════════════════════════════════════════════════
        with tab_a:
            if st.button("🔄 Automation 불러오기", key="load_auto"):
                try:
                    all_autos = []
                    page = 1
                    prog = st.progress(0, text="Automation 불러오는 중...")
                    while True:
                        resp = requests.get(
                            f"{rest_base}/automation/v1/automations",
                            headers={"Authorization": f"Bearer {token}"},
                            params={"$pageSize": 50, "$page": page}
                        )
                        if resp.status_code == 401:
                            st.error("토큰 만료 — 다시 연결해주세요.")
                            break
                        if resp.status_code != 200:
                            st.error(f"오류: {resp.status_code}")
                            break
                        data = resp.json()
                        items = data.get("items", [])
                        all_autos.extend(items)
                        total = data.get("count", data.get("totalCount", len(all_autos)))
                        prog.progress(min(len(all_autos)/max(total,1), 1.0),
                                      text=f"{len(all_autos)} / {total}개 로드 중...")
                        if len(items) < 50 or len(all_autos) >= total:
                            break
                        page += 1
                    prog.empty()
                    st.session_state["automations"] = all_autos
                    st.success(f"✅ {len(all_autos)}개 Automation 불러옴")
                except Exception as e:
                    st.error(f"오류: {e}")

            automations = st.session_state.get("automations", [])

            STATUS_MAP = {
                1:("Ready","#3acc7a","#0a2015"),
                2:("Building","#4a9eff","#0a1a30"),
                3:("PausedSchedule","#f0a030","#201500"),
                4:("Inactive","#555577","#111111"),
                5:("Deleted","#ff5555","#200a0a"),
                6:("Running","#4a9eff","#0a1a30"),
                7:("Stopped","#ff5555","#200a0a"),
                8:("Scheduled","#3acc7a","#0a2015"),
            }
            # 문자열 상태값도 처리 (API가 숫자 대신 문자열로 줄 수 있음)
            STATUS_MAP_STR = {
                "Ready":           ("Ready","#3acc7a","#0a2015"),
                "Building":        ("Building","#4a9eff","#0a1a30"),
                "PausedSchedule":  ("PausedSchedule","#f0a030","#201500"),
                "Paused":          ("PausedSchedule","#f0a030","#201500"),
                "Inactive":        ("Inactive","#555577","#111111"),
                "Deleted":         ("Deleted","#ff5555","#200a0a"),
                "Running":         ("Running","#4a9eff","#0a1a30"),
                "Stopped":         ("Stopped","#ff5555","#200a0a"),
                "Scheduled":       ("Scheduled","#3acc7a","#0a2015"),
                "AwaitingTrigger": ("AwaitingTrigger","#3acc7a","#0a2015"),
                "Error":           ("오류","#ff5555","#200a0a"),
            }

            STATUS_LABEL_KO = {
                "Ready":           "준비",
                "Building":        "빌드 중",
                "PausedSchedule":  "일시정지",
                "Inactive":        "비활성",
                "Deleted":         "삭제됨",
                "Running":         "실행 중",
                "Stopped":         "중단",
                "Scheduled":       "예약됨",
                "AwaitingTrigger": "트리거 대기",
                "알 수 없음":       "알 수 없음",
                "오류":             "오류",
            }

            def get_auto_status(a):
                raw = a.get("status", a.get("statusId", a.get("automationStatus", None)))
                if raw is None:
                    return "알 수 없음", "#555577", "#111111"
                if isinstance(raw, int):
                    return STATUS_MAP.get(raw, ("알 수 없음","#555577","#111111"))
                if isinstance(raw, str):
                    # 문자열 숫자면 int로
                    if raw.isdigit():
                        return STATUS_MAP.get(int(raw), ("알 수 없음","#555577","#111111"))
                    return STATUS_MAP_STR.get(raw, (raw,"#555577","#111111"))
                return "알 수 없음", "#555577", "#111111"

            if automations:
                error_count = sum(1 for a in automations if get_auto_status(a)[0] in ["Stopped","Deleted","오류"])
                running_count = sum(1 for a in automations if get_auto_status(a)[0] in ["Running","Scheduled"])
                paused_count = sum(1 for a in automations if get_auto_status(a)[0] in ["PausedSchedule"])

                am1, am2, am3, am4 = st.columns(4)
                with am1: st.metric("전체", len(automations))
                with am2: st.metric("실행 중", running_count)
                with am3: st.metric("일시정지", paused_count)
                with am4: st.metric("오류/중단", error_count)

                if error_count > 0:
                    st.markdown(f"""
                    <div style="background:#200a0a;border:1px solid #401010;border-radius:6px;
                    padding:10px 14px;font-size:12px;color:#ff5555;margin:8px 0;">
                    ⚠️ 중단/삭제된 Automation {error_count}개 — 확인이 필요합니다.
                    </div>
                    """, unsafe_allow_html=True)

                af1, af2, af3, af4 = st.columns([2, 1, 1, 1])
                with af1:
                    auto_search = st.text_input("Automation 검색", placeholder="이름 검색...", label_visibility="collapsed")
                with af2:
                    auto_status_filter = st.selectbox("상태", ["전체","준비","실행 중","예약됨","트리거 대기","일시정지","비활성","중단","삭제됨"], label_visibility="collapsed")
                with af3:
                    auto_date_filter = st.selectbox("마지막 실행", ["전체","오늘","최근 7일","최근 30일","미실행"], label_visibility="collapsed")
                with af4:
                    auto_page_opt = st.selectbox("표시", ["전체","25개","50개","100개"], label_visibility="collapsed")
                    auto_page = len(automations) if auto_page_opt == "전체" else int(auto_page_opt.replace("개",""))

                # 필터 적용
                from datetime import datetime, timedelta
                now = datetime.now()
                filtered_autos = automations[:]
                if auto_search:
                    filtered_autos = [a for a in filtered_autos if auto_search.lower() in a.get("name","").lower()]
                if auto_status_filter != "전체":
                    ko_to_label = {v: k for k, v in STATUS_LABEL_KO.items()}
                    target_label = ko_to_label.get(auto_status_filter, auto_status_filter)
                    filtered_autos = [a for a in filtered_autos if get_auto_status(a)[0] == target_label]
                if auto_date_filter != "전체":
                    def parse_dt(s):
                        try: return datetime.fromisoformat(s[:19])
                        except: return None
                    if auto_date_filter == "미실행":
                        filtered_autos = [a for a in filtered_autos if not a.get("lastRunTime")]
                    elif auto_date_filter == "오늘":
                        filtered_autos = [a for a in filtered_autos if (d := parse_dt(a.get("lastRunTime",""))) and d.date() == now.date()]
                    elif auto_date_filter == "최근 7일":
                        filtered_autos = [a for a in filtered_autos if (d := parse_dt(a.get("lastRunTime",""))) and d >= now - timedelta(days=7)]
                    elif auto_date_filter == "최근 30일":
                        filtered_autos = [a for a in filtered_autos if (d := parse_dt(a.get("lastRunTime",""))) and d >= now - timedelta(days=30)]
                filtered_total_auto = len(filtered_autos)
                filtered_autos = filtered_autos[:auto_page]

                st.markdown(f"<div style='font-size:12px;color:#555577;margin:4px 0 8px 0;'>{len(filtered_autos)}개 표시 중 (필터 결과 {filtered_total_auto}개 / 전체 {len(automations)}개)</div>", unsafe_allow_html=True)

                st.markdown("---")

                # 헤더
                h1, h2, h3 = st.columns([4, 2, 2])
                with h1: st.markdown("<div style='font-size:11px;font-weight:500;color:#555577;letter-spacing:0.05em;text-transform:uppercase;padding:4px 0;'>이름</div>", unsafe_allow_html=True)
                with h2: st.markdown("<div style='font-size:11px;font-weight:500;color:#555577;letter-spacing:0.05em;text-transform:uppercase;padding:4px 0;'>상태</div>", unsafe_allow_html=True)
                with h3: st.markdown("<div style='font-size:11px;font-weight:500;color:#555577;letter-spacing:0.05em;text-transform:uppercase;padding:4px 0;'>마지막 실행</div>", unsafe_allow_html=True)
                st.markdown("<div style='height:1px;background:#1e1e2e;margin-bottom:4px;'></div>", unsafe_allow_html=True)

                for a in filtered_autos:
                    label, color, bg = get_auto_status(a)
                    label_ko = STATUS_LABEL_KO.get(label, label)
                    name = a.get("name","이름 없음")
                    last_run = a.get("lastRunTime","")[:16].replace("T"," ") if a.get("lastRunTime") else "미실행"
                    aid = a.get("id","")
                    is_error = label in ["Stopped","Deleted","오류"]

                    nc, bc, rc = st.columns([4, 2, 2])
                    with nc:
                        st.markdown(f"""
                        <div style="padding:8px 0;">
                        <div style="font-size:13px;font-weight:500;color:#e8e8f0;">{name}</div>
                        <div style="font-size:11px;color:#444466;margin-top:3px;">ID: {aid}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    with bc:
                        st.markdown(f"""
                        <div style="padding:10px 0;">
                        <span style="display:inline-flex;align-items:center;gap:5px;font-size:12px;font-weight:500;
                        padding:4px 10px;border-radius:99px;background:{bg};color:{color};">
                        <span style="width:6px;height:6px;border-radius:50%;background:{color};display:inline-block;flex-shrink:0;"></span>
                        {label_ko}
                        </span>
                        </div>
                        """, unsafe_allow_html=True)
                    with rc:
                        rc_color = "#ff5555" if is_error else "#8888aa"
                        st.markdown(f"""
                        <div style="padding:12px 0;font-size:13px;color:{rc_color};">{last_run}</div>
                        """, unsafe_allow_html=True)

                    st.markdown("<div style='height:1px;background:#1a1a2e;'></div>", unsafe_allow_html=True)

                if api_key:
                    st.markdown("---")
                    if st.button("🤖 AI Automation 분석", key="ai_a"):
                        with st.spinner("분석 중..."):
                            auto_summary = "\n".join([
                                f"- {a.get('name','?')} | 상태:{get_auto_status(a)[0]} | 마지막실행:{a.get('lastRunTime','없음')[:10] if a.get('lastRunTime') else '없음'}"
                                for a in automations
                            ])
                            result = call_claude(api_key,
                                """SFMC Automation Studio 전문가로서 Automation 목록을 분석하세요.
중단된 것, 오래된 것, 이상 징후를 파악하고 개선 제안을 한국어로 해주세요.""",
                                f"Automation 목록:\n{auto_summary}")
                        st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
