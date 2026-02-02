# MechaSenku
A Gemini 3 Powered scientific chatbot and substitute finder
# 🧠 MechaSenku

**MechaSenku** is a Streamlit-powered science and technology assistant built on **Google Gemini**. It combines a conversational AI chatbot with a **material substitute finder** designed for scientific, engineering, and educational use cases.

Inspired by the analytical style of *Senku*, MechaSenku focuses on **concise, accurate, and practical explanations** without unnecessary fluff.

---

## Features

### 1.  Science Chatbot

* Conversational AI specialized in **science & technology**
* Maintains **chat context** using Streamlit session state
* Explains concepts using:

  * Short, clear sentences
  * Practical tips
  * Mathematical formulas (LaTeX when needed)
* Designed to avoid hallucination and speculation

### 2.  Material Substitute Finder

* Suggests **cheaper or more accessible alternatives** for scientific materials
* Inputs include:

  * Major material
  * Purpose
  * Scientific domain
  * Constraints
  * Number of substitutes required
* Outputs:

  * Numbered substitute list
  * Common places to obtain materials
  * Practical usage tips
  * Relevant formulas when applicable

---

## Tech Stack

| Component             | Technology                             |
| --------------------- | -------------------------------------- |
| Frontend              | Streamlit                              |
| **Core Intelligence** | **Google Gemini 3 (gemini-2.5-flash)** |
| Language              | Python 3                               |
| State Management      | Streamlit Session State                |

---

## 🧠 Why Gemini 3 Is Vital to MechaSenku

MechaSenku is **not a UI wrapper around a generic chatbot**. Its core functionality depends heavily on the **reasoning, constraint-handling, and structured output capabilities of Gemini 3**.

### 1. Advanced Scientific Reasoning

Gemini 3 enables MechaSenku to:

* Understand **scientific domains** (chemistry, physics, materials science)
* Respect **constraints** such as cost, availability, and safety
* Avoid hallucinations when dealing with formulas, materials, and processes

Without Gemini 3, the substitute engine would degrade into guesswork.

---

### 2. Context-Aware Substitute Generation

The **Substitute Finder** relies on Gemini 3 to:

* Parse multi-variable prompts (material, purpose, domain, constraints)
* Rank substitutes by **practical feasibility**, not just similarity
* Generate explanations that include:

  * Where to obtain materials
  * Practical tips
  * Equations (LaTeX) when relevant

This level of structured, multi-criteria reasoning is a direct capability of Gemini 3.

---

### 💬 3. Stateful Scientific Conversation

In the Chatbot tab, Gemini 3 is essential for:

* Maintaining **conversation context** across turns
* Adapting explanations based on prior questions
* Switching seamlessly between:

  * Conceptual explanations
  * Applied science
  * Mathematical formulation

Streamlit handles storage — **Gemini 3 provides understanding**.

---

### 4. Speed + Accuracy Tradeoff (gemini-2.5-flash)

MechaSenku uses **gemini-2.5-flash**, a Gemini 3-class model, because it offers:

* Low latency for real-time interaction
* High factual accuracy for STEM topics
* Cost efficiency for scalable deployment

This makes live demos, classroom use, and hackathon deployment feasible.

---

### 5. Prompt Engineering Synergy

The system instructions in MechaSenku are deliberately designed to leverage Gemini 3’s strengths:

* Instruction-following
* Role adherence ("MechaSenku" persona)
* Safe refusal of dangerous actions
* Structured, concise output

A weaker model would ignore or partially follow these constraints.

---
---

## Project Structure

```
mechasenku/
│
├── MechaSenku.py      # Main Streamlit application
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mechasenku.git
cd mechasenku
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Your Gemini API Key

For security, it is recommended to use environment variables:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

(or use `.env` if preferred)

---

## Running the App

```bash
streamlit run app.py
```

The app will open in your browser with two tabs:

* **Chatbot**
* **Substitute Finder**

---

## 🧠 Design Philosophy

* **Accuracy over verbosity**
* **Practical science first**
* **Minimal UI, maximum clarity**
* Built for:

  * Students
  * Educators
  * Engineers
  * Researchers
  * Hackathons & demos

---

## 🔐 Safety Notes

* The assistant is designed for **educational and scientific purposes**
* It avoids aiding dangerous or unethical actions
* Always verify critical scientific outputs before real-world application

---

## 📌 Future Enhancements

* Charts and data visualization (Altair)
* Exportable reports (PDF)
* Domain-specific modes (Chemistry, Physics, Materials Science)
* Offline substitute database
* Interactive experiment sandbox
---

## 📦 requirements.txt

```txt
streamlit
google-generativeai
```

> ⚠️ Version pinning is recommended for production deployments.

---

## 🚀 Deployment Notes

### Local Deployment

* Ensure Python **3.9+** is installed
* Use a virtual environment to avoid dependency conflicts
* Run using:

```bash
streamlit run app.py
```

### Streamlit Cloud Deployment

1. Push the repository to GitHub
2. Go to **streamlit.io/cloud**
3. Select the repository and branch
4. Set environment variable:

   * `GEMINI_API_KEY`
5. Deploy 🎉

---
---

> *"This is exhilarating! Science is all about replacing the impossible with logic."* 
