from django.shortcuts import render


# Create your views here.
def show_details(request, my_id=1):
    if my_id == 1:
        student = {'id': my_id, 'name': 'Rohit'}
    if my_id == 2:
        student = {'id': my_id, 'name': 'frnak'}
    if my_id == 3:
        student = {'id': my_id, 'name': 'luka'}
    return render(request, 'enroll/show.html', student)


def show_subdetails(request, my_id, subid):
    if my_id == 1 and subid == 5:
        student = {'id': my_id, 'name': 'Rohit', 'info': "this is sub detail"}
    if my_id == 2 and subid == 6:
        student = {'id': my_id, 'name': 'frnak', 'info': "this is sub detail"}
    if my_id == 3 and subid == 7:
        student = {'id': my_id, 'name': 'luka', 'info': "this is sub detail"}
    return render(request, 'enroll/show.html', student)


def home(request, check):
    print(check)
    return render(request, 'enroll/home.html')
