import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Gemini API Configuration ---
# Get the API key from the environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Gemini API key not found. Please set the GEMINI_API_KEY environment variable in your .env file.")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash') # Using the fast and efficient Flash model

# --- Flask App Initialization ---
app = Flask(__name__)

def generate_prompt(recipient, goal, points, tone, name):
    """Creates the detailed prompt for the Gemini model."""
    # This is the prompt template we designed earlier
    return f"""
**Role:** You are an expert email writing assistant named Emailify.
**Task:** Write a clear, concise, and effective email based on the following details.
**Instructions:**
1. Adopt the specified tone of voice flawlessly.
2. Ensure all key points are naturally integrated into the email body.
3. Create a relevant and professional subject line.
4. Do not add any placeholders like "[Your Company Name]" unless explicitly told to.
5. The final output should be ONLY the email, starting with "Subject:" and ending with the signature.

**Email Details:**
* **Recipient Description:** {recipient}
* **Tone of Voice:** {tone}
* **Primary Goal:** {goal}
* **Key Points to Include:**
    * {points}
* **Sign-off Name:** {name}
"""

# --- API Route for Generating Email ---
@app.route('/generate-email', methods=['POST'])
def handle_generate_email():
    """Handles the API request to generate an email."""
    try:
        data = request.json
        # Extract data from the request, providing defaults if missing
        recipient = data.get('recipient', 'a colleague')
        goal = data.get('goal', 'provide an update')
        points = data.get('points', 'no specific points')
        tone = data.get('tone', 'professional')
        name = data.get('name', 'Sender')

        # Create the prompt using our helper function
        prompt = generate_prompt(recipient, goal, points, tone, name)
        
        # Send the prompt to the Gemini model
        response = model.generate_content(prompt)
        
        # Return the generated email text as JSON
        return jsonify({'email': response.text})

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Failed to generate email'}), 500

# --- Route to Serve the Frontend HTML Page ---
@app.route('/')
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

# --- Main Entry Point ---
if __name__ == '__main__':
    # Runs the Flask app
    app.run(debug=True)