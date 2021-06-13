from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import random

from .initialize import initialize


def main(request):  

    # Initialize database if it hasn't been already
    if 'initialize' not in request.session.keys():
        return redirect('/initialize')
        
    return render(request, 'main.html')

def choose_book(request):  

    filter_count = 0
    
    # use user's filter choice to select group of books
    if request.POST['filter'] == 'OT':
        filter_books = Book.objects.filter(Old_Test=True)
        filter_count += 1
    elif request.POST['filter'] == 'NT':
        filter_books = Book.objects.filter(New_Test=True)
        filter_count += 1
    elif request.POST['filter'] == 'gosp':
        filter_books = Book.objects.filter(Gosp=True)
        filter_count += 1
    elif request.POST['filter'] == 'pent':
        filter_books = Book.objects.filter(Pent=True)
        filter_count += 1
    if 'book_ot' in request.POST:
        if request.POST['book_ot'] != '':
            book_ot = request.POST['book_ot']
            filter_books = Book.objects.filter(Name=book_ot)
            filter_count += 1
    if 'book_nt' in request.POST:
        if request.POST['book_nt'] != '':
            book_nt = request.POST['book_nt']
            filter_books = Book.objects.filter(Name=book_nt)
            filter_count += 1
        
    # make sure user only picked one option
    # allowing multiple categories may be allowed in a later version
    if filter_count > 1:
        return redirect('/filter_error')

    if Book.objects.all():
        #no filter, choose all
        if filter_count == 0:
            filter_books = Book.objects.all()

        #create list of weight values for random choice function
        # weight values come from the number of verses in book
        weight_list = []
        for current_book in filter_books:
            weight_list.append(current_book.num_verses)

        #choose book using weighted random choice 
        book_choice = random.choices(filter_books, weights=weight_list, k=1)
        request.session['book'] = book_choice[0].Name

        context={
            'book': request.session['book'],
        }

        return render(request, 'book.html', context)

def choose_chapter(request):  

    book_name = request.session['book']

    # select chapters from chosen book
    filter_chapters = Chapter.objects.filter(Book=book_name)

    # weighted random choice
    chapter_weights = []
    for current_chapter in filter_chapters:
        chapter_weights.append(current_chapter.num_verses)
    chapter_choice = random.choices(filter_chapters, weights=chapter_weights, k=1)

    request.session['chapter'] = chapter_choice[0].Number

    context={
        'chapter': request.session['chapter'],
    }

    return render(request, 'chapter.html', context)
    
def choose_verse(request):  

    book_name = request.session['book']
    chapter_num = request.session['chapter']

    #reselect chapter object
    filter_chapters = Chapter.objects.filter(Book=book_name, Number=chapter_num)
    chapter_final = filter_chapters[0]

    #choose random verse in chapter
    request.session['verse'] = random.randint(1, chapter_final.num_verses)

    context={
        'verse': request.session['verse'],
    }

    return render(request, 'verse.html', context)

def verse_link(request):

    book = (str(request.session['book'])).lower()
    chapter = str(request.session['chapter'])
    verse = str(request.session['verse'])

    # if book name has a number then it needs to be edited for the link to work
    # eg. 2 Chronicles --> 2_Chronicles
    # if not book.isalpha():
    #     book = book.replace(' ', '_')

    # remove spaces so link will work
    book = book.replace(' ', '_')

    # site uses 'songs' instead of 'song of solomon'
    if book == 'song_of_solomon':
        book = 'songs'

    link = 'https://biblehub.com/' + book + '/' + chapter + '-' + verse + '.htm'

    context = {
        'link': link,
    }

    return render(request, 'verse_link.html', context)

def clear_session(request):
    # clear session keys
    if 'book' in request.session.keys():
        del request.session['book']
    if 'chapter' in request.session.keys():
        del request.session['chapter']
    if 'verse' in request.session.keys():
        del request.session['verse']
    return redirect('/')

def filter_error(request):
    # error message used when user chose more than one filter
    return render(request, 'filter_error.html')