# microservices-app
# Multi-Service Application with Docker Compose

## Overview
This project demonstrates a multi-service application with:
1. *UI*: Flask application showing a user form.
2. *API*: Flask API interacting with the database.
3. *Database*: MySQL database storing user data.

## File Structure

my_project/ ├── ui/ ├── api/ ├── database/ ├── docker-compose.yml ├── README.md

## Steps to Run

1. *Build Services*  
   Run: docker-compose build

2. *Start Containers*  
   Run: docker-compose up -d

3. *Check Services*
   - UI: http://localhost:3002
   - API: http://localhost:5002
   - Database: Use any MySQL client (e.g., DBeaver).

4. *Add a User*  
   Add via UI form or API.

5. *Verify User*  
   Use SELECT * FROM users; in the database.

## Health Check Pages
- UI: Form and registered users.
- API: Status shown at http://localhost:5002.

## Stopping Services
Run: docker-compose down
