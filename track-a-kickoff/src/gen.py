# -*- coding: utf-8 -*-
"""IQVIA 템플릿 좌표(13.333x7.5in)를 그대로 옮긴 HTML 슬라이드 생성기.
1in = 96px. 모든 위치·크기는 인치로 쓰고 px로 변환한다."""
import re, html, sys, json

OUT = sys.argv[1]
ROUND = sys.argv[2] if len(sys.argv) > 2 else "R1"
PX = 96
def p(v): return round(v * PX, 2)
def pt(v): return round(v * 96 / 72, 2)

# --- template grid (design-spec.md)
L, R, B = 0.458, 12.958, 6.750
TOP_H, TOP, BODY = 1.829, 1.917, 2.333
W = R - L

# --- palette tokens (design-spec 5)
C = dict(text="#2B3A42", text2="#606B71", blue="#00A3E0", navy="#005587", navy75="#4080A5",
         navy50="#7FAAC3", navy25="#BFD4E1", blue75="#40BAE8", blue25="#BFE8F7", callout="#C6EFFF",
         lg="#F3F3F3", g95="#F2F2F2", g85="#D9D9D9", g75="#BFBFBF", g65="#A6A6A6", g50="#808080",
         amber="#F0B323", amber25="#FCF0D3", green="#43B02A", red="#C00000", teal="#00BFB3")

class Slide:
    def __init__(self, subhead, headline, tag="Track A | Strategy & Launch", source_general=None, num=1):
        self.subhead, self.headline, self.tag = subhead, headline, tag
        self.els, self.notes, self.sources = [], [], []
        self.n = 0
        self.source_general = source_general
        self.num = num
    def fn(self, text):
        """{n:..}/{s:..} 마커를 위첨자 번호로 바꾼다(작성 순서 = 공간 순서로 작성)."""
        def rep(m):
            kind, body = m.group(1), m.group(2)
            self.n += 1
            (self.notes if kind == "n" else self.sources).append((self.n, body))
            return f'<sup>{self.n}</sup>'
        return re.sub(r"\{([ns]):([^}]*)\}", rep, text)
    def add(self, x, y, w, h, inner, cls="bx", style=""):
        self.els.append(f'<div class="{cls}" style="left:{p(x)}px;top:{p(y)}px;width:{p(w)}px;height:{p(h)}px;{style}">{self.fn(inner)}</div>')
    def raw(self, s): self.els.append(s)
    def colhead(self, x, w, text, y=TOP_H, color=None):
        col = color or C["blue"]
        self.add(x, y, w, 0.42, f'<span>{text}</span>', cls="bx colhead", style=f"border-top-color:{col}")
    def html(self):
        foot = []
        if self.notes: foot.append("Note: " + "; ".join(f"{n}. {t}" for n, t in self.notes))
        src = [f"{n}. {t}" for n, t in self.sources]
        if self.source_general: src.append(self.source_general)
        if src: foot.append("Source: " + "; ".join(src))
        return f'''<div class="slide" data-n="{self.num}">
  <div class="ph tag" style="left:{p(8.836)}px;top:{p(0.130)}px;width:{p(4.222)}px;height:{p(0.44)}px">{self.tag}</div>
  <div class="ph sub" style="left:{p(0.358)}px;top:{p(0.329)}px;width:{p(12.7)}px;height:{p(0.44)}px">{self.subhead}</div>
  {"" if self.headline is None else f'<div class="ph head" style="left:{p(0.358)}px;top:{p(0.816)}px;width:{p(12.7)}px;height:{p(0.84)}px">{self.headline}</div>'}
  {"".join(self.els)}
  <div class="ph foot" style="left:{p(0.358)}px;top:{p(6.986)}px;width:{p(11.0)}px;height:{p(0.37)}px"><div>{"<br>".join(foot)}</div></div>
  <div class="ph logo" style="left:{p(11.348)}px;top:{p(7.148)}px;width:{p(1.25)}px;height:{p(0.236)}px">로고 · 템플릿 상속</div>
  <div class="ph pno" style="left:{p(12.821)}px;top:{p(7.157)}px;width:{p(0.386)}px;height:{p(0.194)}px">{self.num}</div>
</div>'''

def chip(t, bg=None, fg=None):
    return f'<span class="chip" style="background:{bg or C["blue25"]};color:{fg or C["navy"]}">{t}</span>'

# =====================================================================
# STUDY VERSION (상세본)
# =====================================================================
def study():
    out = []
    # ---------------- S1
    s = Slide("1. 핵심 Client Challenge",
              "6개 후보를 6개 기준으로 평가해 Round 1·2와 공통 사례로 쓸 3개를 선정하고, Track B와 겹치거나 청중이 좁은 3개는 사례·맥락으로 돌림",
              source_general="리서치 본문 v6, IQVIA analysis", num=1)
    lw, gut = 7.45, 0.25
    rx, rw = L + lw + gut, W - lw - gut
    s.colhead(L, lw, "선정 3개 <em>점수 / 30</em>")
    s.colhead(rx, rw, "탈락 3개와 이유", color=C["g65"])
    sel = [
        ("R1", C["navy"], "26", "특허절벽·미국 약가 레짐 아래, 한국의 성장 기회는 어디로 이동하는가",
         "2025~30년 3,000억 달러 이상이 독점권을 잃어{s:Evaluate, $300bn Patent Cliff} 본사가 런칭 자원과 순서를 다시 짬. MNC 지사(참석 60%)에겐 본사 설득 논리, 국내사에겐 '제네릭 산정률 45% 이후 성장축' 질문. Round 1 질문에 가장 직접적"),
        ("R2", C["blue"], "26", "AI 에이전트가 바꾸는 Launch Operating Model <i>고정</i>",
         "미국에서만 연 50~55개 신약 출시 예상{s:IQVIA, U.S. Medicine Use Trends 2026}. AI 에이전트 사용·평가 47%, 이미 배포 22%{n:헬스케어·생명과학 응답자 600명 이상}{s:NVIDIA, State of AI in HC&amp;LS 2026}. '어느 준비 업무부터, 누가, 어떤 통제로'에 집중해 Track C(참여·성과)와 구분"),
        ("공통", C["navy50"], "25", "'사 온 자산'의 시대: 외부 자산을 성장과 런칭으로",
         "빅파마 인라이선스 자산의 40%가 중국산(2025){s:PharmExec, 2026.6 (IQVIA 집계 인용)}, 한국 기술수출은 약 145억 달러로 최대. 1·2를 '외부 자산' 렌즈로 보는 공통 사례로 R1 '선택'과 R2 '준비'를 잇고, 사례 확보 가능성이 가장 높음"),
    ]
    y, ch, gap = BODY, 1.1, 0.1
    for lab, col, sc, title, why in sel:
        s.add(L, y, 0.62, ch, f'<b>{lab}</b>', cls="bx lab", style=f"background:{col}")
        s.add(L + 0.62, y, lw - 0.62, ch,
              f'<div class="ct"><span class="t">{title}</span><span class="sc">{sc}</span></div><div class="cw">{why}</div>',
              cls="bx card")
        y += ch + gap
    rej = [
        ("D. 약가·급여 제도 전환기", "20 · → 2의 맥락",
         "절실도는 최고(5점)지만 급여·가격 실행은 Track B Round 2 주제. 'Track 중복 없음' 1점으로 탈락 조건 해당. 100일 등재도 희귀신약 시범사업 한정"),
        ("E. 비만·대사 경쟁 런칭", "20 · → 1의 사례",
         "시의성은 높으나 직접 해당 참석사가 소수(추정)라 '참석자 폭' 2점. 시장·채널·가격을 다루면 Track B·C와 겹쳐 1의 '비급여 성장 기회' 사례로"),
        ("F. 첫해 처방 65% 미조제", "18 · → 2에서 일부",
         "원인이 급여 거절 49%·환자 포기 17%인 접근성 문제{s:IQVIA, 미국 2020~24년 신약 99개}로 Track B 영역(중복 1점). Track A는 승인 전 교차기능 핸드오프만"),
    ]
    y = BODY
    for title, pill, why in rej:
        s.add(rx, y, rw, ch, f'<div class="ct"><span class="t">{title}</span><span class="pl">{pill}</span></div><div class="cw">{why}</div>', cls="bx card rej")
        y += ch + gap
    sy = y + 0.02
    strip = [("평가 기준 6개 · 각 5점", "절실도·Round 적합·중복 없음·BU 역량·사례·청중"),
             ("탈락 조건", "'중복 없음' 2점 이하면 제외 (D·F)"),
             ("재검토 트리거", "11/27까지 Round별 사례사 2곳 미확보 시"),
             ("Track 경계", "급여·접근성은 B, HCP 참여·성과는 C")]
    sw = (W - 3 * 0.12) / 4
    for i, (h, t) in enumerate(strip):
        s.add(L + i * (sw + 0.12), sy, sw, B - sy, f'<b>{h}</b><span>{t}</span>', cls="bx strip")
    out.append(s)

    # ---------------- S2
    s = Slide("2. Key Takeaway",
              "참석 리더가 기억할 문장은 Round별 하나씩으로, Round 1은 '다시 선택해야 한다', Round 2는 '도입률이 아니라 병목'임",
              source_general="리서치 본문 v6, IQVIA analysis", num=2)
    cw, gut = (W - 0.4) / 2, 0.4
    x1, x2 = L, L + cw + gut
    s.colhead(x1, cw, "Round 1 · Takeaway ①", color=C["navy"])
    s.colhead(x2, cw, "Round 2 · Takeaway ②", color=C["blue"])
    s.add(x1, BODY, cw, 1.1, "<span>“2027년의 성장 기회는 시장을 찾는 데서 끝나지 않는다. 외부환경 변화에 맞춰 <u>치료영역·자산·출시 순서를 다시 선택</u>해야 한다.”</span>", cls="bx quote", style=f"background:{C['navy']}")
    s.add(x2, BODY, cw, 1.1, "<span>“AI 에이전트의 가치는 도입률이 아니라 <u>런칭 준비의 병목을 얼마나 줄이는가</u>로 결정된다. 우선 업무와 역할·데이터·통제를 함께 설계해야 한다.”</span>", cls="bx quote", style=f"background:{C['blue']}")
    cy = BODY + 1.2
    s.add(x1, cy, cw, 0.36, "".join(chip(t) for t in ["치료영역", "자산", "출시 순서"]), cls="bx chips")
    s.add(x2, cy, cw, 0.36, "".join(chip(t) for t in ["우선 업무", "역할", "데이터", "통제"]), cls="bx chips")
    wy = cy + 0.44
    wh = 6.16 - wy
    s.add(x1, wy, cw, wh, '''<p class="l1">왜 이 문장인가</p>
<p class="l2">특허만료로 본사 자원이 재배분되고, 미국 정책이 출시 순서를 흔들고, 외부 자산이 인라이선스의 40% 이상이 됨</p>
<p class="l2">세 변화가 각각 자산·출시 순서·치료영역 선택에 닿아 핵심 동사는 '다시 선택'</p>
<p class="l2">리더급 청중에게 분석 결과가 아니라 해야 할 결정을 남김</p>
<p class="l1">반증조건</p>
<p class="l2">사전 설문에서 다수가 '우선 치료영역이 작년과 같다'고 답하면 '선택은 같아도 순서는 바뀐다'로 좁힘</p>''', cls="bx txt")
    # right: why + mini bar chart
    bars = [("워크플로 설계", 60), ("컴플라이언스·검증", 55), ("기술 인프라", 42), ("데이터 거버넌스", 38)]
    bh = "".join(f'<div class="br"><span class="bl">{n}</span><span class="bt"><i style="width:{v}%;background:{C["navy"] if i < 2 else C["navy50"]}"></i></span><span class="bv">{v}%</span></div>' for i, (n, v) in enumerate(bars))
    s.add(x2, wy, cw, wh, f'''<p class="l1">왜 이 문장인가</p>
<p class="l2">AI 에이전트 사용·평가 47%, 이미 배포 22%{{s:NVIDIA, State of AI in HC&amp;LS 2026}}</p>
<p class="l2">제약 임원이 꼽은 배포 난관 상위는 기술이 아닌 설계·통제{{s:MIT Technology Review Insights·Globant, 9개국 제약 임원 250명, 2025.10}}</p>
<div class="bars">{bh}</div>
<p class="l1">반증조건</p>
<p class="l2">사례사가 '인프라가 최대 병목'이라 하면 문구 수정</p>''', cls="bx txt")
    s.add(L, 6.24, W, B - 6.24, '<span class="kl">종합 세션용 ③</span><span>외부환경이 불확실할수록 <b>성장 선택(R1)</b>과 <b>런칭 준비(R2)</b>의 연결이 2027년 한국 제약의 성패를 가른다{n:15:35 전체 세션에서 Track Chair가 사용}</span></span>', cls="bx key")
    out.append(s)

    # ---------------- S3
    s = Slide("3. Session · Discussion Topic",
              "Round 1은 '기회 지도 다시 그리기', Round 2는 '에이전트에게 먼저 맡길 준비 업무'로 짜고, '사 온 자산' 사례로 두 Round를 이음",
              source_general="기획서 초안 4·6장, 리서치 본문 v6", num=3)
    kw = 1.52; cw = (W - kw - 0.08 * 2) / 2
    xa, xb = L + kw + 0.08, L + kw + 0.08 + cw + 0.08
    y = TOP
    hh = 0.62
    s.add(L, y, kw, hh, "", cls="bx tk0")
    s.add(xa, y, cw, hh, '<span class="hs">Session 1 · Round 1 · 13:10–14:00</span><b>2027 한국 성장 기회 지도, 다시 그리기</b>', cls="bx th", style=f"background:{C['navy']}")
    s.add(xb, y, cw, hh, '<span class="hs">Session 2 · Round 2 · 14:20–15:10</span><b>런칭 준비 업무 중 에이전트에게 먼저 맡길 것</b>', cls="bx th", style=f"background:{C['blue']}")
    rows = [
        ("Insight 10'", 0.66,
         "<b>INFO·PI</b> 플레너리 Outlook 수치를 받아 치료영역·환자군·자산별 '이동' 지도. 첫 장은 참석 리더 사전 설문",
         "<b>MC·Analytics·Tech</b> R1 요약 2분 → 런칭 부담·에이전트 현황 → 준비도 점검 워크플로 시연 3분{n:시연 가능 여부 Tech 확인 필요}"),
        ("Joint Case 15'", 0.46,
         "<b>MC + MNC 지사 임원</b> 한국 런칭을 본사 우선순위로 올린 사례",
         "<b>MC + MNC 지사 런칭 리더</b> Launch PMO·예측에 AI를 적용한 사례"),
        ("Discussion 15'", 0.8,
         "패널: 국내사 임원, 신사업 대기업 임원, 사례 발표자<br><span class='q'>Q. 2027 기회 지도는 작년과 무엇이 다르고, 무엇을 그만둘 것인가?</span>",
         "패널: 국내사 임원, IQVIA Domain Expert(HTA/HE·CES), 발표자<br><span class='q'>Q. 어떤 준비 업무를 먼저 맡기고, 무엇은 사람이 지킬 것인가?</span>"),
        ("왜 이렇게", 0.8,
         "Outlook과 겹치지 않게 '전망' 대신 '이동'. 리더에게 가장 어려운 결정인 '그만둘 것'을 질문에. 사례(MNC)와 패널(국내·대기업)로 청중 전원을 커버",
         "말로는 Track C와 같아 보여 시연으로 '런칭 준비' 자리를 보임. 교차기능 전문가는 '준비 체크포인트'로만 발언해 Track B·C를 넘지 않음"),
        ("넘김", 0.4,
         "→ R2: 기회를 골랐다면, 런칭은 누가 어떻게 준비하는가",
         "→ Track B(급여) · Track C(HCP 참여 AI) · 종합 세션 ③"),
    ]
    y += hh + 0.06
    for k, h, a, b in rows:
        s.add(L, y, kw, h, k, cls="bx tk")
        s.add(xa, y, cw, h, a, cls="bx td")
        s.add(xb, y, cw, h, b, cls="bx td")
        y += h + 0.06
    s.add(L, y, kw, B - y, "공통 사례", cls="bx tk", style=f"background:{C['navy50']};color:#fff")
    s.add(xa, y, W - kw - 0.08, B - y, "<span><b>사 온 자산의 런칭</b> · R1 “자체 개발과 사 온 자산을 같은 잣대로 고르는가?” → R2 “데이터 공백과 파트너 역할은 누가 메우는가?” 같은 회사가 두 Round에 서면 가장 강함</span>", cls="bx bridge")
    out.append(s)
    return out

# =====================================================================
# BRIEF VERSION (간략본)
# =====================================================================
def brief():
    out = []
    # ---------------- B1
    s = Slide("1. 핵심 Client Challenge",
              "Round 1은 '성장 기회 이동', Round 2는 'AI 에이전트 런칭 운영모델', 두 Round를 잇는 공통 사례는 '사 온 자산'으로 제안함",
              source_general="IQVIA analysis", num=1)
    lw, gut = 6.55, 0.35
    rx, rw = L + lw + gut, W - lw - gut
    s.colhead(L, lw, "후보 6개 평가 <em>점수 / 30</em>")
    s.colhead(rx, rw, "Round 배치")
    cands = [("1", "성장 기회 이동", 26, True, ""), ("2", "AI 에이전트 운영모델", 26, True, ""),
             ("3", "사 온 자산", 25, True, ""), ("D", "약가·급여 제도", 20, False, "Track B 중복"),
             ("E", "비만 경쟁 런칭", 20, False, "청중 좁음"), ("F", "첫해 미조제", 18, False, "Track B 중복")]
    y0, rh = BODY + 0.02, 0.5
    rows = []
    for i, (k, n, v, sel, why) in enumerate(cands):
        col = C["navy"] if sel else C["g75"]
        rows.append(f'<div class="hb" style="top:{p(i*(rh+0.12))}px"><span class="hk" style="background:{col}">{k}</span><span class="hn">{n}</span><span class="ht"><i style="width:{v/30*100:.1f}%;background:{col}"></i><b>{v}</b></span><span class="hw">{why}</span></div>')
    s.add(L, y0, lw, 6 * rh + 5 * 0.12, "".join(rows), cls="bx hbars")
    # right diagram
    ry = BODY + 0.02
    bw = (rw - 0.2) / 2
    s.add(rx, ry, bw, 2.0, '<span class="rl">ROUND 1 · 13:10</span><span class="rn">1</span><span class="rt">한국의 성장 기회는 어디로 이동하는가</span>', cls="bx rbox", style=f"background:{C['navy']}")
    s.add(rx + bw + 0.2, ry, bw, 2.0, '<span class="rl">ROUND 2 · 14:20</span><span class="rn">2</span><span class="rt">AI 에이전트가 바꾸는 Launch Operating Model</span>', cls="bx rbox", style=f"background:{C['blue']}")
    s.add(rx, ry + 2.12, rw, 0.86, '<span class="rn sm">3</span><span><b>공통 사례 · 사 온 자산</b><br>선택(R1) → 준비(R2)</span>', cls="bx rbridge")
    s.add(rx, ry + 3.1, rw, 0.62, '<b>D·E·F</b>는 독립 아젠다에서 빼고 2의 맥락, 1의 사례로 사용', cls="bx rnote")
    s.add(L, 6.22, W, B - 6.22, '<span class="kl">결정 요청</span><span>선정 3개 확정 · 11/27까지 Round별 사례 고객사 2곳 미확보 시 재검토</span>', cls="bx key")
    out.append(s)

    # ---------------- B2
    s = Slide("2. Key Takeaway",
              "Round별로 하나의 문장을 남김: Round 1은 '다시 선택해야 한다', Round 2는 '도입률이 아니라 병목'",
              source_general="IQVIA analysis", num=2)
    cw, gut = (W - 0.4) / 2, 0.4
    x1, x2 = L, L + cw + gut
    for x, lab, col, q, chips_ in [
        (x1, "ROUND 1 · TAKEAWAY ①", C["navy"], "시장을 찾는 데서 끝나지 않는다.<br><u>치료영역·자산·출시 순서</u>를 다시 선택해야 한다.", ["치료영역", "자산", "출시 순서"]),
        (x2, "ROUND 2 · TAKEAWAY ②", C["blue"], "가치는 도입률이 아니라<br><u>런칭 준비의 병목</u>을 얼마나 줄이는가로 결정된다.", ["우선 업무", "역할", "데이터", "통제"])]:
        s.add(x, TOP, cw, 2.5, f'<span class="ql">{lab}</span><span class="qq">{q}</span>', cls="bx bigq", style=f"background:{col}")
        s.add(x, TOP + 2.62, cw, 0.5, "".join(chip(t) for t in chips_), cls="bx chips big")
    s.add(L, TOP + 3.3, W, 0.82, '<span class="kl2">종합 ③</span><span>외부환경이 불확실할수록 <b>성장 선택</b>과 <b>런칭 준비</b>의 연결이 2027년 한국 제약의 성패를 가른다</span>', cls="bx synth")
    s.add(L, 6.22, W, B - 6.22, '<span class="kl">결정 요청</span><span>①·②를 Session Brief(Gate 1, 11/20) Takeaway로 확정 · ③을 종합 세션 메시지로 확정</span>', cls="bx key")
    out.append(s)

    # ---------------- B3
    s = Slide("3. Session · Discussion Topic",
              "두 세션은 '기회 지도 다시 그리기'와 '에이전트에게 먼저 맡길 업무'로 짜고, 사례 하나가 두 Round를 이음",
              source_general="기획서 초안 4·6장, IQVIA analysis", num=3)
    cw, gut = (W - 0.4) / 2, 0.4
    for i, (x, col, lab, title, steps, q) in enumerate([
        (L, C["navy"], "ROUND 1 · 13:10", "2027 한국 성장 기회 지도, 다시 그리기",
         [("Insight", "기회 '이동' 지도"), ("Joint Case", "MNC 지사 임원"), ("Discussion", "국내사·대기업 리더")],
         "무엇이 달라졌고, 무엇을 그만둘 것인가?"),
        (L + cw + gut, C["blue"], "ROUND 2 · 14:20", "런칭 준비 업무 중 에이전트에게 먼저 맡길 것",
         [("Insight", "현황 + 시연 3분"), ("Joint Case", "MNC 런칭 리더"), ("Discussion", "국내사·IQVIA 전문가")],
         "무엇을 먼저 맡기고, 무엇은 사람이 지킬 것인가?")]):
        s.add(x, TOP, cw, 0.9, f'<span class="hs">{lab}</span><b>{title}</b>', cls="bx th big", style=f"background:{col}")
        stw = (cw - 2 * 0.1) / 3
        for j, (a, b) in enumerate(steps):
            s.add(x + j * (stw + 0.1), TOP + 1.02, stw, 1.12, f'<b>{a}</b><span>{b}</span>', cls="bx step" + (" last" if j == 2 else ""), style=f"--c:{col}")
        s.add(x, TOP + 2.26, cw, 1.0, f'<span class="qk" style="color:{col}">핵심 질문</span><span class="qv">“{q}”</span>', cls="bx kq", style=f"border-left-color:{col}")
    s.add(L, TOP + 3.4, W, 0.78, '<span class="kl2">공통 사례</span><span><b>사 온 자산</b> · R1 “같은 잣대로 고르는가?” → R2 “데이터 공백과 파트너 역할은 누가 메우는가?”</span>', cls="bx synth")
    s.add(L, 6.22, W, B - 6.22, '<span class="kl">결정 요청</span><span>세션 제목·핵심 질문 확정 · 시연 3분 포함(Tech 확인) · 공통 사례를 같은 회사로 섭외할지</span>', cls="bx key")
    out.append(s)
    return out

CSS = open(sys.argv[3], encoding="utf-8").read() if len(sys.argv) > 3 else ""
from gen_v2 import brief2
data = {"study": [x.html() for x in study()], "brief": [x.html() for x in brief()], "brief2": [x.html() for x in brief2(Slide, C, L, R, B, W, p, chip)]}
json.dump(data, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
print("ok", ROUND)
