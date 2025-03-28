# LibraryProject

This is a basic Django project created for learning purposes.

## Setup Instructions
1. Install Django:  
   ```bash
   pip install django

# LibraryProject - Secure Django Application

This project is a Django-based library management system with enforced HTTPS for secure web communication.

## 🔒 Security Enhancements

The following security features have been implemented:

### 1️⃣ Enforcing HTTPS
- `SECURE_SSL_REDIRECT = True` → Redirects all HTTP requests to HTTPS.
- `SECURE_HSTS_SECONDS = 31536000` → Enforces HTTPS for 1 year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True` → Applies HTTPS to all subdomains.
- `SECURE_HSTS_PRELOAD = True` → Preloads HTTPS for better security.

### 2️⃣ Secure Cookies
- `SESSION_COOKIE_SECURE = True` → Session cookies are only sent over HTTPS.
- `CSRF_COOKIE_SECURE = True` → CSRF tokens are only sent over HTTPS.

### 3️⃣ Security Headers
- `X_FRAME_OPTIONS = 'DENY'` → Prevents clickjacking attacks.
- `SECURE_CONTENT_TYPE_NOSNIFF = True` → Prevents MIME-type security risks.
- `SECURE_BROWSER_XSS_FILTER = True` → Enables browser's XSS filtering.

## 🔧 Running the Server with HTTPS Locally
To run the Django development server with HTTPS, use:

```bash
python manage.py runserver_plus --cert-file cert.pem

