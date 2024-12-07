# Multithreaded News Client/Server Information System

## Project Title
Multithreaded News Client/Server Information System

## Project Description
This project implements a Python-based client-server system that retrieves news data using NewsAPI. The server handles multiple client connections simultaneously using multithreading and fetches news based on client requests. The client provides an interactive interface for users to search headlines, view sources, and save results.

## Semester
Fall 2024

## Group
- **Group Name:** B13
- **Course Code:** ITNE 352
- **Section:** S2
- **Students:**
  - **Student Name:** Sarah Khalid Ahmed
  - **Student ID:** 202102356
  - **Student Name:** Rawan Mohamed Saleh
  - **Student ID:** 202109367

---

## Table of Contents
1. [Requirements](#requirements)
2. [How to Run the System](#how-to-run-the-system)
3. [The Scripts](#the-scripts)
4. [Acknowledgments](#acknowledgments)

---

## Requirements
To set up and run this project, you need:
- **Python**: Version 3.10 or higher.
- **Required Libraries**:
  - `requests`
  - `socket`
  - `threading`
  - `json`

### Steps to Install Dependencies
1. Install Python from [python.org](https://www.python.org/).
2. Install required libraries by running:
   ```bash
   pip install requests

### Development Environment Setup
1. Clone or download the project repository.
2. Ensure the server.py and client.py scripts are in the same directory
3. Obtain a NewsAPI key from NewsAPI and replace the API_KEY in the server.py script.


## How to Run the System
### Running the Server
Open a terminal and navigate to the project directory.
Start the server:
``` bash
python server.py
```
### Running the Client
Open another terminal and navigate to the project directory.
Start the client:
``` bash
python client.py
```
### Follow the interactive prompts to:
Search headlines by keyword, category, or country.
View available sources by filters (category, country, language).
This will automatically save results to JSON files.
![image](https://github.com/user-attachments/assets/7f09d189-7cc3-4692-a7df-05cab1e2ad52)


## The Scripts
`server.py`
### Purpose: Implements a multithreaded server that handles multiple client connections and fetches news from NewsAPI.
Key Functions:
1. fetch_data: Retrieves data from the NewsAPI based on client requests.
2. handle_client: Manages client connections and processes requests.
3. start_server: Initializes the server and listens for connections.

`client.py`
### Purpose: Provides an interactive interface for users to connect to the server and request news data.
Key Functions:
1. receive_message: Receives data from the server.
2. send_message: Sends data to the server.
3. handle_server_communication: Handles client-server interactions.

## Acknowledgments
NewsAPI: For providing the news data.
