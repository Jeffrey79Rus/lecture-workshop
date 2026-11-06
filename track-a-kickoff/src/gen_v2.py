# -*- coding: utf-8 -*-
"""내부 논의용 v2 (스터디용 상세본 기반). 헤드 메시지 없음 → 콘텐츠 상단을 0.95in로 올림."""
TOP2 = 0.95

def brief2(Slide, C, L, R, B, W, p, chip):
    out = []
    # ================= S1: 6개 Challenge, 같은 비중 박스, 우선순위 순
    s = Slide("1. 핵심 Client Challenge", None, source_general="IQVIA analysis", num=1)
    cols, gut = 3, 0.25
    bw = (W - gut * (cols - 1)) / cols
    bh, rh, g1, g2 = 2.0, 0.56, 0.08, 0.48
    items = [
        # rank, title, tag, color, score, KQ, Why, reason
        (1, "성장 기회는 어디로 이동하는가", "Round 1", C["navy"], 26,
         "특허절벽·미국 약가 변화 이후, 한국에서 우선할 치료영역·환자군·자산은 무엇인가?",
         "본사가 런칭 자원과 순서를 다시 짜는 중. 한국 지사·국내사 모두 기회 지도를 다시 그려야 함",
         "Round 1 질문에 가장 직접적. MNC 리더(참석 60%)의 핵심 의제"),
        (2, "AI 에이전트가 바꾸는 Launch Operating Model", "Round 2 · 고정", C["blue"], 26,
         "런칭 준비 업무 중 무엇을 에이전트에 먼저 맡기고, 역할·데이터·통제는 어떻게 바꾸나?",
         "AI 에이전트 사용·평가 47%, 이미 배포 22%{s:NVIDIA, State of AI in HC&amp;LS 2026}. 도입보다 설계가 과제",
         "'런칭 준비'로 한정해 Track C와 구분. 배정 BU(MC·Analytics·Tech)와 일치"),
        (3, "'사 온 자산'을 성장과 런칭으로", "공통 사례", C["navy50"], 25,
         "외부에서 들여온 자산을 어떤 잣대로 고르고, 런칭 준비는 무엇이 달라야 하나?",
         "빅파마 인라이선스 자산의 40%가 중국산(2025){s:PharmExec 2026.6, IQVIA 집계 인용}. 파이프라인의 출처가 바뀜",
         "R1 '선택'과 R2 '준비'를 잇는 다리. 사례 고객사 확보 가능성 최고"),
        (4, "약가·급여 제도 전환기의 Launch Excellence", "D", None, 20,
         "제네릭 산정률 45%, ICER 상향 등 새 규칙에서 급여·가격·런칭 순서를 어떻게 짜나?",
         "2026~27년 제도 변경이 몰려 고객 절실도는 최고 수준",
         "급여·가격 실행은 Track B Round 2 주제(중복). 2의 맥락으로 활용"),
        (5, "비만·대사 메가 카테고리 경쟁 런칭", "E", None, 20,
         "경구 GLP-1 상륙 후 비급여 시장에서 브랜드·채널·가격을 어떻게 짜나?",
         "경구 비만약 2종 출시로 경쟁 구도가 빠르게 바뀌는 중",
         "직접 해당 참석사가 소수(추정), Track B·C와 겹침. 1의 사례로 활용"),
        (6, "첫해 처방 미조제 (런칭 성과 격차)", "F", None, 18,
         "승인된 신약의 처방이 실제 조제로 이어지지 않는 문제를 어떻게 줄이나?",
         "미국 신약 첫해 처방의 65%가 미조제{s:IQVIA, U.S. Medicine Use Trends 2026 (2020~24년 신약 99개)}",
         "원인이 급여 거절·환자 포기인 접근성 문제로 Track B 영역. 2에서 핸드오프만"),
    ]
    for i, (rk, tt, tag, col, sc, kq, why, rs) in enumerate(items):
        row, c = divmod(i, 3)
        x = L + c * (bw + gut)
        y = TOP2 + row * (bh + g1 + rh + g2)
        on = col is not None
        hc = col if on else C["g65"]
        s.add(x, y, bw, bh,
              f'<div class="cc-h" style="background:{hc}"><span class="rk">{rk}</span><span class="tt">{tt}</span><span class="tg">{tag} · {sc}점</span></div>'
              f'<div class="cc-b"><p><span class="lb">Key Q</span>{kq}</p><p><span class="lb">Why</span>{why}</p></div>',
              cls="bx cc" + ("" if on else " off"))
        s.add(x, y + bh + g1, bw, rh,
              f'<span class="rl">{"선정 사유" if on else "제외 사유"}</span><span>{rs}</span>',
              cls="bx rs" + ("" if on else " off"), style=(f"border-left-color:{col}" if on else ""))
    s.add(L, TOP2 + bh + g1 + rh + 0.1, W, 0.3, '<span>제외 3개 · 독립 아젠다에서 빼고 선정 아젠다의 사례·맥락으로 활용</span>', cls="bx rowlab")
    out.append(s)

    # ================= S2: Key Takeaway (가설) — R1, R2, 종합(비중 확대)
    s = Slide("2. Key Takeaway (가설)", None, source_general="IQVIA analysis", num=2)
    cw, gut = (W - 0.4) / 2, 0.4
    x1, x2 = L, L + cw + gut
    s.colhead(x1, cw, "Round 1 · Takeaway ①", y=TOP2, color=C["navy"])
    s.colhead(x2, cw, "Round 2 · Takeaway ②", y=TOP2, color=C["blue"])
    qy = TOP2 + 0.5
    s.add(x1, qy, cw, 0.95, "<span>“성장 기회는 시장을 찾는 데서 끝나지 않는다. <u>치료영역·자산·출시 순서를 다시 선택</u>해야 한다.”</span>", cls="bx quote", style=f"background:{C['navy']}")
    s.add(x2, qy, cw, 0.95, "<span>“AI 에이전트의 가치는 도입률이 아니라 <u>런칭 준비의 병목을 얼마나 줄이는가</u>로 결정된다.”</span>", cls="bx quote", style=f"background:{C['blue']}")
    hy = qy + 1.05
    hh = 1.86
    s.add(x1, hy, cw, hh, '''<p class="l1">가설적 주장 예시</p>
<p class="l2">MNC 지사의 2027 런칭 우선순위는 시장 크기보다 '본사 포트폴리오 공백을 메우는 정도'로 정해진다</p>
<p class="l2">국내사의 다음 성장축은 제네릭이 아니라 개량신약·비급여·외부 도입 자산에서 나온다</p>
<p class="l2">사 온 자산은 자체 개발 자산과 다른 잣대(데이터 공백, 파트너 조건)로 골라야 한다</p>''', cls="bx txt hyp")
    s.add(x2, hy, cw, hh, '''<p class="l1">가설적 주장 예시</p>
<p class="l2">에이전트가 먼저 효과를 내는 곳은 HCP 접점이 아니라 준비도 점검·예측 같은 내부 반복 업무다</p>
<p class="l2">도입 성과의 차이는 모델 성능보다 업무 재설계와 통제 체계에서 난다</p>
<p class="l2">Launch PMO의 역할은 '진척 관리'에서 '에이전트가 올린 신호를 판단하는 일'로 바뀐다</p>''', cls="bx txt hyp")
    sy = hy + hh + 0.14
    s.add(L, sy, W, B - sy, f'''<div class="sy-h"><span class="kl">종합 세션 ③ · 15:35</span><span class="sy-q">“외부환경이 불확실할수록 <b>성장 선택(R1)</b>과 <b>런칭 준비(R2)</b>의 연결이 2027년 한국 제약의 성패를 가른다.”</span></div>
<div class="sy-b"><div><span class="lb">가설 1</span>성장 기회를 고르는 단계에서 이미 런칭 준비 가능성(데이터·역량·파트너)을 함께 평가해야 한다</div><div><span class="lb">가설 2</span>R1의 선택 기준과 R2의 준비 체계를 같은 지표로 묶은 회사가 2027년 런칭 성과를 앞설 것이다</div></div>''', cls="bx synth2")
    out.append(s)

    # ================= S3: Session · Discussion Topic (넓게)
    s = Slide("3. Session · Discussion Topic", None, source_general="기획서 초안 4·6장, IQVIA analysis", num=3)
    kw = 1.52; cw = (W - kw - 0.08 * 2) / 2
    xa, xb = L + kw + 0.08, L + kw + 0.08 + cw + 0.08
    y = TOP2
    hh = 0.72
    s.add(xa, y, cw, hh, '<span class="hs">Session 1 · Round 1 · 13:10–14:00</span><b>2027 한국 성장 기회 지도, 다시 그리기</b>', cls="bx th big2", style=f"background:{C['navy']}")
    s.add(xb, y, cw, hh, '<span class="hs">Session 2 · Round 2 · 14:20–15:10</span><b>런칭 준비 업무 중 에이전트에게 먼저 맡길 것</b>', cls="bx th big2", style=f"background:{C['blue']}")
    rows = [
        ("Insight 10'", 0.66, "td",
         "<b>INFO·PI</b> 플레너리 Outlook 수치를 받아 치료영역·환자군·자산별 '이동' 지도. 첫 장은 참석 리더 사전 설문",
         "<b>MC·Analytics·Tech</b> R1 요약 2분 → 런칭 부담·에이전트 현황 → 준비도 점검 워크플로 시연 3분{n:시연 가능 여부 Tech 확인 필요}"),
        ("Joint Case 15'", 0.46, "td",
         "<b>MC + MNC 지사 임원</b> 한국 런칭을 본사 우선순위로 올린 사례",
         "<b>MC + MNC 지사 런칭 리더</b> Launch PMO·예측에 AI를 적용한 사례"),
        ("Discussion 15'", 0.46, "td",
         "패널: 국내사 임원, 신사업 대기업 임원, 사례 발표자",
         "패널: 국내사 임원, IQVIA Domain Expert(HTA/HE·CES), 사례 발표자"),
        ("핵심 질문", 0.66, "td kq2",
         "“2027 기회 지도는 작년과 무엇이 다르고, 무엇을 그만둘 것인가?”",
         "“어떤 준비 업무를 먼저 맡기고, 무엇은 사람이 지킬 것인가?”"),
        ("왜 이렇게", 0.86, "td",
         "Outlook과 겹치지 않게 '전망' 대신 '이동'. 리더에게 가장 어려운 결정인 '그만둘 것'을 질문에. 사례(MNC)와 패널(국내·대기업)로 청중 전원을 커버",
         "말로는 Track C와 같아 보여 시연으로 '런칭 준비' 자리를 보임. 교차기능 전문가는 '준비 체크포인트'로만 발언해 Track B·C를 넘지 않음"),
        ("연결", 0.66, "td",
         "<b>→ Round 2</b> “기회를 골랐다면, 그 런칭은 누가 어떻게 준비하는가?”",
         "<b>↔ Track B Round 2</b> 'Evidence를 Patient Access로 어떻게 연결할 것인가?'와 주제 연계. 급여·접근성 실행은 Track B에서 다룸{n:Track은 병렬 진행이므로 청중 이동이 아닌 주제 연계}"),
    ]
    y += hh + 0.06
    for k, h, cls, a, b in rows:
        s.add(L, y, kw, h, k, cls="bx tk")
        s.add(xa, y, cw, h, a, cls="bx " + cls)
        s.add(xb, y, cw, h, b, cls="bx " + cls)
        y += h + 0.06
    s.add(L, y, kw, B - y, "공통 사례", cls="bx tk", style=f"background:{C['navy50']};color:#fff")
    s.add(xa, y, W - kw - 0.08, B - y, "<span><b>사 온 자산의 런칭</b> · R1 “자체 개발과 사 온 자산을 같은 잣대로 고르는가?” → R2 “데이터 공백과 파트너 역할은 누가 메우는가?” 같은 회사가 두 Round에 서면 가장 강함</span>", cls="bx bridge")
    out.append(s)
    return out
