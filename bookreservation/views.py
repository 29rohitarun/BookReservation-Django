from django.shortcuts import render
from bookreservation.models import Bookdetails, Studentdetails
from django.db import connection
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    return render(request, "bookreservation/home.html")


# Create your views here.
