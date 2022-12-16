from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='dictionary'),
    path('add-word', views.add_english_word, name="add-english-word"),
    path('delete-english-word/<str:eng_id>',  views.delete_english_word, name="delete-english-word"),
    path('update-english-word/<str:eng_id>',  views.update_english_word, name="update-english-word")
]
