from django.urls import path, include
from .views import RecruiterRegisterAPI, JobSeekerRegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views
#
urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register/recruiter', RecruiterRegisterAPI.as_view()),
    path('api/auth/register/jobseeker', JobSeekerRegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
]




