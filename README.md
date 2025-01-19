# Vehicle Service Management System

## Overview
This project is a full-stack web application designed for managing vehicle services, including component registration, repair tracking, issue reporting, and payment simulations. It uses the following tech stack:

- **Frontend**: React.js
- **Backend**: Django (Django REST Framework)
- **Database**: SQLite or PostgreSQL
- **Charts**: Recharts (or any chart library of your choice)

## Features
1. **Vehicle Registration & Management**: 
   - Register vehicles with unique identification numbers and details.
2. **Component Management**:
   - Manage vehicle components, including their repair and purchase prices.
3. **Repair Management**:
   - Track repairs, including vehicle details, issue descriptions, labor costs, and selected components.
4. **Revenue Graphs**:
   - Visualize the daily, monthly, and yearly revenue from repairs.
5. **Simulated Payment System**:
   - A simulated feature for calculating and handling the repair payment.

## Tech Stack

### Backend
- **Django**: Web framework for rapid development and clean, pragmatic design.
- **Django REST Framework**: For building RESTful APIs.
- **SQLite/PostgreSQL**: Database options for storing vehicle and repair information.

### Frontend
- **React.js**: A JavaScript library for building user interfaces.
- **Material UI**: For styling the frontend components.

### Other Libraries
- **Axios**: For making HTTP requests.
- **Recharts**: For visualizing repair data in graphs.

## Installation Guide

### Prerequisites
- Python 3.x
- Node.js & npm

---

## Step-by-Step Installation Guide

### Backend Setup (Django)

1. **Clone the Repository**:
   - Open a terminal or command prompt.
   - Clone the repository to your local machine:
     ```bash
     git clone https://github.com/your-username/vehicle-service-management.git
     ```

2. **Navigate to the Backend Directory**:
   - Change to the backend directory:
     ```bash
     cd vehicle-service-management/backend
     ```

3. **Set up a Virtual Environment**:
   - Create a virtual environment for the Django project:
     ```bash
     python -m venv venv
     ```

4. **Activate the Virtual Environment**:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

5. **Install the Backend Dependencies**:
   - Make sure you are in the backend directory and run:
     ```bash
     pip install -r requirements.txt
     ```

6. **Apply Database Migrations**:
   - Run the database migrations to set up the database schema:
     ```bash
     python manage.py migrate
     ```

7. **Run the Backend Server**:
   - Start the Django development server:
     ```bash
     python manage.py runserver
     ```

   - Your backend API will now be running at `http://127.0.0.1:8000/`.

---

### Frontend Setup (React.js)

1. **Navigate to the Frontend Directory**:
   - Open a new terminal window (or tab) and navigate to the frontend directory:
     ```bash
     cd vehicle-service-management/frontend/vehicle-service-management
     ```

2. **Install the Frontend Dependencies**:
   - Install the necessary dependencies using npm:
     ```bash
     npm install
     ```

3. **Run the Frontend Development Server**:
   - Start the React development server:
     ```bash
     npm start
     ```

   - The frontend will now be running at `http://localhost:3000/`.

---

