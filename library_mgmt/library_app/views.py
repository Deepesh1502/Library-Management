from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Member, IssuedBook
from django.utils import timezone

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        isbn = request.POST['isbn']
        published_date = request.POST['published_date']
        Book.objects.create(title=title, author=author, isbn=isbn, published_date=published_date)
        return redirect('list_books')
    return render(request, 'add_book.html')

def issue_book(request):
    if request.method == 'POST':
        book_id = request.POST['book_id']
        member_id = request.POST['member_id']

        book = get_object_or_404(Book, id=book_id)
        member = get_object_or_404(Member, id=member_id)

        if book.available:
            IssuedBook.objects.create(
                book=book,
                member=member,
                issue_date=timezone.now()
            )
            book.available = False
            book.save()
            return redirect('/')
        else:
            return render(request, 'issue_book.html', {'error': 'Book is not available.'})
    return render(request, 'issue_book.html')

def return_book(request):
    if request.method == 'POST':
        book_id = request.POST['book_id']
        book = get_object_or_404(Book, id=book_id)

        issued_record = IssuedBook.objects.filter(book=book, return_date__isnull=True).first()
        if issued_record:
            issued_record.return_date = timezone.now()
            issued_record.save()
            book.available = True
            book.save()
            return redirect('/')
        else:
            return render(request, 'return_book.html', {'error': 'This book is not currently issued.'})
    return render(request, 'return_book.html')