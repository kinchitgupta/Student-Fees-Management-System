# Student Fee Management System

A Django-based web application for managing student registrations, courses, and fee payments across three user roles: **Admin**, **Accountant**, and **Student**.

## Features

### Role-Based Access Control
Session-based authentication with three user types, each redirected to role-specific dashboards. Unauthorized access attempts are redirected to an auth error page.

### Admin
- Register new admins and accountants
- View, edit, and delete accountant records
- Register and manage students
- Register and manage courses (add/edit/delete)
- Enroll students in courses
- Edit/delete fee transactions
- Edit own admin profile
- View detailed student fee summaries (total fee, paid, due)

### Accountant
- Register other accountants and students
- View student and course lists
- Enroll students into courses
- Record fee payments (transactions)
- Edit/delete fee transaction records
- Edit own profile
- Change own password

### Student
- View personal dashboard with enrolled courses and fee history
- View total fees, amount paid, and amount due per course
- Upload/update profile photo
- Change password
- Download a PDF fee receipt (generated via ReportLab) showing payment history and total paid

## Tech Stack
- **Backend:** Django
- **PDF Generation:** ReportLab (`canvas`, `A4` page size)
- **File Storage:** Django `FileSystemStorage` for photo uploads
- **Database:** Django ORM (models: `AdminData`, `AccountantData`, `StudentData`, `StudentCourse`, `CourseData`, `FeesData`, `PhotosData`, `LoginData`)

## Core Models (inferred)

| Model | Purpose |
|---|---|
| `LoginData` | email, password, usertype (auth) |
| `AdminData` | Admin profile info |
| `AccountantData` | Accountant profile info |
| `StudentData` | Student profile, regno |
| `CourseData` | Course catalog (name, cost, duration, description) |
| `StudentCourse` | Enrollment linking student to course + fee/join date |
| `FeesData` | Individual fee payment transactions |
| `PhotosData` | Student profile photo mapping |

## Key URLs / Views (examples)

- `/login/`, `/logout/`
- `/adminhome/`, `/accountanthome/`, `/studenthome/`
- `/adminreg/`, `/accountant_reg/`, `/studentreg/`, `/coursereg/`
- `/show_student/`, `/show_course/`, `/showadmins/`
- `/fees_transitions/`, `/edit_fees/`, `/del_fees/`
- `/uploadphoto/`, `/download_fees_pdf/`

## Setup

```bash
git clone <repo-url>
cd <project-folder>
pip install django reportlab
python manage.py migrate
python manage.py runserver
```

## Known Issues / Areas for Improvement

- Passwords are stored and compared in plain text (`LoginData.objects.get(email=email, password=password)`) — should use Django's built-in password hashing.
- Several views use bare `except:` clauses, which can hide real errors and make debugging difficult.
- Photo deletion via `os.remove` doesn't handle race conditions or validate paths safely.
- No visible CSRF/permission decorators — access control relies entirely on manual session checks inside each view.
- Consider migrating manual `request.session.has_key('usertype')` checks to Django's `@login_required` and custom permission decorators/mixins.

## License

Kinchit Gupta
