from django.conf.urls import url, include
from upload_display import views

urlpatterns = [
    url(r'^$', views.model_form_upload, name='group'),
    url(r'^comments/', include('django_comments.urls')),
]
