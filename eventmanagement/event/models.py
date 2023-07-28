from django.db import models
from django.contrib.auth.models import User

# Create your mod
options = (
    ('accept with pleasure', 'Accept with pleasure'),
    ('Regretfully Decline', 'Regretfully Decline'),
    ('others', 'Others')
)

class Eventcreation(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100)


class Rsvp(models.Model):
    EVENT_CHOICES = (
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        # Add more options as needed
    )
    rsvp = models.CharField(
        max_length=30,
        choices=EVENT_CHOICES,
        default='others',
        null=True,
        blank=False
    )
    event = models.ForeignKey(Eventcreation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
