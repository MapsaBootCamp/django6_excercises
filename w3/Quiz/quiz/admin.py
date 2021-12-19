from django.contrib import admin
from .models import Question,History,Category,User

admin.site.register(Question)

admin.site.register(History)
admin.site.register(Category)
admin.site.register(User)
