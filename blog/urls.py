from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'blog'

urlpatterns = [
    # viewsモジュールのIndexViewを実行
    #as_view()はbase.Viewクラスのメソッドでレンダリング処理とレスポンスを返してくれる
    path('', views.IndexView.as_view(), name='index'),
]