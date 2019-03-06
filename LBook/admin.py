from django.contrib import admin
from .models import Book,Student,IssueBook,Registers,Notify
# Register your models here.

admin.site.register((Book,Student,IssueBook,Registers,Notify))