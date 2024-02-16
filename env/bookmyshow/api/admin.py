from django.contrib import admin
from .models import *




class MoiveAdmin(admin.ModelAdmin):
    # list_display= ['image','background','moviename','runtime','certificate','screentype','genre','release_date','about','languages','trailer_link']
      search_fields = ['cast', 'crew']

class RatingAdmin(admin.ModelAdmin):
    list_display =['movie','rating','reviews']

class CastAdmin(admin.ModelAdmin):
    # list_display = ['movie','actor_name','actor_image','occupation','born','birthplace','spouse','about']
    search_fields = ['movies_cast']


class CrewAdmin(admin.ModelAdmin):
    # list_display = ['movie','crew_member_name','crew_member_image','occupation','born','birthplace','spouse','about']
    search_fields = ['movies_crew']


class TheaterShowAdmin(admin.ModelAdmin):
    list_display = ['name','location','total_rows','movie','show_times','screentype','show_dates','is_active','display_seats_per_row']

    def display_seats_per_row(self, obj):
        return obj.seats_per_row(1)

    display_seats_per_row.short_description = 'Seats per Row'

class SeatBookingAdmin(admin.ModelAdmin):
    list_display = ['theater','seat_number','is_booked','price','movie','user','booking_date','show_time','screentype','show_date','total_amount','payment_status']


admin.site.register(MovieModel,MoiveAdmin)
admin.site.register(RatingModel,RatingAdmin)
admin.site.register(CastModel,CastAdmin)
admin.site.register(CrewModel,CrewAdmin)
admin.site.register(TheaterShowModel,TheaterShowAdmin)
admin.site.register(SeatBookingModel,SeatBookingAdmin)

