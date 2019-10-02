from django.urls import path
from . import views

urlpatterns = [
    # path('[url regex]), [.py file, defined method], name='[name of path]')
    # routes to "posts/"(default) + [nothing] is going to load the index methon from the views.py file
    path('', views.index, name='index'),
    path('details/<int:id>/', views.details, name='details')
]