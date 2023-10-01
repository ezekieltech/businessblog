# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
    path('register/', views.registration_view, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('account/', views.account_view, name='account')
    # url(r'^posts/(?P<slug>.+)/$', views.PostDetail.as_view(), name='post_detail'),
    # url(r'^department/(?P<slug>.+)/$', views.DepartmentDetail.as_view(), name='department_detail'),
    # url(r'^departments/$', views.DepartmentList.as_view(), name='departments'),
    # url(r'^profile/$', views.ProfileList.as_view(), name='profile'),
    # url(r'^department/(?P<user>.+)/$', views.ProfileDetail.as_view(), name='profile_detail')

] 