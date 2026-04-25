# RecruitFlow - Recruitment & Interview Management System

A modern, production-ready recruitment platform built with Django for managing job postings, applications, and interviews.

![Django](https://img.shields.io/badge/Django-4.2+-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Overview

RecruitFlow is a comprehensive recruitment management system that streamlines the hiring process for companies and job seekers. It features role-based authentication, applicant tracking, interview scheduling, and a modern responsive UI.

## ✨ Key Features

### For Candidates
- 🔐 Secure registration and authentication
- 📝 Comprehensive profile with structured fields (education, experience, skills)
- 🔍 Advanced job search and filtering
- 📄 Resume upload and management
- 📊 Application tracking dashboard
- 📅 Interview schedule management
- 🔗 Social media integration (LinkedIn, GitHub, Portfolio)

### For Recruiters
- 🏢 Company profile management
- 📢 Job posting with detailed descriptions
- 👥 Applicant management with filtering
- 📥 Resume download and candidate profiles
- ✅ Application status tracking (Applied → Shortlisted → Interview → Selected/Rejected)
- 📆 Interview scheduling system
- 📈 Dashboard with analytics

### For Admins
- 🛠️ Full Django admin panel access
- 👤 User management (candidates, recruiters)
- 📋 Job and application oversight
- 🗑️ Content moderation

## 🛠️ Tech Stack

- **Backend:** Django 4.2+, Python 3.8+
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **Database:** SQLite 
- **Authentication:** Django built-in auth with role-based access
- **File Storage:** Django media files
- **UI/UX:** Modern purple theme with responsive design

## 📋 Database Models

- **User** - Extended Django user with role-based authentication
- **CandidateProfile** - Detailed candidate information with structured fields
- **RecruiterProfile** - Company and recruiter information
- **Job** - Job postings with requirements and details
- **Application** - Job applications with status tracking
- **Interview** - Interview scheduling and management
- **Notification** - Real-time user notifications

## 🎨 UI Features

- ✅ Modern purple-pink gradient theme
- ✅ Fully responsive (mobile, tablet, desktop)
- ✅ Glass morphism effects
- ✅ Smooth animations and transitions
- ✅ Touch-friendly interface
- ✅ Professional typography (Inter font)
- ✅ Accessible design with proper focus states

## 📱 Responsive Design

The application is fully optimized for:
- 📱 Mobile devices
- 📱 Tablets
- 💻 Desktops
- 🖱️ Touch and mouse interactions

## 🚀 Quick Start

See [SETUP.md](SETUP.md) for detailed installation instructions.

```bash
# Clone repository
https://github.com/cvenkataravikiran/RecruitFlow.git
cd recruitflow

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
```

Visit: http://localhost:8000

## 📂 Project Structure

```
RecruitFlow/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── SETUP.md                     # Installation guide
├── .gitignore                   # Git ignore rules
│
├── recruitflow/                 # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── accounts/                    # User authentication & profiles
├── jobs/                        # Job posting management
├── applications/                # Application tracking
├── interviews/                  # Interview scheduling
├── dashboard/                   # User dashboards
│
├── templates/                   # HTML templates
│   ├── base.html
│   ├── navbar.html
│   ├── footer.html
│   └── [app-specific templates]
│
└── static/                      # CSS and JavaScript
    ├── css/style.css
    └── js/main.js
```

## 🔐 Security Features

- ✅ CSRF protection on all forms
- ✅ Password hashing (PBKDF2)
- ✅ Role-based access control
- ✅ Secure file upload validation
- ✅ XSS and SQL injection prevention
- ✅ Session management

## 🌐 Environment Variables

Create a `.env` file in the root directory:

```env

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

Get Web3Forms key from: https://web3forms.com

## 📸 Screenshots

### Home Page
Modern landing page with job listings and search functionality.

### Candidate Dashboard
Comprehensive dashboard showing profile completeness, applications, and interviews.

### Recruiter Dashboard
Analytics dashboard with job statistics and recent applications.

### Profile Management
Structured profile forms with separate fields for education, experience, and skills.

## 🎯 Use Cases

- **Startups** - Manage hiring process efficiently
- **HR Departments** - Track applications and schedule interviews
- **Job Seekers** - Find jobs and track applications
- **Recruitment Agencies** - Manage multiple job postings

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.


## 🔗 Links

- **Live Demo:** [Coming Soon]
- **Documentation:** [SETUP.md](SETUP.md)
- **Issues:** [GitHub Issues](https://github.com/YOUR_USERNAME/recruitflow/issues)
