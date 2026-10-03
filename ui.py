import streamlit as st

from youtube_analyzer import analyze_youtube_video


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="YouTube Intelligence",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# GLOBAL CSS
# =========================================================

st.markdown("""
<style>

* {
    box-sizing: border-box;
}

.stApp {

    background:
        radial-gradient(
            circle at 15% 25%,
            rgba(35, 85, 255, 0.24),
            transparent 30%
        ),

        radial-gradient(
            circle at 85% 25%,
            rgba(130, 45, 255, 0.20),
            transparent 30%
        ),

        radial-gradient(
            circle at 50% 80%,
            rgba(255, 30, 160, 0.18),
            transparent 35%
        ),

        #07080d;

    color: white;

    overflow-x: hidden;
}


/* ---------------------------------------------------------
   HIDE STREAMLIT DEFAULT UI
--------------------------------------------------------- */

header {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* ---------------------------------------------------------
   ANIMATED GLOW
--------------------------------------------------------- */

.stApp::before {

    content: "";

    position: fixed;

    width: 700px;
    height: 700px;

    left: 50%;
    top: 45%;

    transform: translate(-50%, -50%);

    background:

        radial-gradient(
            circle,
            rgba(55, 95, 255, 0.30),
            rgba(180, 45, 210, 0.20),
            rgba(255, 35, 150, 0.12),
            transparent 70%
        );

    filter: blur(90px);

    pointer-events: none;

    z-index: 0;

    animation:
        floatingGlow 12s ease-in-out infinite alternate;
}


@keyframes floatingGlow {

    0% {

        transform:
            translate(-55%, -50%)
            scale(0.90);
    }

    50% {

        transform:
            translate(-40%, -45%)
            scale(1.15);
    }

    100% {

        transform:
            translate(-48%, -55%)
            scale(1);
    }
}


/* ---------------------------------------------------------
   MAIN CONTAINER
--------------------------------------------------------- */

.block-container {

    max-width: 1180px !important;

    padding-top: 45px !important;

    padding-bottom: 80px !important;

    position: relative;

    z-index: 2;
}


/* ---------------------------------------------------------
   INPUT
--------------------------------------------------------- */

div[data-testid="stTextInput"] {

    max-width: 850px;

    margin: 48px auto 0 auto !important;

    padding: 4px !important;

    border-radius: 28px !important;

    background:

        linear-gradient(
            90deg,
            #4169ff,
            #7548ff,
            #b447e8,
            #f044b6
        ) !important;

    background-size: 300% 100%;

    animation:
        inputGradient 6s linear infinite;

    box-shadow:

        0 0 30px rgba(65,105,255,.25),

        0 0 60px rgba(236,72,153,.12);
}


@keyframes inputGradient {

    0% {
        background-position: 0% center;
    }

    50% {
        background-position: 100% center;
    }

    100% {
        background-position: 0% center;
    }
}


div[data-testid="stTextInput"] > div {

    background: #111219 !important;

    border: none !important;

    border-radius: 23px !important;

    padding: 4px 14px !important;
}


div[data-testid="stTextInput"] label {

    display: none !important;
}


div[data-testid="stTextInput"] input {

    height: 55px !important;

    background: transparent !important;

    border: none !important;

    outline: none !important;

    box-shadow: none !important;

    color: white !important;

    font-size: 16px !important;
}


div[data-testid="stTextInput"] input::placeholder {

    color: #777b88 !important;
}


/* ---------------------------------------------------------
   BUTTON
--------------------------------------------------------- */

div.stButton {

    width: 100%;

    display: flex;

    justify-content: center;

    margin-top: 24px;
}


div.stButton > button {

    min-width: 190px;

    height: 52px;

    border: none !important;

    border-radius: 17px !important;

    color: white !important;

    font-size: 16px !important;

    font-weight: 700 !important;

    background:

        linear-gradient(
            135deg,
            #386cff,
            #7348ff,
            #d946ef
        ) !important;

    box-shadow:

        0 10px 35px rgba(80,70,255,.35);

    transition: all .25s ease !important;
}


div.stButton > button:hover {

    transform:

        translateY(-3px)
        scale(1.04);

    box-shadow:

        0 16px 45px rgba(90,70,255,.55),

        0 0 35px rgba(230,60,200,.20);
}


/* ---------------------------------------------------------
   RESULT MARKDOWN
--------------------------------------------------------- */

[data-testid="stMarkdownContainer"] {

    color: #dedee6;
}


[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3 {

    color: white;
}


/* ---------------------------------------------------------
   ALERT
--------------------------------------------------------- */

div[data-testid="stAlert"] {

    border-radius: 16px;
}


/* ---------------------------------------------------------
   MOBILE
--------------------------------------------------------- */

@media (max-width: 800px) {

    .block-container {

        padding: 30px 18px 60px 18px !important;
    }

    .features-grid {

        grid-template-columns: 1fr !important;
    }

    .hero-title {

        font-size: 48px !important;

        letter-spacing: -2px !important;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TOP BADGE
# =========================================================

st.html("""
<div style="
    width:fit-content;
    margin:0 auto 42px auto;
    padding:8px 17px;
    display:flex;
    align-items:center;
    gap:9px;
    border-radius:30px;
    background:rgba(255,255,255,0.055);
    border:1px solid rgba(255,255,255,0.14);
    backdrop-filter:blur(20px);
    color:#d8d8df;
    font-size:14px;
    box-shadow:0 10px 35px rgba(0,0,0,0.25);
">

    <span style="
        padding:6px 12px;
        border-radius:20px;
        color:white;
        font-weight:700;
        font-size:12px;
        background:linear-gradient(90deg,#376dff,#8b5cf6);
        box-shadow:0 0 18px rgba(90,90,255,0.35);
    ">
        ✦ AI POWERED
    </span>

    <span>
        YouTube Intelligence
    </span>

</div>
""")


# =========================================================
# HERO SECTION
# =========================================================

st.html("""
<div style="
    text-align:center;
    position:relative;
    margin:0 auto;
">

    <div style="
        margin:0;
        font-size:clamp(48px,7vw,82px);
        line-height:1.02;
        letter-spacing:-4px;
        font-weight:850;

        background:

            linear-gradient(
                90deg,
                #ffffff,
                #dbe3ff,
                #ffffff,
                #ffc5ed
            );

        background-size:250% auto;

        -webkit-background-clip:text;
        background-clip:text;

        -webkit-text-fill-color:transparent;

        animation:titleMove 7s linear infinite;
    ">

        Understand YouTube.<br>
        Instantly.

    </div>


    <div style="
        max-width:700px;
        margin:25px auto 0 auto;
        color:#999ca8;
        font-size:18px;
        line-height:1.7;
    ">

        Turn any YouTube video into structured insights,
        key takeaways, timestamps and actionable knowledge
        with AI.

    </div>

</div>


<style>

@keyframes titleMove {

    0% {
        background-position:0% center;
    }

    100% {
        background-position:250% center;
    }

}

</style>
""")


# =========================================================
# YOUTUBE URL
# =========================================================

video_url = st.text_input(
    "YouTube URL",
    placeholder="🔗  Paste your YouTube video link here..."
)


# =========================================================
# ANALYZE BUTTON
# =========================================================

analyze = st.button(
    "✨  Analyze Video"
)


# =========================================================
# FEATURE CARDS
# =========================================================

st.html("""
<div class="features-grid" style="
    max-width:980px;
    margin:70px auto 0 auto;

    display:grid;
    grid-template-columns:repeat(3,1fr);

    gap:20px;
">


    <!-- CARD 1 -->

    <div style="
        min-height:185px;
        padding:28px;
        border-radius:24px;

        background:rgba(255,255,255,0.045);

        border:1px solid rgba(255,255,255,0.085);

        backdrop-filter:blur(25px);

        transition:all .3s ease;
    "

    onmouseover="
        this.style.transform='translateY(-7px)';
        this.style.background='rgba(255,255,255,0.07)';
        this.style.borderColor='rgba(125,115,255,0.38)';
    "

    onmouseout="
        this.style.transform='translateY(0)';
        this.style.background='rgba(255,255,255,0.045)';
        this.style.borderColor='rgba(255,255,255,0.085)';
    ">


        <div style="
            font-size:30px;
            margin-bottom:20px;
        ">
            🧠
        </div>


        <div style="
            font-size:18px;
            font-weight:750;
            color:white;
            margin-bottom:10px;
        ">
            AI Analysis
        </div>


        <div style="
            color:#8d919e;
            font-size:14px;
            line-height:1.6;
        ">
            Let AI understand the video's content
            and generate meaningful insights.
        </div>

    </div>



    <!-- CARD 2 -->

    <div style="
        min-height:185px;
        padding:28px;
        border-radius:24px;

        background:rgba(255,255,255,0.045);

        border:1px solid rgba(255,255,255,0.085);

        backdrop-filter:blur(25px);

        transition:all .3s ease;
    "

    onmouseover="
        this.style.transform='translateY(-7px)';
        this.style.background='rgba(255,255,255,0.07)';
        this.style.borderColor='rgba(125,115,255,0.38)';
    "

    onmouseout="
        this.style.transform='translateY(0)';
        this.style.background='rgba(255,255,255,0.045)';
        this.style.borderColor='rgba(255,255,255,0.085)';
    ">


        <div style="
            font-size:30px;
            margin-bottom:20px;
        ">
            ⏱️
        </div>


        <div style="
            font-size:18px;
            font-weight:750;
            color:white;
            margin-bottom:10px;
        ">
            Smart Timestamps
        </div>


        <div style="
            color:#8d919e;
            font-size:14px;
            line-height:1.6;
        ">
            Quickly identify important sections
            and navigate through the video.
        </div>

    </div>



    <!-- CARD 3 -->

    <div style="
        min-height:185px;
        padding:28px;
        border-radius:24px;

        background:rgba(255,255,255,0.045);

        border:1px solid rgba(255,255,255,0.085);

        backdrop-filter:blur(25px);

        transition:all .3s ease;
    "

    onmouseover="
        this.style.transform='translateY(-7px)';
        this.style.background='rgba(255,255,255,0.07)';
        this.style.borderColor='rgba(125,115,255,0.38)';
    "

    onmouseout="
        this.style.transform='translateY(0)';
        this.style.background='rgba(255,255,255,0.045)';
        this.style.borderColor='rgba(255,255,255,0.085)';
    ">


        <div style="
            font-size:30px;
            margin-bottom:20px;
        ">
            💡
        </div>


        <div style="
            font-size:18px;
            font-weight:750;
            color:white;
            margin-bottom:10px;
        ">
            Key Takeaways
        </div>


        <div style="
            color:#8d919e;
            font-size:14px;
            line-height:1.6;
        ">
            Extract the most valuable concepts
            without watching the entire video.
        </div>

    </div>


</div>
""")


# =========================================================
# ANALYZE VIDEO
# =========================================================

if analyze:

    # -----------------------------------------------------
    # EMPTY INPUT
    # -----------------------------------------------------

    if not video_url.strip():

        st.warning(
            "⚠️ Please paste a YouTube video URL first."
        )

    else:

        # -------------------------------------------------
        # RESULT HEADING
        # -------------------------------------------------

        st.html("""
        <div style="
            max-width:1050px;
            margin:65px auto 20px auto;
            padding:25px 30px;

            border-radius:24px;

            background:rgba(14,15,21,0.82);

            border:1px solid rgba(255,255,255,0.10);

            backdrop-filter:blur(30px);

            display:flex;
            justify-content:space-between;
            align-items:center;
        ">

            <div style="
                color:white;
                font-size:25px;
                font-weight:750;
            ">
                🤖 AI Video Analysis
            </div>


            <div style="
                padding:7px 13px;
                border-radius:20px;

                color:#bdb6ff;

                background:rgba(100,80,255,0.13);

                border:1px solid rgba(130,110,255,0.28);

                font-size:12px;

                font-weight:600;
            ">
                GROQ • LIVE
            </div>

        </div>
        """)


        # -------------------------------------------------
        # AI ANALYSIS
        # -------------------------------------------------

        with st.spinner(
            "🧠 Fetching transcript and analyzing video..."
        ):

            try:

                response = analyze_youtube_video(
                    video_url
                )


                # -------------------------------------------------
                # RESULT
                # -------------------------------------------------

                st.markdown(
                    response.content
                )


                st.success(
                    "✨ Video analysis completed successfully!"
                )


            except Exception as e:

                st.error(
                    "❌ Unable to analyze this YouTube video."
                )

                st.caption(
                    f"Error details: {str(e)}"
                )