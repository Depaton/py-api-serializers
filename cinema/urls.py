from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import GenreViewSet, ActorViewSet, CinemaHallViewSet, MovieViewSet, MovieSessionViewSet

router = DefaultRouter()
router.register("genre", GenreViewSet)
router.register("actor", ActorViewSet)
router.register("cinema_hall", CinemaHallViewSet)
router.register("movie", MovieViewSet)
router.register("movie_session", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
