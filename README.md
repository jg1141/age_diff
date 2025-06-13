# Staff Age Difference Guessing Game

A Streamlit application that allows users to submit their guesses about the age difference between staff members.

## Features

- Simple form interface for submitting age difference guesses
- Input validation to ensure both staff members' names are provided
- Display of all previous submissions in a table format
- Ability to download submissions as a CSV file
- Session-based storage of submissions

## Installation

1. Make sure you have Python 3.7+ installed
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

To run the app, execute the following command in your terminal:
```bash
streamlit run app.py
```

The app will open in your default web browser. If it doesn't, you can access it at http://localhost:8501

## Usage

1. Enter the names of two staff members
2. Input the age difference (in years) between them
3. Optionally add any additional notes
4. Click "Submit Guess" to save your submission
5. View all previous submissions in the table below
6. Download the submissions as a CSV file if needed 