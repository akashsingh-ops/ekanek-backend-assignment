# EkAnek Backend Assignment

This is a backend system built with **Python + Django + Django REST Framework** that allows verified users to upload and manage sensitive data in the form of large files (up to 1GB), with functionality for private access and public sharing via tiny URLs.

---

## 🧩 Features Implemented

- ✅ User login with email and password
- ✅ Token-based authentication
- ✅ File upload with metadata (title, description)
- ✅ Automatic file type detection
- ✅ File listing (private to logged-in user)
- ✅ File deletion
- ✅ Public sharing via short URL
- ✅ Public file download (no auth needed)
- ⚠️ Optional compression logic ready (can be added)
- ✅ Fully RESTful API with clean structure

---

## 🚀 Tech Stack

- **Python 3**
- **Django**
- **Django REST Framework**
- **Token Authentication**
- **SQLite (default) / PostgreSQL compatible**
- **Postman for testing**

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/akashsingh-ops/ekanek-backend-assignment.git
cd ekanek-backend-assignment

### 2. Create and Activate Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate

### 🔹 **Step 4: Run Migrations and Create Admin User**

Already covered here:

```markdown
###3. Run Migrations and Create Admin User

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

### 🔹 **Step 5: Run the Development Server**

Already included:

```markdown
### 4. Run the Development Server

```bash
python manage.py runserver
