# Md Farhan Hossain Sami — Personal Portfolio

A personal portfolio website built with Django, showcasing my education,
research experience, skills, and projects in robotics, IoT, and software.

## Features

- **Home page** — introduction, current role, and skill highlights
- **Projects page** — all projects pulled from the database, displayed as cards
- **Project details page** — full description, technology used, and GitHub link
  for each project (dynamic routing: `/projects/<id>/`)
- **About page** — education timeline, experience, grouped skills, workshops,
  and a contact section
- **Django Admin** — add, edit, and delete projects (with image previews)
  through `/admin/`
- Fully responsive design with a dark "charm" theme (navy + gold), built with
  plain HTML/CSS — no frontend framework required

## Technologies Used

- Python 3
- Django (backend framework, MVT pattern)
- SQLite (default database)
- HTML5 / CSS3 (custom, no CSS framework)
- Pillow (for project image uploads)

## Project Structure

```
portfolio/
├── manage.py
├── requirements.txt
├── myproject/          # Django project settings, URLs
└── my_app/              # Main app
    ├── models.py         # Project model
    ├── views.py          # Home, Projects, Project Detail, About
    ├── urls.py
    ├── admin.py          # Admin panel config
    ├── fixtures/         # Sample project data
    ├── static/my_app/    # CSS + images
    └── templates/my_app/ # HTML templates
```

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd portfolio
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your profile photo**
   Place a photo named `profile.jpg` inside:
   `my_app/static/my_app/images/`

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **(Optional) Load sample projects**
   ```bash
   python manage.py loaddata my_app/fixtures/initial_projects.json
   ```

7. **Create an admin account**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. Open `http://127.0.0.1:8000/` in your browser.
   Visit `http://127.0.0.1:8000/admin/` to manage projects.

## Screenshots

_Add screenshots of your Home, Projects, Project Detail, and Admin pages here
before submission._

## Author

**Md Farhan Hossain Sami**
Email: mdfarhanhossainsami@gmail.com
GitHub: [tenacioussami](https://github.com/tenacioussami)
LinkedIn: [mdfarhanhossainsami](https://linkedin.com/in/mdfarhanhossainsami)
