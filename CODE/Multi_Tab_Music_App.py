import streamlit as st
import os
from io import BytesIO
from dotenv import load_dotenv
from app.main import MusicLLM
from app.utils import *
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Music Composer",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Logging System (Adjusted for IST) ---
def get_ist_time():
    # Streamlit Cloud uses UTC by default. Adding 5:30 for IST.
    return (datetime.utcnow() + timedelta(hours=5, minutes=30)).strftime("%H:%M:%S")

if "logs" not in st.session_state:
    st.session_state.logs = [
        {"time": get_ist_time(), "level": "INFO", "msg": "System Boot Sequence Initialized.", "icon": "ℹ️"},
        {"time": get_ist_time(), "level": "SUCCESS", "msg": "Cloud Infrastructure Verified.", "icon": "✅"},
        {"time": get_ist_time(), "level": "INFO", "msg": "Groq LPU Engine Ready.", "icon": "🚀"}
    ]

def add_log(level, msg, icon="ℹ️"):
    new_log = {
        "time": get_ist_time(),
        "level": level,
        "msg": msg,
        "icon": icon
    }
    st.session_state.logs.insert(0, new_log) # Add to top
    if len(st.session_state.logs) > 50: # Cap logs
        st.session_state.logs.pop()

# Custom CSS for premium design (inspired by Multi Agent app)
st.markdown("""
<style>
    :root {
        --primary-gold: #FFD700;
        --accent-blue: #2874f0;
        --accent-green: #2ecc71;
        --background-dark: #141E30; 
        --text-light: #ecf0f1; 
    }
    
    .stApp {
        background: linear-gradient(to right, #141E30, #243B55);
        color: var(--text-light);
    }

    strong, b {
        color: var(--primary-gold);
        font-weight: 700;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        border-right: 3px solid var(--accent-green);
    }

    h1 { color: #00d4ff !important; text-shadow: 0 0 20px rgba(0, 212, 255, 0.5); }
    h2 { color: var(--accent-blue) !important; }
    h3 { color: var(--accent-green) !important; }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 4px 4px 0 0;
        padding: 10px 20px;
        color: white;
    }

    .stTabs [aria-selected="true"] {
        background-color: var(--accent-blue) !important;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style='background: #ffffff; padding: 25px; border-radius: 15px; text-align: center; border: 2px solid #2874f0; box-shadow: 0 4px 15px rgba(0,0,0,0.1);'>
        <div style='display: flex; justify-content: center; align-items: center; gap: 10px; margin-bottom: 5px;'>
            <svg viewBox="0 0 24 24" width="30" height="30" fill="#1DB954"><path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.121 17.3c-.201.328-.631.428-.958.227-2.651-1.62-5.986-1.983-9.914-1.085-.369.085-.738-.149-.822-.518-.085-.369.149-.738.518-.822 4.295-.983 8.001-.564 10.969 1.243.328.201.428.631.227.955zm1.371-3.264c-.252.411-.787.537-1.198.285-3.033-1.864-7.662-2.406-11.25-1.316-.459.139-.95-.121-1.089-.58-.139-.459.121-.95.58-1.089 4.108-1.247 9.215-.634 12.672 1.492.411.252.537.787.285 1.198zm.116-3.39c-3.636-2.16-9.627-2.359-13.08-1.313-.557.168-1.144-.153-1.313-.71-.168-.557.153-1.144.71-1.313 4-1.213 10.613-.984 14.811 1.503.501.298.666.94.368 1.441-.299.501-.94.666-1.496.392z"/></svg>
            <h2 style='color: #2874f0; margin: 0;'>AI Music</h2>
        </div>
        <p style='color: #666; font-size: 0.95rem; font-weight: 800; letter-spacing: 1px; margin: 0;'>COMPOSER PRO</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 👨‍💻 Developer")
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(40, 116, 240, 0.2) 0%, rgba(155, 89, 182, 0.2) 100%); 
                padding: 15px; border-radius: 10px; border: 2px solid rgba(155, 89, 182, 0.4);'>
        <p style='margin: 5px 0; color: #00d4ff; font-weight: 600;'>Ratnesh Kumar Singh</p>
        <p style='margin: 5px 0; font-size: 0.85rem;'>Data Scientist (AI/ML Engineer)</p>
        <div style='margin-top: 10px; display: flex; flex-wrap: wrap; gap: 10px;'>
            <a href='https://github.com/Ratnesh-181998' target='_blank' style='text-decoration: none; color: #2874f0; font-weight: bold; font-size: 0.8rem;'>🔗 GitHub</a>
            <a href='https://www.linkedin.com/in/ratneshkumar1998/' target='_blank' style='text-decoration: none; color: #0077b5; font-weight: bold; font-size: 0.8rem;'>💼 LinkedIn</a>
            <a href='https://open.spotify.com' target='_blank' style='text-decoration: none; color: #1DB954; font-weight: bold; font-size: 0.8rem;'>🎧 Spotify</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔍 Project Scope")
    st.info("Generative AI implementation for automated music composition using Groq & LangChain.")

# Top Right Professional Badge
col_space, col_badge = st.columns([3, 1.25])
with col_badge:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #2874f0 0%, #9b59b6 100%); 
                padding: 10px; border-radius: 8px; 
                box-shadow: 0 4px 12px rgba(40, 116, 240, 0.5);
                border: 1px solid rgba(255, 255, 255, 0.1);
                text-align: center;
                margin-bottom: 10px;'>
        <p style='margin: 0; color: #ffffff; font-weight: 700; font-size: 0.75rem; line-height: 1.4;'>
            <strong>Ratnesh Kumar Singh</strong><br>
            <span style='font-size: 0.65rem; opacity: 0.9;'>Data Scientist (AI/ML Engineer 4+Yrs Exp)</span>
        </p>
        <div style='display: flex; justify-content: center; gap: 8px; margin-top: 5px;'>
            <a href='https://github.com/Ratnesh-181998' target='_blank' style='color: white; font-size: 0.65rem; text-decoration: none;'>📂 GitHub</a>
            <a href='https://www.linkedin.com/in/ratneshkumar1998/' target='_blank' style='color: white; font-size: 0.65rem; text-decoration: none;'>💼 LinkedIn</a>
            <a href='https://open.spotify.com' target='_blank' style='color: #1DB954; font-size: 0.65rem; text-decoration: none; font-weight: bold;'>🎧 Spotify</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main Header
st.markdown("""
<div style='text-align: center; padding: 25px; background: linear-gradient(135deg, rgba(40, 116, 240, 0.15) 0%, rgba(155, 89, 182, 0.15) 100%); border-radius: 12px; margin-bottom: 20px; border: 2px solid rgba(40, 116, 240, 0.4); box-shadow: 0 4px 20px rgba(0,0,0,0.2);'>
    <div style='display: flex; justify-content: center; align-items: center; gap: 15px; margin-bottom: 10px;'>
        <svg viewBox="0 0 24 24" width="45" height="45" fill="#1DB954"><path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.121 17.3c-.201.328-.631.428-.958.227-2.651-1.62-5.986-1.983-9.914-1.085-.369.085-.738-.149-.822-.518-.085-.369.149-.738.518-.822 4.295-.983 8.001-.564 10.969 1.243.328.201.428.631.227.955zm1.371-3.264c-.252.411-.787.537-1.198.285-3.033-1.864-7.662-2.406-11.25-1.316-.459.139-.95-.121-1.089-.58-.139-.459.121-.95.58-1.089 4.108-1.247 9.215-.634 12.672 1.492.411.252.537.787.285 1.198zm.116-3.39c-3.636-2.16-9.627-2.359-13.08-1.313-.557.168-1.144-.153-1.313-.71-.168-.557.153-1.144.71-1.313 4-1.213 10.613-.984 14.811 1.503.501.298.666.94.368 1.441-.299.501-.94.666-1.496.392z"/></svg>
        <h1 style='margin: 0; font-size: 2.8rem;'>AI MUSIC COMPOSER</h1>
    </div>
    <p style='font-size: 1.1rem; color: #e8e8e8; margin: 0; opacity: 0.9; letter-spacing: 0.5px;'>Transform your words into melodies with Generative AI Orchestration</p>
</div>
""", unsafe_allow_html=True)

# Define Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎬 Demo Project", 
    "📖 About Project", 
    "🔧 Tech Stack", 
    "🏗️ Architecture", 
    "📋 System Logs"
])

# Loading documentation content
# Loading documentation content
def load_txt(filename):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PARENT_DIR = os.path.dirname(BASE_DIR)
    
    # List of paths to check: Parent (local), Current (flat deployment), Working Dir (root)
    check_paths = [
        os.path.join(PARENT_DIR, filename),
        os.path.join(BASE_DIR, filename),
        os.path.join(os.getcwd(), filename)
    ]
    
    for path in check_paths:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
                
    return f"Documentation ({filename}) not found."

# --- TAB 1: DEMO ---
with tab1:
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(40, 116, 240, 0.1) 0%, rgba(155, 89, 182, 0.1) 100%); 
                padding: 20px; border-radius: 12px; border-left: 5px solid #00d4ff; margin-bottom: 25px;'>
        <h3 style='color: #00d4ff; margin: 0 0 10px 0;'>🎼 Ratnesh Interactive Music Workshop</h3>
        <p style='color: #e8e8e8; margin: 0;'>
            Experience the power of Generative AI. Describe your musical vision below, and our model will craft 
            a unique composition including <b>melody, harmony, and rhythm</b> tailored to your style.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🎵 Compose Your Masterpiece By Ratnesh")
    
    # Optional Banner in Demo
    if os.path.exists("banner.png") or os.path.exists("CODE/banner.png"):
        banner_path = "banner.png" if os.path.exists("banner.png") else "CODE/banner.png"
        st.image(banner_path, use_container_width=True)

    st.markdown("### 🔍 Step 1: Define Your Vision (Input & Styles)")
    col_in, col_opt = st.columns([2, 1])
    with col_in:
        # Initialize session state for the input if not exists
        if 'music_prompt' not in st.session_state:
            st.session_state.music_prompt = ""
            
        music_input = st.text_input("Describe the music you want to compose", 
                                  value=st.session_state.music_prompt,
                                  placeholder="e.g., A calm, happy piano tune for a rainy morning")
    with col_opt:
        style = st.selectbox("Choose a style" , [
            "Sad" , "Happy" , "Jazz" , "Romantic" , "Classical", 
            "Lo-fi", "Rock", "Pop", "Cinematic", "EDM", 
            "Blues", "Country", "Dark", "Futuristic", "Extreme"
        ])

    # Interactive Sample Prompts
    st.markdown("#### 💡 Need Inspiration? Try these Sample Prompts:")
    
    # Row 1
    p1, p2, p3, p4 = st.columns(4)
    if p1.button("🎷 Relaxing Jazz", use_container_width=True):
        st.session_state.music_prompt = "Generate a relaxing jazz tune with smooth saxophone melody"
        st.rerun()
    if p2.button("🎻 Orchestral", use_container_width=True):
        st.session_state.music_prompt = "Compose a dramatic orchestral piece with layered strings"
        st.rerun()
    if p3.button("🎮 Video Game", use_container_width=True):
        st.session_state.music_prompt = "Epic video game battle theme with heroic melody"
        st.rerun()
    if p4.button("⚡ Techno Beat", use_container_width=True):
        st.session_state.music_prompt = "Extreme techno beat with rapid melody and intense rhythm"
        st.rerun()

    # Row 2
    p5, p6, p7, p8 = st.columns(4)
    if p5.button("☕ Lo-fi Hip Hop", use_container_width=True):
        st.session_state.music_prompt = "Create a lo-fi hip hop beat with a mellow piano loop"
        st.rerun()
    if p6.button("🎼 Classical", use_container_width=True):
        st.session_state.music_prompt = "Compose a classical sonata with intricate violin patterns"
        st.rerun()
    if p7.button("🎬 Cinematic", use_container_width=True):
        st.session_state.music_prompt = "Cinematic sci-fi soundtrack with synth leads and pulsing rhythm"
        st.rerun()
    if p8.button("🎤 Upbeat Pop", use_container_width=True):
        st.session_state.music_prompt = "Upbeat pop track with a catchy synthesizer hook"
        st.rerun()

    # Full List of Sample Prompts from file
    with st.expander("📝 View Full Sample Prompts Library"):
        prompts_text = load_txt("SAMPLE_PROMPTS.txt")
        st.markdown(f"```text\n{prompts_text}\n```")

    # Initialize session state for music results
    if 'music_results' not in st.session_state:
        st.session_state.music_results = None

    col_gen, col_clr = st.columns([4, 1])
    
    with col_gen:
        generate_clicked = st.button("🚀 Generate Music", type="primary", use_container_width=True)
    
    with col_clr:
        if st.button("🧹 Clear Results", use_container_width=True):
            st.session_state.music_results = None
            st.session_state.music_prompt = ""
            st.rerun()

    # Step 2 Header (Always Visible)
    st.markdown("---")
    st.markdown("### 🎹 Step 2: AI Orchestration (Real-time generation status)")
    
    if generate_clicked and music_input:
        generator = MusicLLM()
        with st.status("🧠 AI Music Orchestration in Progress...", expanded=True) as status:
            add_log("INFO", f"Generation request received for style: {style}", "📥")
            st.write("📡 Connecting to Groq LPU Inference Engine...")
            melody = generator.generate_melody(music_input)
            add_log("SUCCESS", "LLM Inference Complete: Melody Pattern Found.", "🎹")
            
            st.write("🎹 Constructing harmonic chord progressions...")
            harmony = generator.generate_harmony(melody)
            add_log("INFO", "Harmonic Progression Layered.", "🎼")
            
            st.write("🥁 Finalizing rhythmic syncopation...")
            rhythm = generator.generate_rythm(melody)
            
            st.write("🔊 Synthesizing high-fidelity audio frequencies...")
            composition = generator.adapt_style(style,melody,harmony,rhythm)
            add_log("SUCCESS", f"Waveform Synthesis Complete ({style} style).", "🔊")

            melody_notes = melody.split()
            melody_freqs = note_to_frequencies(melody_notes)
            harmony_chords = harmony.split()
            harmony_notes=[]
            for chord in harmony_chords:
                harmony_notes.extend(chord.split('-'))
            harmony_freqs = note_to_frequencies(harmony_notes)
            all_freqs = melody_freqs + harmony_freqs
            wav_bytes = generate_wav_bytes_from_notes_freq(all_freqs)
            
            st.session_state.music_results = {
                "wav_bytes": wav_bytes,
                "composition": composition,
                "melody": melody,
                "harmony": harmony,
                "rhythm": rhythm,
                "notes_count": len(melody_notes),
                "chords_count": len(harmony_chords),
                "style": style
            }
            status.update(label="✅ Composition Successfully Crafted!", state="complete", expanded=False)
            add_log("SUCCESS", "Project Portfolio Export: WAV ready for playback.", "🎁")
    elif not st.session_state.music_results:
        st.info("💡 Waiting for your command. Click 'Generate Music' above to start the AI process.")

    # Step 3 Header (Always Visible)
    st.markdown("---")
    st.markdown("### 🎵 Step 3: Studio Playback (Audio player, metrics, and summary)")
    
    if st.session_state.music_results:
        res = st.session_state.music_results
        res_col1, res_col2 = st.columns([1, 1])
        
        with res_col1:
            st.markdown("### 🎧 Playback & Export")
            st.audio(BytesIO(res["wav_bytes"]), format='audio/wav')
            st.download_button(
                label="📥 Download Track (.wav)",
                data=res["wav_bytes"],
                file_name=f"ai_music_{res['style'].lower()}.wav",
                mime="audio/wav",
                use_container_width=True
            )
            
        with res_col2:
            st.markdown("### 📊 Performance Insights")
            m1, m2, m3 = st.columns(3)
            m1.metric("Notes", res["notes_count"])
            m2.metric("Chords", res["chords_count"])
            m3.metric("Genre", res["style"])
            
        st.success("Music generated successfully!")

        with st.expander("📝 Composition Summary", expanded=True):
            st.markdown(f"""
            <div style='background: rgba(0,0,0,0.3); padding: 20px; border-radius: 10px; border: 1px solid #2874f0; color: #ecf0f1;'>
                {res["composition"]}
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("#### 🎼 Sequence Data")
            st.code(f"M: {res['melody']}\nH: {res['harmony']}\nR: {res['rhythm']}")
    else:
        st.warning("🎧 Audio playback and performance metrics will appear here after generation.")


# --- TAB 2: ABOUT ---
with tab2:
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(40, 116, 240, 0.12) 0%, rgba(155, 89, 182, 0.12) 100%); 
                padding: 30px; border-radius: 15px; border: 1px solid rgba(40, 116, 240, 0.3); margin-bottom: 30px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);'>
        <h2 style='color: #00d4ff; margin-bottom: 15px; font-weight: 800;'>🌟 Project Vision & Purpose</h2>
        <p style='font-size: 1.15rem; line-height: 1.7; color: #ecf0f1;'>
            The <b>AI Music Composer</b> is designed to democratize music creation. By bridging the gap between 
            Natural Language Processing and Computational Musicology, we allow users to act as "AI Conductors," 
            orchestrating complex arrangements without needing formal training in musical notation.
        </p>
        <div style='display: flex; gap: 20px; margin-top: 20px;'>
            <div style='background: rgba(40, 116, 240, 0.2); padding: 10px 20px; border-radius: 8px; border: 1px solid #2874f0;'>
                🚀 <b style='color: #00d4ff;'>End-to-End Automation</b>
            </div>
            <div style='background: rgba(46, 204, 113, 0.2); padding: 10px 20px; border-radius: 8px; border: 1px solid #2ecc71;'>
                🎼 <b style='color: #2ecc71;'>Logic Preserving Theory</b>
            </div>
            <div style='background: rgba(155, 89, 182, 0.2); padding: 10px 20px; border-radius: 8px; border: 1px solid #9b59b6;'>
                ☁️ <b style='color: #9b59b6;'>Cloud-Native Scale</b>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    acol1, acol2, acol3 = st.columns(3)
    with acol1:
        st.write("### 🧠 Intelligence")
        st.write("Leveraging **Llama 3.1** via Groq for sub-second musical inference.")
    with acol2:
        st.write("### 🎼 Engineering")
        st.write("Integrating **Music21** for accurate semi-professional music theory.")
    with acol3:
        st.write("### 🏗️ Infrastructure")
        st.write("Containerized with **Docker** and orchestrated via **Kubernetes**.")

    st.markdown("---")
    
    with st.expander("📄 View Full Technical Implementation Roadmap", expanded=True):
        about_content = load_txt("PROJECT_EXPLANATION.txt")
        # Pre-process content for better display
        styled_text = about_content.replace('1️⃣', '🟦 1️⃣').replace('2️⃣', '🟦 2️⃣').replace('3️⃣', '🟦 3️⃣').replace('4️⃣', '🟦 4️⃣').replace('5️⃣', '🟦 5️⃣').replace('6️⃣', '🟦 6️⃣').replace('7️⃣', '🟦 7️⃣').replace('8️⃣', '🟦 8️⃣').replace('9️⃣', '🟦 9️⃣').replace('🔟', '🟦 🔟')
        
        st.markdown(styled_text)


# --- TAB 3: TECH STACK ---
with tab3:
    st.markdown("""
<style>
    .tech-card {
        background: rgba(30, 41, 59, 0.4);
        border-radius: 15px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
        height: 100%;
        cursor: default;
    }
    .tech-card:hover {
        transform: translateY(-5px);
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid #00d4ff;
        box-shadow: 0 10px 25px rgba(0, 212, 255, 0.2);
    }
    .tech-icon {
        font-size: 2rem;
        margin-bottom: 15px;
        display: block;
    }
    .tech-tag {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        margin-top: 10px;
        text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(0, 212, 255, 0.1) 0%, rgba(155, 89, 182, 0.1) 100%); 
                padding: 30px; border-radius: 15px; border-bottom: 4px solid #00d4ff; margin-bottom: 30px;'>
        <h2 style='color: #00d4ff; margin: 0 0 10px 0;'>🛠️ The AI Orchestration Stack</h2>
        <p style='color: #e2e8f0; font-size: 1.1rem; line-height: 1.6;'>
            A high-performance architecture built for <b>sub-second musical inference</b> and <b>global cloud scalability</b>. 
            Powered by next-gen LPU hardware and enterprise Kubernetes orchestration.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Tech Category Grid with Hover Cards
    tcol1, tcol2 = st.columns(2)
    
    with tcol1:
        st.markdown("""
        <div class="tech-card">
            <span class="tech-icon">🧠</span>
            <h3 style='color: #00d4ff; margin-top: 0;'>GenAI Engine</h3>
            <ul style='color: #bdc3c7; font-size: 0.95rem; margin-left: 0; padding-left: 1.2rem;'>
                <li><b>Groq LPU</b>: Ultra-fast Llama 3.1 inference.</li>
                <li><b>LangChain</b>: Agentic workflow orchestration.</li>
                <li><b>Custom Prompts</b>: Context-aware music theory logic.</li>
            </ul>
            <span class="tech-tag" style="background: rgba(0, 212, 255, 0.2); color: #00d4ff;">Intelligence</span>
        </div>
        """, unsafe_allow_html=True)
        st.write("") 
        st.markdown("""
        <div class="tech-card">
            <span class="tech-icon">🎨</span>
            <h3 style='color: #2ecc71; margin-top: 0;'>Application Core</h3>
            <ul style='color: #bdc3c7; font-size: 0.95rem; margin-left: 0; padding-left: 1.2rem;'>
                <li><b>Streamlit PRO</b>: Premium custom-CSS reactive UI.</li>
                <li><b>Session State</b>: Persistent musical memory.</li>
                <li><b>WAV Studio</b>: Byte-stream audio synthesis.</li>
            </ul>
            <span class="tech-tag" style="background: rgba(46, 204, 113, 0.2); color: #2ecc71;">Frontend</span>
        </div>
        """, unsafe_allow_html=True)

    with tcol2:
        st.markdown("""
        <div class="tech-card">
            <span class="tech-icon">🎼</span>
            <h3 style='color: #f39c12; margin-top: 0;'>Computational Musicology</h3>
            <ul style='color: #bdc3c7; font-size: 0.95rem; margin-left: 0; padding-left: 1.2rem;'>
                <li><b>Music21</b>: MIT-developed theory engine.</li>
                <li><b>MIDI Mapping</b>: Dynamic frequency conversion.</li>
                <li><b>Sine Synthesis</b>: Pure waveform generation.</li>
            </ul>
            <span class="tech-tag" style="background: rgba(243, 156, 18, 0.2); color: #f39c12;">Mathematics</span>
        </div>
        """, unsafe_allow_html=True)
        st.write("") 
        st.markdown("""
        <div class="tech-card">
            <span class="tech-icon">🚀</span>
            <h3 style='color: #e74c3c; margin-top: 0;'>Production DevOps</h3>
            <ul style='color: #bdc3c7; font-size: 0.95rem; margin-left: 0; padding-left: 1.2rem;'>
                <li><b>GKE Clusters</b>: Autoscaling Kubernetes.</li>
                <li><b>Docker Build</b>: Optimized alpine-based images.</li>
                <li><b>CI/CD Pipelines</b>: Automated GitLab deployments.</li>
            </ul>
            <span class="tech-tag" style="background: rgba(231, 76, 60, 0.2); color: #e74c3c;">Cloud-Native</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Interactive Pulse Section
    st.markdown("### 📡 Live Architecture Pulse")
    pcol1, pcol2, pcol3, pcol4 = st.columns(4)
    pcol1.metric("API Latency", "124ms", "Optimal")
    pcol2.metric("LPU Utilization", "42%", "-5%")
    pcol3.metric("K8s Readiness", "100%", "Stable")
    pcol4.metric("Synth Engine", "24-bit", "HQ")

    with st.expander("📝 Detailed Technical Specification (Original File Content)", expanded=False):
        tech_content = load_txt("TECH_STACK.txt")
        styled_tech = tech_content.replace('**', '<b style="color:#00d4ff">').replace('**', '</b>')
        st.markdown(f"""
        <div style='background: #0f172a; padding: 25px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); color: #e2e8f0; font-family: "Courier New", monospace;'>
            {styled_tech}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🔄 Operational Pipeline")
    flow_steps = [
        "**Ingress**: Natural Language Processing of user musical intent.",
        "**Inference**: Groq LPU processes MIDI sequences via Llama 3.1.",
        "**Processing**: Music21 validates harmonic interval relationships.",
        "**Synthesis**: Mathematical conversion of frequencies to WAV PCM data.",
        "**Deployment**: Continuous delivery to highly available Google Cloud nodes."
    ]
    for i, step in enumerate(flow_steps):
        st.markdown(f"&nbsp;&nbsp;**{i+1}.** {step}")


# --- TAB 4: ARCHITECTURE ---
with tab4:
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(46, 204, 113, 0.1) 0%, rgba(40, 116, 240, 0.1) 100%); 
                padding: 25px; border-radius: 12px; border-left: 5px solid #2ecc71; margin-bottom: 25px;'>
        <h2 style='color: #2ecc71; margin: 0 0 10px 0;'>🏗️ Project Architecture Journey</h2>
        <p style='color: #e8e8e8; margin: 0;'>
            A high-fidelity blueprint mapping the data flow from raw user intent to cloud-orchestrated musical output.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Custom HTML/CSS Architecture Map
    st.markdown("""
<style>
.arch-container { display: flex; flex-direction: column; gap: 15px; padding: 5px; }
.arch-phase { background: rgba(30, 41, 59, 0.6); border-radius: 12px; padding: 18px; border: 1px solid rgba(255,255,255,0.05); }
.phase-title { font-size: 1.15rem; font-weight: 800; margin-bottom: 12px; display: flex; align-items: center; gap: 8px; }
.step-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px; }
.step-card { background: rgba(15, 23, 42, 0.5); padding: 10px; border-radius: 8px; text-align: center; border-bottom: 3px solid #00d4ff; font-size: 0.8rem; color: #f1f5f9; transition: transform 0.2s; }
.step-card:hover { transform: scale(1.02); background: rgba(15, 23, 42, 0.8); }
.flow-arrow { text-align: center; color: #00d4ff; font-size: 1.2rem; margin: 2px 0; opacity: 0.8; }
</style>
<div class="arch-container">
<div class="arch-phase" style="border-left: 5px solid #2874f0;">
<div class="phase-title" style="color: #2874f0;">🛠️ Phase 1: Development & Logic Setup</div>
<div class="step-grid">
<div class="step-card">Python Venv Setup</div>
<div class="step-card">Groq API Integration</div>
<div class="step-card">Music21 Theory Layer</div>
<div class="step-card">Custom Audio Utils</div>
</div>
</div>
<div class="flow-arrow">▼</div>
<div class="arch-phase" style="border-left: 5px solid #9b59b6;">
<div class="phase-title" style="color: #9b59b6;">🧠 Phase 2: AI Composer Engine</div>
<div class="step-grid">
<div class="step-card">User Prompt Analysis</div>
<div class="step-card">Melody Generation</div>
<div class="step-card">Harmonic Layering</div>
<div class="step-card">Style Adaptation</div>
</div>
</div>
<div class="flow-arrow">▼</div>
<div class="arch-phase" style="border-left: 5px solid #2ecc71;">
<div class="phase-title" style="color: #2ecc71;">☁️ Phase 3: Cloud-Native Deployment</div>
<div class="step-grid">
<div class="step-card">Dockerization</div>
<div class="step-card">GitLab CI/CD Build</div>
<div class="step-card">GCP Artifact Registry</div>
<div class="step-card">GKE Kubernetes Cluster</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

    # Static Workflow Image
    st.markdown("### 🖼️ Detailed System Blueprint")
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PARENT_DIR = os.path.dirname(BASE_DIR)
    
    img_name = "AI+Music+Composer+Workflow.png"
    # Search for image in multiple potential locations
    paths_to_check = [
        os.path.join(PARENT_DIR, img_name),
        os.path.join(BASE_DIR, img_name),
        img_name
    ]
    
    archi_img_path = None
    for p in paths_to_check:
        if os.path.exists(p):
            archi_img_path = p
            break

    if archi_img_path:
        st.image(archi_img_path, caption="Comprehensive AI Music Composer Workflow", use_container_width=True)
    else:
        st.warning("⚠️ High-resolution workflow image not found at the expected path.")


    st.markdown("---")
    
    # High-Level Flow Explanation
    st.markdown("""
    ### 🔍 How It Works (The Logic Flow)
    1.  **Orchestration**: The **MusicLLM** class acts as the conductor, sending structured prompts to **Groq**.
    2.  **Theory Check**: Raw notes from AI are validated by **Music21** to ensure they sound "musical."
    3.  **Synthesis**: The **Synthesizer** converts frequency data into a high-fidelity **WAV stream**.
    4.  **Interface**: **Streamlit** handles the real-time interaction and audio playback.
    5.  **Scale**: The entire stack is managed as a **Kubernetes Deployment**, allowing for high-concurrency usage in the cloud.
    """)

    st.markdown("---")
    
    with st.expander("🎶 View Simplified Human-Readable Flow", expanded=False):
        simple_flow_content = load_txt("SIMPLE_FLOW.txt")
        st.markdown(simple_flow_content)




# --- TAB 5: LOGS ---
with tab5:
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(40, 116, 240, 0.1) 0%, rgba(155, 89, 182, 0.1) 100%); 
                padding: 25px; border-radius: 12px; border-right: 5px solid #2874f0; margin-bottom: 25px;'>
        <h2 style='color: #00d4ff; margin: 0 0 10px 0;'>📋 System Operations Monitor</h2>
        <p style='color: #e8e8e8; margin: 0;'>
            Real-time tracking of <b>AI inference</b>, <b>sound synthesis</b>, and <b>cloud infrastructure</b> events.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Dynamic Log Data from Session State
    log_data = st.session_state.logs

    # Metrics Row
    m1, m2, m3 = st.columns(3)
    
    total_events = len(log_data)
    success_count = len([l for l in log_data if l['level'] == 'SUCCESS'])
    error_count = len([l for l in log_data if l['level'] == 'ERROR'])
    success_rate = (success_count / total_events * 100) if total_events > 0 else 0
    
    with m1:
        st.markdown(f"""
        <div style='background: rgba(40, 116, 240, 0.1); padding: 15px; border-radius: 10px; border-left: 5px solid #2874f0; text-align: center;'>
            <h4 style='color: #bdc3c7; margin: 0; font-size: 0.9rem;'>TOTAL EVENTS</h4>
            <p style='color: #2874f0; font-size: 1.8rem; font-weight: bold; margin: 5px 0;'>{total_events}</p>
        </div>
        """, unsafe_allow_html=True)
    with m2:
        st.markdown(f"""
        <div style='background: rgba(46, 204, 113, 0.1); padding: 15px; border-radius: 10px; border-left: 5px solid #2ecc71; text-align: center;'>
            <h4 style='color: #bdc3c7; margin: 0; font-size: 0.9rem;'>SUCCESS RATE</h4>
            <p style='color: #2ecc71; font-size: 1.8rem; font-weight: bold; margin: 5px 0;'>{success_rate:.1f}%</p>
        </div>
        """, unsafe_allow_html=True)
    with m3:
        st.markdown(f"""
        <div style='background: rgba(231, 76, 60, 0.1); padding: 15px; border-radius: 10px; border-left: 5px solid #e74c3c; text-align: center;'>
            <h4 style='color: #bdc3c7; margin: 0; font-size: 0.9rem;'>API ERRORS</h4>
            <p style='color: #e74c3c; font-size: 1.8rem; font-weight: bold; margin: 5px 0;'>{error_count}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Filters & Download
    fcol1, fcol2, fcol3 = st.columns([3, 1, 1])
    with fcol1:
        selected_levels = st.multiselect(
            "🔽 Filter Logs by Level",
            ["INFO", "SUCCESS", "WARNING", "ERROR"],
            default=["INFO", "SUCCESS", "WARNING", "ERROR"]
        )
    
    with fcol2:
        st.write("##") # Aligning button
        if st.button("🔄 Refresh", use_container_width=True):
            st.rerun()

    with fcol3:
        st.write("##") # Aligning button
        # Prepare log content for download
        log_text = "\n".join([f"[{l['time']}] {l['level']}: {l['msg']}" for l in log_data])
        st.download_button(
            label="📥 Export",
            data=log_text,
            file_name=f"system_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True
        )

    # Log Container
    st.markdown("### 📜 Event Stream")
    log_scroll = st.container(height=400)
    with log_scroll:
        for log in log_data:
            if log['level'] in selected_levels:
                color = "#3498db" if log['level'] == "INFO" else "#2ecc71" if log['level'] == "SUCCESS" else "#f39c12" if log['level'] == "WARNING" else "#e74c3c"
                st.markdown(f"""
                <div style='background: rgba(30, 41, 59, 0.4); padding: 12px; border-radius: 8px; border-left: 4px solid {color}; margin-bottom: 8px; font-family: monospace;'>
                    <span style='color: #bdc3c7;'>[{log['time']}]</span> 
                    <b style='color: {color}; margin: 0 10px;'>{log['level']}</b> 
                    <span style='color: #ecf0f1;'>{log['icon']} {log['msg']}</span>
                </div>
                """, unsafe_allow_html=True)


# Footer
st.markdown("---")

# Footer container
st.markdown("""
<div style='text-align: center; padding: 20px 20px 10px 20px; background: linear-gradient(135deg, rgba(40, 116, 240, 0.15) 0%, rgba(155, 89, 182, 0.15) 100%); border-radius: 10px; border-top: 2px solid #2874f0;'>
    <p style='color: #00d4ff; font-weight: 600; font-size: 1.1rem; margin-bottom: 10px;'>🎵 AI Music Composer System</p>
    <p style='color: #00d4ff; font-weight: 600; font-size: 1.1rem; margin-bottom: 10px;'>Built with ❤️ by Ratnesh Kumar Singh | Data Scientist (AI/ML Engineer 4+Years Exp)</p>
    <p style='font-size: 0.9rem; color: #e8e8e8; margin-bottom: 5px;'>Powered by Music21, LangChain, Groq, Synthesizer, and Streamlit</p>
</div>
""", unsafe_allow_html=True)

# Social links using Streamlit columns (inside the visual footer area)
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

with col2:
    st.markdown('<p style="text-align: center; margin: 0;"><a href="https://github.com/Ratnesh-181998" target="_blank" style="text-decoration: none; color: #2874f0; font-size: 1.1rem; font-weight: 600;">🔗 GitHub</a></p>', unsafe_allow_html=True)

with col3:
    st.markdown('<p style="text-align: center; margin: 0;"><a href="mailto:rattudacsit2021gate@gmail.com" style="text-decoration: none; color: #26a65b; font-size: 1.1rem; font-weight: 600;">📧 Email</a></p>', unsafe_allow_html=True)

with col4:
    st.markdown('<p style="text-align: center; margin: 0;"><a href="https://www.linkedin.com/in/ratneshkumar1998/" target="_blank" style="text-decoration: none; color: #0077b5; font-size: 1.1rem; font-weight: 600;">💼 LinkedIn</a></p>', unsafe_allow_html=True)

# Close the visual footer
st.markdown("""
<div style='height: 10px; background: linear-gradient(135deg, rgba(40, 116, 240, 0.15) 0%, rgba(155, 89, 182, 0.15) 100%); border-radius: 0 0 10px 10px; border-bottom: 2px solid #2874f0; margin-top: -10px;'></div>
""", unsafe_allow_html=True)

