import json

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .Forms import QuizForm, answers, questions


# Create your views here.
@staff_member_required
def interhome(request):
    return render(request, "index1.html")


@staff_member_required
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
@staff_member_required
def ans(request):
    global i
    if request.is_ajax() and request.method == 'POST':


        question = request.POST.get('Question')
        option = request.POST.getlist('Options[]')
        # obj = json.loads(request.POST.get(''))
        obj1 = json.loads(request.body)
        question = obj1['Question']
        options = obj1['Options']
        i = 0
        for x in options:
            op = options[i]
            opt = op['Option']
            IsTrue = op['IsTrue']
            # print(op)
            print(opt)
            print(IsTrue)
            i = i+1
        # print(options)

        print(question)

        # print(obj)

    # print(request.__dict__)
    # options = {'Options': request.POST.getlist('Options[]')}
    # print(options)
    # options1 = request.__dict__
    # print(request.__dict__)
    # print(request.__list__)
    # form.Question = question
    # form.save()
    # data = json.loads(request.POST.get('Data', ''))
    # print(data)
    # print(options1)
    # print(question)
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

@staff_member_required
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
