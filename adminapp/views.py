from django.shortcuts import render

from .models import *


# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_exam(request):
    if request.method == 'POST':
        title = request.POST['title']
        logo = request.FILES['logo']
        short_desc = request.POST['short_desc']
        no_of_vc = request.POST['no_of_vc']
        exam_date = request.POST['exam_date']
        official_url = request.POST['official_url']
        salary = request.POST['salary']
        latest_url = request.POST['latest_url']
        registration_date = request.POST['registration_date']
        official_notification = request.FILES['official_notification']
        ctr = Exam(title=title,logo=logo, short_description=short_desc, exam_date=exam_date, official_website_link=official_url,
                   registration_date=registration_date, salary=salary, vacancies=no_of_vc,
                   official_website_notification=official_notification, latest_updates_links=latest_url)
        ctr.save()
    return render(request, 'admin/admin-exam-add.html')


def all_exam(request):
    all_exam = Exam.objects.all()
    return render(request, 'admin/admin-exam-all.html', {'exam': all_exam})



