from os import ctermid
from django.contrib import admin
from .models import Post,Category,LetterEmail
# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(LetterEmail)

admin.site.site_header="Blog Admin"
admin.site.site_title="Admin Login"
admin.site.index_title="Welcome to Admin-dashboard"