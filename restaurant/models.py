from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length = 255, null=False)
    no_of_guests = models.IntegerField()
    reservation_date = models.DateTimeField()

    def __str__(self):
        return self.name

class MenuItem(models.Model):
   title = models.CharField(max_length = 255)
   price = models.DecimalField(max_digits = 6, decimal_places = 2)
   inventory = models.SmallIntegerField()

   def __str__(self):
      return f'{self.title} : {str(self.price)}'