from django.urls        import path
from actors.views       import ActorsView, MoviesView

urlpatterns = [
    path('', ActorsView.as_view()),
    path('/movies', MoviesView.as_view())
]