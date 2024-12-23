# Student Advisor App 🎓

## Overview
The **Student Advisor App** is a user-friendly Streamlit application powered by the **Lyzr SDK**. It provides personalized academic and career advice to students based on uploaded marksheets and specified ambitions. By leveraging AI capabilities, the app delivers insights on coursework, grades, and personal development tailored to individual needs.

---

## Features
- **Document Upload**: Supports PDF and DOCX files for academic analysis.
- **AI Integration**: Uses Lyzr ChatBot (GPT-4) for generating detailed advice.
- **Personalized Recommendations**:
  - Coursework insights and performance analysis.
  - Career guidance based on user ambitions.
  - Tips for improving academic strengths and addressing weaknesses.
  - Personal development strategies like time management and extracurricular engagement.
- **Interactive Interface**:
  - Upload marksheets.
  - Specify personal ambition for tailored advice.
  - Receive dynamic, actionable feedback.

---

## Installation

### Prerequisites
- **Python**: Ensure Python 3.8 or higher is installed.
- **Dependencies**: Install required packages via `requirements.txt`.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student-advisor-app.git
   cd student-advisor-app
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your **OpenAI API Key**:
   - Create a `.streamlit/secrets.toml` file in the project directory.
   - Add your API key:
     ```toml
     [apikey]
     apikey = "your_openai_api_key"
     ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

---

## Usage

1. **Upload a Marksheet**: Use the file uploader to upload a PDF or DOCX file containing academic details.
2. **Enter Your Ambition**: Provide your career or academic ambition in the text input field.
3. **Generate Advice**: Click "Get Advice" to receive tailored insights and recommendations.
4. **Review Results**: The app will display personalized academic and career guidance based on the uploaded file and your ambition.

---

## File Structure
```
student-advisor-app/
│
├── app.py                  # Main application file
├── logo/                   # Contains app logo assets
│   ├── lyzr-logo.png
│   ├── lyzr-logo-cut.png
├── data/                   # Directory to store uploaded files
├── requirements.txt        # Python dependencies
└── .streamlit/             # Streamlit configuration
    └── secrets.toml        # API key configuration
```

---

## Key Functionalities

### 1. **File Upload**
- Allows users to upload a PDF or DOCX file.
- Saves the file locally in the `data` directory.

### 2. **Lyzr ChatBot Integration**
- Implements Retrieval-Augmented Generation (RAG) for personalized responses.
- Supports multiple file formats for seamless operation.

### 3. **Dynamic Recommendations**
- Academic performance analysis based on uploaded documents.
- Career advice aligned with the user's specified ambition.

### 4. **Personal Development Tips**
- Productivity techniques.
- Recommendations for extracurricular engagement.

---

## Dependencies
- **Streamlit**: Interactive UI framework.
- **Pillow**: For handling image assets.
- **Lyzr SDK**: AI-powered chatbot integration.
- **Python (>=3.8)**

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## Acknowledgments
- Built with the **Lyzr SDK**.
- Inspired by the need for effective academic and career advising tools.

---

## Contact
For issues or inquiries, please contact:
- **Developer**: Akshay Keerthi
- **Email**: [adhikasavansuresh.a@northeastern.edu](mailto:adhikasavansuresh.a@northeastern.edu)
- **Website**: [Lyzr AI](https://www.lyzr.ai/)

