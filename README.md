
<h1 align="center"> NodePy Server</h1>

<p align="center">
This is a project from Computer Networks Laboratory<br/>
</p>

## 📜 Summary
The objective of this project is to develop a system where NodeJS offers a simple API using Express, while Python will make available a API with data from a web scraping tasks. All data from both APIs has to be shown in a UI like React and it is crucial for React UI not to be idle while awaiting the results from Python and Node servers. In other words, React should release the GUI during Python's web scraping execution.

## 🚀 Technologies

This project was developed using the following techs:
 - JavaScript 
	 - React
	 - NodeJS
	 - Express
	 - Axios
 - Python 
	 - Flask
	 - Selenium Webdriver with Chrome - WebScraping
	 
****Utils:****
- Git & Github
- Pycharm
- Visual Studio Code

## 🛠️ How to build
**Before we start, you will need to install [Node](https://nodejs.org/en) and [Python](https://www.python.org). Also a IDE, you can choose only for [Visual Studio Code](https://code.visualstudio.com) or [Pycharm](https://www.jetbrains.com/pt-br/pycharm/) too.**
Inside the project you can see 3 folders:
 - **node:** Server written with Express to build a local API;
	 Run the following commands: <br> 
	``npm install`` <br>
	``npm run dev`` <br>
	The Node server will start and publish a JSON with some random data mocked inside the code. The endpoint will be available in the link bellow, you can just copy and paste in your browser: <br>
	``http://localhost:5000/node``
 - **python:** Server written with Flask to build a local API;
	 Run the following command: <br>
	``python server.py`` <br>
	The Python server uses web scraping techniques to retrieve data from a website. It will start and be available at: <br>
	``http://localhost:5000/python`` <br>
	
	The `server.py` file contains the implementation of the Python server using Flask. The server has a single route `/python` which handles the **GET** request. Inside the route handler, it calls the `web_scraping_github` function to perform web scraping on the GitHub page. This function uses Selenium WebDriver with Chrome to navigate to the GitHub page, extract the text content of the `h1` and `p` elements, and return the extracted data as a **JSON** response. The server sets the necessary headers for enabling CORS. <br> 

	Both the Node server and Python server have the necessary headers set to allow Cross-Origin Resource Sharing (CORS), enabling communication with the React frontend. <br>

	The `web_scraping_github` function performs the following steps:

	- Configures the browser options for Chrome WebDriver.
	- Opens the GitHub page.
	- Extracts the text content of the h1 and p elements using XPath.
	- Closes the browser.
	- Generates a dictionary containing the extracted text.
	- Converts the Python dictionary to JSON format.
	- Returns the JSON data. <br> <br>
	
	The `app.after_request` decorator in the Flask server sets the necessary headers for enabling CORS on all routes.
	
 - **nodepy:** A simple Frontend to see data fetched from both servers above.
	 Run the following commands: <br>
     ``npm install`` <br>
	 ``npm start`` <br>
	 Running the last command will automatically open your browser and show the React entry page.


## ✅ License

<p>
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=49AA26&labelColor=000000">
</p>

This project is licensed by MIT.

