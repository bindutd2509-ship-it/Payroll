import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-replace-this-with-a-real-one-in-production'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    'corsheaders',

    # Local apps
    'app.core',
    'app.accounts',
    'app.companies',
    'app.organization',
    'app.employees',
    'app.salary',
    'app.leave_management',
    'app.attendance_app',
    'app.audit',
    'app.reimbursements',
    'app.taxation',
    'app.loans',
    'payroll',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'employee_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'employee_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "payroll_db",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
AUTH_USER_MODEL = 'accounts.User'

# REST Framework Settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

CORS_ALLOW_ALL_ORIGINS = True

# JWT Settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': False,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# ──────────────────────────────────────────────
#  Payroll App Constants (Moved from payroll/settings.py)
# ──────────────────────────────────────────────
PAYROLL_STATUS_DRAFT = 'Draft'
PAYROLL_STATUS_GENERATED = 'Generated'
PAYROLL_STATUS_FINALIZED = 'Finalized'
PAYROLL_STATUS_LOCKED = 'Locked'
PAYROLL_STATUS_PAID = 'Paid'

PAYROLL_STATUS_CHOICES = (
    (PAYROLL_STATUS_DRAFT, 'Draft'),
    (PAYROLL_STATUS_GENERATED, 'Generated'),
    (PAYROLL_STATUS_FINALIZED, 'Finalized'),
    (PAYROLL_STATUS_LOCKED, 'Locked'),
    (PAYROLL_STATUS_PAID, 'Paid'),
)

COMPONENT_TYPE_EARNING = 'Earning'
COMPONENT_TYPE_DEDUCTION = 'Deduction'

COMPONENT_TYPE_CHOICES = (
    (COMPONENT_TYPE_EARNING, 'Earning'),
    (COMPONENT_TYPE_DEDUCTION, 'Deduction'),
)

DEFAULT_PF_RATE = 12.0
DEFAULT_PF_EMPLOYER_RATE = 12.0
DEFAULT_ESI_RATE = 0.75
DEFAULT_ESI_EMPLOYER_RATE = 3.25

DEFAULT_PAYROLL_CYCLE = 'Monthly'
PAYROLL_CYCLE_CHOICES = (
    ('Monthly', 'Monthly'),
    ('Fortnightly', 'Fortnightly'),
    ('Weekly', 'Weekly'),
)

PAYSLIP_PREFIX = 'PS-'
ALLOW_PAYSLIP_DOWNLOAD_AFTER_FINAL_ONLY = True
INCLUDE_COMPANY_LOGO_IN_PAYSLIP = True

PAYROLL_SETTINGS = {
    'STATUS_DRAFT': PAYROLL_STATUS_DRAFT,
    'STATUS_GENERATED': PAYROLL_STATUS_GENERATED,
    'STATUS_FINALIZED': PAYROLL_STATUS_FINALIZED,
    'STATUS_LOCKED': PAYROLL_STATUS_LOCKED,
    'STATUS_PAID': PAYROLL_STATUS_PAID,
    'STATUS_CHOICES': PAYROLL_STATUS_CHOICES,
    'COMPONENT_TYPE_EARNING': COMPONENT_TYPE_EARNING,
    'COMPONENT_TYPE_DEDUCTION': COMPONENT_TYPE_DEDUCTION,
    'COMPONENT_TYPE_CHOICES': COMPONENT_TYPE_CHOICES,
    'DEFAULT_PF_RATE': DEFAULT_PF_RATE,
    'DEFAULT_ESI_RATE': DEFAULT_ESI_RATE,
    'DEFAULT_PAYROLL_CYCLE': DEFAULT_PAYROLL_CYCLE,
    'PAYROLL_CYCLE_CHOICES': PAYROLL_CYCLE_CHOICES,
    'PAYSLIP_PREFIX': PAYSLIP_PREFIX,
    'ALLOW_PAYSLIP_DOWNLOAD_AFTER_FINAL_ONLY': ALLOW_PAYSLIP_DOWNLOAD_AFTER_FINAL_ONLY,
}
