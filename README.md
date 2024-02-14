# dsci551-final_project

---

# Backend - FastAPI Directory Structure

This section outlines the structure of the `fastapi/app` folder, including a description of each file and directory and their respective roles within the project.

## Directory Layout

```
app/
├── main.py
├── schema.py
├── routes.py
└── crud.py
```

### Description of Components

- **`main.py` (Application Entry Point)**: Acts as the gateway to the FastAPI application. It initializes the app instance, sets up database connections, and includes the routing configurations. This file integrates the various components of the application, ensuring seamless operation and connection flow.

- **`schema.py` (Data Schemas)**: Defines the data validation and serialization schemas using Pydantic. These schemas ensure that incoming requests and outgoing responses adhere to the expected structure, playing a critical role in data integrity and type safety.

- **`routes.py` (API Routes)**: Specifies the API endpoints and associates them with their respective handler functions. This file organizes the application's endpoints into a coherent structure, facilitating clear and maintainable API design.

- **`crud.py` (Database Operations)**: Implements the CRUD operations interfacing with the database. This file contains the logic to create, read, update, and delete database records, directly handling data manipulation tasks.

---
