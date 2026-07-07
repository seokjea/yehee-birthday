import base64
import html
import mimetypes
import textwrap
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


# =========================================================
# Streamlit 기본 설정
# =========================================================

st.set_page_config(
    page_title="예희야, 생일 축하해",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# =========================================================
# 파일 경로
# =========================================================

MAIN_IMAGE = Path("main.png")
SONG_FILE = Path("song.mp3")

PHOTO_DIR = Path("photos")
LAST_VIDEO = PHOTO_DIR / "1.mp4"

PHOTO_FILES = [
    *[f"{number}.jpg" for number in range(1, 15)],
    *[f"a-{number}.jpg" for number in range(1, 5)],
]

SLIDE_INTERVAL_MS = 4000


# =========================================================
# 공통 함수
# =========================================================

def render_html(markup: str) -> None:
    """
    Markdown 변환 없이 HTML을 직접 출력한다.
    div, h1, span 태그가 글자로 노출되는 문제를 막는다.
    """
    st.html(textwrap.dedent(markup).strip())


def file_to_data_uri(path: Path) -> str:
    """
    로컬 파일을 HTML 내부에서 재생할 수 있도록
    Base64 Data URI로 변환한다.
    """
    mime_type, _ = mimetypes.guess_type(path.name)
    mime_type = mime_type or "application/octet-stream"

    encoded = base64.b64encode(
        path.read_bytes()
    ).decode("utf-8")

    return f"data:{mime_type};base64,{encoded}"


# =========================================================
# 전체 CSS
# =========================================================

render_html(
    """
    <style>
    @import url(
        'https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Noto+Sans+KR:wght@400;500;700&display=swap'
    );

    :root {
        --rose: #b95f73;
        --dark: #573c48;
        --text: #765d68;
        --paper: rgba(255, 255, 255, 0.82);
    }

    html,
    body,
    [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 20% 10%,
                rgba(255, 221, 225, 0.72),
                transparent 35%
            ),
            radial-gradient(
                circle at 85% 25%,
                rgba(255, 239, 213, 0.75),
                transparent 35%
            ),
            linear-gradient(
                150deg,
                #fffaf7 0%,
                #fff4f4 52%,
                #f9f1ff 100%
            );
    }

    header,
    footer,
    #MainMenu {
        visibility: hidden;
    }

    .block-container {
        max-width: 840px;
        padding-top: 2.4rem;
        padding-bottom: 4rem;
    }

    .hero {
        padding: 58px 28px 42px;
        border: 1px solid rgba(255, 255, 255, 0.94);
        border-radius: 32px;
        background: rgba(255, 255, 255, 0.74);
        box-shadow: 0 18px 60px rgba(110, 74, 93, 0.12);
        text-align: center;
        backdrop-filter: blur(12px);
    }

    .eyebrow {
        margin-bottom: 16px;
        color: #b06b7a;
        font-size: 0.9rem;
        font-weight: 700;
        letter-spacing: 0.22em;
    }

    .hero h1 {
        margin: 0;
        color: var(--dark);
        font-family: 'Gowun Batang', serif;
        font-size: clamp(2.4rem, 7vw, 4.7rem);
        line-height: 1.17;
    }

    .hero p {
        margin: 22px 0 0;
        color: var(--text);
        font-family: 'Gowun Batang', serif;
        font-size: 1.18rem;
        line-height: 1.9;
    }

    .birthday-date {
        display: inline-block;
        margin-top: 20px;
        padding: 9px 18px;
        border: 1px solid rgba(185, 95, 115, 0.22);
        border-radius: 999px;
        color: #a45f70;
        background: rgba(255, 255, 255, 0.65);
        font-family: 'Gowun Batang', serif;
        font-size: 1rem;
        font-weight: 700;
        letter-spacing: 0.18em;
    }

    .heart {
        display: inline-block;
        animation: heartbeat 1.35s infinite;
    }

    @keyframes heartbeat {
        0%,
        100% {
            transform: scale(1);
        }

        50% {
            transform: scale(1.12);
        }
    }

    .memory-card,
    .letter-card,
    .gallery-title-card {
        margin-top: 28px;
        padding: 34px 32px;
        border: 1px solid rgba(255, 255, 255, 0.94);
        border-radius: 26px;
        background: var(--paper);
        box-shadow: 0 14px 42px rgba(110, 74, 93, 0.10);
    }

    .memory-title {
        margin-bottom: 14px;
        color: #b06b7a;
        font-size: 0.93rem;
        font-weight: 700;
        letter-spacing: 0.10em;
    }

    .memory-text,
    .letter-text {
        color: #59464f;
        font-family: 'Gowun Batang', serif;
        font-size: 1.08rem;
        line-height: 2;
        word-break: keep-all;
    }

    .highlight {
        color: var(--rose);
        font-weight: 700;
    }

    .signature {
        margin-top: 28px;
        color: #755c67;
        font-family: 'Gowun Batang', serif;
        font-size: 1.06rem;
        text-align: right;
    }

    .main-photo-title {
        margin: 28px 0 12px;
        color: #9c6876;
        font-family: 'Gowun Batang', serif;
        font-size: 1rem;
        text-align: center;
    }

    [data-testid="stImage"] {
        padding: 12px;
        border-radius: 28px;
        background: rgba(255, 255, 255, 0.80);
        box-shadow: 0 16px 46px rgba(110, 74, 93, 0.14);
    }

    [data-testid="stImage"] img {
        max-height: 690px;
        border-radius: 20px;
        object-fit: contain;
    }

    [data-testid="stImageCaption"] {
        padding-top: 8px;
        color: #765d68;
        font-family: 'Gowun Batang', serif;
        font-size: 0.98rem;
        text-align: center;
    }

    .audio-note {
        margin: 20px 0 10px;
        color: #8d7380;
        font-size: 0.9rem;
        line-height: 1.8;
        text-align: center;
    }

    .footer-message {
        margin-top: 34px;
        color: #9a7a88;
        font-family: 'Gowun Batang', serif;
        line-height: 1.8;
        text-align: center;
    }

    .stButton > button {
        width: 100%;
        padding: 0.92rem 1.4rem;
        border: none;
        border-radius: 999px;
        color: white;
        background: linear-gradient(
            135deg,
            #c46d82,
            #9c6fb0
        );
        box-shadow: 0 10px 26px rgba(177, 102, 130, 0.28);
        font-size: 1.05rem;
        font-weight: 700;
        transition: 0.25s ease;
    }

    .stButton > button:hover {
        color: white;
        box-shadow: 0 14px 30px rgba(177, 102, 130, 0.35);
        transform: translateY(-2px);
    }

    @media (max-width: 640px) {
        .block-container {
            padding-top: 1.1rem;
        }

        .hero {
            padding: 43px 20px 33px;
            border-radius: 24px;
        }

        .memory-card,
        .letter-card,
        .gallery-title-card {
            padding: 27px 22px;
        }

        [data-testid="stImage"] {
            padding: 8px;
            border-radius: 22px;
        }

        [data-testid="stImage"] img {
            border-radius: 16px;
        }
    }
    </style>
    """
)


# =========================================================
# 대표 이미지
# =========================================================

def show_main_image() -> None:
    if not MAIN_IMAGE.exists():
        st.warning(
            "`main.png` 파일이 없습니다. "
            "app.py와 같은 폴더에 넣어주세요."
        )
        return

    render_html(
        """
        <div class="main-photo-title">
            편지를 열기 전에,
            먼저 보여주고 싶은 한 장
        </div>
        """
    )

    st.image(
        str(MAIN_IMAGE),
        caption="우리가 함께한 순간 중, 예희가 좋아하는 한 장!",
        use_container_width=True,
    )


# =========================================================
# 생일 노래
# =========================================================

def show_birthday_song() -> None:
    if not SONG_FILE.exists():
        st.warning(
            "`song.mp3` 파일이 없습니다. "
            "app.py와 같은 폴더에 넣어주세요."
        )
        return

    song_uri = file_to_data_uri(SONG_FILE)

    components.html(
        f"""
        <div style="
            padding: 14px;
            border-radius: 22px;
            background: rgba(255, 255, 255, 0.86);
            box-shadow: 0 12px 34px rgba(110, 74, 93, 0.12);
        ">
            <audio
                id="birthday-song"
                controls
                autoplay
                loop
                preload="auto"
                style="width: 100%;"
            >
                <source
                    src="{song_uri}"
                    type="audio/mpeg"
                >
                이 브라우저에서는 음악을 재생할 수 없습니다.
            </audio>
        </div>

        <script>
            const player =
                document.getElementById("birthday-song");

            player.volume = 0.85;

            player.play().catch(() => {{
                console.log(
                    "모바일에서는 재생 버튼을 한 번 눌러야 할 수 있습니다."
                );
            }});
        </script>
        """,
        height=90,
    )


# =========================================================
# 사진 및 마지막 영상 슬라이드
# =========================================================

def show_photo_carousel() -> None:
    items: list[dict[str, str]] = []

    for filename in PHOTO_FILES:
        path = PHOTO_DIR / filename

        if path.exists():
            items.append(
                {
                    "type": "image",
                    "name": filename,
                    "uri": file_to_data_uri(path),
                }
            )

    video_found = LAST_VIDEO.exists()

    if video_found:
        items.append(
            {
                "type": "video",
                "name": LAST_VIDEO.name,
                "uri": file_to_data_uri(LAST_VIDEO),
            }
        )

    if not items:
        st.warning(
            "`photos` 폴더에 "
            "1.jpg~14.jpg, "
            "a-1.jpg~a-4.jpg, "
            "1.mp4를 넣어주세요."
        )
        return

    if not video_found:
        st.warning(
            "마지막 영상 `photos/1.mp4`를 찾지 못했습니다."
        )

    slide_parts: list[str] = []

    for index, item in enumerate(items):
        display = "block" if index == 0 else "none"
        safe_name = html.escape(item["name"])

        if item["type"] == "image":
            media = (
                f'<img '
                f'src="{item["uri"]}" '
                f'alt="{safe_name}" '
                f'draggable="false">'
            )

        else:
            media = f"""
            <div class="video-wrap">
                <video
                    class="final-video"
                    muted
                    controls
                    playsinline
                    preload="auto"
                >
                    <source
                        src="{item["uri"]}"
                        type="video/mp4"
                    >
                    이 브라우저에서는 영상을 재생할 수 없습니다.
                </video>

                <div class="video-caption">
                    이 장면 다음에도,
                    우리 이야기는 계속될 거야.
                </div>
            </div>
            """

        slide_parts.append(
            f"""
            <div
                class="slide"
                data-kind="{item["type"]}"
                style="display: {display};"
            >
                {media}
            </div>
            """
        )

    slides_markup = "\n".join(slide_parts)
    total_count = len(items)

    carousel_html = """
    <!doctype html>

    <html lang="ko">
    <head>
        <meta charset="utf-8">

        <meta
            name="viewport"
            content="width=device-width, initial-scale=1"
        >

        <style>
        @import url(
            'https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Noto+Sans+KR:wght@400;500;700&display=swap'
        );

        * {
            box-sizing: border-box;
        }

        html,
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
            background: transparent;
            font-family: 'Noto Sans KR', sans-serif;
        }

        .shell {
            width: 100%;
            padding: 12px;
            border-radius: 28px;
            background: rgba(255, 255, 255, 0.88);
            box-shadow: 0 16px 44px rgba(110, 74, 93, 0.14);
        }

        .stage {
            position: relative;
            width: 100%;
            overflow: hidden;
            border-radius: 21px;
            background: #f3e9ed;
            touch-action: pan-y;
        }

        .slide {
            width: 100%;
            animation: fade-in 0.42s ease;
        }

        .slide img,
        .slide video {
            display: block;
            width: 100%;
            height: 580px;
            background: #f3e9ed;
            object-fit: contain;
            user-select: none;
        }

        .slide video {
            background: #000;
        }

        .video-caption {
            padding: 17px 12px 19px;
            color: #765d68;
            background: rgba(255, 255, 255, 0.95);
            font-family: 'Gowun Batang', serif;
            font-size: 1rem;
            text-align: center;
        }

        @keyframes fade-in {
            from {
                opacity: 0.35;
                transform: scale(0.995);
            }

            to {
                opacity: 1;
                transform: scale(1);
            }
        }

        .nav {
            position: absolute;
            top: 50%;
            z-index: 10;
            width: 46px;
            height: 46px;
            border: 0;
            border-radius: 50%;
            color: #8f5365;
            background: rgba(255, 255, 255, 0.90);
            box-shadow: 0 7px 20px rgba(70, 40, 52, 0.20);
            font-size: 25px;
            line-height: 1;
            cursor: pointer;
            transform: translateY(-50%);
        }

        .nav:hover {
            background: white;
        }

        .prev {
            left: 15px;
        }

        .next {
            right: 15px;
        }

        .progress-track {
            width: 100%;
            height: 4px;
            margin-top: 10px;
            overflow: hidden;
            border-radius: 999px;
            background: rgba(176, 107, 122, 0.15);
        }

        .progress-bar {
            width: 0;
            height: 100%;
            border-radius: 999px;
            background: linear-gradient(
                90deg,
                #c46d82,
                #9c6fb0
            );
        }

        .progress-bar.running {
            animation: progress __INTERVAL__ms linear forwards;
        }

        @keyframes progress {
            from {
                width: 0;
            }

            to {
                width: 100%;
            }
        }

        .meta {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            padding: 14px 9px 4px;
            color: #765d68;
            font-size: 14px;
        }

        .counter {
            flex: 0 0 auto;
            font-weight: 700;
        }

        .hint {
            min-width: 0;
            color: #9c808b;
            font-size: 13px;
            text-align: right;
        }

        @media (max-width: 640px) {
            .slide img,
            .slide video {
                height: 460px;
            }

            .nav {
                width: 42px;
                height: 42px;
            }
        }

        @media (max-width: 420px) {
            .shell {
                padding: 8px;
                border-radius: 22px;
            }

            .stage {
                border-radius: 17px;
            }

            .slide img,
            .slide video {
                height: 390px;
            }

            .nav {
                width: 38px;
                height: 38px;
                font-size: 22px;
            }

            .prev {
                left: 9px;
            }

            .next {
                right: 9px;
            }
        }
        </style>
    </head>

    <body>
        <div class="shell">

            <div
                class="stage"
                id="stage"
            >
                __SLIDES__

                <button
                    class="nav prev"
                    id="prev-button"
                    type="button"
                    aria-label="이전"
                >
                    ‹
                </button>

                <button
                    class="nav next"
                    id="next-button"
                    type="button"
                    aria-label="다음"
                >
                    ›
                </button>
            </div>

            <div class="progress-track">
                <div
                    class="progress-bar"
                    id="progress-bar"
                ></div>
            </div>

            <div class="meta">
                <div class="counter">
                    <span id="current-number">1</span>
                    /
                    __TOTAL__
                </div>

                <div
                    class="hint"
                    id="hint"
                >
                    사진은 4초마다 자동으로 넘어가
                </div>
            </div>

        </div>

        <script>
        (() => {
            const interval = __INTERVAL__;

            const slides = Array.from(
                document.querySelectorAll(".slide")
            );

            const currentNumber =
                document.getElementById("current-number");

            const hint =
                document.getElementById("hint");

            const progress =
                document.getElementById("progress-bar");

            const stage =
                document.getElementById("stage");

            const prev =
                document.getElementById("prev-button");

            const next =
                document.getElementById("next-button");

            let current = 0;
            let timer = null;
            let touchStartX = 0;


            function stopTimer() {
                if (timer !== null) {
                    window.clearTimeout(timer);
                    timer = null;
                }

                progress.classList.remove("running");
                void progress.offsetWidth;
            }


            function stopVideos() {
                document
                    .querySelectorAll(".slide video")
                    .forEach((video) => {
                        video.pause();

                        try {
                            video.currentTime = 0;
                        }
                        catch (error) {
                            console.log(error);
                        }

                        video.onended = null;
                    });
            }


            function startProgress() {
                progress.classList.remove("running");
                void progress.offsetWidth;
                progress.classList.add("running");
            }


            function playFinalVideo(video) {
                const startPlayback = () => {
                    video.play().catch(() => {
                        hint.textContent =
                            "재생 버튼을 눌러 마지막 영상을 봐줘";
                    });
                };

                if (video.readyState >= 2) {
                    startPlayback();
                }
                else {
                    video.addEventListener(
                        "loadeddata",
                        startPlayback,
                        {
                            once: true
                        }
                    );

                    video.load();
                }
            }


            function schedule() {
                stopTimer();

                const activeSlide = slides[current];
                const kind = activeSlide.dataset.kind;

                if (kind === "video") {
                    const video =
                        activeSlide.querySelector("video");

                    hint.textContent =
                        "마지막 영상이야. 천천히 봐줘";

                    progress.style.width = "100%";

                    window.setTimeout(() => {
                        playFinalVideo(video);
                    }, 150);

                    video.onended = () => {
                        show(0);
                    };

                    return;
                }

                hint.textContent =
                    "사진은 4초마다 자동으로 넘어가";

                progress.style.width = "";

                startProgress();

                timer = window.setTimeout(
                    () => {
                        show(current + 1);
                    },
                    interval
                );
            }


            function show(index) {
                stopTimer();
                stopVideos();

                slides[current].style.display = "none";

                current = (
                    index + slides.length
                ) % slides.length;

                slides[current].style.display = "block";

                currentNumber.textContent =
                    String(current + 1);

                schedule();
            }


            prev.addEventListener(
                "click",
                () => {
                    show(current - 1);
                }
            );


            next.addEventListener(
                "click",
                () => {
                    show(current + 1);
                }
            );


            stage.addEventListener(
                "touchstart",
                (event) => {
                    touchStartX =
                        event.changedTouches[0].screenX;
                },
                {
                    passive: true
                }
            );


            stage.addEventListener(
                "touchend",
                (event) => {
                    const touchEndX =
                        event.changedTouches[0].screenX;

                    const distance =
                        touchStartX - touchEndX;

                    if (Math.abs(distance) < 50) {
                        return;
                    }

                    show(
                        distance > 0
                            ? current + 1
                            : current - 1
                    );
                },
                {
                    passive: true
                }
            );


            schedule();
        })();
        </script>

    </body>
    </html>
    """

    carousel_html = (
        carousel_html
        .replace("__SLIDES__", slides_markup)
        .replace("__TOTAL__", str(total_count))
        .replace("__INTERVAL__", str(SLIDE_INTERVAL_MS))
    )

    components.html(
        carousel_html,
        height=735,
        scrolling=False,
    )


# =========================================================
# 세션 상태
# =========================================================

if "opened" not in st.session_state:
    st.session_state.opened = False


# =========================================================
# 편지를 열기 전 화면
# =========================================================

if not st.session_state.opened:

    render_html(
        """
        <section class="hero">

            <div class="eyebrow">
                A LETTER FOR YEHEE
            </div>

            <h1>
                예희에게 도착한<br>
                작은 생일 편지

                <span class="heart">
                    💗
                </span>
            </h1>

            <p>
                오늘을 위해 준비한 이야기가 있어.<br>
                천천히 열어봐 줘.
            </p>

        </section>
        """
    )

    show_main_image()

    st.write("")

    if st.button(
        "편지 열기 · 노래 듣기 🎧",
        key="open-letter",
    ):
        st.session_state.opened = True
        st.rerun()


# =========================================================
# 편지를 연 뒤 화면
# =========================================================

else:

    render_html(
        """
        <section class="hero">

            <div class="eyebrow">
                HAPPY BIRTHDAY
            </div>

            <h1>
                예희야,<br>
                22살 생일 축하해

                <span class="heart">
                    ♥
                </span>
            </h1>

            <div class="birthday-date">
                2026 · 07 · 15
            </div>

            <p>
                우리가 함께 맞는 두 번째 생일.<br>
                오늘은 누구보다 행복한 하루였으면 좋겠어.
            </p>

        </section>
        """
    )


    render_html(
        """
        <p class="audio-note">
            예희를 위해 만든 노래야.<br>
            재생 버튼을 누르고 천천히 읽어줘 🎧
        </p>
        """
    )


    show_birthday_song()


    render_html(
        """
        <section class="memory-card">

            <div class="memory-title">
                OUR FIRST MOMENT
            </div>

            <div class="memory-text">

                축제의 밤,
                함께 노래를 들으며

                <span class="highlight">
                    처음 네 손을 잡았던 순간
                </span>이

                아직도 엊그제처럼 생생해.

                <br><br>

                그때는 손을 잡는 것만으로도
                떨렸는데,

                어느새 너와 함께
                두 번째 생일을 맞이하고 있네.

                <br><br>

                시간이 참 빠르면서도,
                그날의 설렘은 여전히
                그대로인 것 같아.

            </div>

        </section>
        """
    )


    render_html(
        """
        <section class="letter-card">

            <div class="memory-title">
                TO. 예희
            </div>

            <div class="letter-text">

                예희야,<br>

                네가 내 곁에 온 뒤로
                평범했던 하루들이
                조금씩 특별해졌어.

                <br><br>

                앞으로도 네가 웃을 수 있도록,
                지금보다 더 잘해주려고
                계속 노력할게.

                늘 네가 행복했으면 좋겠고,
                나와 함께하는 시간이
                따뜻하고 편안했으면 좋겠어.

                <br><br>

                함께 지내다 보면
                내가 미워지는 날도 있겠지만,

                그런 날이 오더라도
                다시 나를 더 사랑할 수 있도록
                말보다 행동으로 보여줄게.

                <br><br>

                네가 힘든 날에는
                가장 가까운 곳에서 네 편이 되고,

                좋은 날에는 누구보다 크게
                함께 웃어주는 사람이 될게.

                <br><br>

                결국에는 네가 나와 함께 있을 때
                가장 편안하고 행복하다고
                느끼게 해주고 싶어.

                <br><br>

                <span class="highlight">

                    태어나줘서 고마워.<br>

                    우리가 함께 맞는
                    두 번째 생일을
                    진심으로 축하해.

                </span>

            </div>

            <div class="signature">
                오래도록 네 손을 잡고 싶은
                사람으로부터
            </div>

        </section>
        """
    )


    render_html(
        """
        <section class="gallery-title-card">

            <div class="memory-title">
                OUR MEMORIES
            </div>

            <div class="memory-text">
                우리가 함께 지나온 순간들
            </div>

        </section>
        """
    )


    show_photo_carousel()


    render_html(
        """
        <div class="footer-message">
            오늘의 모든 순간이<br>
            예희에게 따뜻한 기억으로 남기를 🎂
        </div>
        """
    )


    st.write("")


    if st.button(
        "처음 화면으로 돌아가기",
        key="go-back",
    ):
        st.session_state.opened = False
        st.rerun()