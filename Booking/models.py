from django.db import models
from Customer.models import Customer
from Room.models import Room
# Create your models here.
class Booking(models.Model):
    booked_by=models.ForeignKey(Customer,related_name='customer',on_delete=models.CASCADE)
    room_booked=models.ForeignKey(Room,related_name="booked_room",on_delete=models.CASCADE)
    booked_at=models.DateTimeField(blank=False,null=False)
    staying_people=models.IntegerField(null=False,blank=False)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"Room No.{self.room_booked.room_number} is booked by {self.booked_by.name} on/for {self.booked_at} for {self.staying_people} person/s."