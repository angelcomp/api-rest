
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
	 - WebScraping
	 
****Utils:****
- Git & Github
- Pycharm
- Visual Studio Code

## 🛠️ How to build
**Before we start, you will need to install [Node](https://nodejs.org/en) and [Python](https://www.python.org). Also a IDE, you can choose only for [Visual Studio Code](https://code.visualstudio.com) or [Pycharm](https://www.jetbrains.com/pt-br/pycharm/) too.**
Inside the project you can see 3 folders:
 - **node:** Server written with Express to build a local API;
	 Run the following commands:
	``npm install``
	``npm run dev``
	The Node server will start and publish a JSON with some random data mocked inside the code. The endpoint will be available in the link bellow, you can just copy and paste in your browser:
	``http://localhost:5000/node``
 - **python:** Server written with Flask to build a local API;
	 Run the following commands:
	``?``
	
 - **nodepy:** A simple Frontend to see data fetched from both servers above.
	 Run the following commands:
     ``npm install``
	 ``npm start``
	 Running the last command will automatically open your browser and show the React entry page.


## ✅ License

<p>
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=49AA26&labelColor=000000">
</p>

This project is licensed by MIT.

