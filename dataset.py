from home.models import CustomUser  # Replace 'your_app' with your actual app name
from faker import Faker

fake = Faker()

for _ in range(10):
    user = CustomUser.objects.create_user(
        username=fake.user_name(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        password="Test@1234"  # Set a default password
    )
    print(f"Created user: {user.username}")
