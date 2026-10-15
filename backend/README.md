# Employee API

A FastAPI backend to search employees, using MySQL.

## How to run

1. Install packages
   ```
   pip install -r requirements.txt
   ```
2. Create the database in MySQL
   ```sql
   CREATE DATABASE office;
   ```
3. Create a `.env` file (see `.env.example`)
   ```
   DATABASE_URL=mysql+pymysql://USER:PASSWORD@localhost:3306/office
   FRONTEND_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
   ```
   `FRONTEND_ORIGINS` is the list of frontend URLs allowed to call the API (CORS).
   In production, set it to your real frontend URL.
4. Add sample employees (only needed once)
   ```
   python -m app.seed
   ```
5. Start the server
   ```
   uvicorn app.main:app --reload
   ```
6. Open http://127.0.0.1:8000/docs to try the API for testing.

## Database choice

The database choice is done by the assignment pdf. In the requirement it said prefer Mysql so no choice left for me if i had the choice then i would have taken postgres

## How API is optimized (conceptually)

when you have millions of data the backend can't return the millions of data it is not optimal and time consuming so instead we do pagination so we return data in chunks so that the data is sent faster and optimized puts minimal load on the server
