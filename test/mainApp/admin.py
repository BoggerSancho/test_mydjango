from django.contrib import admin
from .models import Books, Transletors, Reader, Journal

admin.site.register(Books)
admin.site.register(Transletors)
admin.site.register(Reader)
admin.site.register(Journal)

