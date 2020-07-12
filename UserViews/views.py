import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from InterviewPanel.models import Quiz, Answers, Questions
# Create your views here.
from . import UserViewsForms
from .models import Application, grades, canAccess


@login_required
def UserHome(request):
    return render(request, 'UserViews/Userindex.html')


def testing(request):
    if request.method == 'POST':
        form1 = UserViewsForms.Uapplication(request.POST, request.FILES)

        if form1.is_valid():
            x = form1.save(commit=False)
            x.user = request.user
            x.save()
            messages.success(request, 'Your password was updated successfully!', extra_tags="Success")
            return redirect('../')
    else:
        form1 = UserViewsForms.Uapplication()
    return render(request, 'UserViews/testing.html', {'vv': form1})


@login_required
# @permission_required(,login_url='accounts/login' , raise_exception=False)
def application(request):
    if request.method == 'POST':
        form1 = UserViewsForms.applicationForm(request.POST)
        if form1.is_valid():
            form1.save()
            redirect('../..')
        else:
            messages.error(request, "Error")

    else:
        form1 = UserViewsForms.applicationForm()

        context = {
            'abc': form1,
        }
        return render(request, "UserViews/application.html", context)


def detailView(request):
    obj = Application.objects.all()
    context = {
        'object': obj
    }
    return render(request, "UserViews/Detailview.html", context)
    # def get_object(self, **kwargs):
    #     pk_ = self.kwargs.get("pk")
    #     return get_object_or_404(Application, pk=pk_)


def detailView2(request, user):
    object1 = Application.objects.all()
    flag = 0
    for obj1 in object1:
        if request.user == obj1.user:
            context = {
                'obj': obj1

            }
            return render(request, "UserViews/DetailView2.html", context)
        else:
            flag = flag + 1
    if flag != 0:
        messages.error(request, "Please fill the application", extra_tags="danger")
        print(flag)
    return render(request, "UserViews/DetailView2.html", )


def test(request):
    if request.method == "POST":
        z = UserViewsForms.testform(request.POST)
        if z.is_valid():
            x = z.save(commit=False)
            x.user = request.user
            x.save()
            return redirect('../../')
    else:
        z = UserViewsForms.testform()

    return render(request, "UserViews/test.html", {'form': z})


def Application_update_view(request, id=id):
    obj = get_object_or_404(Application, id=id)
    form = UserViewsForms.Uapplication(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, "Updated successFully!!", extra_tags="success")

    return render(request, "UserViews/test.html", {'form1': form})  # else:
    #     messages.error(request, "Your Application Is Not There.....May be you deleted it", extra_tags="danger")
    #     return render(request, "UserViews/test.html")
    # return redirect('../../')


def Application_Delete_view(request, id):
    obj = get_object_or_404(Application, id=id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Deleted SuccessFully!!", extra_tags="success")
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "UserViews/DeletionView.html", context)


@login_required
def QuizPortal(request):
    global context
    if request.user.is_authenticated and request.user.has_perm('InterviewPanel.change_quiz'):
        print(request.user)
        access = canAccess.objects.get(user=request.user)
        quiz = get_object_or_404(Quiz, url=access.QuizName)
        if quiz.title == access.QuizName:
            context = {
                'quiz': quiz
            }
    else:
        # messages.error(request,
        #                "Permission Denied!! may be you have Already Attempted This Quiz..Check Your Grades Or contact your Admin",
        #                extra_tags='')
        context = {
            'quiz': '1'
        }
    return render(request, "UserViews/question_Solving.html", context)


def GetQuestions(request, slug):
    global context
    quiz = get_object_or_404(Quiz, url=slug)

    if request.user.is_authenticated and request.user.has_perm(
            'InterviewPanel.change_quiz'):
        access = canAccess.objects.get(user=request.user)
        if quiz.title == access.QuizName:
            question = Quiz.objects.get(url=slug).questions_set.all()
            question1 = list(question.values('id', 'question'))
            answerlist = list(Answers.objects.filter(question__in=question).values('id', 'question_id', 'answer'))
            length = len(question1)
            a = json.dumps(question1)
            b = json.dumps(answerlist)
            c = json.dumps(slug)

            # d = json.dumps(quiz)
            # o = slice(1)
            # form = questions(question=question)
            # print(form,question)
            context = {
                'quest': a, 'answer': b, 'len': c,
            }
    else:
        messages.error(request, "Permission Denied!!", extra_tags='danger')

    return render(request, "UserViews/question.html", context)


@csrf_protect
def MarkQuiz(request):
    global list_Of_Answers_User, i, j
    if request.is_ajax() and request.method == 'POST':
        i = 0
        j = 0
        list_Of_Answers_User = []
        solution = json.loads(request.body)
        quiz_settings = list(Quiz.objects.filter(url=solution[0]['quiz']).values())
        total = Quiz.objects.get(url=solution[0]['quiz']).questions_set.all().count()
        grades_calulation = grades()
        grades_calulation.user = request.user
        grades_calulation.name = User.objects.get(username=request.user)
        grades_calulation.quiz = get_object_or_404(Quiz, url=solution[0]['quiz'])
        q = get_object_or_404(Quiz, url=solution[0]['quiz'])
        grades_calulation.category = q.category
        Ans = Answers()
        for x in solution:
            question_id = solution[i]['question_id']
            user_answer = solution[i]['answer']
            status = Ans.check_correct(user_answer, question_id)
            if status:
                j = j + 1
            actual_correct = Ans.get_correct_answer(question_id)
            question = list(Questions.objects.filter(id=question_id).values())
            list_Of_Answers_User.append(
                {'question': question, 'UserAnswer': user_answer, 'status': status, 'correct_is': actual_correct})
            i = i + 1
        grades_calulation.total_marks = total
        grades_calulation.obtained_marks = j
        grades_calulation.percentage = (j / total) * 100
        try:
            grades_calulation.save()
            permission = Permission.objects.get(codename='change_quiz')
            user1 = User.objects.get(username=request.user)
            user1.user_permissions.remove(permission)
            access = canAccess.objects.get(user=request.user).delete()
            data = list_Of_Answers_User, quiz_settings
            return JsonResponse(data, safe=False, status=200)
        except IntegrityError as e:
            print("except block")
            print(e.args)
            data = {'message': 'Already Attempted This Quiz'}
            return JsonResponse(data, status=500)
    else:
        print("error in this")
    return render(request, "UserViews/question.html")


def GradePortal(request):
    category = list(User.objects.get(username=request.user).grades_set.all().values('category'))

    context = {
        "category": category
    }
    return render(request, "UserViews/Categories.html", context)


def GradeShow(request, slug):
    grade = list(grades.objects.filter(category=slug).values())
    print(grade)
    context = {
        'grades': grade,
        'length': len(grade)
    }
    return render(request, "UserViews/Grades.html", context)
