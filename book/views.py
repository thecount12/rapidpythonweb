from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from book.models import Book
from django.shortcuts import get_object_or_404, redirect
from book.forms import PostCommentBook
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


class BookListView(ListView):
	model = Book
	paginate_by = 10
	# queryset=Post.objects.order_by('-created')
	"""if you don't want queryset you ca add the following to model.
	and it only works on date field
	nested: class Meta:
					ordering = ['-created']
	"""


class BookDetailView(DetailView):
	model = Book


@login_required
def BookCommentView(request,pk):
	user = User.objects.get(pk=pk)
	post = get_object_or_404(Book, pk=pk)
	if request.method == 'POST':
		form = PostCommentBook(request.POST)
		if form.is_valid():
			bcomment = form.save(commit=False)
			bcomment.post = post
			bcomment.author=user
			bcomment.save()
			return redirect('/thanks/')
			# return redirect('asdf.html',pk=post.pk)
	else:
		form = PostCommentBook()
	return render(request, 'bookcomment.html', {'form': form})

