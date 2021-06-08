from django.urls import path
from .views import renderTodo,rendrTodoDetail,errorEndPoint
urlpatterns = [
    path('all/',renderTodo),
    path('<int:id>',rendrTodoDetail),
    path('error/',errorEndPoint)
]