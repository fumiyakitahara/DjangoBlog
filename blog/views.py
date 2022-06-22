from django.shortcuts import render

# django.views.genericからListView、DetailViewをインポート
from django.views.generic import ListView, DetailView, TemplateView

from .models import BlogPost

class IndexView(ListView):
    '''トップページのビュー
    
    投稿記事を一覧表示するのでListViewを継承する
    
    Attributes:
      template_name: レンダリングするテンプレート
      context_object_name: object_listキーの別名を設定
      queryset: データベースのクエリ
    '''
    # index.htmlをレンダリングする
    template_name ='index.html'
    # object_listキーの別名を設定
    context_object_name = 'orderby_records'
    # モデルBlogPostのオブジェクトにorder_by()を適用して
    # BlogPostのレコードを投稿日時の降順で並べ替える
    #objectsはManagerクラスのインスタンス、クエリを実行する際のインターフェースになる
    queryset = BlogPost.objects.order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 4

    def get_context_data(self, **kwargs):#実験　ターミナルにcontextの中身が出るよ
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    """
    model = BlogPost.objects.all()は
    queryset = BlogPost.objecs.all()とした時と同じもの
    
    ListIndex内で実行されるメソッドたち
    setup(),dispatch(),http_method_not_allowed(),get_template_names(),get_queryset()
    get_context_object_name(),get_context?data(),get(),render_to_response()
    queryset(クラス変数ですよ)が設定されていない場合は、すべてのレコードを取得

    クラス変数
    context_data
    template_name
    model
    context_object_name   テーブルから取り出したレコードはcontextに辞書方として格納される。この時のキーがobject_listだが、そのキーの名前を変更できる

    """
