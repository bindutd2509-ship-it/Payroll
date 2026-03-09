import os
import sys
import django

# Add the project root to sys.path
sys.path.append(os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_project.settings')
django.setup()

from app.companies.models import Company
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

def verify_automation():
    test_company_name = "Automation Test Corp"
    test_email = "admin@autotest.com"
    
    # Check if company exists, if so delete to start fresh
    Company.objects.filter(name=test_company_name).delete()
    User.objects.filter(email=test_email).delete()
    
    print(f"Creating company: {test_company_name}")
    company = Company.objects.create(
        name=test_company_name,
        email=test_email
    )
    
    # Check if user was created automatically
    user = User.objects.filter(email=test_email).first()
    
    if user:
        print(f"SUCCESS: User automatically created: {user.email}")
        print(f"User linked to company: {user.company.name}")
        
        # Check group
        ops_group = Group.objects.get(name='Operations Admins')
        if ops_group in user.groups.all():
            print("SUCCESS: User added to 'Operations Admins' group.")
        else:
            print("FAILURE: User NOT added to group.")
            
        if user.is_staff:
            print("SUCCESS: User has is_staff=True.")
        else:
            print("FAILURE: User is_staff is False.")
    else:
        print("FAILURE: User was NOT automatically created.")

if __name__ == "__main__":
    verify_automation()
