from django.db import models
from django.core.urlresolvers import reverse


class State(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('mueni:detail', kwargs={'pk': self.pk})

    def get_excerpt(self, char):
        return self.name[:char]

    def __unicode__(self):
        return u'%s %s' % (self.name, self.description)


class Author(models.Model):
    name = models.CharField(max_length=250)
    number_of_books = models.CharField(max_length=100)
    awards = models.CharField(max_length=100)

    def __unicode__(self):
        # return self.Authors + '-' + self.Books
        return u'%s' % self.name

    def get_excerpt(self, char):
        return self.name[:char]


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    state = models.ForeignKey(State)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.description)

    def get_excerpt(self, char):
        return self.name[:char]

    class Meta:
        verbose_name_plural = "Categories"


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    edition = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    isbn = models.CharField(max_length=50)
    state = models.ForeignKey(State, default=False)

    def __unicode__(self):
        return u'%s %s' % (self.title, self.edition)

    def get_excerpt(self, char):
        return self.title[:char]


class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=5000)
    date_of_birth = models.DateField()
    state = models.ForeignKey(State)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def get_excerpt(self, char):
        return self.first_name[:char]


class LibraryRecord(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    returned = models.BooleanField(default=False)
    book = models.ForeignKey(Book)
    expected_return_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    state = models.ForeignKey(State)

    def __unicode__(self):
        return u'%s %s' % (self.book, self.expected_return_date)

    def get_excerpt(self, char):
        return self.book[:char]
