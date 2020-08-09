from django.urls import path
from model_selection import views
from django.conf.urls import url
from django.views.generic.base import TemplateView
app_name = 'modelSelection'
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('index/', TemplateView.as_view(template_name='index.html'))
]