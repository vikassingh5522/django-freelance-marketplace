

## 📌 Project Description

### 🖥️ Overview

This project is a **Freelancing Marketplace Platform** built with **Django (Python)** as the backend and a responsive **HTML + CSS (Bootstrap) + JavaScript frontend**. It demonstrates a complete full-stack web application where users can register, manage profiles, interact with the system through APIs, and access the Django admin dashboard for backend management.



### ⚙️ Tech Stack

* **Backend:** Python 3, Django 5.0, Django REST Framework
* **Database:** SQLite3 (default Django DB)
* **Frontend:** HTML5, CSS3, Bootstrap, JavaScript
* **Admin Panel:** Django’s built-in admin (`django.contrib.admin`)
* **API:** Django REST Framework for RESTful APIs
* **Static Files:** Managed via Django `STATICFILES_DIRS`

---

### 🚀 Features

* ✅ User authentication & authorization
* ✅ Admin dashboard for managing users, data, and system configurations
* ✅ SQLite database integration
* ✅ REST APIs for frontend–backend communication
* ✅ Mobile-friendly responsive UI with Bootstrap
* ✅ Organized folder structure for templates and static files

---

### 📂 Project Structure

```
vikassingh2/
│── vikassingh2/          # Main project settings
│   ├── settings.py       # Django project settings
│   ├── urls.py           # URL routing
│   ├── wsgi.py           # WSGI application
│
│── application/          # Custom Django app
│   ├── models.py         # Database models
│   ├── views.py          # Backend views & APIs
│   ├── urls.py           # App-specific URLs
│   ├── serializers.py    # API serializers (DRF)
│
│── templates/            # HTML templates (frontend)
│── static/               # CSS, JS, Images
│── db.sqlite3            # SQLite database
│── manage.py             # Django management script
```

---

### ⚡ How to Run Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/django-freelance-marketplace.git
   cd django-freelance-marketplace
   ```

2. Create & activate virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Run development server:

   ```bash
   python manage.py runserver
   ```

7. Visit:

   * App → [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   * Admin → [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

project img detail 

<img width="1863" height="974" alt="Screenshot 2025-09-15 230045" src="https://github.com/user-attachments/assets/06702b59-5e39-44f3-bc31-5b7fcb0906e8" />
<img width="1901" height="903" alt="Screenshot 2025-09-15 221916" src="https://github.com/user-attachments/assets/26e98182-ca1a-4d6c-9034-96dcdf38050c" />
<img width="1919" height="891" alt="Screenshot 2025-09-15 221951" src="https://github.com/user-attachments/assets/47c32be8-06a3-4b80-a9fc-dab310c2508d" />
<img width="1857" height="871" alt="Screenshot 2025-09-15 222022" src="https://github.com/user-attachments/assets/ec59f68f-8be7-4f73-a10b-64640701ff92" />
<img width="1904" height="886" alt="Screenshot 2025-09-15 225543" src="https://github.com/user-attachments/assets/2d7f018b-1ac5-4890-86b6-f3708a057c3a" />
<img width="1910" height="885" alt="Screenshot 2025-09-15 221831" src="https://github.com/user-attachments/assets/315664f3-0f8e-4cab-be9f-54fff5219f45" />
<img width="1909" height="892" alt="Screenshot 2025-09-15 221802" src="https://github.com/user-attachments/assets/80a8ff48-86a0-44ce-946a-8d55dbc10773" />
<img width="1890" height="888" alt="Screenshot 2025-09-15 221717" src="https://github.com/user-attachments/assets/33b5a60a-e129-4b26-927e-c96fd364800d" />
<img width="1891" height="890" alt="Screenshot 2025-09-15 221725" src="https://github.com/user-attachments/assets/eb6ff36d-18c7-49ee-833b-f3acd85b036d" />

































































  
