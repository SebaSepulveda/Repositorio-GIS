from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin


urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^upload$", TemplateView.as_view(template_name="upload.html"), name="upload"),
    url(r"^download$", TemplateView.as_view(template_name="download.html"), name="download"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
