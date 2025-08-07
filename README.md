# ChatbotTranslate

ChatbotTranslate is a serverless chatbot powered by AWS that translates user inputted text into various languages using Amazon Translate. It is designed using Amazon Lex to handle conversational interaction and AWS Lambda to process translation requests.

---

## 📌 Overview

ChatbotTranslate is a cloud application that provides language translation via chatbot interaction. The user inputs a sentence and selects a target language, and the bot responds with the translated result.

It is a demonstration of building multilingual bots using AWS AI services without managing infrastructure.

---

## Services Used

- **Amazon Lex** – Natural language chatbot interface for capturing user input and intent.
- **Amazon Translate** – Translates user input into supported languages.
- **AWS Lambda** – Processes the translation request and builds Lex responses.
- **AWS IAM** – Manages permissions between services to ensure secure operations.

---

## How It Works

1. A user engages with the chatbot and provides a sentence to be translated and a target language.
2. Amazon Lex captures both through defined **slots**.
3. The data is passed to a **Lambda function** via a code hook.
4. The function uses **Amazon Translate** to perform the translation.
5. The translated result is returned to Lex and displayed to the user.

---

## Example Inputs

`  {
    "text": "Hello, how are you?",
    "language": "French"
  }`

## Testing the Bot

Try out sample phrases like:
- “Translate ‘Good morning’ to Spanish.”
- “I want to translate something to Japanese.”
- “Can you convert my text into German?”
Lex will guide the user through missing information by prompting for the text or language slot.

## Requirements

To run this project, you’ll need:
- An AWS account with access to:
- Amazon Lex
- AWS Lambda
- A Lambda function written in Python (3.12+)
- An IAM role with the permissions for basic Lambda functions

## Architecture Diagram

  User → Amazon Lex → AWS Lambda → Amazon Translate → Lambda → Lex → User

## Example Input/Output

<img width="664" height="666" alt="image" src="https://github.com/user-attachments/assets/4eb05fc8-0fc9-4794-92b1-6d529fb25177" />


