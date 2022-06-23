from django.shortcuts import render

# django.views.genericからListView、DetailViewをインポート
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from .form import ContactForm
from django.contrib import messages
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

class BlogDetail(DetailView):
    '''詳細ページのビュー
    
    投稿記事の詳細を表示するのでDetailViewを継承する
     Attributes:
      template_name: レンダリングするテンプレート
      Model: モデルのクラス

      DetailViewのスーパークラスSingleObjectMixinにおいて
      if pk is not None:
        queryset = queryset.filter(pk=pk)   が実行されている
    '''
    # post.htmlをレンダリングする
    template_name ='detail.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost

class ScienceView(ListView):
    '''科学(science)カテゴリの記事を一覧表示するビュー
    
    '''
    # science_list.htmlをレンダリングする
    template_name ='science_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'science_records'
    # category='science'のレコードを抽出して
    # 投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(
        category='science').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 2

class DailylifeView(ListView):
    '''日常(dailylife)カテゴリの記事を一覧表示するビュー
    
    '''
    # dailylife_list.htmlをレンダリングする
    template_name ='dailylife_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'dailylife_records'
    # category='dailylife'のレコードを抽出して
    # 投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(
        category='dailylife').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 2

class MusicView(ListView):
    '''音楽(music)カテゴリの記事を一覧表示するビュー
    
    '''
    # music_list.htmlをレンダリングする
    template_name ='music_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'music_records'
    # category='music'のレコードを抽出して
    # 投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(
        category='music').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 2

class ContactView(FormView):
    """
    form_class django.views.generic.edit.FormMixinで定義されているクラス変数
    reverse_lazy  URLを逆引き形式にする ex)blog:contactをURLに
    form_valid()  フォームに入力されたデータがPOSTされた時に呼ばれるメソッド FormMixinで定義されている

    """
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("blog:contact")

    def form_valid(self, form):
        form.send_email()

        messages.success(
            self.request, "お問い合わせは正常に送信されました"
        )

        return super().form_valid(form)

