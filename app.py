import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title='✨ 제목학원 - 나만의 센스 있는 별명 만들기', page_icon='✨')

# 스타일 (파스텔톤 배경, 깔끔한 폰트)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    html, body, [class*="css"]  {
        background: linear-gradient(135deg, #ffeef5 0%, #fff7ea 100%);
        font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial;
    }
    .title {
        color: #5a3e85;
        font-weight: 700;
    }
    .subtle {
        color: #6b5b50;
    }
    .result-box {
        background: rgba(255,255,255,0.6);
        border-radius: 14px;
        padding: 18px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    }
    .nickname {
        font-size: 28px;
        color: #d6336c;
        font-weight: 700;
    }
    .fortune {
        font-size: 18px;
        color: #5a3e85;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 헤더
st.markdown("<div class='title'><h1>✨ 제목학원 - 나만의 센스 있는 별명 만들기</h1></div>", unsafe_allow_html=True)
st.markdown("<div class='subtle'>유머와 센스가 묻어나는 나만의 이름과 문장 만들기</div>", unsafe_allow_html=True)
st.write('')

# 입력란
key_word = st.text_input('나를 한 단어로 표현한다면?', placeholder='예: 감성, 쿨, 부지런', key='key_word')
likes_input = st.text_input('내가 좋아하는 것 2가지 (콤마로 구분)', placeholder='예: 초코, 고양이, 꽃', key='likes')

# 변수 저장 (요청된 변수명)
# key_word, likes
likes = [x.strip() for x in likes_input.split(',') if x.strip()][:2]

def make_nick(word, likes_list):
    base = word.strip() if word and word.strip() else '멋쟁이'

    def portmanteau(a, b):
        # 간단한 합성어: 각 단어 앞부분을 붙여서 발랄한 별명 생성
        a_part = a.replace(' ', '')[:3]
        b_part = b.replace(' ', '')[:3]
        return (a_part + b_part).capitalize()

    candidates = []

    # 패턴 베이스
    if likes_list:
        l1 = likes_list[0]
        candidates.extend([
            f"{base}한 {l1}",
            f"{l1}의 {base}",
            f"{base} {l1}",
            f"{base}의 {l1} & {likes_list[1]}" if len(likes_list) > 1 else None,
        ])

        if len(likes_list) > 1:
            l2 = likes_list[1]
            candidates.extend([
                f"{l1}{l2} {base}",
                f"{portmanteau(base, l1)}", 
                f"{portmanteau(l1, l2)} {base}",
            ])
        else:
            candidates.extend([f"{portmanteau(base, l1)}", f"{base} 스팽글"])
    else:
        candidates.extend([f"{base}한 친구", f"{base}한 스토리", f"{base}플레이어"])

    # 스타일/토핑(유머 요소)
    prefixes = ["힙한", "감성", "쫀득한", "스윗한", "무드 있는", "레전드급"]
    suffixes = ["보스", "요정", "마스터", "스튜디오", "스냅"]

    for p in prefixes:
        candidates.append(f"{p} {base}")
    for s in suffixes:
        candidates.append(f"{base} {s}")

    # 특별 변형: 'Captain', 'Queen/King' 스타일
    candidates.extend([f"Captain {base}", f"{base} the Great", f"Mini {base}"])

    # 필터링 및 선택
    candidates = [c for c in candidates if c]
    # 조금 더 센스 있게 랜덤 가중치: 포트맨토나 좋아요 기반 조합에 가중치 부여
    weights = [3 if (len(c.split()) == 1 and len(c) <= 10) else 1 for c in candidates]
    return random.choices(candidates, weights=weights, k=1)[0]

def make_fortune(nick):
    templates = [
        f"너에게 딱 맞는 별명은 {nick}. 이미 전설의 시작이야 ✨",
        f"별명 '{nick}'으로 시작하는 순간, 너의 감성이 모두를 사로잡는다 🌟",
        f"{nick} — 이 이름 하나면 분위기 완승! 😎",
        f"이제부터 넌 '{nick}'. 좋아요 백만 개 예약 완료! 🎉",
        f"조금 특별한 이름, {nick}. 오늘의 하이라이트는 너야 🌈",
        f"'{nick}'— 사람들 머릿속에 한 번 들으면 잊히지 않아요 ✨",
        f"작은 시작, 큰 임팩트. '{nick}'이 바로 그 이름 🌟",
        f"'{nick}'으로 불리는 순간, 분위기 점화! 🔥",
    ]
    # 조금 더 센스 있는 선택: 길이/이모지 조합에 따라 가중치
    return random.choice(templates)

if st.button('별명 생성하기'):
    if not key_word and not likes:
        st.info('먼저 한 단어와 좋아하는 것 중 적어도 하나를 입력해 주세요.')
    else:
        nickname = make_nick(key_word, likes)
        fortune = make_fortune(nickname)

        st.markdown("<div class='result-box'>", unsafe_allow_html=True)
        st.markdown(f"<div class='nickname'>🎉 너의 별명은 '{nickname}' 🎉</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='fortune'>🌟 {fortune}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # 간단한 예시 출력
        st.write('')
        st.caption('결과는 유머와 센스를 반영하여 짧고 간결하게 표시됩니다.')

else:
    st.write('')
    st.info('한 단어와 좋아하는 것 2가지를 입력하고 "별명 생성하기" 버튼을 눌러보세요!')
