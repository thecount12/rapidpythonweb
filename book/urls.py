from django.conf.urls import url, include

from book.views import BookListView
from book.views import BookDetailView
from book.views import BookCommentView

urlpatterns = [
        url(r'^$',BookListView.as_view(), name='book-list'),
        url(r'^(?P<pk>\d+)/$',BookDetailView.as_view(), name='book-detail'),
	url(r'^(?P<pk>\d+)/comment/$',BookCommentView,name='bookcomment'),

]
