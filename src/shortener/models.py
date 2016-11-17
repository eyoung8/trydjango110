from django.conf import settings
from django.db import models
#from django.core.urlresolvers import reverse
from django_hosts.resolvers import reverse
from .utils import create_shortcode
from .validators import validate_url, validate_dot_com
# Create your models here.

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = KirrURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        for num_new_codes, q in enumerate(qs):
            q.shortcode = create_shortcode(q)
            q.save()
        return "New codes made: {}".format(num_new_codes+1)


class KirrURL(models.Model):
    url       = models.CharField(max_length=220, validators=[validate_url])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated   = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active    = models.BooleanField(default=True)

    objects = KirrURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        if not (self.url.startswith('http://') or self.url.startswith('https://')):
            self.url = "http://" + self.url
        super(KirrURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse("scode", kwargs={"shortcode":self.shortcode}, host='www', scheme='http')
        return url_path