from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json

from .Forms import QuizForm, answers, questions
# Create your views here.
@staff_member_required
stafff jlsjdjsjd
sdkfhksdjhkfhsdk
sjhkshdfhsk
kjsdghfjksh
def interhome(request):
    return render(request, "index1.html")


def QuizView(request):
    if request.method == 'POST':
        form1 = QuizForm(request.POST)
        if form1.is_valid():
            abc = form1.save(commit=False)
            abc.save()

            return redirect('../')
    else:
        form1 = QuizForm()
    context = {
        'form': form1
    }
    return render(request, "index.html", context)

@csrf_exempt
def ans(request):
    if request.is_ajax() and request.method == 'POST':
        form = questions()

        question = request.POST.get('Question')
        option = request.POST.getlist('Options[]')

        # print(request.__dict__)
        options = {'Options': request.json['Options']}
        print(options)
        # options1 = request.__dict__
        # print(request.__dict__)
        # print(request.__list__)
        # form.Question = question
        # form.save()
        # data = json.loads(request.POST.get('Data', ''))
        # print(data)
        # print(options1)
        print(question)
        return HttpResponse("success njkhhkh")
    return render(request, "MasterDetail.html")




    # form = answers(request.POST or None)
    # if form.is_valid():
    #
    #     for answer in form:
    #         form.answer = form.cleaned_data('answer')
    #         form.is_correct = form.cleaned_data('is_correct')
    #         print(answer)
    #         print(form)
    #     form.save()


def QuestionAdd(request):
    if request.method == 'POST':
        form1 = questions(request.POST)
        form = answers(request.POST)
        if form1.is_valid():
            dd = form1.save(commit=False)
            dd.save()
            print(dd)
            messages.success(request, "Question Added", extra_tags="success")
            return redirect('../')
        if form.is_valid():
            x = form.save(commit=False)
            x.question = form1.question
            x.save()
    else:
        form1 = questions()
        form = answers()
    context = {
        'form1': form1,
        'form2': form
    }
    return render(request, "index.html", context)
