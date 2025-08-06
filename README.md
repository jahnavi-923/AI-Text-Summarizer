# 📝 AI Text Summarizer

## 📖 Overview

This project is a fully functional web application that uses the power of Artificial Intelligence to summarize long articles and texts. The goal was to build an end-to-end AI/ML project, starting from a basic idea and finishing with a working application. The app takes any long piece of text as input, processes it using a sophisticated pre-trained NLP model, and returns a short, coherent summary. It also provides useful metrics about the text reduction.

---

## ✨ Features

-   **Abstractive Summarization:** Uses the `facebook/bart-large-cnn` model from Hugging Face, which generates new, human-like sentences that capture the core meaning of the original text.
-   **Handles Long Articles:** Implements a text-chunking algorithm to process articles of any length, overcoming the input size limitations of the model.
-   **Analytics & Metrics:** Calculates and displays key statistics for each summary:
    -   Original Word Count
    -   Summary Word Count
    -   Readability Score (Flesch Reading Ease)
-   **Web Interface:** A clean and simple user interface built with Flask, allowing anyone to use the tool through their web browser.
-   **Summary History:** Keeps a running log of the summaries generated during a session.

---

## 🛠️ Technologies Used

-   **Backend:** Python
-   **Web Framework:** Flask
-   **AI/ML Library:** Hugging Face `transformers`
-   **Deep Learning Framework:** PyTorch
-   **Text Analytics:** `textstat`
-   **Environment Management:** Anaconda (Conda)
-   **Version Control:** Git & GitHub

---

## 🚀 Setup and Run Instructions

To get this project running on your local machine, follow these steps:

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/Bunty722/AI-Text-Summarizer.git](https://github.com/Bunty722/AI-Text-Summarizer.git)
    cd AI-Text-Summarizer
    ```

2.  **Create a Conda Environment**
    This creates an isolated environment with Python 3.11 to avoid conflicts.
    ```bash
    conda create --name summarizer_env python=3.11
    ```

3.  **Activate the Environment**
    You must activate the environment every time you work on the project.
    ```bash
    conda activate summarizer_env
    ```

4.  **Install Dependencies**
    The `requirements.txt` file contains all the necessary libraries.
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Application**
    This will start a local development server.
    ```bash
    python app.py
    ```

6.  **View in Browser**
    Open your web browser and navigate to: `http://127.0.0.1:5000`

---

## 👣 Step-by-Step Work Done

This project was built incrementally, with each step adding a new layer of functionality.

1.  **Environment Setup:** We created a dedicated Conda environment to ensure all our libraries and dependencies were managed cleanly.
2.  **Core Logic:** We first wrote a simple Python script (`src/summarizer.py`) to test the core AI functionality. We used the Hugging Face `pipeline` to load the `BART` model and generate a summary from a sample text. This confirmed our core technology worked.
3.  **Web App Foundation:** We built a basic web application using Flask. This involved creating `app.py` to handle web requests and an HTML file (`templates/index.html`) to create the user interface with a text box and a button.
4.  **Adding Metrics:** We enhanced the application by adding useful analytics. We installed the `textstat` library and modified our code to calculate and display the word counts of the original and summarized texts, along with a readability score.
5.  **Handling Long Articles:** We addressed a major limitation of the model by implementing a "text chunking" strategy. The code was updated to split very long articles into smaller, overlapping pieces, summarize each piece, and then stitch the summaries together for a final result.
6.  **Adding History:** As a final feature, we added a session-based history log. We used a simple Python list in `app.py` to store each summary generated and then used a loop in the HTML file to display this history on the page.
7.  **Version Control:** Throughout the process, we used Git for version control. We set up a GitHub repository, created a `.gitignore` file to exclude unnecessary files, and pushed our final, working code to the remote repository.

---

## ⚠️ Errors Faced and How We Solved Them

During development, we encountered a few common but important issues.

#### 1. Git Push Failed: `main` vs. `master`
-   **Error:** When we first tried to push our code to GitHub, we got an error: `src refspec main does not match any`.
-   **Reason:** Our local Git repository had automatically created a default branch named `master`, but GitHub now uses `main` as its default. We were trying to push to a branch that didn't exist in our local setup.
-   **Solution:** We solved this with a single command to rename our local branch from `master` to `main`, which then allowed the `git push` command to work perfectly.
    ```bash
    git branch -M main
    ```

#### 2. Logical Bug: Long Articles Were Not Summarized
-   **Error:** When we tested our chunking logic with a very long article, the app only summarized the first paragraph. The console did not show the text being split into multiple chunks.
-   **Reason:** A single parameter in our tokenizer function, `truncation=True`, was causing the problem. It was cutting off the input text at the model's maximum length *before* our chunking code had a chance to run.
-   **Solution:** We fixed this by simply modifying that line of code to tokenize the entire article first, without truncating it. This allowed our loop to correctly slice the full text into processable chunks.
    ```python
    # Incorrect line that caused the bug
    inputs = tokenizer(article_text, return_tensors='pt', max_length=1000, truncation=True)
    
    # Corrected line that fixed the bug
    inputs = tokenizer(article_text, return_tensors='pt')
    ```

---

## ✅ Final Output

The final result is a responsive web application that presents a clean user interface. A user can paste an article of any length into the text area. Upon clicking "Summarize," the application displays the generated summary along with three key metrics: original word count, summary word count, and readability score. Below the latest result, a history of previously generated summaries is maintained for the duration of the session.

---

## 🎓 Conclusion & Learnings

This project was a practical, hands-on journey through the entire lifecycle of an AI application. Key learnings include:

-   **The Power of Pre-trained Models:** We were able to implement a state-of-the-art NLP model with just a few lines of code thanks to the Hugging Face library.
-   **End-to-End Development:** We learned how to connect a powerful backend AI model to a user-friendly frontend with Flask.
-   **Problem Solving:** We faced and debugged real-world issues, from version control mismatches to subtle logical bugs in the AI processing pipeline.
-   **Importance of Project Structure:** Creating a well-organized project with separate folders, a `requirements.txt` file, and a good `README.md` is crucial for maintainability and collaboration.

---
