from django.urls import path
from usuario import views
from django.contrib.auth.views import LogoutView

app_name = 'usuario'

urlpatterns = [
    path('login/',views.login, name='login'),
    path('logout/',LogoutView.as_view(template_name = 'usuario/logout.html'), name='logout'),
    path('signup/', views.signup, name = 'signup'),
    path('perfil/edit/', views.edicion_perfil, name = 'edit_user'),
    path('perfil/edit/password/', views.ModificarPass.as_view(), name = 'edit_pass'),
    path('perfil/data/',views.user_data, name='user_data'),
    #path('perfil/user_data',views.listar_alumnos, name = "alumnos"),
    #path('perfil/user_data/<int:pk>/', views.DetalleUser.as_view(), name = 'user_data'),
    
]
