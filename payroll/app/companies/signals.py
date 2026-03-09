from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import Company

User = get_user_model()

@receiver(post_save, sender=Company)
def create_company_admin(sender, instance, created, **kwargs):
    if created:
        # Define default password
        default_password = 'Password@123'
        
        # Create user using company email
        username = f"admin_{instance.name.lower().replace(' ', '_')}"
        email = instance.email
        
        if not User.objects.filter(email=email).exists():
            user = User.objects.create_user(
                email=email,
                username=username,
                password=default_password,
                company=instance,
                is_staff=True
            )
            
            # Add to Operations Admins group
            ops_group = Group.objects.get(name='Operations Admins')
            user.groups.add(ops_group)
            
            print(f"Automated Admin created for {instance.name}: {email}")
