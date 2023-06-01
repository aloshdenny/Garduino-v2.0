from django.db import models

# Create your models here.

class PlantData(models.Model):
    
    # All required data from plant
    name = models.CharField(max_length=50, default="Not set")
    temp = models.FloatField(default=0.0)
    humidity = models.FloatField(default=0.0)
    next_spray = models.IntegerField(default=0) # Actually pump status
    fertilizer_level = models.FloatField(default=0.0)
    led_intensity = models.FloatField(default=0.0)
    time_to_sundown = models.TimeField()
    status = models.CharField(max_length=20, default="No stats")

    def __str__(self):
        return f"Plant: {self.name}"