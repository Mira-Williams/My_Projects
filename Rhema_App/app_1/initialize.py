from .models import *
from django.shortcuts import render, redirect

def initialize(request):

    book_1 = Book.objects.create(
        Name = 'Genesis',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = True,
        num_verses = 1533
    )
    book_2 = Book.objects.create(
        Name = 'Exodus',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = True,
        num_verses = 1213
    )
    book_3 = Book.objects.create(
        Name = 'Leviticus',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = True,
        num_verses = 859
    )
    book_4 = Book.objects.create(
        Name = 'Numbers',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = True,
        num_verses = 1288
    )
    book_5 = Book.objects.create(
        Name = 'Deuteronomy',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = True,
        num_verses = 959
    )
    book_6 = Book.objects.create(
        Name = 'Joshua',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 658
    )
    book_7 = Book.objects.create(
        Name = 'Judges',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 618
    )
    book_8 = Book.objects.create(
        Name = 'Ruth',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 85
    )
    book_9 = Book.objects.create(
        Name = '1 Samuel',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 810
    )
    book_10 = Book.objects.create(
        Name = '2 Samuel',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 695
    )
    book_11 = Book.objects.create(
        Name = '1 Kings',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 816
    )
    book_12 = Book.objects.create(
        Name = '2 Kings',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 719
    )
    book_13 = Book.objects.create(
        Name = '1 Chronicles',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 942
    )
    book_14 = Book.objects.create(
        Name = '2 Chronicles',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 822
    )
    book_15 = Book.objects.create(
        Name = 'Ezra',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 280
    )
    book_16 = Book.objects.create(
        Name = 'Nehemiah',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 406
    )
    book_17 = Book.objects.create(
        Name = 'Esther',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 167
    )
    book_18 = Book.objects.create(
        Name = 'Job',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 1070
    )
    book_19 = Book.objects.create(
        Name = 'Psalms',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 2461
    )
    book_20 = Book.objects.create(
        Name = 'Proverbs',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 915
    )
    book_21 = Book.objects.create(
        Name = 'Ecclesiastes',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 222
    )
    book_22 = Book.objects.create(
        Name = 'Song of Solomon',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 117
    )
    book_23 = Book.objects.create(
        Name = 'Isaiah',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 1292
    )
    book_24 = Book.objects.create(
        Name = 'Jeremiah',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 1364
    )
    book_25 = Book.objects.create(
        Name = 'Lamentations',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 154
    )
    book_26 = Book.objects.create(
        Name = 'Ezekiel',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 1273
    )
    book_27 = Book.objects.create(
        Name = 'Daniel',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 357
    )
    book_28 = Book.objects.create(
        Name = 'Hosea',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 197
    )
    book_29 = Book.objects.create(
        Name = 'Joel',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 73
    )
    book_30 = Book.objects.create(
        Name = 'Amos',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 146
    )
    book_31 = Book.objects.create(
        Name = 'Obadiah',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 21
    )
    book_32 = Book.objects.create(
        Name = 'Jonah',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 48
    )
    book_33 = Book.objects.create(
        Name = 'Micah',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 105
    )
    book_34 = Book.objects.create(
        Name = 'Nahum',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 47
    )
    book_35 = Book.objects.create(
        Name = 'Habakkuk',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 56
    )
    book_36 = Book.objects.create(
        Name = 'Zephaniah',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 53
    )
    book_37 = Book.objects.create(
        Name = 'Haggai',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 38
    )
    book_38 = Book.objects.create(
        Name = 'Zechariah',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 211
    )
    book_39 = Book.objects.create(
        Name = 'Malachi',
        Old_Test = True,
        New_Test = False,
        Gosp = False,
        Pent = False,
        num_verses = 55
    )


    book_40 = Book.objects.create(
        Name = 'Matthew',
        Old_Test = False,
        New_Test = True,
        Gosp = True,
        Pent = False,
        num_verses = 1071
    )
    book_41 = Book.objects.create(
        Name = 'Mark',
        Old_Test = False,
        New_Test = True,
        Gosp = True,
        Pent = False,
        num_verses = 678
    )
    book_42 = Book.objects.create(
        Name = 'Luke',
        Old_Test = False,
        New_Test = True,
        Gosp = True,
        Pent = False,
        num_verses = 1151
    )
    book_43 = Book.objects.create(
        Name = 'John',
        Old_Test = False,
        New_Test = True,
        Gosp = True,
        Pent = False,
        num_verses = 879
    )
    book_44 = Book.objects.create(
        Name = 'Acts',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 1007
    )
    book_45 = Book.objects.create(
        Name = 'Romans',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 433
    )
    book_46 = Book.objects.create(
        Name = '1 Corinthians',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 437
    )
    book_47 = Book.objects.create(
        Name = '2 Corinthians',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 257
    )
    book_48 = Book.objects.create(
        Name = 'Galatians',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 149
    )
    book_49 = Book.objects.create(
        Name = 'Ephesians',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 155
    )
    book_50 = Book.objects.create(
        Name = 'Philippians',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 104
    )
    book_51 = Book.objects.create(
        Name = 'Colossians',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 95
    )
    book_52 = Book.objects.create(
        Name = '1 Thessalonians',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 89
    )
    book_53 = Book.objects.create(
        Name = '2 Thessalonians',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 47
    )
    book_54 = Book.objects.create(
        Name = '1 Timothy',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 113
    )
    book_55 = Book.objects.create(
        Name = '2 Timothy',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 83
    )
    book_56 = Book.objects.create(
        Name = 'Titus',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 46
    )
    book_57 = Book.objects.create(
        Name = 'Philemon',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 25
    )
    book_58 = Book.objects.create(
        Name = 'Hebrews',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 303
    )
    book_59 = Book.objects.create(
        Name = 'James',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 108
    )
    book_60 = Book.objects.create(
        Name = '1 Peter',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 105
    )
    book_61 = Book.objects.create(
        Name = '2 Peter',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 61
    )
    book_62 = Book.objects.create(
        Name = '1 John',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 105
    )
    book_63 = Book.objects.create(
        Name = '2 John',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 13
    )
    book_64 = Book.objects.create(
        Name = '3 John',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 14
    )
    book_65 = Book.objects.create(
        Name = 'Jude',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 25
    )
    book_66 = Book.objects.create(
        Name = 'Revelation',
        Old_Test = False,
        New_Test = True,
        Gosp = False,
        Pent = False,
        num_verses = 404
    )



    chapter_1 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 1,
        num_verses = 31,
    )
    chapter_2 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 2,
        num_verses = 25,
    )
    chapter_3 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 3,
        num_verses = 24,
    )
    chapter_4 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 4,
        num_verses = 26,
    )
    chapter_5 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 5,
        num_verses = 32,
    )
    chapter_6 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 6,
        num_verses = 22,
    )
    chapter_7 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 7,
        num_verses = 24,
    )
    chapter_8 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 8,
        num_verses = 22,
    )
    chapter_9 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 9,
        num_verses = 29,
    )
    chapter_10 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 10,
        num_verses = 32,
    )
    chapter_11 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 11,
        num_verses = 32,
    )
    chapter_12 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 12,
        num_verses = 20,
    )
    chapter_13 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 13,
        num_verses = 18,
    )
    chapter_14 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 14,
        num_verses = 24,
    )
    chapter_15 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 15,
        num_verses = 21,
    )
    chapter_16 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 16,
        num_verses = 16,
    )
    chapter_17 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 17,
        num_verses = 27,
    )
    chapter_18 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 18,
        num_verses = 33,
    )
    chapter_19 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 19,
        num_verses = 38,
    )
    chapter_20 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 20,
        num_verses = 18,
    )
    chapter_21 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 21,
        num_verses = 34,
    )
    chapter_22 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 22,
        num_verses = 24,
    )
    chapter_23 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 23,
        num_verses = 20,
    )
    chapter_24 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 24,
        num_verses = 67,
    )
    chapter_25 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 25,
        num_verses = 34,
    )
    chapter_26 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 26,
        num_verses = 35,
    )
    chapter_27 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 27,
        num_verses = 46,
    )
    chapter_28 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 28,
        num_verses = 22,
    )
    chapter_29 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 29,
        num_verses = 35,
    )
    chapter_30 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 30,
        num_verses = 43,
    )
    chapter_31 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 31,
        num_verses = 54,
    )
    chapter_32 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 32,
        num_verses = 33,
    )
    chapter_33 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 33,
        num_verses = 20,
    )
    chapter_34 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 34,
        num_verses = 31,
    )
    chapter_35 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 35,
        num_verses = 29,
    )
    chapter_36 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 36,
        num_verses = 43,
    )
    chapter_37 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 37,
        num_verses = 36,
    )
    chapter_38 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 38,
        num_verses = 30,
    )
    chapter_39 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 39,
        num_verses = 23,
    )
    chapter_40 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 40,
        num_verses = 23,
    )
    chapter_41 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 41,
        num_verses = 57,
    )
    chapter_42 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 42,
        num_verses = 38,
    )
    chapter_43 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 43,
        num_verses = 34,
    )
    chapter_44 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 44,
        num_verses = 34,
    )
    chapter_45 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 45,
        num_verses = 28,
    )
    chapter_46 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 46,
        num_verses = 34,
    )
    chapter_47 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 47,
        num_verses = 31,
    )
    chapter_48 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 48,
        num_verses = 22,
    )
    chapter_49 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 49,
        num_verses = 33,
    )
    chapter_50 = Chapter.objects.create(
        Book = 'Genesis',
        Number = 50,
        num_verses = 26,
    )

    chapter_1 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 1,
        num_verses = 22,
    )
    chapter_2 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 2,
        num_verses = 25,
    )   
    chapter_3 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 3,
        num_verses = 22,
    )   
    chapter_4 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 4,
        num_verses = 31,
    )   
    chapter_5 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 5,
        num_verses = 23,
    )   
    chapter_6 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 6,
        num_verses = 30,
    )   
    chapter_7 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 7,
        num_verses = 29,
    )   
    chapter_8 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 8,
        num_verses = 28,
    )   
    chapter_9 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 9,
        num_verses = 35,
    )   
    chapter_10 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 10,
        num_verses = 29,
    )   
    chapter_11 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 11,
        num_verses = 10,
    )   
    chapter_12 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 12,
        num_verses = 51,
    )   
    chapter_13 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 13,
        num_verses = 22,
    )   
    chapter_14 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 14,
        num_verses = 31,
    )   
    chapter_15 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 15,
        num_verses = 27,
    )   
    chapter_16 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 16,
        num_verses = 36,
    )   
    chapter_17 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 17,
        num_verses = 16,
    )   
    chapter_18 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 18,
        num_verses = 27,
    )   
    chapter_19 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 19,
        num_verses = 25,
    )   
    chapter_20 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 20,
        num_verses = 26,
    )
    chapter_21 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 21,
        num_verses = 37,
    )
    chapter_22 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 22,
        num_verses = 30,
    )   
    chapter_23 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 23,
        num_verses = 33,
    )   
    chapter_24 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 24,
        num_verses = 18,
    )   
    chapter_25 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 25,
        num_verses = 40,
    )   
    chapter_26 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 26,
        num_verses = 37,
    )   
    chapter_27 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 27,
        num_verses = 21,
    )   
    chapter_28 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 28,
        num_verses = 43,
    )   
    chapter_29 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 29,
        num_verses = 46,
    )   
    chapter_30 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 30,
        num_verses = 38,
    )   
    chapter_31 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 31,
        num_verses = 18,
    )   
    chapter_32 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 32,
        num_verses = 35,
    )   
    chapter_33 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 33,
        num_verses = 23,
    )   
    chapter_34 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 34,
        num_verses = 35,
    )   
    chapter_35 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 35,
        num_verses = 35,
    )   
    chapter_36 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 36,
        num_verses = 38,
    )   
    chapter_37 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 37,
        num_verses = 29,
    )   
    chapter_38 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 38,
        num_verses = 31,
    )   
    chapter_39 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 39,
        num_verses = 43,
    )   
    chapter_40 = Chapter.objects.create(
        Book = 'Exodus',
        Number = 40,
        num_verses = 38,
    )

    chapter_1 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 1,
        num_verses = 17,
    ) 
    chapter_2 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 2,
        num_verses = 16,
    ) 
    chapter_3 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 3,
        num_verses = 17,
    ) 
    chapter_4 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 4,
        num_verses = 35,
    ) 
    chapter_5 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 5,
        num_verses = 26,
    ) 
    chapter_6 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 6,
        num_verses = 23,
    ) 
    chapter_7 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 7,
        num_verses = 38,
    ) 
    chapter_8 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 8,
        num_verses = 36,
    ) 
    chapter_9 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 9,
        num_verses = 24,
    ) 
    chapter_10 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 10,
        num_verses = 20,
    ) 
    chapter_11 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 11,
        num_verses = 47,
    ) 
    chapter_12 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 12,
        num_verses = 8,
    ) 
    chapter_13 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 13,
        num_verses = 59,
    ) 
    chapter_14 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 14,
        num_verses = 57,
    ) 
    chapter_15 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 15,
        num_verses = 33,
    ) 
    chapter_16 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 16,
        num_verses = 34,
    ) 
    chapter_17 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 17,
        num_verses = 16,
    ) 
    chapter_18 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 18,
        num_verses = 30,
    ) 
    chapter_19 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 19,
        num_verses = 37,
    ) 
    chapter_20 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 20,
        num_verses = 27,
    ) 
    chapter_21 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 21,
        num_verses = 24,
    ) 
    chapter_22 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 22,
        num_verses = 33,
    ) 
    chapter_23 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 23,
        num_verses = 44,
    ) 
    chapter_24 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 24,
        num_verses = 23,
    ) 
    chapter_25 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 25,
        num_verses = 55,
    ) 
    chapter_26 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 26,
        num_verses = 46,
    ) 
    chapter_27 = Chapter.objects.create(
        Book = 'Leviticus',
        Number = 27,
        num_verses = 34,
    ) 

    chapter_1 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 1,
        num_verses = 54,
    ) 
    chapter_2 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 2,
        num_verses = 34,
    ) 
    chapter_3 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 3,
        num_verses = 51,
    ) 
    chapter_4 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 4,
        num_verses = 49,
    )
    chapter_5 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 5,
        num_verses = 31,
    ) 
    chapter_6 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 6,
        num_verses = 27,
    ) 
    chapter_7 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 7,
        num_verses = 89,
    ) 
    chapter_8 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 8,
        num_verses = 26,
    ) 
    chapter_9 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 9,
        num_verses = 23,
    ) 
    chapter_10 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 10,
        num_verses = 36,
    ) 
    chapter_11 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 11,
        num_verses = 35,
    ) 
    chapter_12 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 12,
        num_verses = 16,
    ) 
    chapter_13 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 13,
        num_verses = 33,
    ) 
    chapter_14 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 14,
        num_verses = 45,
    ) 
    chapter_15 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 15,
        num_verses = 41,
    )
    chapter_16 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 16,
        num_verses = 35,
    ) 
    chapter_17 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 17,
        num_verses = 28,
    ) 
    chapter_18 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 18,
        num_verses = 32,
    ) 
    chapter_19 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 19,
        num_verses = 22,
    ) 
    chapter_20 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 20,
        num_verses = 29,
    ) 
    chapter_21 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 21,
        num_verses = 35,
    ) 
    chapter_22 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 22,
        num_verses = 41,
    ) 
    chapter_23 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 23,
        num_verses = 30,
    ) 
    chapter_24 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 24,
        num_verses = 25,
    ) 
    chapter_25 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 25,
        num_verses = 18,
    ) 
    chapter_26 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 26,
        num_verses = 65,
    )
    chapter_27 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 27,
        num_verses = 23,
    ) 
    chapter_28 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 28,
        num_verses = 31,
    ) 
    chapter_29 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 29,
        num_verses = 39,
    ) 
    chapter_30 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 30,
        num_verses = 17,
    ) 
    chapter_31 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 31,
        num_verses = 54,
    ) 
    chapter_32 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 32,
        num_verses = 42,
    )
    chapter_33 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 33,
        num_verses = 56,
    ) 
    chapter_34 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 34,
        num_verses = 29,
    ) 
    chapter_35 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 35,
        num_verses = 34,
    ) 
    chapter_36 = Chapter.objects.create(
        Book = 'Numbers',
        Number = 36,
        num_verses = 13,
    ) 


    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 1,
        num_verses = 46,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 2,
        num_verses = 37,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 3,
        num_verses = 29,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 4,
        num_verses = 49,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 5,
        num_verses = 33,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 6,
        num_verses = 25,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 7,
        num_verses = 26,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 8,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 9,
        num_verses = 29,
    )
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 10,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 11,
        num_verses = 32,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 12,
        num_verses = 31,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 13,
        num_verses = 19,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 14,
        num_verses = 29,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 15,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 16,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 17,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 18,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 19,
        num_verses = 21,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 20,
        num_verses = 20,
    )
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 21,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 22,
        num_verses = 29,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 23,
        num_verses = 26,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 24,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 25,
        num_verses = 19,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 26,
        num_verses = 19,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 27,
        num_verses = 26,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 28,
        num_verses = 69,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 29,
        num_verses = 28,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 30,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 31,
        num_verses = 30,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 32,
        num_verses = 52,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 33,
        num_verses = 29,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Deuteronomy',
        Number = 34,
        num_verses = 12,
    ) 

    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 1,
        num_verses = 18,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 2,
        num_verses = 24,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 3,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 4,
        num_verses = 24,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 5,
        num_verses = 15,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 6,
        num_verses = 27,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 7,
        num_verses = 26,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 8,
        num_verses = 35,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 9,
        num_verses = 27,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 10,
        num_verses = 43,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 11,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 12,
        num_verses = 24,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 13,
        num_verses = 33,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 14,
        num_verses = 15,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 15,
        num_verses = 63,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 16,
        num_verses = 10,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 17,
        num_verses = 18,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 18,
        num_verses = 28,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 19,
        num_verses = 51,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 20,
        num_verses = 9,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 21,
        num_verses = 45,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 22,
        num_verses = 34,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 23,
        num_verses = 16,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Joshua',
        Number = 24,
        num_verses = 33,
    ) 

    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 1,
        num_verses = 36,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 2,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 3,
        num_verses = 31,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 4,
        num_verses = 24,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 5,
        num_verses = 31,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 6,
        num_verses = 40,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 7,
        num_verses = 25,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 8,
        num_verses = 35,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 9,
        num_verses = 57,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 10,
        num_verses = 18,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 11,
        num_verses = 40,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 12,
        num_verses = 15,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 13,
        num_verses = 25,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 14,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 15,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 16,
        num_verses = 31,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 17,
        num_verses = 13,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 18,
        num_verses = 31,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 19,
        num_verses = 30,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 20,
        num_verses = 48,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Judges',
        Number = 21,
        num_verses = 25,
    ) 

    chapter = Chapter.objects.create(
        Book = 'Ruth',
        Number = 1,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ruth',
        Number = 2,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ruth',
        Number = 3,
        num_verses = 18,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ruth',
        Number = 4,
        num_verses = 22,
    ) 

    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 1,
        num_verses = 28,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 2,
        num_verses = 36,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 3,
        num_verses = 21,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 4,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 5,
        num_verses = 12,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 6,
        num_verses = 21,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 7,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 8,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 9,
        num_verses = 27,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 10,
        num_verses = 27,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 11,
        num_verses = 15,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 12,
        num_verses = 25,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 13,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 14,
        num_verses = 52,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 15,
        num_verses = 35,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 16,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 17,
        num_verses = 58,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 18,
        num_verses = 30,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 19,
        num_verses = 24,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 20,
        num_verses = 42,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 21,
        num_verses = 15,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 22,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 23,
        num_verses = 29,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 24,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 25,
        num_verses = 44,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 26,
        num_verses = 25,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 27,
        num_verses = 12,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 28,
        num_verses = 25,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 29,
        num_verses = 11,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 30,
        num_verses = 31,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Samuel',
        Number = 31,
        num_verses = 13,
    ) 
    
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 1,
        num_verses = 27,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 2,
        num_verses = 32,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 3,
        num_verses = 39,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 4,
        num_verses = 12,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 5,
        num_verses = 25,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 6,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 7,
        num_verses = 29,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 8,
        num_verses = 18,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 9,
        num_verses = 13,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 10,
        num_verses = 19,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 11,
        num_verses = 27,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 12,
        num_verses = 31,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 13,
        num_verses = 39,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 14,
        num_verses = 33,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 15,
        num_verses = 37,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 16,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 17,
        num_verses = 29,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 18,
        num_verses = 32,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 19,
        num_verses = 44,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 20,
        num_verses = 26,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 21,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 22,
        num_verses = 51,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 23,
        num_verses = 39,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Samuel',
        Number = 24,
        num_verses = 25,
    ) 
    
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 1,
        num_verses = 53,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 2,
        num_verses = 46,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 3,
        num_verses = 28,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 4,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 5,
        num_verses = 32,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 6,
        num_verses = 38,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 7,
        num_verses = 51,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 8,
        num_verses = 66,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 9,
        num_verses = 28,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 10,
        num_verses = 29,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 11,
        num_verses = 43,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 12,
        num_verses = 33,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 13,
        num_verses = 34,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 14,
        num_verses = 31,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 15,
        num_verses = 34,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 16,
        num_verses = 34,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 17,
        num_verses = 24,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 18,
        num_verses = 46,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 19,
        num_verses = 21,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 20,
        num_verses = 43,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 21,
        num_verses = 29,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Kings',
        Number = 22,
        num_verses = 54,
    ) 

    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 1,
        num_verses = 18,
    )
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 2,
        num_verses = 25,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 3,
        num_verses = 27,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 4,
        num_verses = 44,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 5,
        num_verses = 27,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 6,
        num_verses = 33,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 7,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 8,
        num_verses = 29,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 9,
        num_verses = 37,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 10,
        num_verses = 36,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 11,
        num_verses = 20,
    )
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 12,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 13,
        num_verses = 25,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 14,
        num_verses = 29,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 15,
        num_verses = 38,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 16,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 17,
        num_verses = 41,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 18,
        num_verses = 37,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 19,
        num_verses = 37,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 20,
        num_verses = 21,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 21,
        num_verses = 26,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 22,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 23,
        num_verses = 37,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 24,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Kings',
        Number = 25,
        num_verses = 30,
    ) 

    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 1,
        num_verses = 54,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 2,
        num_verses = 55,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 3,
        num_verses = 24,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 4,
        num_verses = 43,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 5,
        num_verses = 41,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 6,
        num_verses = 66,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 7,
        num_verses = 40,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 8,
        num_verses = 40,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 9,
        num_verses = 44,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 10,
        num_verses = 14,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 11,
        num_verses = 47,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 12,
        num_verses = 41,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 13,
        num_verses = 14,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 14,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 15,
        num_verses = 29,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 16,
        num_verses = 43,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 17,
        num_verses = 27,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 18,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 19,
        num_verses = 19,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 20,
        num_verses = 8,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 21,
        num_verses = 30,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 22,
        num_verses = 19,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 23,
        num_verses = 32,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 24,
        num_verses = 31,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 25,
        num_verses = 31,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 26,
        num_verses = 32,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 27,
        num_verses = 34,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 28,
        num_verses = 21,
    ) 
    chapter = Chapter.objects.create(
        Book = '1 Chronicles',
        Number = 29,
        num_verses = 30,
    ) 

    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 1,
        num_verses = 18,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 2,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 3,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 4,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 5,
        num_verses = 14,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 6,
        num_verses = 42,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 7,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 8,
        num_verses = 18,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 9,
        num_verses = 31,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 10,
        num_verses = 19,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 11,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 12,
        num_verses = 16,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 13,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 14,
        num_verses = 14,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 15,
        num_verses = 19,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 16,
        num_verses = 14,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 17,
        num_verses = 19,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 18,
        num_verses = 34,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 19,
        num_verses = 11,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 20,
        num_verses = 37,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 21,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 22,
        num_verses = 12,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 23,
        num_verses = 21,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 24,
        num_verses = 27,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 25,
        num_verses = 28,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 26,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 27,
        num_verses = 9,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 28,
        num_verses = 27,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 29,
        num_verses = 36,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 30,
        num_verses = 27,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 31,
        num_verses = 21,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 32,
        num_verses = 33,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 33,
        num_verses = 25,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 34,
        num_verses = 33,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 35,
        num_verses = 26,
    ) 
    chapter = Chapter.objects.create(
        Book = '2 Chronicles',
        Number = 36,
        num_verses = 23,
    ) 

    chapter = Chapter.objects.create(
        Book = 'Ezra',
        Number = 1,
        num_verses = 11,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ezra',
        Number = 2,
        num_verses = 70,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ezra',
        Number = 3,
        num_verses = 13,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ezra',
        Number = 4,
        num_verses = 24,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ezra',
        Number = 5,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ezra',
        Number = 6,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ezra',
        Number = 7,
        num_verses = 28,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ezra',
        Number = 8,
        num_verses = 36,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ezra',
        Number = 9,
        num_verses = 15,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ezra',
        Number = 10,
        num_verses = 44,
    ) 

    chapter = Chapter.objects.create(
        Book = 'Nehemiah',
        Number = 1,
        num_verses = 11,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Nehemiah',
        Number = 2,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Nehemiah',
        Number = 3,
        num_verses = 38,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Nehemiah',
        Number = 4,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Nehemiah',
        Number = 5,
        num_verses = 19,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Nehemiah',
        Number = 6,
        num_verses = 19,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Nehemiah',
        Number = 7,
        num_verses = 72,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Nehemiah',
        Number = 8,
        num_verses = 18,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Nehemiah',
        Number = 9,
        num_verses = 37,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Nehemiah',
        Number = 10,
        num_verses = 40,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Nehemiah',
        Number = 11,
        num_verses = 36,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Nehemiah',
        Number = 12,
        num_verses = 47,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Nehemiah',
        Number = 13,
        num_verses = 31,
    ) 

    chapter = Chapter.objects.create(
        Book = 'Esther',
        Number = 1,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Esther',
        Number = 2,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Esther',
        Number = 3,
        num_verses = 15,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Esther',
        Number = 4,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Esther',
        Number = 5,
        num_verses = 14,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Esther',
        Number = 6,
        num_verses = 14,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Esther',
        Number = 7,
        num_verses = 10,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Esther',
        Number = 8,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Esther',
        Number = 9,
        num_verses = 32,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Esther',
        Number = 10,
        num_verses = 3,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Esther',
        Number = 11,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Esther',
        Number = 12,
        num_verses = 8,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Esther',
        Number = 13,
        num_verses = 30,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Esther',
        Number = 14,
        num_verses = 16,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Esther',
        Number = 15,
        num_verses = 24,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Esther',
        Number = 16,
        num_verses = 10,
    ) 

    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 1,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 2,
        num_verses = 13,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 3,
        num_verses = 26,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 4,
        num_verses = 27,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 5,
        num_verses = 30,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 6,
        num_verses = 30,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 7,
        num_verses = 21,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 8,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 9,
        num_verses = 35,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 10,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 11,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 12,
        num_verses = 25,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 13,
        num_verses = 28,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 14,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 15,
        num_verses = 35,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 16,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 17,
        num_verses = 16,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 18,
        num_verses = 21,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 19,
        num_verses = 29,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 20,
        num_verses = 29,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 21,
        num_verses = 34,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 22,
        num_verses = 30,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 23,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 24,
        num_verses = 25,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 25,
        num_verses = 6,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 26,
        num_verses = 14,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 27,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 28,
        num_verses = 28,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 29,
        num_verses = 25,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 30,
        num_verses = 31,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 31,
        num_verses = 40,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 32,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 33,
        num_verses = 33,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 34,
        num_verses = 37,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 35,
        num_verses = 16,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 36,
        num_verses = 33,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 37,
        num_verses = 24,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 38,
        num_verses = 41,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 39,
        num_verses = 30,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 40,
        num_verses = 24,
    )     
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 41,
        num_verses = 34,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Job',
        Number = 42,
        num_verses = 17,
    ) 

    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 1,
        num_verses = 6,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 2,
        num_verses = 12,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 3,
        num_verses = 8,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 4,
        num_verses = 8,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 5,
        num_verses = 12,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 6,
        num_verses = 10,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 7,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 8,
        num_verses = 9,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 9,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 10,
        num_verses = 18,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 11,
        num_verses = 7,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 12,
        num_verses = 8,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 13,
        num_verses = 6,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 14,
        num_verses = 7,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 15,
        num_verses = 5,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 16,
        num_verses = 11,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 17,
        num_verses = 15,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 18,
        num_verses = 50,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 19,
        num_verses = 14,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 20,
        num_verses = 9,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 21,
        num_verses = 13,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 22,
        num_verses = 31,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 23,
        num_verses = 6,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 24,
        num_verses = 10,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 25,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 26,
        num_verses = 12,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 27,
        num_verses = 14,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 28,
        num_verses = 9,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 29,
        num_verses = 11,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 30,
        num_verses = 12,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 31,
        num_verses = 24,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 32,
        num_verses = 11,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 33,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 34,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 35,
        num_verses = 28,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 36,
        num_verses = 12,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 37,
        num_verses = 40,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 38,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 39,
        num_verses = 13,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 40,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 41,
        num_verses = 13,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 42,
        num_verses = 11,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 43,
        num_verses = 5,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 44,
        num_verses = 26,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 45,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 46,
        num_verses = 11,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 47,
        num_verses = 9,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 48,
        num_verses = 14,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 49,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 50,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 51,
        num_verses = 19,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 52,
        num_verses = 9,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 53,
        num_verses = 6,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 54,
        num_verses = 7,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 55,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 56,
        num_verses = 13,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 57,
        num_verses = 11,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 58,
        num_verses = 11,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 59,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 60,
        num_verses = 12,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 61,
        num_verses = 8,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 62,
        num_verses = 12,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 63,
        num_verses = 11,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 64,
        num_verses = 10,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 65,
        num_verses = 13,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 66,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 67,
        num_verses = 7,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 68,
        num_verses = 35,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 69,
        num_verses = 36,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 70,
        num_verses = 5,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 71,
        num_verses = 24,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 72,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 73,
        num_verses = 28,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 74,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 75,
        num_verses = 10,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 76,
        num_verses = 12,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 77,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 78,
        num_verses = 72,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 79,
        num_verses = 13,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 80,
        num_verses = 19,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 81,
        num_verses = 16,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 82,
        num_verses = 8,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 83,
        num_verses = 18,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 84,
        num_verses = 12,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 85,
        num_verses = 13,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 86,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 87,
        num_verses = 7,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 88,
        num_verses = 18,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 89,
        num_verses = 52,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 90,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 91,
        num_verses = 16,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 92,
        num_verses = 15,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 93,
        num_verses = 5,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 94,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 95,
        num_verses = 11,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 96,
        num_verses = 13,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 97,
        num_verses = 12,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 98,
        num_verses = 9,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 99,
        num_verses = 9,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 100,
        num_verses = 5,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 101,
        num_verses = 8,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 102,
        num_verses = 28,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 103,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 104,
        num_verses = 35,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 105,
        num_verses = 45,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 106,
        num_verses = 48,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 107,
        num_verses = 43,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 108,
        num_verses = 13,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 109,
        num_verses = 31,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 110,
        num_verses = 7,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 111,
        num_verses = 10,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 112,
        num_verses = 10,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 113,
        num_verses = 9,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 114,
        num_verses = 8,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 115,
        num_verses = 18,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 116,
        num_verses = 19,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 117,
        num_verses = 2,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 118,
        num_verses = 29,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 119,
        num_verses = 176,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 120,
        num_verses = 7,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 121,
        num_verses = 8,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 122,
        num_verses = 9,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 123,
        num_verses = 4,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 124,
        num_verses = 8,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 125,
        num_verses = 5,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 126,
        num_verses = 6,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 127,
        num_verses = 5,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 128,
        num_verses = 6,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 129,
        num_verses = 8,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 130,
        num_verses = 8,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 131,
        num_verses = 3,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 132,
        num_verses = 18,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 133,
        num_verses = 3,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 134,
        num_verses = 3,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 135,
        num_verses = 21,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 136,
        num_verses = 26,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 137,
        num_verses = 9,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 138,
        num_verses = 8,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 139,
        num_verses = 24,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 140,
        num_verses = 13,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 141,
        num_verses = 10,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 142,
        num_verses = 7,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 143,
        num_verses = 12,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 144,
        num_verses = 15,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 145,
        num_verses = 21,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 146,
        num_verses = 10,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 147,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 148,
        num_verses = 14,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 149,
        num_verses = 9,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Psalms',
        Number = 150,
        num_verses = 6,
    ) 

    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 1,
        num_verses = 33,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 2,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 3,
        num_verses = 35,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 4,
        num_verses = 27,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 5,
        num_verses = 23,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 6,
        num_verses = 35,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 7,
        num_verses = 27,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 8,
        num_verses = 36,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 9,
        num_verses = 18,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 10,
        num_verses = 32,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 11,
        num_verses = 31,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 12,
        num_verses = 28,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 13,
        num_verses = 25,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 14,
        num_verses = 35,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 15,
        num_verses = 33,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 16,
        num_verses = 33,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 17,
        num_verses = 28,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 18,
        num_verses = 24,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 19,
        num_verses = 29,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 20,
        num_verses = 30,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 21,
        num_verses = 31,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 22,
        num_verses = 29,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 23,
        num_verses = 35,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 24,
        num_verses = 34,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 25,
        num_verses = 28,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 26,
        num_verses = 28,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 27,
        num_verses = 27,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 28,
        num_verses = 28,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 29,
        num_verses = 27,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 30,
        num_verses = 33,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Proverbs',
        Number = 31,
        num_verses = 31,
    ) 

    chapter = Chapter.objects.create(
        Book = 'Ecclesiastes',
        Number = 1,
        num_verses = 18,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ecclesiastes',
        Number = 2,
        num_verses = 26,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ecclesiastes',
        Number = 3,
        num_verses = 22,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ecclesiastes',
        Number = 4,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ecclesiastes',
        Number = 5,
        num_verses = 19,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ecclesiastes',
        Number = 6,
        num_verses = 12,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ecclesiastes',
        Number = 7,
        num_verses = 29,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ecclesiastes',
        Number = 8,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ecclesiastes',
        Number = 9,
        num_verses = 18,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ecclesiastes',
        Number = 10,
        num_verses = 20,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ecclesiastes',
        Number = 11,
        num_verses = 10,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Ecclesiastes',
        Number = 12,
        num_verses = 14,
    ) 

    chapter = Chapter.objects.create(
        Book = 'Song of Solomon',
        Number = 1,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = 'Song of Solomon',
        Number = 2,
        num_verses = 17,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Song of Solomon',
        Number = 3,
        num_verses = 11,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Song of Solomon',
        Number = 4,
        num_verses = 16,
    ) 
    chapter = Chapter.objects.create(
        Book = 'Song of Solomon',
        Number = 5,
        num_verses = 16,
    )
    chapter = Chapter.objects.create(
        Book = 'Song of Solomon',
        Number = 6,
        num_verses = 12,
    )
    chapter = Chapter.objects.create(
        Book = 'Song of Solomon',
        Number = 7,
        num_verses = 14,
    )
    chapter = Chapter.objects.create(
        Book = 'Song of Solomon',
        Number = 8,
        num_verses = 14,
    )

    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 1,
        num_verses = 31,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 2,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 3,
        num_verses = 26,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 4,
        num_verses = 6,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 5,
        num_verses = 30,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 6,
        num_verses = 13,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 7,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 8,
        num_verses = 23,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 9,
        num_verses = 20,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 10,
        num_verses = 34,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 11,
        num_verses = 16,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 12,
        num_verses = 6,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 13,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 14,
        num_verses = 32,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 15,
        num_verses = 9,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 16,
        num_verses = 14,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 17,
        num_verses = 14,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 18,
        num_verses = 7,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 19,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 20,
        num_verses = 6,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 21,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 22,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 23,
        num_verses = 18,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 24,
        num_verses = 23,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 25,
        num_verses = 12,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 26,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 27,
        num_verses = 13,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 28,
        num_verses = 29,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 29,
        num_verses = 24,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 30,
        num_verses = 33,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 31,
        num_verses = 9,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 32,
        num_verses = 20,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 33,
        num_verses = 24,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 34,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 35,
        num_verses = 10,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 36,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 37,
        num_verses = 38,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 38,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 39,
        num_verses = 8,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 40,
        num_verses = 31,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 41,
        num_verses = 29,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 42,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 43,
        num_verses = 28,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 44,
        num_verses = 28,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 45,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 46,
        num_verses = 13,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 47,
        num_verses = 15,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 48,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 49,
        num_verses = 26,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 50,
        num_verses = 11,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 51,
        num_verses = 23,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 52,
        num_verses = 15,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 53,
        num_verses = 12,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 54,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 55,
        num_verses = 13,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 56,
        num_verses = 12,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 57,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 58,
        num_verses = 14,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 59,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 60,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 61,
        num_verses = 11,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 62,
        num_verses = 12,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 63,
        num_verses = 19,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 64,
        num_verses = 12,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 65,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = 'Isaiah',
        Number = 66,
        num_verses = 24,
    )

    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 1,
        num_verses = 19,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 2,
        num_verses = 37,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 3,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 4,
        num_verses = 31,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 5,
        num_verses = 31,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 6,
        num_verses = 30,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 7,
        num_verses = 34,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 8,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 9,
        num_verses = 26,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 10,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 11,
        num_verses = 23,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 12,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 13,
        num_verses = 27,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 14,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 15,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 16,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 17,
        num_verses = 27,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 18,
        num_verses = 23,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 19,
        num_verses = 15,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 20,
        num_verses = 18,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 21,
        num_verses = 14,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 22,
        num_verses = 30,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 23,
        num_verses = 40,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 24,
        num_verses = 10,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 25,
        num_verses = 38,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 26,
        num_verses = 24,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 27,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 28,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 29,
        num_verses = 32,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 30,
        num_verses = 24,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 31,
        num_verses = 40,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 32,
        num_verses = 44,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 33,
        num_verses = 26,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 34,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 35,
        num_verses = 19,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 36,
        num_verses = 32,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 37,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 38,
        num_verses = 28,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 39,
        num_verses = 18,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 40,
        num_verses = 16,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 41,
        num_verses = 18,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 42,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 43,
        num_verses = 13,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 44,
        num_verses = 30,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 45,
        num_verses = 5,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 46,
        num_verses = 28,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 47,
        num_verses = 7,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 48,
        num_verses = 47,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 49,
        num_verses = 39,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 50,
        num_verses = 46,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 51,
        num_verses = 64,
    )
    chapter = Chapter.objects.create(
        Book = 'Jeremiah',
        Number = 52,
        num_verses = 34,
    )

    chapter = Chapter.objects.create(
        Book = 'Lamentations',
        Number = 1,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = 'Lamentations',
        Number = 2,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = 'Lamentations',
        Number = 3,
        num_verses = 66,
    )
    chapter = Chapter.objects.create(
        Book = 'Lamentations',
        Number = 4,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = 'Lamentations',
        Number = 5,
        num_verses = 22,
    )

    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 1,
        num_verses = 28,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 2,
        num_verses = 10,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 3,
        num_verses = 27,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 4,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 5,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 6,
        num_verses = 14,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 7,
        num_verses = 27,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 8,
        num_verses = 18,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 9,
        num_verses = 11,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 10,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 11,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 12,
        num_verses = 28,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 13,
        num_verses = 23,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 14,
        num_verses = 23,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 15,
        num_verses = 8,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 16,
        num_verses = 63,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 17,
        num_verses = 24,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 18,
        num_verses = 32,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 19,
        num_verses = 14,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 20,
        num_verses = 49,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 21,
        num_verses = 32,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 22,
        num_verses = 31,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 23,
        num_verses = 49,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 24,
        num_verses = 27,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 25,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 26,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 27,
        num_verses = 36,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 28,
        num_verses = 26,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 29,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 30,
        num_verses = 26,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 31,
        num_verses = 18,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 32,
        num_verses = 32,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 33,
        num_verses = 33,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 34,
        num_verses = 31,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 35,
        num_verses = 15,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 36,
        num_verses = 38,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 37,
        num_verses = 28,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 38,
        num_verses = 23,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 39,
        num_verses = 29,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 40,
        num_verses = 49,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 41,
        num_verses = 26,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 42,
        num_verses = 20,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 43,
        num_verses = 27,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 44,
        num_verses = 31,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 45,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 46,
        num_verses = 24,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 47,
        num_verses = 23,
    )
    chapter = Chapter.objects.create(
        Book = 'Ezekiel',
        Number = 48,
        num_verses = 35,
    )

    chapter = Chapter.objects.create(
        Book = 'Daniel',
        Number = 1,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Daniel',
        Number = 2,
        num_verses = 49,
    )
    chapter = Chapter.objects.create(
        Book = 'Daniel',
        Number = 3,
        num_verses = 100,
    )
    chapter = Chapter.objects.create(
        Book = 'Daniel',
        Number = 4,
        num_verses = 34,
    )
    chapter = Chapter.objects.create(
        Book = 'Daniel',
        Number = 5,
        num_verses = 30,
    )
    chapter = Chapter.objects.create(
        Book = 'Daniel',
        Number = 6,
        num_verses = 29,
    )
    chapter = Chapter.objects.create(
        Book = 'Daniel',
        Number = 7,
        num_verses = 28,
    )
    chapter = Chapter.objects.create(
        Book = 'Daniel',
        Number = 8,
        num_verses = 27,
    )
    chapter = Chapter.objects.create(
        Book = 'Daniel',
        Number = 9,
        num_verses = 27,
    )
    chapter = Chapter.objects.create(
        Book = 'Daniel',
        Number = 10,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Daniel',
        Number = 11,
        num_verses = 45,
    )
    chapter = Chapter.objects.create(
        Book = 'Daniel',
        Number = 12,
        num_verses = 13,
    )
    chapter = Chapter.objects.create(
        Book = 'Daniel',
        Number = 13,
        num_verses = 64,
    )
    chapter = Chapter.objects.create(
        Book = 'Daniel',
        Number = 14,
        num_verses = 42,
    )

    chapter = Chapter.objects.create(
        Book = 'Hosea',
        Number = 1,
        num_verses = 9,
    )
    chapter = Chapter.objects.create(
        Book = 'Hosea',
        Number = 2,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = 'Hosea',
        Number = 3,
        num_verses = 5,
    )
    chapter = Chapter.objects.create(
        Book = 'Hosea',
        Number = 4,
        num_verses = 19,
    )
    chapter = Chapter.objects.create(
        Book = 'Hosea',
        Number = 5,
        num_verses = 15,
    )
    chapter = Chapter.objects.create(
        Book = 'Hosea',
        Number = 6,
        num_verses = 11,
    )
    chapter = Chapter.objects.create(
        Book = 'Hosea',
        Number = 7,
        num_verses = 16,
    )
    chapter = Chapter.objects.create(
        Book = 'Hosea',
        Number = 8,
        num_verses = 14,
    )
    chapter = Chapter.objects.create(
        Book = 'Hosea',
        Number = 9,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = 'Hosea',
        Number = 10,
        num_verses = 15,
    )
    chapter = Chapter.objects.create(
        Book = 'Hosea',
        Number = 11,
        num_verses = 11,
    )
    chapter = Chapter.objects.create(
        Book = 'Hosea',
        Number = 12,
        num_verses = 15,
    )
    chapter = Chapter.objects.create(
        Book = 'Hosea',
        Number = 13,
        num_verses = 15,
    )
    chapter = Chapter.objects.create(
        Book = 'Hosea',
        Number = 14,
        num_verses = 10,
    )

    chapter = Chapter.objects.create(
        Book = 'Joel',
        Number = 1,
        num_verses = 20,
    )
    chapter = Chapter.objects.create(
        Book = 'Joel',
        Number = 2,
        num_verses = 27,
    )
    chapter = Chapter.objects.create(
        Book = 'Joel',
        Number = 3,
        num_verses = 5,
    )
    chapter = Chapter.objects.create(
        Book = 'Joel',
        Number = 4,
        num_verses = 21,
    )

    chapter = Chapter.objects.create(
        Book = 'Amos',
        Number = 1,
        num_verses = 15,
    )
    chapter = Chapter.objects.create(
        Book = 'Amos',
        Number = 2,
        num_verses = 16,
    )
    chapter = Chapter.objects.create(
        Book = 'Amos',
        Number = 3,
        num_verses = 15,
    )
    chapter = Chapter.objects.create(
        Book = 'Amos',
        Number = 4,
        num_verses = 13,
    )
    chapter = Chapter.objects.create(
        Book = 'Amos',
        Number = 5,
        num_verses = 27,
    )
    chapter = Chapter.objects.create(
        Book = 'Amos',
        Number = 6,
        num_verses = 14,
    )
    chapter = Chapter.objects.create(
        Book = 'Amos',
        Number = 7,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = 'Amos',
        Number = 8,
        num_verses = 14,
    )
    chapter = Chapter.objects.create(
        Book = 'Amos',
        Number = 9,
        num_verses = 15,
    )

    chapter = Chapter.objects.create(
        Book = 'Obadiah',
        Number = 1,
        num_verses = 21,
    )

    chapter = Chapter.objects.create(
        Book = 'Jonah',
        Number = 1,
        num_verses = 16,
    )
    chapter = Chapter.objects.create(
        Book = 'Jonah',
        Number = 2,
        num_verses = 11,
    )
    chapter = Chapter.objects.create(
        Book = 'Jonah',
        Number = 3,
        num_verses = 10,
    )
    chapter = Chapter.objects.create(
        Book = 'Jonah',
        Number = 4,
        num_verses = 11,
    )

    chapter = Chapter.objects.create(
        Book = 'Micah',
        Number = 1,
        num_verses = 16,
    )
    chapter = Chapter.objects.create(
        Book = 'Micah',
        Number = 2,
        num_verses = 13,
    )
    chapter = Chapter.objects.create(
        Book = 'Micah',
        Number = 3,
        num_verses = 12,
    )
    chapter = Chapter.objects.create(
        Book = 'Micah',
        Number = 4,
        num_verses = 14,
    )
    chapter = Chapter.objects.create(
        Book = 'Micah',
        Number = 5,
        num_verses = 14,
    )
    chapter = Chapter.objects.create(
        Book = 'Micah',
        Number = 6,
        num_verses = 16,
    )
    chapter = Chapter.objects.create(
        Book = 'Micah',
        Number = 7,
        num_verses = 20,
    )

    chapter = Chapter.objects.create(
        Book = 'Nahum',
        Number = 1,
        num_verses = 14,
    )
    chapter = Chapter.objects.create(
        Book = 'Nahum',
        Number = 2,
        num_verses = 14,
    )
    chapter = Chapter.objects.create(
        Book = 'Nahum',
        Number = 3,
        num_verses = 19,
    )

    chapter = Chapter.objects.create(
        Book = 'Habakkuk',
        Number = 1,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = 'Habakkuk',
        Number = 2,
        num_verses = 20,
    )
    chapter = Chapter.objects.create(
        Book = 'Habakkuk',
        Number = 3,
        num_verses = 19,
    )

    chapter = Chapter.objects.create(
        Book = 'Zephaniah',
        Number = 1,
        num_verses = 18,
    )
    chapter = Chapter.objects.create(
        Book = 'Zephaniah',
        Number = 2,
        num_verses = 15,
    )
    chapter = Chapter.objects.create(
        Book = 'Zephaniah',
        Number = 3,
        num_verses = 20,
    )

    chapter = Chapter.objects.create(
        Book = 'Haggai',
        Number = 1,
        num_verses = 15,
    )
    chapter = Chapter.objects.create(
        Book = 'Haggai',
        Number = 2,
        num_verses = 23,
    )

    chapter = Chapter.objects.create(
        Book = 'Zechariah',
        Number = 1,
        num_verses = 17,
    )   
    chapter = Chapter.objects.create(
        Book = 'Zechariah',
        Number = 2,
        num_verses = 17,
    )   
    chapter = Chapter.objects.create(
        Book = 'Zechariah',
        Number = 3,
        num_verses = 10,
    )   
    chapter = Chapter.objects.create(
        Book = 'Zechariah',
        Number = 4,
        num_verses = 14,
    )   
    chapter = Chapter.objects.create(
        Book = 'Zechariah',
        Number = 5,
        num_verses = 11,
    )   
    chapter = Chapter.objects.create(
        Book = 'Zechariah',
        Number = 6,
        num_verses = 15,
    )   
    chapter = Chapter.objects.create(
        Book = 'Zechariah',
        Number = 7,
        num_verses = 14,
    )   
    chapter = Chapter.objects.create(
        Book = 'Zechariah',
        Number = 8,
        num_verses = 23,
    )   
    chapter = Chapter.objects.create(
        Book = 'Zechariah',
        Number = 9,
        num_verses = 17,
    )   
    chapter = Chapter.objects.create(
        Book = 'Zechariah',
        Number = 10,
        num_verses = 12,
    )   
    chapter = Chapter.objects.create(
        Book = 'Zechariah',
        Number = 11,
        num_verses = 17,
    )   
    chapter = Chapter.objects.create(
        Book = 'Zechariah',
        Number = 12,
        num_verses = 14,
    )   
    chapter = Chapter.objects.create(
        Book = 'Zechariah',
        Number = 13,
        num_verses = 9,
    )   
    chapter = Chapter.objects.create(
        Book = 'Zechariah',
        Number = 14,
        num_verses = 21,
    )   

    chapter = Chapter.objects.create(
        Book = 'Malachi',
        Number = 1,
        num_verses = 14,
    )  
    chapter = Chapter.objects.create(
        Book = 'Malachi',
        Number = 2,
        num_verses = 17,
    )  
    chapter = Chapter.objects.create(
        Book = 'Malachi',
        Number = 3,
        num_verses = 24,
    )  

    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 1,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 2,
        num_verses = 23,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 3,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 4,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 5,
        num_verses = 48,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 6,
        num_verses = 34,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 7,
        num_verses = 29,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 8,
        num_verses = 34,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 9,
        num_verses = 38,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 10,
        num_verses = 42,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 11,
        num_verses = 30,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 12,
        num_verses = 50,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 13,
        num_verses = 58,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 14,
        num_verses = 36,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 15,
        num_verses = 39,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 16,
        num_verses = 28,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 17,
        num_verses = 27,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 18,
        num_verses = 35,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 19,
        num_verses = 30,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 20,
        num_verses = 34,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 21,
        num_verses = 46,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 22,
        num_verses = 46,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 23,
        num_verses = 39,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 24,
        num_verses = 51,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 25,
        num_verses = 46,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 26,
        num_verses = 75,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 27,
        num_verses = 66,
    )
    chapter = Chapter.objects.create(
        Book = 'Matthew',
        Number = 28,
        num_verses = 20,
    )

    chapter = Chapter.objects.create(
        Book = 'Mark',
        Number = 1,
        num_verses = 45,
    )
    chapter = Chapter.objects.create(
        Book = 'Mark',
        Number = 2,
        num_verses = 28,
    )
    chapter = Chapter.objects.create(
        Book = 'Mark',
        Number = 3,
        num_verses = 35,
    )
    chapter = Chapter.objects.create(
        Book = 'Mark',
        Number = 4,
        num_verses = 41,
    )
    chapter = Chapter.objects.create(
        Book = 'Mark',
        Number = 5,
        num_verses = 43,
    )
    chapter = Chapter.objects.create(
        Book = 'Mark',
        Number = 6,
        num_verses = 56,
    )
    chapter = Chapter.objects.create(
        Book = 'Mark',
        Number = 7,
        num_verses = 37,
    )
    chapter = Chapter.objects.create(
        Book = 'Mark',
        Number = 8,
        num_verses = 38,
    )
    chapter = Chapter.objects.create(
        Book = 'Mark',
        Number = 9,
        num_verses = 50,
    )
    chapter = Chapter.objects.create(
        Book = 'Mark',
        Number = 10,
        num_verses = 52,
    )
    chapter = Chapter.objects.create(
        Book = 'Mark',
        Number = 11,
        num_verses = 33,
    )
    chapter = Chapter.objects.create(
        Book = 'Mark',
        Number = 12,
        num_verses = 44,
    )
    chapter = Chapter.objects.create(
        Book = 'Mark',
        Number = 13,
        num_verses = 37,
    )
    chapter = Chapter.objects.create(
        Book = 'Mark',
        Number = 14,
        num_verses = 72,
    )
    chapter = Chapter.objects.create(
        Book = 'Mark',
        Number = 15,
        num_verses = 47,
    )
    chapter = Chapter.objects.create(
        Book = 'Mark',
        Number = 16,
        num_verses = 20,
    )

    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 1,
        num_verses = 80,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 2,
        num_verses = 52,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 3,
        num_verses = 38,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 4,
        num_verses = 44,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 5,
        num_verses = 39,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 6,
        num_verses = 49,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 7,
        num_verses = 50,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 8,
        num_verses = 56,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 9,
        num_verses = 62,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 10,
        num_verses = 42,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 11,
        num_verses = 54,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 12,
        num_verses = 59,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 13,
        num_verses = 35,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 14,
        num_verses = 35,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 15,
        num_verses = 32,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 16,
        num_verses = 31,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 17,
        num_verses = 37,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 18,
        num_verses = 43,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 19,
        num_verses = 48,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 20,
        num_verses = 47,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 21,
        num_verses = 38,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 22,
        num_verses = 71,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 23,
        num_verses = 56,
    )
    chapter = Chapter.objects.create(
        Book = 'Luke',
        Number = 24,
        num_verses = 53,
    )

    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 1,
        num_verses = 51,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 2,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 3,
        num_verses = 36,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 4,
        num_verses = 54,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 5,
        num_verses = 47,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 6,
        num_verses = 71,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 7,
        num_verses = 53,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 8,
        num_verses = 59,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 9,
        num_verses = 41,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 10,
        num_verses = 42,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 11,
        num_verses = 57,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 12,
        num_verses = 50,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 13,
        num_verses = 38,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 14,
        num_verses = 31,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 15,
        num_verses = 27,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 16,
        num_verses = 33,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 17,
        num_verses = 26,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 18,
        num_verses = 40,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 19,
        num_verses = 42,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 20,
        num_verses = 31,
    )
    chapter = Chapter.objects.create(
        Book = 'John',
        Number = 21,
        num_verses = 25,
    )

    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 1,
        num_verses = 26,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 2,
        num_verses = 47,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 3,
        num_verses = 26,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 4,
        num_verses = 37,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 5,
        num_verses = 42,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 6,
        num_verses = 15,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 7,
        num_verses = 60,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 8,
        num_verses = 40,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 9,
        num_verses = 43,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 10,
        num_verses = 48,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 11,
        num_verses = 30,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 12,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 13,
        num_verses = 52,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 14,
        num_verses = 28,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 15,
        num_verses = 41,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 16,
        num_verses = 40,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 17,
        num_verses = 34,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 18,
        num_verses = 28,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 19,
        num_verses = 41,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 20,
        num_verses = 38,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 21,
        num_verses = 40,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 22,
        num_verses = 30,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 23,
        num_verses = 35,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 24,
        num_verses = 27,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 25,
        num_verses = 27,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 26,
        num_verses = 32,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 27,
        num_verses = 44,
    )
    chapter = Chapter.objects.create(
        Book = 'Acts',
        Number = 28,
        num_verses = 31,
    )

    chapter = Chapter.objects.create(
        Book = 'Romans',
        Number = 1,
        num_verses = 32,
    )
    chapter = Chapter.objects.create(
        Book = 'Romans',
        Number = 2,
        num_verses = 29,
    )
    chapter = Chapter.objects.create(
        Book = 'Romans',
        Number = 3,
        num_verses = 31,
    )
    chapter = Chapter.objects.create(
        Book = 'Romans',
        Number = 4,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = 'Romans',
        Number = 5,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Romans',
        Number = 6,
        num_verses = 23,
    )
    chapter = Chapter.objects.create(
        Book = 'Romans',
        Number = 7,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = 'Romans',
        Number = 8,
        num_verses = 39,
    )
    chapter = Chapter.objects.create(
        Book = 'Romans',
        Number = 9,
        num_verses = 33,
    )
    chapter = Chapter.objects.create(
        Book = 'Romans',
        Number = 10,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Romans',
        Number = 11,
        num_verses = 36,
    )
    chapter = Chapter.objects.create(
        Book = 'Romans',
        Number = 12,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Romans',
        Number = 13,
        num_verses = 14,
    )
    chapter = Chapter.objects.create(
        Book = 'Romans',
        Number = 14,
        num_verses = 23,
    )
    chapter = Chapter.objects.create(
        Book = 'Romans',
        Number = 15,
        num_verses = 33,
    )
    chapter = Chapter.objects.create(
        Book = 'Romans',
        Number = 16,
        num_verses = 27,
    )
    
    chapter = Chapter.objects.create(
        Book = '1 Corinthians',
        Number = 1,
        num_verses = 31,
    )
    chapter = Chapter.objects.create(
        Book = '1 Corinthians',
        Number = 2,
        num_verses = 16,
    )
    chapter = Chapter.objects.create(
        Book = '1 Corinthians',
        Number = 3,
        num_verses = 23,
    )
    chapter = Chapter.objects.create(
        Book = '1 Corinthians',
        Number = 4,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = '1 Corinthians',
        Number = 5,
        num_verses = 13,
    )
    chapter = Chapter.objects.create(
        Book = '1 Corinthians',
        Number = 6,
        num_verses = 20,
    )
    chapter = Chapter.objects.create(
        Book = '1 Corinthians',
        Number = 7,
        num_verses = 40,
    )
    chapter = Chapter.objects.create(
        Book = '1 Corinthians',
        Number = 8,
        num_verses = 13,
    )
    chapter = Chapter.objects.create(
        Book = '1 Corinthians',
        Number = 9,
        num_verses = 27,
    )
    chapter = Chapter.objects.create(
        Book = '1 Corinthians',
        Number = 10,
        num_verses = 33,
    )
    chapter = Chapter.objects.create(
        Book = '1 Corinthians',
        Number = 11,
        num_verses = 34,
    )
    chapter = Chapter.objects.create(
        Book = '1 Corinthians',
        Number = 12,
        num_verses = 31,
    )
    chapter = Chapter.objects.create(
        Book = '1 Corinthians',
        Number = 13,
        num_verses = 13,
    )
    chapter = Chapter.objects.create(
        Book = '1 Corinthians',
        Number = 14,
        num_verses = 40,
    )
    chapter = Chapter.objects.create(
        Book = '1 Corinthians',
        Number = 15,
        num_verses = 58,
    )
    chapter = Chapter.objects.create(
        Book = '1 Corinthians',
        Number = 16,
        num_verses = 24,
    )

    chapter = Chapter.objects.create(
        Book = '2 Corinthians',
        Number = 1,
        num_verses = 24,
    )
    chapter = Chapter.objects.create(
        Book = '2 Corinthians',
        Number = 2,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = '2 Corinthians',
        Number = 3,
        num_verses = 18,
    )
    chapter = Chapter.objects.create(
        Book = '2 Corinthians',
        Number = 4,
        num_verses = 18,
    )
    chapter = Chapter.objects.create(
        Book = '2 Corinthians',
        Number = 5,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = '2 Corinthians',
        Number = 6,
        num_verses = 18,
    )
    chapter = Chapter.objects.create(
        Book = '2 Corinthians',
        Number = 7,
        num_verses = 16,
    )
    chapter = Chapter.objects.create(
        Book = '2 Corinthians',
        Number = 8,
        num_verses = 24,
    )
    chapter = Chapter.objects.create(
        Book = '2 Corinthians',
        Number = 9,
        num_verses = 15,
    )
    chapter = Chapter.objects.create(
        Book = '2 Corinthians',
        Number = 10,
        num_verses = 18,
    )
    chapter = Chapter.objects.create(
        Book = '2 Corinthians',
        Number = 11,
        num_verses = 33,
    )
    chapter = Chapter.objects.create(
        Book = '2 Corinthians',
        Number = 12,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = '2 Corinthians',
        Number = 13,
        num_verses = 13,
    )

    chapter = Chapter.objects.create(
        Book = 'Galatians',
        Number = 1,
        num_verses = 24,
    )
    chapter = Chapter.objects.create(
        Book = 'Galatians',
        Number = 2,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Galatians',
        Number = 3,
        num_verses = 29,
    )
    chapter = Chapter.objects.create(
        Book = 'Galatians',
        Number = 4,
        num_verses = 31,
    )
    chapter = Chapter.objects.create(
        Book = 'Galatians',
        Number = 5,
        num_verses = 26,
    )
    chapter = Chapter.objects.create(
        Book = 'Galatians',
        Number = 6,
        num_verses = 18,
    )

    chapter = Chapter.objects.create(
        Book = 'Ephesians',
        Number = 1,
        num_verses = 23,
    )
    chapter = Chapter.objects.create(
        Book = 'Ephesians',
        Number = 2,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = 'Ephesians',
        Number = 3,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Ephesians',
        Number = 4,
        num_verses = 32,
    )
    chapter = Chapter.objects.create(
        Book = 'Ephesians',
        Number = 5,
        num_verses = 33,
    )
    chapter = Chapter.objects.create(
        Book = 'Ephesians',
        Number = 6,
        num_verses = 24,
    )

    chapter = Chapter.objects.create(
        Book = 'Philippians',
        Number = 1,
        num_verses = 30,
    )
    chapter = Chapter.objects.create(
        Book = 'Philippians',
        Number = 2,
        num_verses = 30,
    )
    chapter = Chapter.objects.create(
        Book = 'Philippians',
        Number = 3,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Philippians',
        Number = 4,
        num_verses = 23,
    )

    chapter = Chapter.objects.create(
        Book = 'Colossians',
        Number = 1,
        num_verses = 29,
    )
    chapter = Chapter.objects.create(
        Book = 'Colossians',
        Number = 2,
        num_verses = 23,
    )
    chapter = Chapter.objects.create(
        Book = 'Colossians',
        Number = 3,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = 'Colossians',
        Number = 4,
        num_verses = 18,
    )

    chapter = Chapter.objects.create(
        Book = '1 Thessalonians',
        Number = 1,
        num_verses = 10,
    )
    chapter = Chapter.objects.create(
        Book = '1 Thessalonians',
        Number = 2,
        num_verses = 20,
    )
    chapter = Chapter.objects.create(
        Book = '1 Thessalonians',
        Number = 3,
        num_verses = 13,
    )
    chapter = Chapter.objects.create(
        Book = '1 Thessalonians',
        Number = 4,
        num_verses = 18,
    )
    chapter = Chapter.objects.create(
        Book = '1 Thessalonians',
        Number = 5,
        num_verses = 28,
    )

    chapter = Chapter.objects.create(
        Book = '2 Thessalonians',
        Number = 1,
        num_verses = 12,
    )
    chapter = Chapter.objects.create(
        Book = '2 Thessalonians',
        Number = 2,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = '2 Thessalonians',
        Number = 3,
        num_verses = 18,
    )

    chapter = Chapter.objects.create(
        Book = '1 Timothy',
        Number = 1,
        num_verses = 20,
    )
    chapter = Chapter.objects.create(
        Book = '1 Timothy',
        Number = 2,
        num_verses = 15,
    )
    chapter = Chapter.objects.create(
        Book = '1 Timothy',
        Number = 3,
        num_verses = 16,
    )
    chapter = Chapter.objects.create(
        Book = '1 Timothy',
        Number = 4,
        num_verses = 16,
    )
    chapter = Chapter.objects.create(
        Book = '1 Timothy',
        Number = 5,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = '1 Timothy',
        Number = 6,
        num_verses = 21,
    )

    chapter = Chapter.objects.create(
        Book = '2 Timothy',
        Number = 1,
        num_verses = 18,
    )
    chapter = Chapter.objects.create(
        Book = '2 Timothy',
        Number = 2,
        num_verses = 26,
    )
    chapter = Chapter.objects.create(
        Book = '2 Timothy',
        Number = 3,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = '2 Timothy',
        Number = 4,
        num_verses = 22,
    )

    chapter = Chapter.objects.create(
        Book = 'Titus',
        Number = 1,
        num_verses = 16,
    )
    chapter = Chapter.objects.create(
        Book = 'Titus',
        Number = 2,
        num_verses = 15,
    )
    chapter = Chapter.objects.create(
        Book = 'Titus',
        Number = 3,
        num_verses = 15,
    )

    chapter = Chapter.objects.create(
        Book = 'Philemon',
        Number = 1,
        num_verses = 25,
    )

    chapter = Chapter.objects.create(
        Book = 'Hebrews',
        Number = 1,
        num_verses = 14,
    )
    chapter = Chapter.objects.create(
        Book = 'Hebrews',
        Number = 2,
        num_verses = 18,
    )
    chapter = Chapter.objects.create(
        Book = 'Hebrews',
        Number = 3,
        num_verses = 19,
    )
    chapter = Chapter.objects.create(
        Book = 'Hebrews',
        Number = 4,
        num_verses = 16,
    )
    chapter = Chapter.objects.create(
        Book = 'Hebrews',
        Number = 5,
        num_verses = 14,
    )
    chapter = Chapter.objects.create(
        Book = 'Hebrews',
        Number = 6,
        num_verses = 20,
    )
    chapter = Chapter.objects.create(
        Book = 'Hebrews',
        Number = 7,
        num_verses = 28,
    )
    chapter = Chapter.objects.create(
        Book = 'Hebrews',
        Number = 8,
        num_verses = 13,
    )
    chapter = Chapter.objects.create(
        Book = 'Hebrews',
        Number = 9,
        num_verses = 28,
    )
    chapter = Chapter.objects.create(
        Book = 'Hebrews',
        Number = 10,
        num_verses = 39,
    )
    chapter = Chapter.objects.create(
        Book = 'Hebrews',
        Number = 11,
        num_verses = 40,
    )
    chapter = Chapter.objects.create(
        Book = 'Hebrews',
        Number = 12,
        num_verses = 29,
    )
    chapter = Chapter.objects.create(
        Book = 'Hebrews',
        Number = 13,
        num_verses = 25,
    )

    chapter = Chapter.objects.create(
        Book = 'James',
        Number = 1,
        num_verses = 27,
    )
    chapter = Chapter.objects.create(
        Book = 'James',
        Number = 2,
        num_verses = 26,
    )
    chapter = Chapter.objects.create(
        Book = 'James',
        Number = 3,
        num_verses = 18,
    )
    chapter = Chapter.objects.create(
        Book = 'James',
        Number = 4,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = 'James',
        Number = 5,
        num_verses = 20,
    )

    chapter = Chapter.objects.create(
        Book = '1 Peter',
        Number = 1,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = '1 Peter',
        Number = 2,
        num_verses = 25,
    )
    chapter = Chapter.objects.create(
        Book = '1 Peter',
        Number = 3,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = '1 Peter',
        Number = 4,
        num_verses = 19,
    )
    chapter = Chapter.objects.create(
        Book = '1 Peter',
        Number = 5,
        num_verses = 14,
    )

    chapter = Chapter.objects.create(
        Book = '2 Peter',
        Number = 1,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = '2 Peter',
        Number = 2,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = '2 Peter',
        Number = 3,
        num_verses = 18,
    )

    chapter = Chapter.objects.create(
        Book = '1 John',
        Number = 1,
        num_verses = 10,
    )
    chapter = Chapter.objects.create(
        Book = '1 John',
        Number = 2,
        num_verses = 29,
    )
    chapter = Chapter.objects.create(
        Book = '1 John',
        Number = 3,
        num_verses = 24,
    )
    chapter = Chapter.objects.create(
        Book = '1 John',
        Number = 4,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = '1 John',
        Number = 5,
        num_verses = 21,
    )

    chapter = Chapter.objects.create(
        Book = '2 John',
        Number = 1,
        num_verses = 13,
    )

    chapter = Chapter.objects.create(
        Book = '3 John',
        Number = 1,
        num_verses = 15,
    )

    chapter = Chapter.objects.create(
        Book = 'Jude',
        Number = 1,
        num_verses = 25,
    )

    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 1,
        num_verses = 20,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 2,
        num_verses = 29,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 3,
        num_verses = 22,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 4,
        num_verses = 11,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 5,
        num_verses = 14,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 6,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 7,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 8,
        num_verses = 13,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 9,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 10,
        num_verses = 11,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 11,
        num_verses = 19,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 12,
        num_verses = 17,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 13,
        num_verses = 18,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 14,
        num_verses = 20,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 15,
        num_verses = 8,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 16,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 17,
        num_verses = 18,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 18,
        num_verses = 24,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 19,
        num_verses = 21,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 20,
        num_verses = 15,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 21,
        num_verses = 27,
    )
    chapter = Chapter.objects.create(
        Book = 'Revelations',
        Number = 22,
        num_verses = 21,
    )

    request.session['initialize'] = True
    # print('$$$')
    # print('initialized!')
    # print('$$$')
    return redirect('/')