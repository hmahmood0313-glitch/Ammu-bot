# Ammu-Bot

Bilingual (Bangla/English) voice companion for elderly users.

## Pipeline
Microphone → Speech-to-Text (Google, bn-BD / en-US) → LLM (Groq, gpt-oss-120b) → Text-to-Speech (edge-tts) → Speaker

## Features
- Automatic language detection via confidence comparison
- Conversation context memory
- Fault-tolerant API handling

## Setup
pip install -r requirements.txt
echo GROQ_API_KEY=your_key > .env
python brain.py