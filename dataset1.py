from home.models import Blog, CustomUser  # Replace 'your_app' with your actual app name
from faker import Faker

fake = Faker()

# Select 3 random authors from the provided list
authors = [ "angelaclark", "joelcohen","justinkoch","frank21","qstevens","taylor49","kanerebecca","tylergray","cody34"]
selected_authors = CustomUser.objects.filter(username__in=authors)

# Create 3 blog posts
for author in selected_authors:
    for i in range(3):  
        blog = Blog.objects.create(
            title=fake.sentence(nb_words=6),  # Random title
            content=fake.paragraph(nb_sentences=15),  # Random content
            author=author,
            likes=fake.random_int(min=0, max=500)  # Random number of likes
        )
        print(f"Created Blog: {blog.title} by {author.username}")
