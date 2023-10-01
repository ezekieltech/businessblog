# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('posts/(?P<slug>.+)/', views.PostDetail.as_view(), name='post_detail'),
    path('service/(?P<slug>.+)/', views.DepartmentDetail.as_view(), name='department_detail'),
    path('services/', views.DepartmentList.as_view(), name='departments'),
    path('department/(?P<user>.+)/', views.ProfileDetail.as_view(), name='profile_detail')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# url(r'^$', views.PostListView.as_view(), name='home'),
# url(r'^posts/$', views.PostListView.as_view(), name='post'),
# url(r'^projects/(?P<pk>\d+)$', views.ProjectDetailView.as_view(), name='project-detail'),
# url(r'^industry/$', views.IndustryListView.as_view(), name='industry'),
# url(r'^industry/(?P<pk>\d+)$', views.IndustryDetailView.as_view(), name='industry-detail'),
# url(r'^services/$', views.ServiceListView.as_view(), name='services'),
# url(r'^services/(?P<pk>\d+)$', views.ServiceDetailView.as_view(), name='service-detail'),
# url(r'^about-us/$', views.StaffListView.as_view(), name='about-us'),
# url(r'^about-us/(?P<pk>\d+)$', views.StaffDetailView.as_view(), name='staff-detail'),
# #url(r'^contact/$', views.contact, name='contact'),
# url('email/', views.emailView, name='email'),
# url('success/', views.successView, name='success'),

#]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()

# used like this: <a href="{% url 'index' %}">Home</a> on the template
