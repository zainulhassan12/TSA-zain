import json

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .Forms import QuizForm, answers, questions
# Create your views here.
from .models import Questions, Answers


@staff_member_required
def interhome(request):
    return render(request, "index1.html", )


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


def check_true(IsTrue):
    if IsTrue == "true":
        return True
    else:
        return False


@csrf_exempt
@staff_member_required
def ans(request):
    global i
    if request.is_ajax() and request.method == 'POST':

        obj1 = json.loads(request.body)
        question = obj1['Question']
        question = Questions(question=question)
        question.save()
        obj = get_object_or_404(Questions, question=question)
        print(obj)
        options = obj1['Options']
        i = 0
        for x in options:
            op = options[i]
            opt = op['Option']
            IsTrue = op['IsTrue']
            print(IsTrue)
            answer = Answers(answer=opt, is_correct=check_true(IsTrue), question=obj)
            answer.save()
            # # print(op)
            print("option  " + opt)
            i = i + 1
        # print(options)
        print(question)

        return HttpResponse("{'result':Question added}")
    return render(request, "MasterDetail.html")


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


def Questions_Detail_view(request):
    #  Questions Details views
    global ques, ans, z, xx, lis, context, quest
    obj = Questions.objects.all()
    lis = []
    for x in obj.iterator():
        quest = x
        ans = Answers.objects.filter(question=x)
        xx = (ans.values('answer', 'is_correct', 'question_id'))
        lis.append((quest, xx))

    return render(request, "index1.html", {'ans': lis})

    # print(x)
    # print(xx)
    # print(xxx)

    # z = 0
    # for x in obj.iterator():
    #     ques = obj[z]
    #     print(ques)
    #     print(ques.id)
    #     id_ = obj[z].id
    #     z = z + 1
    #
    #     for c in ans:
    #         ans = get_object_or_404(Answers, question=id_)
    #         print(ans.id)
    #         print(ans)
