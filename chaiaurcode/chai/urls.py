
from django.urls import path
from . import views
urlpatterns = [
    path('',views.all_chai,name='all_home'), 
    path('<int:chai_id>/',views.chai_details,name='chai_details'),
]