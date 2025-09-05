# Django Online Course Assessment Platform

A comprehensive Django web application that provides an online course platform with integrated assessment and grading system. This project serves as the capstone final project for the **IBM "Developing Applications with SQL Databases and Django"** course on [Coursera](https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/home/welcome).

## 📚 Course Context

This project was developed as part of the IBM course curriculum, demonstrating practical application of:

- Django web framework fundamentals
- Database modeling and relationships
- User authentication and authorization
- Template rendering and Bootstrap styling
- Assessment and grading systems
- Django admin interface configuration

## 🚀 Features

### ✅ **Implemented Assessment Features**

- **Question, Choice, and Submission Models** - Complete database schema for assessments
- **Admin Interface** - Full administrative controls for managing courses and assessments
- **Course Details Page** - Bootstrap-styled course presentation with integrated assessments
- **Assessment Submission System** - Student answer submission and processing
- **Exam Results Display** - Detailed results with scoring and feedback
- **User Authentication** - Login/signup system with session management

### 🎯 **Key Functionality**

- **Multi-Course Support** - Manage multiple courses with lessons and assessments
- **Question Banking** - Multiple choice questions with configurable point values
- **Automatic Grading** - Real-time scoring with percentage calculations
- **Result Analytics** - Detailed breakdown of correct/incorrect answers
- **Responsive Design** - Mobile-friendly Bootstrap interface
- **Admin Dashboard** - Complete course and assessment management

## 🛠 **Technology Stack**

- **Backend:** Django 5.2.6
- **Database:** SQLite (development)
- **Frontend:** Bootstrap 5.1.3, HTML5, CSS3
- **Icons:** Font Awesome 6.0
- **Image Processing:** Pillow 11.3.0
- **Authentication:** Django built-in auth system

## 📦 **Installation & Setup**

### **Prerequisites**

- Python 3.8+ installed
- pip package manager

### **Quick Start**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ahmedelhadi17776/onlinecourse.git
   cd onlinecourse
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create Superuser**

   ```bash
   python manage.py createsuperuser
   ```

5. **Run Development Server**

   ```bash
   python manage.py runserver
   ```

6. **Access the Application**
   - Main Site: http://localhost:8000/
   - Admin Interface: http://localhost:8000/admin/

## 🎓 **Sample Data**

The project includes pre-configured sample data:

### **Courses Available:**

1. **Introduction to Python Programming**
   - 2 lessons with assessment questions
   - Topics: Variables, Data Types, Control Structures, Functions
2. **Web Development with Django**
   - 1 lesson with assessment questions
   - Topics: Django Models and Database

### **Test Accounts:**

- **Admin:** `admin` / `admin123`
- **Student:** `student` / `student123`

## 🏗 **Project Structure**

```
onlinecourse/
├── course/                     # Main Django app
│   ├── models.py              # Data models (Course, Question, Choice, Submission)
│   ├── views.py               # View functions (course display, assessment handling)
│   ├── admin.py               # Admin interface configuration
│   ├── urls.py                # URL routing
│   └── templates/course/      # HTML templates
│       ├── index.html         # Course listing page
│       ├── course_detail_bootstrap.html  # Course details with assessments
│       ├── exam_result.html   # Assessment results page
│       ├── login.html         # User login
│       └── signup.html        # User registration
├── onlinecourse_project/      # Django project settings
├── requirements.txt           # Python dependencies
├── manage.py                  # Django management script
└── db.sqlite3                 # Database file
```

## 🎯 **Assessment System**

### **For Students:**

1. Browse available courses
2. Register/Login to access assessments
3. Answer multiple-choice questions
4. Submit assessment for immediate grading
5. View detailed results with correct answers

### **For Instructors (Admin):**

1. Access Django admin interface
2. Create/manage courses and lessons
3. Add assessment questions with multiple choices
4. Mark correct answers for automatic grading
5. View student submissions and results

## 🔧 **Development Notes**

### **Key Models:**

- **Course** - Course information with instructors and enrollment data
- **Lesson** - Individual lessons within courses
- **Question** - Assessment questions linked to lessons
- **Choice** - Multiple choice options with correct answer flags
- **Submission** - Student assessment submissions with selected answers

### **Assessment Logic:**

- Questions support configurable point values
- Automatic scoring based on correct choice selection
- Percentage calculation with grade thresholds
- Detailed feedback showing correct vs. selected answers

## 🎓 **Learning Outcomes**

This project demonstrates mastery of:

- Django ORM and database relationships
- User authentication and session management
- Template inheritance and Bootstrap integration
- Form handling and data validation
- Admin interface customization
- Assessment and grading system implementation

## 📝 **IBM Course Reference**

This project fulfills the requirements of the IBM "Developing Applications with SQL Databases and Django" final project. The course curriculum covered:

- Django framework fundamentals
- SQL database integration
- Model-View-Template (MVT) architecture
- User management and authentication
- Web application deployment concepts

**Course Link:** [IBM - Developing Applications with SQL Databases and Django](https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/home/welcome)

## 🚀 **Future Enhancements**

Potential improvements for production deployment:

- PostgreSQL database integration
- Docker containerization
- AWS/Heroku deployment
- Email notifications for assessment completion
- Advanced analytics and reporting
- File upload capabilities for course materials

