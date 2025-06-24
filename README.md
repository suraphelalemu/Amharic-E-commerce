🛒 Building an Amharic E-commerce Data Extractor

A comprehensive repository dedicated to extracting insights and data from Telegram channels, aimed at optimizing the e-commerce landscape in Ethiopia.
🔍 Overview

This repository serves as a framework for leveraging Named Entity Recognition (NER) in the Amharic language, specifically tailored for e-commerce applications.
Selected Channels are
ZemenExpress,
Fashiontera,
nevacomputer,
ethio_brand_collection,
Shewabrand

The following Ethiopian-based Telegram e-commerce channels have been selected for data ingestion:

    

📂 Project Structure

+---.github
| └── workflows
|
+---.vscode
| └── settings.json
+---notebooks
| ├── data_processing.ipynb
| ├── init.ipynb
| └── README.md
+---scripts
| ├── data_labeler.py
| ├── data_preprocessor.py
| ├── data_scrapper.py
| ├── init.py
| └── README.md
+---src
| └── README.md
| └── init.py
+---tests
| ├── README.md
| └── init.py
| ├── .gitignore
| ├── labeled_data.conll
| ├── README.md
| └── requirements.txt

🛠️ Tools and Libraries

    Python: The primary programming language used for the implementation.
    Telethon: A Python library for interacting with Telegram’s API to scrape messages.
    Pandas: For data manipulation and storage in structured formats.
    NLTK or SpaCy: For text preprocessing and tokenization specific to Amharic linguistic features.
