from django.shortcuts import render
from bookreservation.models import Bookdetails, Studentdetails, Reservationinformation
from django.db import connection
from bookreservation.models import Bookdetails, Studentdetails
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import HttpResponse

# Create your views here.

@login_required
def dashboard(request):
    totstudents = Studentdetails.objects.count()
    avg_gpa = Studentdetails.objects.aggregate(average_gpa=Avg('gpa'))['average_gpa']
    freshman_students = Studentdetails.objects.filter(year="Freshman").count()
    sophomore_students = Studentdetails.objects.filter(year="Sophomore").count()
    junior_students = Studentdetails.objects.filter(year="Junior").count()
    senior_students = Studentdetails.objects.filter(year="Senior").count()
    context = {'avggpa': avg_gpa, 'totalstudents': totstudents, 'freshman': freshman_students, 'sophomore': sophomore_students, 'junior': junior_students, 'senior': senior_students}
    return render(request, "bookreservation/dashboard.html", context)

@login_required
def student_details(request):

    studentdata = Studentdetails.objects.all()

    paginator = Paginator(studentdata, 10)

    page = request.GET.get('page')

    page_data = paginator.get_page(page)
    context = {'data': page_data}
    return render(request, 'bookreservation/studentdetails.html', context)

@login_required
def book_details(request):
    bookdata = Bookdetails.objects.all().order_by('-numberoftimescheckedout')
    paginator = Paginator(bookdata, 10)
    page = request.GET.get('page')
    page_data = paginator.get_page(page)
    context = {'data': page_data}
    return render(request, 'bookreservation/bookdetails.html', context)

@login_required
def book_reservation(request):
    studentdata = Studentdetails.objects.all()
    available_books = Bookdetails.objects.filter(currentlycheckedout=False)
    reservationdata = Reservationinformation.objects.all()
    context = {'student': studentdata, 'book': available_books, 'reservation': reservationdata}
    return render(request, 'bookreservation/reservation.html', context)

@login_required
def savereservation(request):
    if 'first_name' in request.GET and 'book_name' in request.GET:
        fname = request.GET.get('first_name')
        bookname = request.GET.get('book_name')

        student_book_count = Reservationinformation.objects.filter(first_name=fname).count()
        if(student_book_count >= 4):
            return HttpResponse("Student cannot reserve more than 4 books")

        book_reserved = Reservationinformation.objects.filter(book_name=bookname).exists()
        if(book_reserved):
            return HttpResponse("Book is already reserved")

        student = Studentdetails.objects.filter(firstname=fname).first()
        book = Bookdetails.objects.filter(bookname=bookname).first()

        reservation = Reservationinformation(
            student_id=student.studentid,
            first_name=student.firstname,
            last_name=student.lastname,
            book_id=book.bookid,
            book_name=book.bookname,
        )
        reservation.save()

        book.currentlycheckedout = True
        book.numberoftimescheckedout += 1
        book.save()

        return HttpResponse("success")
    return HttpResponse("error")
