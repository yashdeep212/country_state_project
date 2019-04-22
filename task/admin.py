from django.contrib import admin
from task.models import Person, Country, State, City
# Register your models here.
admin.site.register(Person)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)

