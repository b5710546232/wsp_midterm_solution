from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Bookstore
from django.db import connection


def insert_view(request):
    return render(request, 'bookstore/insert.html')



def success(request):
    print(request.user)
    user = request.user
    return HttpResponse("Welcome %s" % user.username)


def insert_book(request):
    book_id = request.POST['book_id']
    isbn = request.POST['isbn']
    book_name = request.POST['book_name']
    price = request.POST['price']
    author = request.POST['author']
    book = Bookstore.objects.create(Book_id = book_id, ISBN = isbn ,Book_name=  book_name, Price = price,Author =author)
    book.save()
    print('ok')
    return HttpResponseRedirect(reverse('bookstore:index'))

def index(request):
    book = ""
    for row in Bookstore.objects.all():
        # print(row.Book_id)
        # print(row.ISBN)
        # print(row.Book_name)
        # print(row.Price)
        # print(row.Author)
        book += '''
        <form action="update/action " method="put">
        <tr>
                <td><input type = "type" value = '''+row.Book_id+''' name="id"></td>
                <td><input type = "type" value = '''+row.ISBN+''' name="isbn"></td>
                <td><input type = "type" value = '''+row.Book_name+''' name="book_name"></td>
                <td><input type = "type" value = '''+row.Price+''' name="price"></td>
                <td><input type = "type" value = '''+row.Author+''' name="author"></td>
                <td><input type = "submit" value =update></td>
                <td><button><a href =delete/?id='''+str(row.Book_id)+'''">delete</a></button></td>
        </tr>
        </form>
                '''

        message = """
                <html>
                <head></head>
                <body>
                <table border = "1">
                """ + book + """
                <a href =/bookstore/insert>Back to Insert</a>
                </table>
                </body>
                </html>
                    """
    return HttpResponse(message)



def delete(request):
    print( request.GET)
    book_id = request.GET.get('id','')
    book_id = book_id[0:len(book_id)-1]
    print('safe  :: '+book_id)
    Bookstore.objects.filter(Book_id=book_id).delete()
    return HttpResponseRedirect(reverse('bookstore:index'))
#
# def update_view(request):
#     print( request.GET)
#     book_id = request.GET.get('id','')
#     book_id = book_id[0:len(book_id)-1]
#     print('safe  :: '+book_id)
#     return HttpResponseRedirect(reverse('bookstore:index'))
#
#


def update(request):
    book = ""
    print( request.GET)
    book_id = request.GET.get('id','')
    book_id = book_id[0:len(book_id)-1]
    print('safe  update  :: '+book_id)
    for row in Bookstore.objects.all():
        if row.Book_id == book_id:
            book += '''
            <form action="action " method="put">
              <tr>
                       <td><input type = "type" value = '''+row.Book_id+''' name="id"></td>
                       <td><input type = "type" value = '''+row.ISBN+''' name="isbn"></td>
                       <td><input type = "type" value = '''+row.Book_name+''' name="book_name"></td>
                       <td><input type = "type" value = '''+row.Price+''' name="price"></td>
                       <td><input type = "type" value = '''+row.Author+''' name="author"></td>
                       <td><button>update</button></td>
                       <td><a href =delete/?id=''' + str(row.Book_id) + '''">Delete</a></td>
               </tr>
            </form>
                       '''


        else:

            book += '''
               <tr>
                       <td>''' + row.Book_id + '''</td>
                       <td>''' + row.ISBN + '''</td>
                       <td>''' + row.Book_name + '''</td>
                       <td>''' + row.Price + '''</td>
                       <td>''' + row.Author + '''</td>
                       <td><a href =/upload/?id=''' + str(row.Book_id) + '''">Update</a></td>
                       <td><a href =/delete/?id=''' + str(row.Book_id) + '''">Delete</a></td>
               </tr>
                       '''
        message = """
                   <html>
                   <head></head>
                   <body>
                   <table border = "1">
                   """ + book + """
                   <a href =/bookstore/insert>Back to Insert</a>
                   <br>
                   <a href =/bookstore/>Back to Index</a>
                   </table>
                   </body>
                   </html>
                       """
    return HttpResponse(message)

def action(request):
    print(request.GET)
    book_id = request.GET.get('id', '')
    isbn = request.GET.get('isbn', '')
    book_name = request.GET.get('book_name', '')
    price = request.GET.get('price', '')
    author = request.GET.get('author', '')
    print('isbn '+isbn)
    Bookstore.objects.filter(Book_id=book_id).update(Book_id=book_id,ISBN=isbn,Book_name=book_name,Price=price,Author=author)
    return HttpResponseRedirect(reverse('bookstore:index'))

