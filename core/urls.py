from django.conf.urls import include, url
from views import validate

urlpatterns = [
    url(r'validate/(?P<postcode>.*)/$', validate, name="validate_postcode"),
]
