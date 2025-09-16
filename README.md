# IQSF Luxe Editorial - Global Queer Safety Index

This project is a full-stack web application designed to track, display, and analyze LGBTQ+ safety data from around the world. It features a Vue.js frontend, a Python FastAPI backend, and a Supabase PostgreSQL database.

## Project Structure

- **Frontend:** (Root directory) A Vite-powered Vue 3 application.
- **Backend:** (`/oracle-chamber`) A FastAPI server that connects to the database.

---

## Getting Started

### Prerequisites

- Node.js and npm
- Python 3.8+ and pip
- A Supabase account and project

### 1. Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd oracle-chamber
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables:**
    Create a file named `.env` inside the `oracle-chamber` directory by copying the example:
    ```bash
    cp .env.example .env
    ```
    Now, edit the `.env` file and add your actual Supabase credentials.

4.  **Run the backend server:**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be running at `http://127.0.0.1:8000`.

### 2. Frontend Setup

1.  **Navigate to the project root directory and install dependencies:**
    ```bash
    npm install
    ```

2.  **Run the frontend development server:**
    ```bash
    npm run dev
    ```
    The application will be available at `http://localhost:5173`. The `vite.config.js` is already configured to proxy API requests to the backend.

---
