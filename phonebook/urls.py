from django.urls import path

from . import views
app_name = "phonebook"

urlpatterns = [
    path('', views.home, name='list-all'),
    path('add/', views.Add_New_Contact, name="add-new-contact"),
    path('delete/<str:name>', views.delete_contact, name="delete-contact"),
    path('update_page/<str:name>', views.update_contact_view, name="update-contact-view"),
    path('update/<int:id>', views.update_contact, name='update-contact'),
]
