# 🎵 GenAI-Music-Composer: AI-Powered Orchestration Studio

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit Cloud](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://appudtzei3tyyttd6xjhwur.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Groq LPU](https://img.shields.io/badge/Inference-Groq_LPU-orange.svg)](https://groq.com/)

An advanced **Generative AI** application that transforms natural language descriptions into professional musical compositions. By orchestrating **Llama 3.1 (via Groq LPU)** with **Music21** theory layers and digital synthesis, this project bridges the gap between human creativity and algorithmic composition.

---

## 🌟 Key Highlights

-   **🧠 Real-Time Inference**: Leveraging Groq's LPU for sub-second melody generation.
-   **🎼 Music Theory Aware**: Integrated with `Music21` to ensure harmonic and rhythmic integrity.
-   **🎨 Infinite Styles**: From Lo-fi Hip Hop to Cinematic Orchestras and Classical Piano.
-   **🏗️ Cloud-Native Stack**: Architected for scale using Docker, Kubernetes (GKE), and CI/CD.
-   **📊 Operations Monitor**: Built-in system logging and metrics for observability.

---
## 🌐🎬 Live Demo
🚀 **Try it now:**
- **Streamlit Profile** - https://share.streamlit.io/user/ratnesh-181998
- **Project Demo** - https://genai-music-composer-qnshg7dgddexrjverkd2e5.streamlit.app/
- 
---
## 🎬 Live Demonstration

### **Interactive Workshop in Action**
![Demo Recording](ai_music_composer_demo_final.webp)
*Transforming a "Lo-fi Hip Hop" prompt into a 2:23 minute composition.*

### **Final Composition Result**
![Generation Result](music_generation_result.png)
*Detailed metrics showing complexity (267 notes) and harmonic density (440 chords).*

---

## 🏗️ Technical Architecture Journey

The system is built on a high-fidelity three-phase architecture:

1.  **🛠️ Phase 1: Logic & Foundation**: Python-based orchestration using `LangChain` to communicate with the Groq LLM and `Music21` for structural musical validation.
2.  **🧠 Phase 2: AI Composer Engine**: Analyzes user prompts for mood, style, and tempo. Generates structured MIDI-like data and performs harmonic layering.
3.  **☁️ Phase 3: Cloud-Native Deployment**: Containerized with **Docker**, built via **GitLab CI/CD**, and orchestrated on **Google Kubernetes Engine (GKE)** for high availability.

---

## 🔧 Technology Stack

| Category | Technologies | Description |
| :--- | :--- | :--- |
| **Intelligence** | `Llama 3.1`, `Groq LPU`, `LangChain` | High-speed LLM inference and AI workflow orchestration. |
| **Engineering** | `Music21`, `Synthesizer`, `Scipy` | Music theory validation, wave synthesis, and audio processing. |
| **Frontend** | `Streamlit`, `Python` | Interactive multi-tab web application with real-time feedback. |
| **DevOps** | `Docker`, `GitLab CI/CD` | Automated builds, containerization, and registry management. |
| **Infrastructure** | `GCP Artifact Registry`, `GKE` | Cloud-native deployment on Kubernetes clusters. |

---

## 📂 Tab-by-Tab Breakdown

### **1. 🎬 Demo Project**
The heart of the app. Features an **Interactive Music Workshop** with categorized sample prompts (Lo-fi, Cinematic, Rock, etc.). Users can trigger generation, track the orchestration status, and play back the resulting WAV file.

### **2. 📖 About Project**
A comprehensive breakdown of the project scope. Includes a technical roadmap, implementation details, and the core value proposition of AI-driven music.

### **3. 🔧 Tech Stack**
A visual representation of the technology layers. Uses an interactive categorical grid to explain the role of each tool (Docker, Music21, GCP, etc.).

### **4. 🏗️ Architecture**
Displays the **Project Architecture Journey** map and the **Simple Logic Flow**. It bridges the gap between high-level user intent and technical cloud deployment.

### **5. 📋 System Logs**
A real-time **Operations Monitor**. Tracks event counts, success rates, and live API heartbeats with an exportable log stream for maintenance and auditing.

---

## 🚀 Installation & Local Setup

### **1. Clone the Repository**
```bash
git clone https://github.com/Ratnesh-181998/GenAI-Music-Composer.git
cd GenAI-Music-Composer
```

### **2. Set Up Environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r CODE/requirements.txt
```

### **3. Configure API Keys**
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### **4. Run the Application**
```bash
cd CODE
streamlit run Multi_Tab_Music_App.py
```

---

## ☁️ Deployment & Scalability

-   **Dockerization**: The app is fully containerized for environmental consistency.
-   **CI/CD Pipeline**: Automated GitLab pipelines build images and push to **Google Artifact Registry**.
-   **K8s Orchestration**: Deployed on **GKE** to handle concurrent users and auto-scaling.
-   **Git LFS**: Large assets (recordings/images) are managed via **Git LFS** up to 2GB for optimal repository performance.

### **Git LFS Setup**
```bash
git lfs install
git lfs track "*.webp"
git lfs track "*.png"
git add .gitattributes
```

---

## 📄 License

This project is licensed under the **MIT License**. Feel free to explore, modify, and build upon this orchestration.

---

## 📞 Contact

**Ratnesh Kumar Singh**  
*Data Scientist (AI/ML Engineer 4+ Years Exp)*

-   📧 **Email**: [rattudacsit2021gate@gmail.com](mailto:rattudacsit2021gate@gmail.com)
-   💼 **LinkedIn**: [ratneshkumar1998](https://www.linkedin.com/in/ratneshkumar1998/)
-   🐙 **GitHub**: [Ratnesh-181998](https://github.com/Ratnesh-181998)
-   📱 **Phone**: +91-947XXXXX46

### **Project Links**
-   🌐 **Live Demo**: [Streamlit App](https://genai-music-composer-qnshg7dgddexrjverkd2e5.streamlit.app/)
-   📖 **Documentation**: [GitHub Wiki](https://github.com/Ratnesh-181998/GenAI-Music-Composer/wiki)
-   🐛 **Issue Tracker**: [GitHub Issues](https://github.com/Ratnesh-181998/GenAI-Music-Composer/issues)
-   💬 **Discussions**: [GitHub Discussions](https://github.com/Ratnesh-181998/GenAI-Music-Composer/discussions)

---
*Built with ❤️ by Ratnesh and the power of Generative AI.*
