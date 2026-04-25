# RecruitFlow - Setup & Installation Guide

Complete guide to set up and run RecruitFlow on your local machine.

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation Steps](#installation-steps)
3. [Environment Configuration](#environment-configuration)
4. [Database Setup](#database-setup)
5. [Running the Application](#running-the-application)
6. [Creating Admin Account](#creating-admin-account)
7. [Troubleshooting](#troubleshooting)
8. [Deployment](#deployment)

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

### Required Software:
- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package manager (comes with Python)
- **Git** - [Download Git](https://git-scm.com/downloads)

### Optional (Recommended):
- **Virtual Environment** - For isolated Python environment
- **PostgreSQL** - For production deployment (SQLite is used for development)

### Check Your Installation:
```bash
# Check Python version
python --version
# Should show: Python 3.8.x or higher

# Check pip version
pip --version
# Should show: pip 20.x.x or higher

# Check Git version
git --version
# Should show: git version 2.x.x or higher
```

---

## 🚀 Installation Steps

### Step 1: Clone the Repository

```bash
# Clone from GitHub
git clone https://github.com/YOUR_USERNAME/recruitflow.git

# Navigate to project directory
cd recruitflow
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

**Linux/Mac:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

**Note:** You should see `(venv)` in your terminal prompt after activation.

### Step 3: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt
```

**This will install:**
- Django 4.2+
- Pillow (for image handling)
- requests (for Web3Forms)
- Other dependencies

---

## 🔧 Environment Configuration

### Step 1: Create .env File

Create a `.env` file in the root directory (same level as manage.py):

```bash
# Copy the example file
cp .env.example .env
```

Or create manually with this content:

```env

SECRET_KEY=your django SECRET_KEY
DEBUG=True
ALLOWED_HOSTS=domain.onrender.com
WEB3FORMS_ACCESS_KEY=your SECRET_KEY 
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your email id 
EMAIL_HOST_PASSWORD=your 16 digits app passoword 


```

### Step 2: Get Web3Forms API Key

1. Visit [https://web3forms.com](https://web3forms.com)
2. Sign up for a free account
3. Create a new form
4. Copy your Access Key
5. Paste it in `.env` file as `WEB3FORMS_ACCESS_KEY`

### Step 3: Generate Django Secret Key (Optional for Development)

For production, generate a new secret key:

```python
# Run in Python shell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output and paste it in `.env` as `SECRET_KEY`.

---

## 🗄️ Database Setup

### Step 1: Run Migrations

```bash
# Create database tables
python manage.py migrate
```

**What this does:**
- Creates SQLite database file (`db.sqlite3`)
- Sets up all tables (users, jobs, applications, interviews, etc.)
- Applies all migration files

**Expected Output:**
```
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_candidateprofile_current_company_and_more... OK
  Applying accounts.0003_recruiterprofile_about_company_and_more... OK
  Applying jobs.0001_initial... OK
  Applying applications.0001_initial... OK
  Applying interviews.0001_initial... OK
  Applying sessions.0001_initial... OK
```

### Step 2: Create Media Directories

```bash
# Create directories for file uploads (if not exist)
mkdir media
mkdir media/resumes
mkdir media/profile_images
mkdir media/company_logos
```

---

## ▶️ Running the Application

### Start Development Server

```bash
python manage.py runserver
```

**Expected Output:**
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 25, 2024 - 10:00:00
Django version 4.2.x, using settings 'recruitflow.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Access the Application

Open your browser and visit:
- **Main Application:** http://localhost:8000
- **Admin Panel:** http://localhost:8000/admin

### Stop the Server

Press `CTRL + C` in the terminal to stop the server.

---

## 👤 Creating Admin Account

### Create Superuser

```bash
python manage.py createsuperuser
```

**You will be prompted to enter:**
```
Username: admin
Email address: admin@example.com
Password: ********
Password (again): ********
```

**Password Requirements:**
- At least 8 characters
- Not too common
- Not entirely numeric

### Access Admin Panel

1. Start the server: `python manage.py runserver`
2. Visit: http://localhost:8000/admin
3. Login with your superuser credentials
4. You can now manage all users, jobs, applications, and interviews

---

## 🎯 First Time Usage

### For Testing as Candidate:

1. Click "Register"
2. Select "Candidate" role
3. Fill in registration details
4. Login and complete your profile
5. Browse jobs and apply

### For Testing as Recruiter:

1. Click "Register"
2. Select "Recruiter" role
3. Fill in company details
4. Login and post a job
5. View applicants and manage applications

---

## 🔧 Troubleshooting

### Issue: "No module named 'django'"

**Solution:**
```bash
# Make sure virtual environment is activated
# Then reinstall dependencies
pip install -r requirements.txt
```

### Issue: "Port 8000 is already in use"

**Solution:**
```bash
# Use a different port
python manage.py runserver 8080

# Or find and kill the process using port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux/Mac:
lsof -ti:8000 | xargs kill -9
```

### Issue: "CSRF verification failed"

**Solution:**
- Clear browser cookies
- Make sure `{% csrf_token %}` is in all forms
- Check if `CSRF_COOKIE_SECURE` is False in development

### Issue: "Static files not loading"

**Solution:**
```bash
# Collect static files
python manage.py collectstatic

# Make sure DEBUG=True in development
```

### Issue: "Image upload not working"

**Solution:**
```bash
# Install Pillow
pip install Pillow

# Check media directories exist
mkdir media/resumes media/profile_images media/company_logos
```

---

## 🚀 Deployment

### For Production Deployment:

1. **Update Settings:**
   ```python
   # In .env file
   
SECRET_KEY=your django SECRET_KEY
DEBUG=False
ALLOWED_HOSTS=domain.onrender.com
WEB3FORMS_ACCESS_KEY=your SECRET_KEY 
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your email id 
EMAIL_HOST_PASSWORD=your 16 digits app passoword 


   ```

2. **Use PostgreSQL Database:**
   ```bash
   pip install psycopg2-binary
   ```

3. **Collect Static Files:**
   ```bash
   python manage.py collectstatic
   ```

4. **Use Production Server:**
   - Gunicorn (Linux)
   - Waitress (Windows)
   - Or deploy to: Render, Railway, PythonAnywhere, Heroku

### Recommended Platforms:

- **Render** - Free tier available, PostgreSQL included
- **Railway** - Easy deployment with GitHub integration
- **PythonAnywhere** - Python-specific hosting
- **Heroku** - Popular platform with add-ons

---

## 📝 Additional Commands

### Create New Migrations (After Model Changes)
```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Django Shell
```bash
python manage.py shell
```

### Check for Issues
```bash
python manage.py check
```

### View All Migrations
```bash
python manage.py showmigrations
```

### Create Test Data (Optional)
```bash
python manage.py loaddata fixtures/sample_data.json
```

---

## 🆘 Getting Help

If you encounter any issues:

1. Check the [Troubleshooting](#troubleshooting) section
2. Review Django documentation: https://docs.djangoproject.com
3. Open an issue on GitHub
4. Contact support

---

## ✅ Setup Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed from requirements.txt
- [ ] .env file created with Web3Forms key
- [ ] Database migrations applied
- [ ] Media directories created
- [ ] Superuser account created
- [ ] Development server running
- [ ] Application accessible at localhost:8000
- [ ] Admin panel accessible at localhost:8000/admin

---

**Congratulations! 🎉 Your RecruitFlow application is now set up and ready to use!**
