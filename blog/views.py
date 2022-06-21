from django.shortcuts import render

# django.views.genericからListView、DetailViewをインポート
from django.views.generic import ListView, DetailView, TemplateView

class IndexView(TemplateView):
    # index.htmlをレンダリングする
    #template_nameはTemplateResponseMixinで定義されている
    template_name ='index.html'