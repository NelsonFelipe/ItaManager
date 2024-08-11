from django.db import models

class Cultural_Event(models.Model):
    EVENT_TYPES = [
        ('show', 'Show'),
        ('theatre', 'Apresentação Teatral'),
        ('orchestra', 'Orquestra'),
        ('musical', 'Musical'),
        ('comedy', 'Show de Humor'),
       
    ]
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    title = models.CharField(max_length=100)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_free = models.BooleanField(default=False)
    location = models.CharField(max_length=200)
    time = models.TimeField()
    city = models.CharField(max_length=100)
    seats = models.PositiveIntegerField(null=True, blank=True)

    
    def __str__(self):
        return self.title
        