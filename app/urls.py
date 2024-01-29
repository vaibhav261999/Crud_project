from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name='home'),
    path("Signup/",Signup,name='Signup'),
    path("Login/",Login,name='Login'),
    path("about/",about,name='about'),
    path("Contact/",Contact,name='Contact'),
    path("Services/",Services,name='Services'),
    
    path("savedata/",savedata,name='savedata'),
    path("Login_data/",Login_data,name='Login_data'),
    
    path("query/",query,name='query'),

    path("ShowData/<str:pk>", ShowData,name='ShowData'),

    path("edit/<int:editId>", edit,name='edit'),

    path("delete/<int:delId>", delete ,name='delete'),

    path('Update/<int:upId>', Update,name='Update'),

    path('search/<str:pk>', search,name='search'),
    path('back/<str:pk>', back,name='back'),

]

