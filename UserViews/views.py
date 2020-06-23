from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from InterviewPanel.models import Quiz, Answers
# Create your views here.
from . import UserViewsForms
from .models import Application


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


def QuizManager(request):
    context = {
        'Quiz': 'No Quiz'
    }
    return render(request, "UserViews/question_Solving.html", context)


def QuizPortal(request, slug):
    quiz = get_object_or_404(Quiz, url=slug)
    if quiz is not None:
        context = {
            'quiz': quiz
        }
    return render(request, "UserViews/question_Solving.html", context)


def GetQuestions(request, slug):
    question = Quiz.objects.get(url=slug).questions_set.all()
    answerlist = list(Answers.objects.filter(question__in=question).values('question_id','answer'))

    # o = slice(1)
    # form = questions(question=question)
    # print(form,question)
    context = {
        'quest': question, 'answer': answerlist,
    }
    return render(request, "UserViews/question.html", context)
