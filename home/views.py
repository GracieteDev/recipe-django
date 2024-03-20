from django.urls import path
from .views import Index  # import the Recipes view from the home app

urlpatterns = [
    # other url patterns...
    path('', Index.as_view(), name='home'),
]
