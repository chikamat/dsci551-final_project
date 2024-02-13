# dsci551-final_project

---

# Backend - FastAPI Directory Structure

This section outlines the structure of the `fastapi/app` folder, including a description of each file and directory and their respective roles within the project.

## Directory Layout

```
app/
├── main.py
├── schema.py
└── database/
    ├── base.py
    ├── crud.py
    └── model.py
```

### Description of Components

- **`main.py` (router)**: The entry point to the application. It defines the FastAPI app instance and includes all the router configurations. This file maps the URLs to the corresponding business logic and is responsible for connecting all the parts of the application together.

- **`schema.py`**: Defines the Pydantic models (schemas) that are used for validating data. These schemas represent the structure of request and response data for the application. They are crucial for data validation and serialization.

- **`database/` directory**: Contains all database-related modules.
  
  - **`base.py`**: Sets up the database connection and session management. It typically includes the SQLAlchemy `engine`, `sessionmaker`, and a `Base` class from which all ORM models inherit.
  
  - **`crud.py`**: Contains the CRUD (Create, Read, Update, Delete) operations for the database. These functions or classes interact directly with the database to perform data manipulation and querying.
  
  - **`model.py`**: Contains the ORM (Object-Relational Mapping) models for the application. These models define the structure of the database tables and their relationships. This is where you define the entities of your application.

---