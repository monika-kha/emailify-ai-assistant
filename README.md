# 🚀 Emailify AI Assistant

A simple web application that uses the Google Gemini API to generate professional and personal emails in various tones.

## ✨ Features

-   Generate emails for any purpose (e.g., asking for a day off, following up with a client).
-   Specify key points that must be included in the email.
-   Choose from multiple tones: Formal, Friendly, Persuasive, and more.
-   Simple, clean user interface.

## 🛠️ Tech Stack

-   **Backend:** Python, Flask
-   **AI:** Google Gemini API
-   **Frontend:** HTML, CSS, JavaScript

## ⚙️ Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```
    git clone [https://github.com/YOUR_USERNAME/emailify-ai-assistant.git](https://github.com/YOUR_USERNAME/emailify-ai-assistant.git)
    cd emailify-ai-assistant
    ```
2.  **Create a virtual environment and activate it:**
    ```
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```
3.  **Install the dependencies:**
    ```
    pip install -r requirements.txt
    ```
4.  **Create a `.env` file** in the root directory and add your Gemini API key:
    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```
5.  **Run the application:**
    ```
    flask run
    ```
The application will be available at `http://127.0.0.1:5000`.
## 🖼️ Preview

Here's a look at the Emailify AI Assistant in action.

**Main Interface:**
![Emailify Main UI](./images/emailify-main.png)

**Generated Email Example:**
![Emailify Result UI](./images/emailify-result.png)