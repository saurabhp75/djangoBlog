from django.db import models
# imported anually
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # the name and of default image and location of images (profile_pics)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # over ride default save method
    def save(self, **kwargs):
    # def save(self):
        super().save()

        img = Image.open(self.image.path)

        # resize if image is large
        # you can delete old image when user's image is updated
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)