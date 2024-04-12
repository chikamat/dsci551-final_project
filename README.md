# Local Food Exchange Network Application

## Overview

The Local Food Exchange Network is a web-based application designed to connect local farmers with customers to facilitate the discovery and purchase of locally sourced food products. Developed as part of the DSCI551 Spring 2024 coursework at USC, this project implements a distributed database that stores data across two NoSQL systems, managed by a hash function.

## Getting Started

### Prerequisites
- Docker Desktop must have been installed and run previously (Please refer to https://docs.docker.com/desktop/install/mac-install/).
  Windows users need to install Linux distribution by using WSL as well (Please refer to https://learn.microsoft.com/ja-jp/windows/wsl/install).
  In addition, Windows users need to have docker enable integration with the Linux distribution (Please check Settings/Resources/WSL integration on your Docker Desktop).
  Windows users will execute Docker commands in your Linux distribution terminal. Mac users will execute Docker commands in your terminal.

### Installation and Setup
1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Execute the following command to start the application:

    ```sh
    docker-compose up -d
    ```

### Accessing the Application
Once the application is running, open your web browser and go to the following URL to access the web interface:

- Web application for end users (user and farmer) - http://localhost:8501
- User itnerface for database managers (administrator) - http://localhost/docs

### Importing Sample Data
Once the application is running, you can load sample data with the following command:

```sh
./import_data.sh
```

If you need, you can delete all data with the following command:

```sh
./clear_data.sh
```

To execute `clear_data.sh`, you may need to install jq with the following command:

```sh
sudo apt-get update
sudo apt-get install jq
```

## Application Structure

- `fastapi/`: Contains FastAPI backend logic with CRUD operations for the database manager.
  - `app/`: The main directory for FastAPI application.
    - `crud.py`: Functions for creating, reading, updating, and deleting database entries.
    - `main.py`: Entry point for the FastAPI application, defining the API endpoints.
    - `routes_farmer.py`: API routes specific to farmer operations.
    - `routes_user.py`: API routes specific to user operations.
    - `schema.py`: Pydantic schemas for data validation.
  - `Dockerfile`: Docker configuration for FastAPI application.
  - `requirements.txt`: List of Python dependencies for FastAPI.

- `streamlit/`: Holds the Streamlit frontend interface.
  - `pages/`: The main directory for Streamlit application.
    - `1_Farmer`: Contains frontend code for the farmer page.
    - `2_User`: Contains frontend code for the User page.
    - `3_Products`: Contains frontend code to display list of all the products.
    - `4_Contact_Us`: Contains frontend code for Contact Us page.
  - `Welcome.py/`: Contains frontend of the main page of the local food exchange application.
  - `streamlit_app.py`: Main Streamlit application file, rendering the user interface.
  - `Dockerfile`: Docker configuration for Streamlit application.
  - `requirements.txt`: List of Python dependencies for Streamlit.
  - `style.css`: Custom CSS styles for the Streamlit interface.
  - `logo.png`: Image of the logo which is displayed in the frontend.

- `env/`: Environment variables and configuration files.

- `README.md`: Documentation and instructions for setting up and running the application (this file).

- `compose.yaml`: Docker Compose file to orchestrate the multi-container setup.

- `import_data.sh`: Loading sample data for testing the application.

- `clear_data.sh`: Removing all data from the database.

## Team Contributions

- **Shruti Subramanyam**: Focused on frontend development using Streamlit, crafting the user interfaces for the web application and connecting them to backend service.
- **Kyosuke Chikamatsu**: Concentrated on backend development, including database management and ensuring data integrity across the distributed system.

## Future Work

Further development can include features such as payment integration, extended user profiles, and a more detailed analytics dashboard for farmers to track sales and product performance.

## Contact

For any inquiries regarding the Local Food Exchange Network application, please reach out to the contributors:

- Shruti Subramanyam - shrutisu@usc.edu 
- Kyosuke Chikamatsu - chikamat@usc.edu

We appreciate your interest in our project and welcome any feedback or contributions!
