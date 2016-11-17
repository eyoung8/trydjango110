from django.conf.urls import url
from django.contrib import admin
from shortener.views import kirr_redirect_view, URLRedirectView, HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^a/(?P<shortcode>[\w-]{6,15})$', kirr_redirect_view),
    url(r'^(?P<shortcode>[\w-]{6,16})$', URLRedirectView.as_view(), name='scode'),
]
