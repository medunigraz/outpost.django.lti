from django.conf.urls import url

from . import views

app_name = "lti"

urlpatterns = [url(r"^$", views.LTIView.as_view(), name="index")]
