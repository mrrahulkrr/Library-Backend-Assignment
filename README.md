# Library Management Assignment

## Overview

This project is a FastAPI application designed to manage student records stored in a MongoDB database. It provides endpoints for creating, reading, updating, and deleting student records.

## Features

- Create new student records
- Retrieve student records based on various criteria such as country and age
- Retrieve a specific student record by ID
- Update existing student records
- Delete student records

## Technologies Used

- FastAPI: A modern web framework for building APIs with Python.
- MongoDB: A NoSQL database used for storing student records.
- Pydantic: A data validation library used for defining data models.
- PyMongo: A Python driver for MongoDB used for interacting with the database.
- Python-dotenv: A Python module for reading environment variables from a .env file.
- AWS Ec2 server: Used AWS Ec2 server to deploy it

## Setup

1. Clone the repository:

```bash
git clone https://github.com/mrrahulkrr/Library-Backend-Assignment.git
cd CosmoCloud-Assignment
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:

Create a `.env` file in the root directory of the project and add the following:

```plaintext
MONGODB_URI=<your_MongoDB_URI_here>
```

Replace `<your_MongoDB_URI_here>` with the connection URI for your MongoDB database.

4. Run the application:

```bash
uvicorn main:app --reload
```

The application will start running at `http://localhost:8000`.

## Usage

Once the application is running, you can access the API documentation by navigating to `http://localhost:8000/docs` in your web browser. From there, you can explore the available endpoints and interact with the API to manage student records.
