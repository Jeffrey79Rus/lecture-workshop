# -*- coding: utf-8 -*-
"""Track A 킥오프 · 내부 논의용 v2 (3장) — IQVIA MC 템플릿 PPT 빌드.
HTML 초안(04_kickoff-slides-iqvia.html #brief2)과 같은 좌표를 쓴다.
사용자 지시에 따른 템플릿 예외: 헤드 메시지 없음(콘텐츠 상단 0.95in), 표지·Thank You 없음."""
import sys
SKILL = sys.argv[1]
OUT = sys.argv[2]
sys.path.insert(0, SKILL + "/scripts")
from iqvia_deck import IQVIADeck, C, make_para  # noqa: E402

d = IQVIADeck()
TAG = "Track A | Strategy & Launch"
L, R, B, W = C.L, C.R, C.B, C.W
TOP2 = 0.95
NAVY, BLUE, NAVY50 = "navy", "blue", "navy50"
LIGHT = "E6F0F6"


def P(content, size=12, bold=False, color="text", align="l", style="P", spc=0, ls=110):
    return make_para(content, style=style, size=size, bold=bold, color=color, align=align,
                     spc_before=spc, line_spacing=ls)


# ============================================================ 1. 핵심 Client Challenge
s = d.content("1. 핵심 Client Challenge", None, section=TAG, source="IQVIA analysis")
cols, gut = 3, 0.25
bw = (W - gut * (cols - 1)) / cols
bh, rh, g1, g2, hh = 2.08, 0.52, 0.08, 0.42, 0.77
items = [
    (1, "성장 기회는 어디로 이동하는가", "Round 1", NAVY, 26,
     "특허절벽·미국 약가 변화 이후 한국에서 우선할 치료영역·환자군·자산은?",
     "본사가 런칭 자원·순서를 재편 중. 한국 지사·국내사 모두 기회 지도를 다시 그려야 함",
     "Round 1 질문에 가장 직접적. MNC 리더(참석 60%)의 핵심 의제"),
    (2, "AI 에이전트가 바꾸는 Launch Operating Model", "Round 2 · 고정", BLUE, 26,
     "런칭 준비 업무 중 무엇을 에이전트에 먼저 맡기고, 역할·데이터·통제는 어떻게 바꾸나?",
     "AI 에이전트 사용·평가 47%, 배포 22%{s:NVIDIA, State of AI in Healthcare and Life Sciences 2026}. 도입보다 설계가 과제",
     "'런칭 준비'로 한정해 Track C와 구분. 배정 BU(MC·Analytics·Tech)와 일치"),
    (3, "'사 온 자산'을 성장과 런칭으로", "공통 사례", NAVY50, 25,
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
    hc = col if on else "gray65"
    txt = "text" if on else "gray50"
    lab = "navy" if on else "gray50"
    # header band: 채움 사각형 + 순위 원 + 제목
    d.shape(s, "rect", x, y, bw, hh, fill=hc)
    d.shape(s, "oval", x + 0.12, y + (hh - 0.34) / 2, 0.34, 0.34, str(rk), fill="white",
            color=(NAVY if on else "gray50"), size=14)
    d.box(s, x + 0.54, y, bw - 0.54, hh,
          [P(tt, size=14, bold=True, color="white", ls=100),
           P(f"{tag} · {sc}점", size=12, color="white", ls=100, spc=2)],
          anchor="ctr", inset=0.06)
    # body: Key Q / Why
    d.box(s, x, y + hh, bw, bh - hh,
          [P([("Key Q  ", {"b": True, "color": lab}), kq], color=txt, ls=110),
           P([("Why  ", {"b": True, "color": lab}), why], color=txt, ls=110, spc=6)],
          fill=("lightgray" if on else "F7F7F7"), inset=0.12)
    # reason strip
    ry = y + bh + g1
    d.shape(s, "rect", x, ry, 0.06, rh, fill=(col if on else "gray75"))
    d.box(s, x + 0.06, ry, bw - 0.06, rh,
          [P([(("선정 사유  " if on else "제외 사유  "), {"b": True, "color": lab}), rs], color=txt, ls=105)],
          fill=(LIGHT if on else "gray95"), anchor="ctr", inset=0.1)
ly = TOP2 + bh + g1 + rh + 0.07
d.box(s, L, ly, 6.0, 0.3, [P("제외 3개 · 독립 아젠다에서 빼고 선정 아젠다의 사례·맥락으로 활용", bold=True, color="gray50")],
      anchor="ctr", inset=0.0)
d.hline(s, L + 6.05, ly + 0.15, W - 6.05, color="gray75", weight=0.75)

# ============================================================ 2. Key Takeaway (가설)
s = d.content("2. Key Takeaway (가설)", None, section=TAG, source="IQVIA analysis")
cw, gut = (W - 0.4) / 2, 0.4
x1, x2 = L, L + cw + gut
d.column_header(s, x1, cw, "Round 1 · Takeaway ①", y=TOP2)
d.column_header(s, x2, cw, "Round 2 · Takeaway ②", y=TOP2)
qy = TOP2 + 0.5
d.box(s, x1, qy, cw, 0.95,
      [P(["“성장 기회는 시장을 찾는 데서 끝나지 않는다. ", ("치료영역·자산·출시 순서를 다시 선택", {"color": "blue25"}), "해야 한다.”"],
         size=16, bold=True, color="white", ls=110)], fill=NAVY, anchor="ctr", inset=0.15)
d.box(s, x2, qy, cw, 0.95,
      [P(["“AI 에이전트의 가치는 도입률이 아니라 ", ("런칭 준비의 병목을 얼마나 줄이는가", {"color": "blue25"}), "로 결정된다.”"],
         size=16, bold=True, color="white", ls=110)], fill=BLUE, anchor="ctr", inset=0.15)
hy, hh2 = qy + 1.05, 1.98
for x, hyps in [
    (x1, ["MNC 지사의 2027 런칭 우선순위는 시장 크기보다 '본사 포트폴리오 공백 기여도'로 정해진다",
          "국내사의 다음 성장축은 제네릭이 아니라 개량신약·비급여·외부 도입 자산에서 나온다",
          "사 온 자산은 자체 개발과 다른 잣대(데이터 공백·파트너 조건)로 골라야 한다"]),
    (x2, ["에이전트가 먼저 효과를 내는 곳은 HCP 접점이 아닌 준비도 점검·예측 같은 내부 반복 업무다",
          "도입 성과의 차이는 모델 성능보다 업무 재설계와 통제 체계에서 난다",
          "Launch PMO의 역할은 '진척 관리'에서 '에이전트가 올린 신호를 판단하는 일'로 바뀐다"])]:
    d.box(s, x, hy, cw, hh2, [("가설적 주장 예시", "L1")] + [(h, "L2") for h in hyps], fill="lightgray", inset=0.12)
sy = hy + hh2 + 0.1
d.shape(s, "rect", L, sy, W, B - sy, fill="callout")
d.pill(s, L + 0.18, sy + 0.2, 2.0, 0.34, "종합 세션 ③ · 15:35", fill=NAVY, size=12)
d.box(s, L + 2.35, sy + 0.08, W - 2.5, 0.72,
      [P(["“외부환경이 불확실할수록 ", ("성장 선택(R1)", {"u": True}), "과 ", ("런칭 준비(R2)", {"u": True}),
          "의 연결이 2027년 한국 제약의 성패를 가른다.”"], size=18, bold=True, color=NAVY, ls=105)],
      anchor="ctr", inset=0.05)
hw = (W - 0.36 - 0.18) / 2
for k, (lab, t) in enumerate([("가설 1", "성장 기회를 고르는 단계에서 이미 런칭 준비 가능성(데이터·역량·파트너)을 함께 평가해야 한다"),
                              ("가설 2", "R1의 선택 기준과 R2의 준비 체계를 같은 지표로 묶은 회사가 2027년 런칭 성과를 앞설 것이다")]):
    d.box(s, L + 0.18 + k * (hw + 0.18), sy + 0.92, hw, B - sy - 1.1,
          [P([(lab + "  ", {"b": True, "color": NAVY}), t], size=14, ls=110)], fill="white", anchor="ctr", inset=0.14)

# ============================================================ 3. Session · Discussion Topic
s = d.content("3. Session · Discussion Topic", None, section=TAG, source="기획서 초안 4·6장; IQVIA analysis")
kw = 1.52
cw = (W - kw - 0.08 * 2) / 2
xa, xb = L + kw + 0.08, L + kw + 0.08 + cw + 0.08
y, hh3 = TOP2, 0.72
for x, col, a, b in [(xa, NAVY, "Session 1 · Round 1 · 13:10–14:00", "2027 한국 성장 기회 지도, 다시 그리기"),
                     (xb, BLUE, "Session 2 · Round 2 · 14:20–15:10", "런칭 준비 업무 중 에이전트에게 먼저 맡길 것")]:
    d.box(s, x, y, cw, hh3, [P(a, size=12, color="white", ls=100), P(b, size=18, bold=True, color="white", ls=100, spc=2)],
          fill=col, anchor="ctr", inset=0.12)
rows = [
    ("Insight 10'", 0.66, False,
     [("INFO·PI  ", {"b": True, "color": NAVY}), "플레너리 Outlook 수치를 받아 치료영역·환자군·자산별 '이동' 지도. 첫 장은 참석 리더 사전 설문"],
     [("MC·Analytics·Tech  ", {"b": True, "color": NAVY}), "R1 요약 2분 → 런칭 부담·에이전트 현황 → 준비도 점검 워크플로 시연 3분{n:시연 가능 여부 Tech 확인 필요}"]),
    ("Joint Case 15'", 0.46, False,
     [("MC + MNC 지사 임원  ", {"b": True, "color": NAVY}), "한국 런칭을 본사 우선순위로 올린 사례"],
     [("MC + MNC 지사 런칭 리더  ", {"b": True, "color": NAVY}), "Launch PMO·예측에 AI를 적용한 사례"]),
    ("Discussion 15'", 0.46, False,
     ["패널: 국내사 임원, 신사업 대기업 임원, 사례 발표자"],
     ["패널: 국내사 임원, IQVIA Domain Expert(HTA/HE·CES), 사례 발표자"]),
    ("핵심 질문", 0.66, True,
     ["“2027 기회 지도는 작년과 무엇이 다르고, 무엇을 그만둘 것인가?”"],
     ["“어떤 준비 업무를 먼저 맡기고, 무엇은 사람이 지킬 것인가?”"]),
    ("왜 이렇게", 0.86, False,
     ["Outlook과 겹치지 않게 '전망' 대신 '이동'. 리더에게 가장 어려운 결정인 '그만둘 것'을 질문에. 사례(MNC)와 패널(국내·대기업)로 청중 전원을 커버"],
     ["말로는 Track C와 같아 보여 시연으로 '런칭 준비' 자리를 보임. 교차기능 전문가는 '준비 체크포인트'로만 발언해 Track B·C를 넘지 않음"]),
    ("연결", 0.66, False,
     [("→ Round 2  ", {"b": True, "color": NAVY}), "“기회를 골랐다면, 그 런칭은 누가 어떻게 준비하는가?”"],
     [("↔ Track B Round 2  ", {"b": True, "color": NAVY}), "'Evidence를 Patient Access로 어떻게 연결할 것인가?'와 주제 연계. 급여·접근성 실행은 Track B에서 다룸{n:Track은 병렬 진행이므로 청중 이동이 아닌 주제 연계}"]),
]
y += hh3 + 0.06
for k, h, kq, a, b in rows:
    d.box(s, L, y, kw, h, [P(k, bold=True, color=NAVY)], fill="navy25", anchor="ctr", inset=0.1)
    for x, cont in [(xa, a), (xb, b)]:
        if kq:
            d.box(s, x, y, cw, h, [P(cont, size=14, bold=True, color=NAVY, ls=105)], fill=LIGHT, anchor="ctr", inset=0.12)
        else:
            d.box(s, x, y, cw, h, [P(cont, ls=110)], fill="lightgray", anchor="ctr", inset=0.1)
    y += h + 0.06
d.box(s, L, y, kw, B - y, [P("공통 사례", bold=True, color="white")], fill=NAVY50, anchor="ctr", inset=0.1)
d.box(s, xa, y, W - kw - 0.08, B - y,
      [P([("사 온 자산의 런칭", {"b": True, "color": NAVY}),
          " · R1 “자체 개발과 사 온 자산을 같은 잣대로 고르는가?” → R2 “데이터 공백과 파트너 역할은 누가 메우는가?” 같은 회사가 두 Round에 서면 가장 강함"], ls=110)],
      fill=LIGHT, line=NAVY50, line_w=1.5, anchor="ctr", inset=0.12)

d.save(OUT)
print("saved", OUT)
