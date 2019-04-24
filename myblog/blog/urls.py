from django.conf.urls import url

from . import views
app_name = 'blog'
urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^detail/(\d+)$',views.detail, name='detail'),
    url(r'^achives/(\d+)/(\d+)$',views.achives, name='achives'),
    url(r'^category/(\d+)$',views.category, name='category'),
    url(r'^tag/(\d+)$',views.tag, name='tag'),
]