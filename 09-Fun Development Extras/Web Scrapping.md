## WebScrapping

### **Introduction**

- Websites are useful to get the data as visual data is percived by humans easily as they find it difficult to extract the same data if given in a table format or database directly.

- Webscrapping is extracting the data from a website and store it in a organised manner like in Excel sheet(csv), Database, Pdf etc.

- It is the process of extracting and parsing data from websites in an automated fashion using a computer program.

- It's a useful technique for creating datasets for research and learning.

- While web scraping often involves parsing and processing HTML documents, some platforms also offer REST APIs to retrieve information in a machine-readable format like JSON.

### **Request Response Cycle**

- When we try to access a specific website we use a web address (http://www.xxx.xxx) then a request is made to the server, the server then give back a response in the form of html, the browser knows how to parse a html text so it displays the website.

### **Process of Web Scrapping**

- We request the server from a http request module, parse the http response and then pass it to a extractor which is going to orgainse the data.

  - Extractor will be a function that we will create.

- The request is given using modules like axios (js), http (dart) etc.

- Parsing is done using cherio (similar to beautiful soup in python) module, this is used in web scrapping.

- Organisation of data is done using some other modules.

### **Steps to build a web scraping project in Python**

- Pick a website and describe your objective

  - Browse through different sites and pick on to scrape.
  - Identify the information you'd like to scrape from the site. Decide the format of the output file like csv, json etc.
  - Summarize your project idea and outline your strategy in a Jupyter notebook.

- Use the requests library to download web pages

  - Inspect the website's HTML source and identify the right URLs to download.
  - Download and save web pages locally using the requests library.
  - Create a function to automate downloading for different topics/search queries.

- Use Beautiful Soup to parse and extract information

      - Parse and explore the structure of downloaded web pages using Beautiful soup.
      - Use the right properties and methods to extract the required information.
      - Create functions to extract from the page into lists and dictionaries.
      - (Optional) Use a REST API to acquire additional information if required.

- Create CSV file(s) with the extracted information

  - Create functions for the end-to-end process of downloading, parsing, and saving CSVs.
  - Execute the function with different inputs to create a dataset of CSV files.
  - Verify the information in the CSV files by reading them back using Pandas.

- Document and share your work

  - Add proper headings and documentation in your Jupyter notebook.
  - (Optional) Write a blog post about your project and share it online.

- Creating documentation is not an easy task so an easy but time consuming way to do so is by first making the code work with little comments and documentation in a rough jupyter notebook and when this starts working properly then put the whole thing together in another notebook.

- NOTE: End the documentation by References and future work section which will have sub-topics like:

  - Summary of what we did
  - Reference to link that we find useful
  - Ideas for future work

### **Here are some things to keep in mind w.r.t. web scraping**

- Most websites disallow web scraping for commercial purposes
- Prefer using web scraping only for learning and research purposes
- Some websites may block your IP or stop sending valid information if you send too many requests
- Review the terms and conditions of a website before scraping data from it
- Remove sensitive and personally identifiable information before publishing a dataset online
- Use official REST APIs wherever available, with proper API keys
- Scraping data that requires logging in is harder (it requires special cookies and headers)
- Websites change their HTML layout frequently, which may cause your scarping scripts to break
- Websites with dynamic content cannot be scraped using BeautifulSoup. One way to scrape dynamic website is by using Selenium

- The process of scraping a page, parsing links and then using the links to parsing other pages on the same site is called **web crawling**.
  - You can do some basic crawling with requests, Beautiful soup, and few simple for loops in Python.
  - It's how search engines like Google are able to index and search data from millions of websites on the internet. Python offer libraries like Scrapy for crawling websites easily.

### **Using a REST API to retrieve data as JSON**

- Using a REST API to retrieve data as JSON some points to a JSON document, which has a structure quite similar to a Python dictionary.

  - In fact, you can use the json module from python to convert a JSON document into a Python dictionary.

- Unlike HTML, it's really easy to work with JSON using Python, simply fetch the contents of the URL and convert it to a dictionary.

  - Such URLs are often called REST APIs or REST API endpoints.
  - Many websites offer well-documented REST APIs to access data from the site in JSON format.

- Using an API is the officially supported way of extracting information from a website.
  - To use an API, you will often need to register as a developer on the platform and generate an API key, which you'll need to send with every request to authenticate yourself.

### Questions for Revision

- Why do we need to scrape websites?
- What are the applications of web-scraping?
- What are the steps involved in web-scraping?
- What technique is used to retrieve data in a machine-readable format in python?
  - Parsing
- How do we make sure that the webpage is downloaded successfully?
  - Status Code = 200
- What defines the content and structure of the downloaded webpage?
- What is a source code? In what language is it usually written in?
- How different are the original webpage and scraped webpage?
- Is it possible to be blocked by website when you scrape more pages? If yes, how can one avoid this?
- How do we get the information we need from the downloaded website?
- What are REST APIs? How are they different from usual URLs?
- What is the official way to extract information from a website? What do we need for that? How does it help one in extracting information?
- Can we extract data from all the websites on web? If not, why?
- What is web crawling and how is it different from web scraping?
- What are the applications of web crawling?
- How do we extract data from dynamic websites?
