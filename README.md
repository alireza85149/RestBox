# RestBox

RestBox is a Django-based villa booking web application that connects **Guests** and **Hosts** through a simple reservation platform.
Guests can browse available villas and make reservations, while hosts can manage their properties, availability, and bookings through dedicated dashboards.

---

## Features

### Authentication

* User registration and login
* Session-based authentication
* Host and Guest roles

### Villa Management

* Create new villas
* Update villa information
* Delete villas
* View all listed villas
* Villa detail pages

### Availability Management

* Manage available dates
* Update monthly availability
* Prevent reservations on unavailable dates

### Reservation System

* Book available villas
* View reservation history
* Reservation validation
* Reservation status management

### Dashboards

#### Guest Dashboard

* View reservations
* Check reservation status
* Access booking history

#### Host Dashboard

* Manage owned villas
* Monitor reservations
* Update villa availability

---

## Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3
* **Templates:** Django Template Language (DTL)
* **Database:** SQLite
* **Authentication:** Django Sessions
* **Version Control:** Git & GitHub

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/alireza85149/RestBox.git
```

### 2. Move into the project

```bash
cd RestBox
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/users/
```

---

## What we Learned

During the development of RestBox, we gained practical experience with:

* Django Models and ORM
* URL Routing
* Function-Based Views
* Django Templates (DTL)
* CRUD Operations
* User Authentication
* Session Management
* Form Handling and Validation
* Database Relationships
* Git and GitHub

---

## Future Improvements

* REST API using Django REST Framework
* PostgreSQL support
* Online payment integration
* Search and filtering
* Reviews and ratings
* Email notifications
* Docker support
* Deployment to the cloud

---

## License

This project is intended for educational and portfolio purposes.
