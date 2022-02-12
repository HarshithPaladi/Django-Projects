import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project1.settings')
import django
django.setup()
from test_models.models import *
from faker import Faker
fakegen = Faker()
def populate(N=5):
    for entry in range(N):
        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        email = fakegen.ascii_email()
        usr = User.objects.get_or_create(first_name=first_name,last_name=last_name,email=email)[0]

if __name__ == '__main__':
    print("Populating Script")
    populate(10)
    print("Populating complete")