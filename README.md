# Typing Speed Test Web App

This is a Flask-based web application that allows users to test their typing speed and accuracy in real time. It generates random sentences for users to type and evaluates their performance based on speed (WPM), accuracy, and mistakes.

##  Features

- Real-time typing speed test
- Calculates Words Per Minute (WPM)
- Tracks number of mistakes
- Provides accuracy percentage and motivational feedback
- Simple, clean interface

##  Project Structure

```
typing-speed-test/
│
├── app.py               # Flask backend logic
├── templates/
│   ├── index.html       # Main typing test interface
│   └── result.html      # Result display after test
├── static/              # (Optional) CSS or JS files
└── README.md            # Project documentation
```

## How to Run the Project

###  1. Clone the Repository

```bash
git clone https://github.com/<your-username>/typing-speed-test.git
cd typing-speed-test
```

###  2. Set Up a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate      # On Windows
```

###  3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install manually:

```bash
pip install flask essential_generators
```

###  4. Run the App

```bash
python app.py
```

Then open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

##  Metrics Calculated

- **WPM (Words Per Minute)**: Speed of typing
- **Accuracy (%)**: Correct words vs. total words
- **Mistakes**: Total incorrect or missed words
