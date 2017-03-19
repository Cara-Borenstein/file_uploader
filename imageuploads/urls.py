from django.conf.urls import url
from .views import UploadList, UploadEnvelopeList, UploadDetailView

urlpatterns = [
    #url(r'^$', UploadList.as_view(), name='upload'),
    url(r'^$', UploadEnvelopeList.as_view(), name='upload-envelope')
    #url(r'^$', UploadDetailView.as_view(), name='upload-detail')


]
