# Chai aur Tweet 🍵🐦

A Django-based Twitter-style microblogging platform where users can share thoughts, images, and engage with content in a clean, responsive interface.

## ✨ Features

- **User Authentication**: Secure registration, login, and logout system
- **Tweet Management**: Create, read, update, and delete tweets with image support
- **Smart Routing**: Intelligent navigation based on user authentication status
- **Global Feed**: Browse tweets from all users (read-only for guests)
- **Personal Dashboard**: Manage your own tweets with full CRUD operations
- **Responsive Design**: Modern UI built with Bootstrap 5 and custom CSS
- **Image Uploads**: Support for photo attachments using Django ImageField
- **Security**: CSRF protection, user ownership validation, and secure forms

## 🚀 Live Demo

Visit the application: [Your Live URL Here]

## 🛠️ Technology Stack

- **Backend**: Django 5.2.5, Python 3.13
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.3, JavaScript
- **Image Processing**: Pillow 11.3.0
- **Authentication**: Django's built-in user system
- **Deployment**: Development server (ready for production deployment)

## 📋 Prerequisites

- Python 3.8+
- pip (Python package installer)
- Git

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/chai-aur-tweet.git
   cd chai-aur-tweet/tweets
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r ../requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser**
   Navigate to `http://127.0.0.1:8000/`

## 📱 Usage

### For Guests (Not Logged In)
- Browse the global feed of tweets from all users
- Register for a new account
- Login to existing account

### For Registered Users
- **Homepage**: View global feed and access personal features
- **My Tweets**: Manage your own tweets (create, edit, delete)
- **Create Tweet**: Share new thoughts with optional image uploads
- **Edit/Delete**: Full control over your content

## 🏗️ Project Structure

```
tweets/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── tweets/               # Project settings and configuration
│   ├── __init__.py
│   ├── settings.py       # Django settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── myapp/                # Main application
│   ├── models.py        # Tweet and User models
│   ├── views.py         # View functions and logic
│   ├── forms.py         # Django forms
│   ├── urls.py          # App-specific URLs
│   └── templates/       # HTML templates
│       ├── index.html
│       ├── tweet_list.html
│       ├── tweet_form.html
│       └── registration/
│           ├── login.html
│           ├── register.html
│           └── logged_out.html
├── static/               # Static files (CSS, JS, images)
│   └── css/
│       └── app.css
└── templates/            # Base templates
    └── layout.html
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Database
The project uses SQLite3 by default. To use PostgreSQL or MySQL, update `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🎨 Customization

### Styling
- Modify `static/css/app.css` for custom styles
- Update Bootstrap classes in templates
- Customize color scheme in CSS variables

### Features
- Add like/comment functionality
- Implement user profiles
- Add search and filtering
- Create hashtag system

## 🚀 Deployment

### Production Settings
1. Set `DEBUG = False` in `settings.py`
2. Configure production database
3. Set up static file serving
4. Configure `ALLOWED_HOSTS`
5. Use environment variables for sensitive data

### Deployment Options
- **Heroku**: Easy deployment with Git
- **DigitalOcean**: VPS deployment
- **AWS**: Scalable cloud deployment
- **Docker**: Containerized deployment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Team
- Python Community
- Open Source Contributors

## 📞 Support

If you have any questions or need help:
- Open an issue on GitHub
- Contact: [your-email@example.com]
- Project Link: [https://github.com/yourusername/chai-aur-tweet](https://github.com/yourusername/chai-aur-tweet)

---

**Made with ❤️ using Django and Bootstrap**

⭐ **Star this repository if you found it helpful!**
