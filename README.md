# SUMMARY--AI
# CLARIFYX — AI Text Summarizer

**Complexity, simplified.**

CLARIFYX is an AI-powered text summarization web application that converts long and complex text into concise, clear, and easy-to-understand summaries using Google's Gemini AI.

APP DEMO:
https://summary--ai-betn44cftvetdcssryefa4.streamlit.app/

SCREENSHOTS:
<img width="959" height="365" alt="APP4" src="https://github.com/user-attachments/assets/3b7bf5ab-adb7-4ab0-9316-40e95c406599" />
<img width="959" height="368" alt="APP2" src="https://github.com/user-attachments/assets/f2b1791b-334c-4a38-b861-fb7385269962" />
<img width="958" height="412" alt="APP 1" src="https://github.com/user-attachments/assets/2eb2cd22-a862-4395-bc62-84a18afcc452" />


## Features

- **AI-Powered Summarization:** Generates summaries using Google Gemini AI.
- **Multiple Summary Lengths:** Choose short, balanced, or detailed summaries.
- **Flexible Output Formats:** Generate summaries as paragraphs, bullet points, or study notes.
- **Text Input:** Paste text directly into the application.
- **File Upload:** Upload supported text files for summarization.
- **Word and Character Count:** View the input text statistics.
- **Live Output:** View the summary as it is generated.
- **Download Summary:** Download the generated summary as a text file.
- **Simple User Interface:** Clean, user-friendly design.

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google Gen AI Python SDK
- python-dotenv

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

Replace the repository URL and folder name with your actual GitHub details.

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the API Key

Create a `.env` file in the project folder and add your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace `your_gemini_api_key` with your actual API key.

**Security Note:** Never upload your API key or `.env` file to GitHub.

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

## Deployment

CLARIFYX can be deployed using Streamlit Community Cloud.

1. Push the project files to a GitHub repository.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your GitHub repository.
4. Select `app.py` as the main file.
5. Add your `GEMINI_API_KEY` under the application's Secrets settings.
6. Deploy the application.

## Project Structure

```text
CLARIFYX/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Use Cases

- Summarizing academic notes and study materials
- Understanding lengthy articles and documents
- Preparing quick revision notes
- Extracting key points from large amounts of text
- Improving reading and learning efficiency

## Future Enhancements

- Support for PDF and DOCX files
- Multilingual summarization
- Summary history
- Key-point extraction and keyword highlighting
- Additional output formats

## Privacy and Security

The application uses the Google Gemini API to process text and generate summaries. Users should avoid submitting confidential or sensitive information. API credentials must be stored securely using environment variables or Streamlit Secrets.

## Author

**HARI PRIYA.B**
BSC CS WITH AI 
*CLARIFYX — Complexity, simplified.*

