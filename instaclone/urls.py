from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("register/", v.register, name="register"),
    # path('post/', include('post.urls')),
    path('user/', include('authy.urls')),
    path('', include('insta.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
