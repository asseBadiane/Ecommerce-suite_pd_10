"""
Si c'est Google
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.google.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "ton mail Google"
EMAIL_HOST_PASSWORD = "ton mot de passe Google"
EMAIL_USE_TLS = True




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jaba_local',
        'USER': 'username',
        'PASSWORD': 'password!',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
"""

# PAydunya
PAYDUNYA_ACCESS_TOKENS = {
    'PAYDUNYA-MASTER-KEY': "",
    'PAYDUNYA-PRIVATE-KEY': "",
    'PAYDUNYA-TOKEN': "",
}