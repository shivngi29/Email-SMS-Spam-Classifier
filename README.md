# 📧 Email Spam Classifier

## Overview

This project is a Machine Learning-based Email Spam Classifier that predicts whether a message is **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP) techniques.

The application preprocesses the input text, converts it into numerical features using **TF-IDF Vectorization**, and classifies it using a **Multinomial Naive Bayes** model. The project is deployed as an interactive **Streamlit** web application.

---

## 🚀 Live Demo

🔗 **Live Application:**
*https://email-sms-spam-classifier-aiml.streamlit.app/*

---

## 📸 Application Preview

*![Home Page](screenshots/Home.jpeg)

![Spam Prediction](screenshots/Spam.jpeg)

![Ham Prediction](screenshots/NotSpam.jpeg)*

---

## Features

* Detects Spam and Not Spam (Ham) messages.
* Text preprocessing using NLTK.
* TF-IDF Vectorization for feature extraction.
* Multinomial Naive Bayes classifier.
* Interactive Streamlit web interface.

---

## Dataset

The model was trained on the **SMS Spam Collection Dataset**.

* **Original Dataset:** 5,572 messages and 5 columns.
* **Processed Dataset:** 5,169 messages with the final training columns:

  * `target`
  * `transformed_text`

---

## Feature Engineering

The input text undergoes the following preprocessing steps:

* Convert text to lowercase
* Tokenization
* Remove special characters
* Remove stopwords
* Remove punctuation
* Apply stemming

The cleaned text is stored in the `transformed_text` column and converted into numerical features using **TF-IDF Vectorization** with **3000 maximum features**.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Streamlit
* Pickle
* Git & GitHub

---

## Installation

Clone the repository:

```bash
git clone https://github.com/shivngi29/Email-SMS-Spam-Classifier
```

Navigate to the project folder:

```bash
cd Email-Spam-Classifier
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Future Improvements

* Improve detection of phishing, fake job offers, banking scams, and delivery scams.
* Train the model on a larger and more diverse dataset.
* Experiment with deep learning models for text classification.

---

## Author

**Shivangi Upadhyay**
