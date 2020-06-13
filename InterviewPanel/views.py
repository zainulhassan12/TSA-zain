import json

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView

from .Forms import QuizForm, answers, questions, Add_Questions_to_Quiz
# Create your views here.
from .models import Questions, Answers, Quiz


@staff_member_required
def interhome(request):
    return render(request, "home.html", )


@staff_member_required
def QuizView(request):
    if request.method == 'POST':
        form1 = QuizForm(request.POST)
        if form1.is_valid():
            abc = form1.save(commit=False)
            abc.save()
            messages.success(request, "Quiz Added!!", extra_tags="success")
            # print(abc)
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


class QuizListView(ListView):
    model = Quiz
    template_name = "quiz_list.html"

    # @login_required
    def get_queryset(self):
        queryset = super(QuizListView, self).get_queryset()
        return queryset


class QuizDetails(DetailView):
    model = Quiz

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    # global z
    # x = []
    # Quiz1 = Quiz.objects.all().values()
    # q = Quiz.objects.get(id__in=Quiz1).questions_set.all().values()
    # for qu in q:
    #     z = (Questions.objects.get(id__exact=qu['id']).answers_set.all().values())
    #     x.append(z)
    #
    # print(Quiz1,'\n\n', q,'\n\n', x,'\n\n')

    # context = {
    #     'Quiz': Quiz1
    # }
    # return render(request, 'testingquiz.html')


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
        # print(question)

        return redirect('../../')
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


@staff_member_required
def Questions_Detail_view(request):
    #  Questions Details views
    global ques, ans, z, xx, lis, context, quest
    obj = Questions.objects.all()
    lis = []

    for x in obj.iterator():
        quest = x
        ans = Answers.objects.filter(question=x)
        xx = list((ans.values('answer', 'is_correct', 'question_id')))
        lis.append(quest)
        z = 0
        for v in xx:
            q = xx[z]
            lis.append(q)
            # print(lis)
            z += 1

    return render(request, "home.html", {'ans': lis})


@staff_member_required
def Add_Questions(request):
    if request.method == 'POST':
        form = Add_Questions_to_Quiz(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            form.save_m2m()
            # data.question.add(bc)
            messages.success(request, "Quiz Added Successfully!!!", extra_tags="success")
            return redirect('../')

    else:
        form = Add_Questions_to_Quiz()
    context1 = {
        'add': form,
    }
    return render(request, 'QuizAdding.html', context1)


@csrf_exempt
@staff_member_required
def GetQuizData(request):  # ajax validation
    global quizlist, quiz
    if request.is_ajax():
        data = json.loads(request.body)
        id_ = data['quiz']
        quiz = Quiz.objects.filter(id=id_)
    if quiz is not None:
        quizlist = list(quiz.values())
    return JsonResponse(quizlist, safe=False)
