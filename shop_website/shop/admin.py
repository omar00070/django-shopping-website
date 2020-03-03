from django.contrib import admin
from .models import Product
from .models import Collection

admin.site.register(Product)
admin.site.register(Collection)