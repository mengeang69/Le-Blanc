import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leblanc_backend.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "reachzin"
email = "admin@leblanc.com"
password = "YourSecretPassword123"  # <-- Change this to your preferred password

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created successfully.")
else:
    # If the user exists, update the password to ensure you can log in
    u = User.objects.get(username=username)
    u.set_password(password)
    u.save()
    print(f"Password updated for '{username}'.")