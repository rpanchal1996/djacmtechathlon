from django.shortcuts import render

from .forms import UserForm

from django.http import HttpResponseRedirect, HttpResponse
from .models import Question , TestStart, CorrectAnswers

from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
import operator







def register(request):


    registered = False

    if request.method == 'POST':
    
        user_form = UserForm(data=request.POST)
        

        if user_form.is_valid():
      
            user = user_form.save()

           
            user.set_password(user.password)
            user.save()

            
            
            registered = True

      
        else:
            print("invalid form")

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        

    # Render the template depending on the context.
    return render(request,
            'register.html',
            {'user_form': user_form,'registered': registered} )



def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: ")
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})

def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/login')


def answer_submit1(request):
    #qno=0;
    #send=str(request.path)
    #send1=send[8:]
    #send2=int(send1)
    #to_enter=' ' 
    nnscore=0
    if(request.user.is_authenticated()):
        if request.method == 'POST':
            to_enter=str(request.user.username)
            
            answer=request.POST.get('answer')
            

            if(TestStart.objects.filter(answered_by=to_enter).exists()):
                nscore=0
            else:
                new_start=TestStart.objects.create(answered_by=to_enter)
                new_start.save()


            if(Question.objects.filter(answered_by=to_enter).filter(questionNumber=1).exists()):
                
                if(answer!=CorrectAnswers.objects.get(questionNumber=1).answer):
                    
                    question=Question.objects.get(answered_by=to_enter,questionNumber=1)
                    if(question.status==0):
                        nscore=question.score
                        question.score=nscore-10
                        #passed=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        question.status=0
                        question.answer=answer
                        question.save()
                    else:
                        nscore=question.score
                        question.score=nscore-10
                        #passed=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        question.status=1
                        
                        question.save()

                if(answer==CorrectAnswers.objects.get(questionNumber=1).answer):
                    question=Question.objects.get(answered_by=to_enter,questionNumber=1)
                    if(question.status==0):
                        diff=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        nscore=question.score
                        question.score=nscore+100
                        question.status=1
                        question.time_elapsed=diff.total_seconds()
                        question.answer=answer
                        question.save()
                    

            else:
                new_question=Question.objects.create(questionNumber=1,answered_by=to_enter,score=0)
                new_question.save()
                if(answer==CorrectAnswers.objects.get(questionNumber=1).answer):
                    diff=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                    nscore=100
                    question=Question.objects.get(answered_by=to_enter,questionNumber=1)
                    question.score=nscore
                    question.status=1
                    question.time_elapsed=diff.total_seconds()
                    question.answer=answer
                    question.save()

                else:
                    nscore=-10
                    question=Question.objects.get(answered_by=to_enter,questionNumber=1)
                    question.score=nscore
                    question.answer=answer
                    question.save()
        return render(request,'submit1.html')
    else:
        return HttpResponseRedirect('/login/')

def answer_submit2(request):
    #qno=0;
    #send=str(request.path)
    #send1=send[8:]
    #send2=int(send1)
    #to_enter=' ' 
    nnscore=0
    if(request.user.is_authenticated()):
        if request.method == 'POST':
            to_enter=str(request.user.username)
            
            answer=request.POST.get('answer')
            

            if(TestStart.objects.filter(answered_by=to_enter).exists()):
                nscore=0
            else:
                new_start=TestStart.objects.create(answered_by=to_enter)
                new_start.save()


            if(Question.objects.filter(answered_by=to_enter).filter(questionNumber=2).exists()):
                
                if(answer!=CorrectAnswers.objects.get(questionNumber=2).answer):
                    
                    question=Question.objects.get(answered_by=to_enter,questionNumber=2)
                    if(question.status==0):
                        nscore=question.score
                        question.score=nscore-10
                        #passed=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        question.status=0
                        question.answer=answer
                        question.save()
                    else:
                        nscore=question.score
                        question.score=nscore-10
                        #passed=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        question.status=1
                        
                        question.save()

                if(answer==CorrectAnswers.objects.get(questionNumber=2).answer):
                    question=Question.objects.get(answered_by=to_enter,questionNumber=2)
                    if(question.status==0):
                        diff=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        nscore=question.score
                        question.score=nscore+100
                        question.status=1
                        question.time_elapsed=diff.total_seconds()
                        question.answer=answer
                        question.save()
                    

            else:
                new_question=Question.objects.create(questionNumber=2,answered_by=to_enter,score=0)
                new_question.save()
                if(answer==CorrectAnswers.objects.get(questionNumber=2).answer):
                    diff=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                    nscore=100
                    question=Question.objects.get(answered_by=to_enter,questionNumber=2)
                    question.score=nscore
                    question.status=1
                    question.time_elapsed=diff.total_seconds()
                    question.answer=answer
                    question.save()

                else:
                    nscore=-10
                    question=Question.objects.get(answered_by=to_enter,questionNumber=2)
                    question.score=nscore
                    question.answer=answer
                    question.save()
        return render(request,'submit2.html')
    else:
        return HttpResponseRedirect('/login/')

def answer_submit3(request):
    #qno=0;
    #send=str(request.path)
    #send1=send[8:]
    #send2=int(send1)
    #to_enter=' ' 
    nnscore=0
    if(request.user.is_authenticated()):
        if request.method == 'POST':
            to_enter=str(request.user.username)
            
            answer=request.POST.get('answer')
            

            if(TestStart.objects.filter(answered_by=to_enter).exists()):
                nscore=0
            else:
                new_start=TestStart.objects.create(answered_by=to_enter)
                new_start.save()


            if(Question.objects.filter(answered_by=to_enter).filter(questionNumber=3).exists()):
                
                if(answer!=CorrectAnswers.objects.get(questionNumber=3).answer):
                    
                    question=Question.objects.get(answered_by=to_enter,questionNumber=3)
                    if(question.status==0):
                        nscore=question.score
                        question.score=nscore-10
                        #passed=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        question.status=0
                        question.answer=answer
                        question.save()
                    else:
                        nscore=question.score
                        question.score=nscore-10
                        #passed=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        question.status=1
                        
                        question.save()

                if(answer==CorrectAnswers.objects.get(questionNumber=3).answer):
                    question=Question.objects.get(answered_by=to_enter,questionNumber=3)
                    if(question.status==0):
                        diff=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        nscore=question.score
                        question.score=nscore+100
                        question.status=1
                        question.time_elapsed=diff.total_seconds()
                        question.answer=answer
                        question.save()
                    

            else:
                new_question=Question.objects.create(questionNumber=3,answered_by=to_enter,score=0)
                new_question.save()
                if(answer==CorrectAnswers.objects.get(questionNumber=3).answer):
                    diff=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                    nscore=100
                    question=Question.objects.get(answered_by=to_enter,questionNumber=3)
                    question.score=nscore
                    question.status=1
                    question.time_elapsed=diff.total_seconds()
                    question.answer=answer
                    question.save()

                else:
                    nscore=-10
                    question=Question.objects.get(answered_by=to_enter,questionNumber=3)
                    question.score=nscore
                    question.answer=answer
                    question.save()
        return render(request,'submit3.html')
    else:
        return HttpResponseRedirect('/login/')

def answer_submit4(request):
    #qno=0;
    #send=str(request.path)
    #send1=send[8:]
    #send2=int(send1)
    #to_enter=' ' 
    nnscore=0
    if(request.user.is_authenticated()):
        if request.method == 'POST':
            to_enter=str(request.user.username)
            
            answer=request.POST.get('answer')
            

            if(TestStart.objects.filter(answered_by=to_enter).exists()):
                nscore=0
            else:
                new_start=TestStart.objects.create(answered_by=to_enter)
                new_start.save()


            if(Question.objects.filter(answered_by=to_enter).filter(questionNumber=4).exists()):
                
                if(answer!=CorrectAnswers.objects.get(questionNumber=4).answer):
                    
                    question=Question.objects.get(answered_by=to_enter,questionNumber=4)
                    if(question.status==0):
                        nscore=question.score
                        question.score=nscore-10
                        #passed=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        question.status=0
                        question.answer=answer
                        question.save()
                    else:
                        nscore=question.score
                        question.score=nscore-10
                        #passed=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        question.status=1
                        
                        question.save()

                if(answer==CorrectAnswers.objects.get(questionNumber=4).answer):
                    question=Question.objects.get(answered_by=to_enter,questionNumber=4)
                    if(question.status==0):
                        diff=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        nscore=question.score
                        question.score=nscore+100
                        question.status=1
                        question.time_elapsed=diff.total_seconds()
                        question.answer=answer
                        question.save()
                    

            else:
                new_question=Question.objects.create(questionNumber=4,answered_by=to_enter,score=0)
                new_question.save()
                if(answer==CorrectAnswers.objects.get(questionNumber=4).answer):
                    diff=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                    nscore=100
                    question=Question.objects.get(answered_by=to_enter,questionNumber=4)
                    question.score=nscore
                    question.status=1
                    question.time_elapsed=diff.total_seconds()
                    question.answer=answer
                    question.save()

                else:
                    nscore=-10
                    question=Question.objects.get(answered_by=to_enter,questionNumber=4)
                    question.score=nscore
                    question.answer=answer
                    question.save()
        return render(request,'submit4.html')
    else:
        return HttpResponseRedirect('/login/')

def answer_submit5(request):
    #qno=0;
    #send=str(request.path)
    #send1=send[8:]
    #send2=int(send1)
    #to_enter=' ' 
    nnscore=0
    if(request.user.is_authenticated()):
        if request.method == 'POST':
            to_enter=str(request.user.username)
            
            answer=request.POST.get('answer')
            

            if(TestStart.objects.filter(answered_by=to_enter).exists()):
                nscore=0
            else:
                new_start=TestStart.objects.create(answered_by=to_enter)
                new_start.save()


            if(Question.objects.filter(answered_by=to_enter).filter(questionNumber=5).exists()):
                
                if(answer!=CorrectAnswers.objects.get(questionNumber=5).answer):
                    
                    question=Question.objects.get(answered_by=to_enter,questionNumber=5)
                    if(question.status==0):
                        nscore=question.score
                        question.score=nscore-10
                        #passed=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        question.status=0
                        question.answer=answer
                        question.save()
                    else:
                        nscore=question.score
                        question.score=nscore-10
                        #passed=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        question.status=1
                        
                        question.save()

                if(answer==CorrectAnswers.objects.get(questionNumber=5).answer):
                    question=Question.objects.get(answered_by=to_enter,questionNumber=5)
                    if(question.status==0):
                        diff=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        nscore=question.score
                        question.score=nscore+100
                        question.status=1
                        question.time_elapsed=diff.total_seconds()
                        question.answer=answer
                        question.save()
                    

            else:
                new_question=Question.objects.create(questionNumber=5,answered_by=to_enter,score=0)
                new_question.save()
                if(answer==CorrectAnswers.objects.get(questionNumber=5).answer):
                    diff=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                    nscore=100
                    question=Question.objects.get(answered_by=to_enter,questionNumber=5)
                    question.score=nscore
                    question.status=1
                    question.time_elapsed=diff.total_seconds()
                    question.answer=answer
                    question.save()

                else:
                    nscore=-10
                    question=Question.objects.get(answered_by=to_enter,questionNumber=5)
                    question.score=nscore
                    question.answer=answer
                    question.save()
        return render(request,'submit5.html')
    else:
        return HttpResponseRedirect('/login/')

def answer_submit6(request):
    #qno=0;
    #send=str(request.path)
    #send1=send[8:]
    #send2=int(send1)
    #to_enter=' ' 
    nnscore=0
    if(request.user.is_authenticated()):
        if request.method == 'POST':
            to_enter=str(request.user.username)
            
            answer=request.POST.get('answer')
            

            if(TestStart.objects.filter(answered_by=to_enter).exists()):
                nscore=0
            else:
                new_start=TestStart.objects.create(answered_by=to_enter)
                new_start.save()


            if(Question.objects.filter(answered_by=to_enter).filter(questionNumber=6).exists()):
                
                if(answer!=CorrectAnswers.objects.get(questionNumber=6).answer):
                    
                    question=Question.objects.get(answered_by=to_enter,questionNumber=6)
                    if(question.status==0):
                        nscore=question.score
                        question.score=nscore-10
                        #passed=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        question.status=0
                        question.answer=answer
                        question.save()
                    else:
                        nscore=question.score
                        question.score=nscore-10
                        #passed=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        question.status=1
                        
                        question.save()

                if(answer==CorrectAnswers.objects.get(questionNumber=6).answer):
                    question=Question.objects.get(answered_by=to_enter,questionNumber=6)
                    if(question.status==0):
                        diff=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        nscore=question.score
                        question.score=nscore+100
                        question.status=1
                        question.time_elapsed=diff.total_seconds()
                        question.answer=answer
                        question.save()
                    

            else:
                new_question=Question.objects.create(questionNumber=6,answered_by=to_enter)
                new_question.save()
                if(answer==CorrectAnswers.objects.get(questionNumber=6).answer):
                    diff=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                    nscore=100
                    question=Question.objects.get(answered_by=to_enter,questionNumber=6)
                    question.score=nscore
                    question.status=1
                    question.time_elapsed=diff.total_seconds()
                    question.answer=answer
                    question.save()

                else:
                    nscore=-10
                    question=Question.objects.get(answered_by=to_enter,questionNumber=6)
                    question.score=nscore
                    question.answer=answer
                    question.save()
        return render(request,'submit6.html')
    else:
        return HttpResponseRedirect('/login/')


def answer_submit7(request):
    #qno=0;
    #send=str(request.path)
    #send1=send[8:]
    #send2=int(send1)
    #to_enter=' ' 
    nnscore=0
    if(request.user.is_authenticated()):
        if request.method == 'POST':
            to_enter=str(request.user.username)
            
            answer=request.POST.get('answer')
            

            if(TestStart.objects.filter(answered_by=to_enter).exists()):
                nscore=0
            else:
                new_start=TestStart.objects.create(answered_by=to_enter)
                new_start.save()


            if(Question.objects.filter(answered_by=to_enter).filter(questionNumber=7).exists()):
                
                if(answer!=CorrectAnswers.objects.get(questionNumber=7).answer):
                    
                    question=Question.objects.get(answered_by=to_enter,questionNumber=7)
                    if(question.status==0):
                        nscore=question.score
                        question.score=nscore-10
                        #passed=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        question.status=0
                        question.answer=answer
                        question.save()
                    else:
                        nscore=question.score
                        question.score=nscore-10
                        #passed=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        question.status=1
                        
                        question.save()

                if(answer==CorrectAnswers.objects.get(questionNumber=7).answer):
                    question=Question.objects.get(answered_by=to_enter,questionNumber=7)
                    if(question.status==0):
                        diff=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        nscore=question.score
                        question.score=nscore+100
                        question.status=1
                        question.time_elapsed=diff.total_seconds()
                        question.answer=answer
                        question.save()
                    

            else:
                new_question=Question.objects.create(questionNumber=7,answered_by=to_enter)
                new_question.save()
                if(answer==CorrectAnswers.objects.get(questionNumber=7).answer):
                    diff=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                    nscore=100
                    question=Question.objects.get(answered_by=to_enter,questionNumber=7)
                    question.score=nscore
                    question.status=1
                    question.time_elapsed=diff.total_seconds()
                    question.answer=answer
                    question.save()

                else:
                    nscore=-10
                    question=Question.objects.get(answered_by=to_enter,questionNumber=7)
                    question.score=nscore
                    question.answer=answer
                    question.save()
        return render(request,'submit7.html')
    else:
        return HttpResponseRedirect('/login/')

def answer_submit8(request):
    #qno=0;
    #send=str(request.path)
    #send1=send[8:]
    #send2=int(send1)
    #to_enter=' ' 
    nnscore=0
    if(request.user.is_authenticated()):
        if request.method == 'POST':
            to_enter=str(request.user.username)
            
            answer=request.POST.get('answer')
            

            if(TestStart.objects.filter(answered_by=to_enter).exists()):
                nscore=0
            else:
                new_start=TestStart.objects.create(answered_by=to_enter)
                new_start.save()


            if(Question.objects.filter(answered_by=to_enter).filter(questionNumber=8).exists()):
                
                if(answer!=CorrectAnswers.objects.get(questionNumber=8).answer):
                    
                    question=Question.objects.get(answered_by=to_enter,questionNumber=8)
                    if(question.status==0):
                        nscore=question.score
                        question.score=nscore-10
                        #passed=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        question.status=0
                        question.answer=answer
                        question.save()
                    else:
                        nscore=question.score
                        question.score=nscore-10
                        #passed=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        question.status=1
                        
                        question.save()

                if(answer==CorrectAnswers.objects.get(questionNumber=8).answer):
                    question=Question.objects.get(answered_by=to_enter,questionNumber=8)
                    if(question.status==0):
                        diff=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        nscore=question.score
                        question.score=nscore+100
                        question.status=1
                        question.time_elapsed=diff.total_seconds()
                        question.answer=answer
                        question.save()
                    

            else:
                new_question=Question.objects.create(questionNumber=8,answered_by=to_enter)
                new_question.save()
                if(answer==CorrectAnswers.objects.get(questionNumber=8).answer):
                    diff=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                    nscore=100
                    question=Question.objects.get(answered_by=to_enter,questionNumber=8)
                    question.score=nscore
                    question.status=1
                    question.time_elapsed=diff.total_seconds()
                    question.answer=answer
                    question.save()

                else:
                    nscore=-10
                    question=Question.objects.get(answered_by=to_enter,questionNumber=8)
                    question.score=nscore
                    question.answer=answer
                    question.save()
        return render(request,'submit8.html')
    else:
        return HttpResponseRedirect('/login/')

def answer_submit9(request):
    #qno=0;
    #send=str(request.path)
    #send1=send[8:]
    #send2=int(send1)
    #to_enter=' ' 
    nnscore=0
    if(request.user.is_authenticated()):
        if request.method == 'POST':
            to_enter=str(request.user.username)
            
            answer=request.POST.get('answer')
            

            if(TestStart.objects.filter(answered_by=to_enter).exists()):
                nscore=0
            else:
                new_start=TestStart.objects.create(answered_by=to_enter)
                new_start.save()


            if(Question.objects.filter(answered_by=to_enter).filter(questionNumber=9).exists()):
                
                if(answer!=CorrectAnswers.objects.get(questionNumber=9).answer):
                    
                    question=Question.objects.get(answered_by=to_enter,questionNumber=9)
                    if(question.status==0):
                        nscore=question.score
                        question.score=nscore-10
                        #passed=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        question.status=0
                        question.answer=answer
                        question.save()
                    else:
                        nscore=question.score
                        question.score=nscore-10
                        #passed=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        question.status=1
                        
                        question.save()

                if(answer==CorrectAnswers.objects.get(questionNumber=9).answer):
                    question=Question.objects.get(answered_by=to_enter,questionNumber=9)
                    if(question.status==0):
                        diff=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                        nscore=question.score
                        question.score=nscore+100
                        question.status=1
                        question.time_elapsed=diff.total_seconds()
                        question.answer=answer
                        question.save()
                    

            else:
                new_question=Question.objects.create(questionNumber=9,answered_by=to_enter)
                new_question.save()
                if(answer==CorrectAnswers.objects.get(questionNumber=9).answer):
                    diff=TestStart.objects.get(answered_by=to_enter).time_started-timezone.now()
                    nscore=100
                    question=Question.objects.get(answered_by=to_enter,questionNumber=9)
                    question.score=nscore
                    question.status=1
                    question.time_elapsed=diff.total_seconds()
                    question.answer=answer
                    question.save()

                else:
                    nscore=-10
                    question=Question.objects.get(answered_by=to_enter,questionNumber=9)
                    question.score=nscore
                    question.answer=answer
                    question.save()
        return render(request,'submit9.html')
    else:
        return HttpResponseRedirect('/login/')



def score(request):
    all_users=User.objects.all()
    new_user=[]
    new_value=[]
    new_list=[]
    ctr=0
    tot=0
    for i in all_users:
        all_questions=Question.objects.filter(answered_by=i.username)
        new_user.append(i.username)
        
        for j in all_questions:
            tot=tot+j.score+(j.time_elapsed)/60
        new_value.append(tot)
        tot=0
        new_list.append(ctr)
        ctr=ctr+1
    new_dict=dict(zip(new_user,new_value))
    dicti={}
    sorted_x = sorted(new_dict.items(), key=operator.itemgetter(1),reverse=True)
    return render(request,'score.html',{'new_dict':sorted_x})

def home(request):
    if(request.user.is_authenticated()):
        return render(request,'home.html',{})
    else:
        return HttpResponseRedirect('/login/')




        


    