from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from .models import Books



urlpatterns = [
    url(r'^$', views.get, name='index'),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.login, name='login'),
    url(r'^auth/logout', views.logout, name='logout'),
    url(r'^book/(?P<pk>\d+)$', DetailView.as_view(model = Books, template_name="mainApp/book.html")),
    # url(r'^login/$', views.LoginFormView.as_view()),
    # url(r'^news/$', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
    #                                   template_name="news/posts.html")),
    # url(r'^news/(?P<pk>\d+)$', DetailView.as_view(model = Articles, template_name="news/post.html"))

]