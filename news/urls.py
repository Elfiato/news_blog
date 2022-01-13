from django.urls import path
from . import views as news_views

urlpatterns = [
    path('', news_views.HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', news_views.NewsByCategory.as_view(), name='category'),
    path('category/<int:category_id>/', news_views.ViewOneNew.as_view(), name='category'),
    path('new/<int:pk>', news_views.ViewOneNew.as_view(), name='one-new'),
    path('new/add-new', news_views.CreateNew.as_view(), name='add-new'),
]
