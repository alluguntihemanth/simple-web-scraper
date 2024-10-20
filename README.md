# 🕸️ **Simple Web Scraper**

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Web_scraping.svg/1280px-Web_scraping.svg.png" alt="Web Scraping" width="400" height="220" style="margin-right: 20px;"/>
  <img src="https://miro.medium.com/v2/resize:fit:1200/1*Qe_xdqaV9aXgQ_ox8Z02Kg.png" alt="Data Extraction" width="400"/>
</p>

---

## 📝 **Overview**  
This project is a **simple Python web scraper** that extracts articles from TechCrunch and retrieves essential information such as the title, publication date, author, and content. The scraped data is then saved to a CSV file for easy access and further analysis.

---

## ✨ **Key Features**  
1. **Article Scraping**:  
   - Extracts article data from TechCrunch.

2. **Data Extraction**:  
   - Retrieves the title, publication date, author, and content of articles.

3. **CSV Export**:  
   - Saves the scraped data into a CSV file for easy access.

---

## 📂 **Directory Structure**  
D:/ML/simple-web-scraper/
│
├── scraper.py              # Main script for scraping articles
└── requirements.txt        # List of dependencies

---

## 🚀 **Run the Application**  

1. **Prerequisites**  
   - Install [Python](https://www.python.org/downloads/).  
   - Install the necessary dependencies:  
     ```bash
     pip install requests beautifulsoup4 pandas
     ```

2. **Run the Script**  
   - Execute the scraper script to retrieve article data:  
     ```bash
     python scraper.py
     ```

3. **Output**  
   - The scraped article data will be saved in a file named `scraped_article.csv` in the same directory.

---

## 💬 **Example Usage**  
To use the scraper, simply run the `scraper.py` file. Upon execution, it will perform the following:

1. Retrieve the article from TechCrunch.
2. Extract the title, publication date, author, and content.
3. Save the data into a CSV file.

---

## 🛠️ **Key Functions**  
- **`scrape_article(url)`**:  
  Scrapes the article data from the provided URL and returns it as a dictionary.

---

## 🤝 **Contributing**  
We appreciate your interest! Please feel free to fork the repository and experiment with the code. We will be adding formal contribution guidelines soon.

---

## 📄 **License**  
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## 📧 **Contact**  
For any inquiries, feel free to reach out via:  
- **Email**: hemanthallugunti.com  
- **LinkedIn**: [Hemanth Reddy Allugunti](https://www.linkedin.com/in/hemanth-reddy-allugunti-883b36216/)

---

Happy scraping with this **Simple Web Scraper** project! 🎉
