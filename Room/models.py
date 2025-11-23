from django.db import models
import os
# Create your models here.
class Room(models.Model):
    ROOM_TYPES=(
        ('double_room','Double'),
        ('single_room','Single')
    )
    ROOM_STATUS=(
        ('available','Available'),
        ('occupied','Occupied'),
        ('under_maintenance','Under Maintenance')
    )
    room_number=models.IntegerField(blank=False,null=False)
    type=models.CharField(max_length=20,choices=ROOM_TYPES)
    status=models.CharField(max_length=50,choices=ROOM_STATUS,blank=False,null=False)
    status=models.CharField(choices=ROOM_STATUS,blank=False,null=False)
    price=models.IntegerField(blank=False,null=False)
    image=models.ImageField(upload_to='room_images/')
    added_on=models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    def save(self, *args, **kwargs):
        if self.image:
            # Get the extension of the uploaded file
            ext = os.path.splitext(self.image.name)[1]
            # Set filename as room number + extension
            self.image.name = f"{self.room_number}{ext}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.room_number} is added on {self.added_on}"
