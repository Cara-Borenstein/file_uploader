from django.conf.urls import url
from .views import UploadList

urlpatterns = [
    url(r'^$', UploadList.as_view(), name='upload')
]
