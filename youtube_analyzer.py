import re
from textwrap import dedent

from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from youtube_transcript_api import YouTubeTranscriptApi


load_dotenv()


# =========================================================
# YOUTUBE VIDEO ID
# =========================================================

def extract_video_id(url: str):

    url = url.strip()

    patterns = [
        r"youtube\.com/watch\?v=([A-Za-z0-9_-]{11})",
        r"youtu\.be/([A-Za-z0-9_-]{11})",
        r"youtube\.com/shorts/([A-Za-z0-9_-]{11})",
        r"youtube\.com/embed/([A-Za-z0-9_-]{11})",
    ]

    for pattern in patterns:

        match = re.search(pattern, url)

        if match:
            return match.group(1)

    raise ValueError(
        "Invalid YouTube URL. Please enter a valid YouTube video link."
    )


# =========================================================
# TIMESTAMP FORMAT
# =========================================================

def format_timestamp(seconds):

    seconds = int(seconds)

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if hours > 0:

        return f"{hours:02d}:{minutes:02d}:{secs:02d}"

    return f"{minutes:02d}:{secs:02d}"


# =========================================================
# FETCH YOUTUBE TRANSCRIPT
# =========================================================

def get_transcript(url):

    video_id = extract_video_id(url)

    youtube_api = YouTubeTranscriptApi()

    transcript = None

    # -----------------------------------------------------
    # Try English / Hindi
    # -----------------------------------------------------

    try:

        transcript = youtube_api.fetch(
            video_id,
            languages=["en", "hi"]
        )

    except Exception:

        # -------------------------------------------------
        # Try whatever transcript is available
        # -------------------------------------------------

        try:

            transcript = youtube_api.fetch(video_id)

        except Exception as e:

            raise Exception(
                f"Could not fetch the YouTube transcript.\n\n{str(e)}"
            )

    # -----------------------------------------------------
    # Convert transcript to raw data
    # -----------------------------------------------------

    raw_data = transcript.to_raw_data()

    if not raw_data:

        raise Exception(
            "No transcript was found for this YouTube video."
        )

    transcript_lines = []

    for item in raw_data:

        start_time = format_timestamp(
            item["start"]
        )

        text = item["text"].strip()

        if text:

            transcript_lines.append(
                f"[{start_time}] {text}"
            )

    transcript_text = "\n".join(
        transcript_lines
    )

    if not transcript_text.strip():

        raise Exception(
            "The YouTube transcript is empty."
        )

    return video_id, transcript_text


# =========================================================
# GROQ AI AGENT
# =========================================================

def build_youtube_agent():

    return Agent(

        name="YouTube Intelligence Agent",

        model=Groq(
            id="openai/gpt-oss-120b"
        ),

        instructions=dedent("""
        You are an expert YouTube content analyst.

        You will receive a YouTube transcript.

        The transcript contains timestamps.

        Analyze ONLY the information available
        in the transcript.

        NEVER invent facts.

        Create a professional, clear and useful
        YouTube analysis.

        Follow this exact structure:

        ## 🎥 Video Overview

        Explain what the video is about
        in a concise and understandable way.

        ## 📚 Main Topics

        List the major topics discussed.

        ## ⏱️ Important Timestamps

        Identify important sections using
        timestamps from the transcript.

        Format:

        - **00:00** — Introduction
        - **02:35** — Main concept
        - **07:42** — Important explanation

        Do NOT invent timestamps.

        ## 💡 Key Takeaways

        Give the most important points
        the viewer should remember.

        ## 🧠 Important Concepts

        Explain the important concepts
        discussed in the video.

        ## 🚀 Practical Insights

        Explain useful practical applications
        of the information.

        Keep the response organized,
        professional and readable.

        Use emojis naturally.

        Do not invent the speaker,
        video duration, statistics,
        facts or metadata that are not
        present in the transcript.
        """),

        markdown=True,

        add_datetime_to_context=True
    )


# =========================================================
# ANALYZE YOUTUBE VIDEO
# =========================================================

def analyze_youtube_video(url):

    # -----------------------------------------------------
    # Get transcript
    # -----------------------------------------------------

    video_id, transcript = get_transcript(
        url
    )

    # -----------------------------------------------------
    # Prevent extremely large prompts
    # -----------------------------------------------------

    max_chars = 60000

    if len(transcript) > max_chars:

        transcript = transcript[:max_chars]

        transcript += (
            "\n\n[Transcript truncated because "
            "the video transcript was very long.]"
        )

    # -----------------------------------------------------
    # Build agent
    # -----------------------------------------------------

    agent = build_youtube_agent()

    # -----------------------------------------------------
    # Send transcript to Groq
    # -----------------------------------------------------

    prompt = f"""
Analyze this YouTube video.

Video ID:
{video_id}

Transcript:

{transcript}

Create the complete analysis using
the required structure.
"""

    response = agent.run(
        prompt
    )

    return response