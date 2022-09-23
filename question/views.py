from django.shortcuts import render,redirect
from .models import *
# Create your views here.

name = []
def index(request):
    if request.method == 'POST':
        name.append(request.POST['name'])
        return redirect('first')
    return render(request, 'question/login.html')



def firstQuestion(request):
    questions = Question.objects.all()[0]


    if request.method == 'POST':
        try:
            selected_choice = questions.choice_set.get(pk=request.POST['question'])
        except:
            # return HttpResponseRedirect(reverse('index'))
            return render(request, 'question/survey.html', {"error_message":"You did not choose an option"})
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return redirect('second')
    context = {'questions': questions}
    return render(request, 'question/index2.html', context)

def secondQuestion(request):
    questions = Question.objects.all()[1]
    context = {'questions':questions}
    if request.method == 'POST':
        try:
            selected_choice = questions.choice_set.get(pk=request.POST['question'])
        except:
            return render(request, 'question/questions.html', {"error_message":"You did not choose an option"})
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return redirect('third')
    return render(request, 'question/index2.html', context)



def thirdQuestion(request):
    questions = Question.objects.all()[2]
    context = {'questions':questions}
    if request.method == 'POST':
        try:
            selected_choice = questions.choice_set.get(pk=request.POST['question'])
        except:
            return render(request, 'question/questions.html', {"error_message":"You did not choose an option"})
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return redirect('fourth')
    return render(request, 'question/index2.html', context)


def fourthQuestion(request):
    questions = Question.objects.all()[3]
    context = {'questions':questions}
    if request.method == 'POST':
        try:
            selected_choice = questions.choice_set.get(pk=request.POST['question'])
        except:
            return render(request, 'question/questions.html', {"error_message":"You did not choose an option"})
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return redirect('fifth')
    return render(request, 'question/index2.html', context)


def fifthQuestion(request):
    questions = Question.objects.all()[4]

    if request.method == 'POST':
        Choice.objects.create(
            question = questions,
            choice_text = request.POST['choice']
        )
        return redirect('done')

    context = {'questions': questions}
    return render(request, 'question/index5.html',context)



def Done(request):
    try:
        user = len(name)
        fullname = name[user -1]
    except:
        fullname = ' '
    context = {'name':fullname}
    return render(request, 'question/done.html',context)


def Votes(request):
    questions = Question.objects.all()

    context = {'questions': questions}
    return render(request, 'question/review.html',context)
