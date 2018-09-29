from django.urls import path
from djoser import views as djoser_views
from rest_framework_jwt import views as jwt_views
from restAPI import views


urlpatterns = [
    path('api/view/', views.RestUserView.as_view(), name='api-view'),
    path('api/delete/', views.RestUserDeleteView.as_view(), name='api-delete'),
    path('api/logout/all/', views.RestUserLogoutAllView.as_view(), name='api-logout-all'),

    # Views are defined in Djoser, but we're assigning custom paths.
    path('api/register/', djoser_views.UserCreateView.as_view(), name='api-register'),
    path('api/add-idea/', views.RestAddIdeaView.as_view(), name='api-add-idea'),

    # Views are defined in Rest Framework JWT, but we're assigning custom paths.
    path('api/login/', jwt_views.ObtainJSONWebToken.as_view(), name='api-login'),
    path('api/login/refresh/', jwt_views.RefreshJSONWebToken.as_view(), name='api-login-refresh'),
]
