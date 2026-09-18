from django.shortcuts import render, get_object_or_404
from .models import Project


def home(request):
    context = {
        'name': 'Md Farhan Hossain Sami',
        'role': 'Student · Researcher',
        'intro': (
            "I'm a Computer Science & Engineering student at Independent University, Bangladesh, "
            "currently working as a research intern at CASSA on a Transiting Array Radio Telescope. "
            "I enjoy building things at the intersection of robotics, software, and astronomy."
        ),
        'skills': [
            'Python', 'C++', 'JavaScript', 'ROS2', 'Arduino IDE',
            'GitHub', 'PyCharm', 'VS Code', 'Google Colab', 'Overleaf',
        ],
    }
    return render(request, 'my_app/home.html', context)


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'my_app/projects.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'my_app/project_detail.html', {'project': project})


def about(request):
    education = [
        {
            'degree': 'B.Sc. in Computer Science & Engineering (CSE)',
            'school': 'Independent University, Bangladesh (IUB)',
            'period': '2023 – Present',
            'details': 'Coursework: Machine Learning, Digital Logic Design, Microprocessor, Data Structures, Web Development, Artificial Intelligence.',
        },
        {
            'degree': 'Higher Secondary Certificate (HSC) — Science',
            'school': 'Milestone College, Dhaka',
            'period': '2021',
            'details': 'Achieved strong academic performance with a focus on Science.',
        },
    ]

    experience = [
        {
            'role': 'Research Intern',
            'org': 'Center for Astronomy, Space Science and Astrophysics (CASSA), IUB',
            'period': 'Since 11 Oct 2025',
            'details': (
                'Contributing to the development of a Transiting Array Radio Telescope (TART). '
                'Responsible for hardware setup, system integration, and data calibration to ensure '
                'accurate radio signal acquisition and analysis.'
            ),
        },
    ]

    workshops = [
        {
            'title': 'Robotics Workshop Competition (3 Days)',
            'details': 'Hands-on with ROS2, RViz visualization, robot kinematics and simulation. Achieved First Prize.',
        },
        {
            'title': 'AI & Machine Learning Workshop (Nov 27–29, 2025)',
            'details': 'Covered ML foundations, CNNs for image processing, and NLP for text analysis; built and deployed models end-to-end.',
        },
    ]

    skill_groups = [
        ('Programming', ['Python', 'C++', 'JavaScript']),
        ('Software & Tools', ['GitHub', 'VS Code', 'PyCharm', 'Arduino IDE', 'ROS2', 'Canva', 'Google Colab', 'MS Office', 'Overleaf']),
        ('Research', ['Transiting Array Radio Telescope (Ongoing)']),
        ('Soft Skills', ['Analytical & Problem-Solving', 'Communication & Clarity']),
        ('Languages', ['Bangla', 'English']),
    ]

    context = {
        'education': education,
        'experience': experience,
        'workshops': workshops,
        'skill_groups': skill_groups,
    }
    return render(request, 'my_app/about.html', context)
