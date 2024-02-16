from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class MovieModel(models.Model):
    image = models.ImageField(upload_to='movies/', null=True, blank=True)
    background = models.ImageField(upload_to='movies/', null=True, blank=True)
    moviename = models.CharField(max_length = 50)
    runtime = models.CharField(max_length = 10, null=True, blank=True)
    certificate = models.CharField(max_length = 10, null=True, blank=True)
    screentype = models.CharField(max_length = 50)
    genre = models.CharField(max_length = 50)
    release_date = models.DateField()
    about = models.CharField(max_length = 1000, null=True, blank=True)
    languages = models.CharField(max_length = 50)
    trailer_link = models.URLField(null=True, blank=True)


    cast = models.ManyToManyField('CastModel', related_name='movies_cast_members', blank=True)
    crew = models.ManyToManyField('CrewModel', related_name='movies_crew_members', blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.cast.add(*self.cast.all())
        self.crew.add(*self.crew.all())


    def __str__(self):
        return self.moviename
    

class RatingModel(models.Model):
    movie = models.ForeignKey(MovieModel, on_delete=models.CASCADE, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    reviews = models.TextField(null=True, blank=True)

    

class CastModel(models.Model):
    actor_name = models.CharField(max_length=50)
    actor_image = models.ImageField(upload_to='movies/cast/', null=True, blank=True)
    role_name = models.CharField(max_length = 20, null =True, blank = True)
    occupation = models.JSONField(default = list)
    born = models.DateField(null=True, blank=True)
    birthplace = models.CharField(max_length = 100, null=True, blank=True)
    spouse = models.CharField(max_length = 50, null=True, blank=True)
    about = models.TextField(null = True, blank=True)


    movies_cast = models.ManyToManyField(MovieModel, related_name='cast_members')

    def __str__(self):
        return self.actor_name
    
    


class CrewModel(models.Model):
    crew_member_name = models.CharField(max_length=50)
    crew_member_image = models.ImageField(upload_to='movies/crew/', null=True, blank=True)
    occupation = models.JSONField(default = list)
    born = models.DateField(null=True, blank=True)
    birthplace = models.CharField(max_length = 100, null=True, blank=True)
    spouse = models.CharField(max_length = 50, null=True, blank=True)
    about = models.TextField(null = True, blank=True)

    movies_crew = models.ManyToManyField(MovieModel, related_name='crew_members')

    def __str__(self):
        return self.crew_member_name




class TheaterShowModel(models.Model):
   
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    total_rows = models.IntegerField(default=20)
    movie = models.ForeignKey(MovieModel,  related_name='theater_show', on_delete=models.CASCADE)
    screentype = models.CharField(max_length = 50)
    show_times = models.JSONField(default=list)
    show_dates = models.JSONField(default=list)
    is_active = models.BooleanField(default=True)

    def seats_per_row(self, row_number):
        if row_number == 1:
            return 22  
        elif 2 <= row_number <= 5:
            return 18 
        elif 6 <= row_number <= 7:
            return 20 
        elif 8 <= row_number <= 9:
            return 18 
        else:
            return 22 

    def __str__(self):
        return f"{self.name} - {self.location} - {self.movie} - {self.screentype}"
    


class SeatBookingModel(models.Model):
    theater = models.ForeignKey(TheaterShowModel, related_name='seat_bookings', on_delete=models.CASCADE)
    seat_number = models.JSONField(default=list)
    is_booked = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    movie = models.ForeignKey(MovieModel, related_name='movie_seat_bookings',  on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, related_name='user_seat_bookings', on_delete=models.CASCADE, null=True,  blank=True)
    show_date = models.DateField(null=True)
    screentype = models.CharField(max_length = 50)
    show_time = models.JSONField(default=list)
    booking_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, default='Pending')


    def formatted_show_time(self):
        # Format the time as 12-hour without seconds
           return self.show_time.strftime('%I:%M %p')[:-6] if self.show_time else None

    def save(self, *args, **kwargs):
        self.seat_number =  [seat.upper() for seat in self.seat_number]
        super().save(*args, **kwargs)

    def confirm_booking(self):
        self.payment_status = 'Confirmed'
        self.save()

    def cancel_booking(self):
        self.payment_status = 'Canceled'
        self.save()

    def __str__(self):
        username = self.user.username if self.user else 'Guest'
        return f"{username} - {self.movie.moviename} - {self.booking_date}  {self.screentype} -  {self.seat_number} - {self.theater.name}"




