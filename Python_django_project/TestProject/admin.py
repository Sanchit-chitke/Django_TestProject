from django.contrib import admin
from .models import FirstModel,SecondModel,ThirdModel
# Register your models here.
admin.site.register(FirstModel)
admin.site.register(SecondModel)
admin.site.register(ThirdModel)