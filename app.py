
import base64
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="예희야, 생일 축하해",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed",
)

AUDIO_FILE = Path("birthday_song.mp3")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Noto+Sans+KR:wght@400;500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 20% 10%, rgba(255, 221, 225, 0.70), transparent 35%),
            radial-gradient(circle at 85% 25%, rgba(255, 239, 213, 0.75), transparent 35%),
            linear-gradient(150deg, #fffaf7 0%, #fff4f4 52%, #f9f1ff 100%);
    }

    header, footer, #MainMenu {
        visibility: hidden;
    }

    .block-container {
        max-width: 840px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }

    .hero {
        text-align: center;
        padding: 64px 28px 46px;
        border-radius: 32px;
        background: rgba(255, 255, 255, 0.70);
        border: 1px solid rgba(255, 255, 255, 0.90);
        box-shadow: 0 18px 60px rgba(110, 74, 93, 0.12);
        backdrop-filter: blur(12px);
    }

    .eyebrow {
        font-size: 0.9rem;
        letter-spacing: 0.22em;
        color: #b06b7a;
        font-weight: 700;
        margin-bottom: 16px;
    }

    .hero h1 {
        font-family: 'Gowun Batang', serif;
        font-size: clamp(2.4rem, 7vw, 4.7rem);
        line-height: 1.15;
        color: #573c48;
        margin: 0;
    }

    .hero p {
        margin-top: 22px;
        font-family: 'Gowun Batang', serif;
        font-size: 1.18rem;
        line-height: 1.9;
        color: #765d68;
    }

    .heart {
        display: inline-block;
        animation: beat 1.35s infinite;
    }

    @keyframes beat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.12); }
    }

    .memory-card, .letter-card {
        margin-top: 28px;
        padding: 34px 32px;
        border-radius: 26px;
        background: rgba(255,255,255,0.78);
        box-shadow: 0 14px 42px rgba(110, 74, 93, 0.10);
        border: 1px solid rgba(255,255,255,0.92);
    }

    .memory-title {
        color: #b06b7a;
        font-weight: 700;
        font-size: 0.93rem;
        letter-spacing: 0.10em;
        margin-bottom: 14px;
    }

    .memory-text, .letter-text {
        font-family: 'Gowun Batang', serif;
        color: #59464f;
        font-size: 1.08rem;
        line-height: 2;
        word-break: keep-all;
    }

    .highlight {
        color: #b95f73;
        font-weight: 700;
    }

    .signature {
        margin-top: 28px;
        text-align: right;
        font-family: 'Gowun Batang', serif;
        color: #755c67;
        font-size: 1.06rem;
    }

    .stButton > button {
        width: 100%;
        border: none;
        border-radius: 999px;
        padding: 0.9rem 1.4rem;
        font-size: 1.05rem;
        font-weight: 700;
        color: white;
        background: linear-gradient(135deg, #c46d82, #9c6fb0);
        box-shadow: 0 10px 26px rgba(177, 102, 130, 0.28);
        transition: 0.25s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 14px 30px rgba(177, 102, 130, 0.35);
        color: white;
    }

    .audio-note {
        text-align: center;
        color: #8d7380;
        font-size: 0.88rem;
        margin: 12px 0 2px;
    }

    .footer-message {
        text-align: center;
        margin-top: 32px;
        color: #9a7a88;
        font-family: 'Gowun Batang', serif;
        line-height: 1.8;
    }

    @media (max-width: 640px) {
        .block-container {
            padding-top: 1.3rem;
        }
        .hero {
            padding: 46px 21px 34px;
            border-radius: 24px;
        }
        .memory-card, .letter-card {
            padding: 28px 23px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def audio_player(path: Path):
    if not path.exists():
        st.warning(
            "음악 파일이 아직 없습니다. Suno에서 만든 곡을 "
            "`birthday_song.mp3`라는 이름으로 app.py와 같은 폴더에 넣어주세요."
        )
        return

    audio_bytes = path.read_bytes()
    audio_base64 = base64.b64encode(audio_bytes).decode()

    components.html(
        f"""
        <audio id="birthday-audio" autoplay controls loop style="width:100%;">
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mpeg">
        </audio>
        <script>
            const audio = document.getElementById("birthday-audio");
            audio.volume = 0.85;
            audio.play().catch(() => {{
                console.log("브라우저 자동 재생 정책으로 재생 버튼 입력이 필요합니다.");
            }});
        </script>
        """,
        height=72,
    )

if "opened" not in st.session_state:
    st.session_state.opened = False

if not st.session_state.opened:
    st.markdown(
        """
        <div class="hero">
            <div class="eyebrow">A LETTER FOR YEHEE</div>
            <h1>예희에게 도착한<br>작은 생일 편지 <span class="heart">💗</span></h1>
            <p>
                오늘을 위해 준비한 이야기가 있어.<br>
                천천히 열어봐 줘.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    if st.button("편지 열기  ·  노래 듣기 🎧"):
        st.session_state.opened = True
        st.rerun()

else:
    st.markdown(
        """
        <div class="hero">
            <div class="eyebrow">HAPPY 2ND BIRTHDAY TOGETHER</div>
            <h1>예희야,<br>생일 축하해 <span class="heart">♥</span></h1>
            <p>
                우리가 함께 맞는 두 번째 생일.<br>
                오늘은 누구보다 행복한 하루였으면 좋겠어.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<p class="audio-note">이 페이지를 위해 만든 노래야. 재생 버튼을 눌러 들어줘.</p>', unsafe_allow_html=True)
    audio_player(AUDIO_FILE)

    st.markdown(
        """
        <div class="memory-card">
            <div class="memory-title">OUR FIRST MOMENT</div>
            <div class="memory-text">
                축제의 밤, 함께 노래를 들으며
                <span class="highlight">처음 네 손을 잡았던 순간</span>이
                아직도 엊그제처럼 생생해.<br><br>
                그때는 손을 잡는 것만으로도 떨렸는데,
                어느새 너와 함께 두 번째 생일을 맞이하고 있네.
                시간이 참 빠르면서도, 그날의 설렘은 여전히 그대로인 것 같아.
            </div>
        </div>

        <div class="letter-card">
            <div class="memory-title">TO. 예희</div>
            <div class="letter-text">
                예희야, 네가 내 곁에 온 뒤로 평범했던 하루들이 조금씩 특별해졌어.<br><br>

                같이 웃었던 날도, 아무 말 없이 곁에 있어 주었던 순간도,
                사소해서 지나칠 수 있었던 시간들까지
                이제는 전부 오래 기억하고 싶은 추억이 됐어.<br><br>

                앞으로도 행복한 날에는 누구보다 크게 함께 웃고,
                힘든 날에는 가장 가까운 곳에서 네 편이 되어줄게.<br><br>

                화려한 말보다 매일의 행동으로,
                처음 네 손을 잡았던 그 마음을 오래 지켜가고 싶어.<br><br>

                <span class="highlight">
                    태어나줘서 고마워.<br>
                    우리가 함께 맞는 두 번째 생일을 진심으로 축하해.
                </span>
            </div>
            <div class="signature">
                오래도록 네 손을 잡고 싶은 사람으로부터
            </div>
        </div>

        <div class="footer-message">
            오늘의 모든 순간이<br>
            예희에게 따뜻한 기억으로 남기를 🎂
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    if st.button("처음 화면으로 돌아가기"):
        st.session_state.opened = False
        st.rerun()
