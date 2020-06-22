from django.db import models


class Book(models.Model):
    chapter = models.CharField(max_length=180)
    body = models.TextField()

    def __unicode__(self):
        return self.chapter

    def __str__(self):
        return self.chapter


class CommentBook(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(default='author', max_length=80)
    body = models.TextField()
    post = models.ForeignKey(Book, related_name='commentsbook', on_delete=models.DO_NOTHING)
    approved_comment = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))
