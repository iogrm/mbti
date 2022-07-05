from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.test_page, name='home'),
    path('passport/', views.PassportPage.as_view(), name='passport'),
    path('test/', views.test_page, name='test'),
    url(r'^question/all/$', views.AllQuestionsAPIView.as_view(), name='all_questions'),
    url(r'^mbti/place/$', views.PlaceByMbtiAPIView.as_view(), name='place_by_mbti'),
    url(r'^mbti/avatar/$', views.AvatarByMbtiAPIView.as_view(), name='avatar_by_mbti'),
    url(r'^mbti/chars/$', views.CharactersByMbtiAPIView.as_view(), name='chars_by_mbti'),
    # url(r'^mbti/answers/$', views.SubmitAnswerAPIView.as_view(), name='submit_answers'),
]
