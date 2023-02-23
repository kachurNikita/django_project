from django.contrib import admin
from .models import Question, Choice
# Register your models here.


# Display our model to admin panel
admin.site.register(Question)
