# 📚 Talecraft

**Talecraft** is a Flask app that uses the [GroqCloud API](https://console.groq.com/) to generate imaginative stories for children based on user input such as title, theme, place, and prompts about characters and settings.

## 🛠️ Tech Stack

- **Flask**
- **HTML**
- **Matcha.css**

## ✨ Features

- 🔐 Authentication (authN)
- 📖 Create, view, and delete stories
- 🤖 Generate stories using AI

## 🛤️ Roadmap

- 🔍 Search stories
- ✏️ Update stories
- 🌟 Story Hub for sharing cool stories

## 🚀 How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/pheonix-coder/TaleCraft
   ```

2. **Set up a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install requirements:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database:**

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. **Run the application:**

   ```bash
   python run.py
   ```

## 🎯 Submission

This project is a submission to [Quira Quest 16](https://quira.sh/quests/creator/submissions?questId=16).

## 🎥 Demo Video

Demo video coming soon!
