from django.shortcuts import render,redirect
from . models import Feedback
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['studentName'] and request.POST['studentID'] and request.POST['email'] and request.POST['college'] and request.POST['FB']:
            feedback = Feedback()
            feedback.name = request.POST['studentName']
            feedback.idnum = request.POST['studentID']
            feedback.email=request.POST['email']
            feedback.collage=request.POST['college']
            feedback.summary=request.POST['FB']
            feedback.date= timezone.datetime.now()
            feedback.hunter = request.user
            feedback.save()
            return redirect("/feedback/"+str(feedback.id))
        else:
            return render(request, 'feedback/fb.html',{'error':'All fields are required.'})
    else:
        return render(request, 'feedback/fb.html')

@login_required(login_url="/accounts/signup")
def detail(request,feedback_id):
    feedback=get_object_or_404(Feedback, pk=feedback_id)
    return render(request,'feedback/detail.html',{'feedback':feedback})