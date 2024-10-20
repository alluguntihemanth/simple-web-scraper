# 📰 **Web Scraper Project**  
## 🌐 **Data Extraction from Articles**  

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:820/1*TC2JtooA4LoOauX34_fUWA.png" alt="Web Scraper" width="600"/>
</p>

---

## 📝 **Overview**  
This project facilitates the **extraction of data from any article or webpage**. It utilizes **BeautifulSoup** for parsing HTML and **requests** for making HTTP requests, making it easy to gather information from various online sources.

---

## ✨ **Key Features**  
1. **Data Extraction**:  
   - Extracts the **title**, **publication date**, **author**, and **content** from any specified article or URL.  

2. **CSV Output**:  
   - Saves the extracted data into a **CSV** file for easy access and analysis.

---

## 📂 **Directory Structure**  
D:/ML/simple-web-scraper/
│
├── scraper.py              # Main script for extracting data from articles
├── requirements.txt        # List of dependencies
└── scraped_article.csv     # Output file containing extracted data

---

## 🚀 **Run the Application**  

1. **Prerequisites**  
   - Install [Python](https://www.python.org/downloads/).  
   - Install the necessary dependencies:  
     ```bash
     pip install requests beautifulsoup4 pandas
     ```

2. **Modify the Script**  
   - Change the `url` variable in `scraper.py` to the desired article or webpage URL.

3. **Run the Script**  
   - Execute the script to extract data and save it to a CSV file:  
     ```bash
     python scraper.py
     ```

---

## 💬 **Example Usage**  
To use the script, simply specify any article URL in the `scraper.py` file. Upon execution, it will perform the following:

1. Extract the title, publication date, author, and content of the article.
2. Save the extracted data into a CSV file.

---

## 🛠️ **Key Functions**  
- **`scrape_article(url)`**:  
  Extracts data from the specified URL and returns a dictionary with the article's details.  

---

## 🤝 **Contributing**  
We appreciate your interest! However, we are still finalizing the contribution process.  
In the meantime, feel free to fork the repository and experiment with the code. We plan to introduce formal contribution guidelines soon.

---

## 📄 **License**  
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## 📧 **Contact**  
For any inquiries, feel free to reach out via:  
- **Email**: hemanthallugunti.com  
- **LinkedIn**: [Hemanth Reddy Allugunti](https://www.linkedin.com/in/hemanth-reddy-allugunti-883b36216/)

---

Enjoy extracting data with this **Web Scraper Project**! 🎉
