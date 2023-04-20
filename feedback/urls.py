from django.urls import path
from . import views
urlpatterns = [
    path('create/',views.create,name='create'),
    path('<int:feedback_id>/',views.detail,name='detail')
]
