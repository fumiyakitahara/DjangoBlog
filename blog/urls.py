from django.urls import path
from . import views


# URLパターンを逆引きできるように名前を付ける
app_name = 'blog'

urlpatterns = [
    # viewsモジュールのIndexViewを実行
    #as_view()はbase.Viewクラスのメソッドでレンダリング処理とレスポンスを返してくれる
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/',views.BlogDetail.as_view(), name="detail"),
    path('science-list/', views.ScienceView.as_view(),name='science_list'),
    path('dailylife-list/', views.DailylifeView.as_view(), name='dailylife_list'),
    path('music-list/', views.MusicView.as_view(), name='music_list'),
    path('contact/', views.ContactView.as_view(), name = 'contact'),
]