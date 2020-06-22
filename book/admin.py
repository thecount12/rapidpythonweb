from django.contrib import admin

# Register your models here.

from book.models import Book
from book.models import CommentBook


class PostBook(admin.ModelAdmin):
	list_display = ["chapter"]


class CommentBookAdmin(admin.ModelAdmin):
	def book_chapter(self, instance):
		return instance.post.chapter
	list_display = ["author", "book_chapter"]
	search_fields = ["book_chapter"]
		

admin.site.register(Book, PostBook)
admin.site.register(CommentBook, CommentBookAdmin)
