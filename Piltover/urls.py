from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('velkoz/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

urlpatterns += [
    re_path('^' + settings.MEDIA_URL.lstrip('/') + r'(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': settings.DEBUG
    }),
]
