# childapp/urls.py
from django.urls import path
from .views import ChildListView, ChildDetailView, ChildCreateView, ChildUpdateView, ChildDeleteView, VideoCreateView,  VideoDetailView, VideoUpdateView, VideoDeleteView
from .views import HomePageView, ContactPageView
from .views import VideoListView
from . import views
from .views import HelpPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('home/', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('help/', HelpPageView.as_view(), name='help'),
    path('children/', ChildListView.as_view(), name='child_list'),
    path('children/<int:pk>/', ChildDetailView.as_view(), name='child_detail'),
    path('children/create/', ChildCreateView.as_view(), name='child_create'),
    path('children/<int:pk>/update/', ChildUpdateView.as_view(), name='child_update'),
    path('children/<int:pk>/delete/', ChildDeleteView.as_view(), name='child_delete'),
    path('videos/', VideoListView.as_view(), name='video_list'),
    path('success/',views.success,name='success'),
    path('videos/create/', VideoCreateView.as_view(), name='video_create'),
    path('videos/<int:pk>/', VideoDetailView.as_view(), name='video_detail'),
    path('videos/<int:pk>/update/', VideoUpdateView.as_view(), name='video_update'),
    path('videos/<int:pk>/delete/', VideoDeleteView.as_view(), name='video_delete'),

]
