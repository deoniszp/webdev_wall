from django.conf.urls import url
from app_wall import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add_message/$', views.MessageAddView.as_view(), name='add_message'),
    url(r'^add_comment/$', views.add_comment, name='add_comment'),
    url(r'^get_content/$', views.get_content, name="get_content"),
]