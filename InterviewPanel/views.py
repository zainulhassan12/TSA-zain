import json

import pandas as pd
import numpy as np
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from UserViews.models import canAccess, Application
from .Forms import QuizForm, AddingNewQuestions, InterviewForm, InterQuestion
# Create your views here.
from .models import Answers, Quiz, Questions, InterviewQuestions


# import seaborn as sns;sns.set()
# import matplotlib.pyplot as plt

# import seaborn as sns;sns.set()
# import matplotlib.pyplot as plt


@staff_member_required
def InterviewHome(request):
    return render(request, "home.html", )


@staff_member_required
def QuizAddingView(request):
    if request.method == 'POST':
        form1 = QuizForm(request.POST)
        if form1.is_valid():
            abc = form1.save(commit=False)
            abc.save()
            messages.success(request, "Quiz Added!!", extra_tags="success")
            return redirect('../')
        else:
            print(form1.errors)

    else:
        form1 = QuizForm()
    context = {
        'form': form1
    }
    return render(request, "QuizCreation.html", context)


class QuizListView(ListView):
    model = Quiz
    template_name = "quiz_list.html"

    # @login_required
    def get_queryset(self):
        queryset = super(QuizListView, self).get_queryset()
        return queryset


class QuizDetailView(DetailView):
    model = Quiz
    slug_field = 'url'
    template_name = "quiz_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


@csrf_exempt
@staff_member_required
def QuestionAndAnswers(request):
    global i, h, form
    if request.is_ajax() and request.method == 'POST':
        obj1 = json.loads(request.body)
        questiondata = obj1['Question']

        question = questiondata[0]['Question']
        explanation = questiondata[0]['Explanation']
        abc = Questions(question=question, explanation=explanation)
        abc.save()
        id_ = get_object_or_404(Questions, question=question)
        options = obj1['Options']
        i = 0
        for x in options:
            op = options[i]
            opt = op['Option']
            IsTrue = op['IsTrue']
            answer = Answers(answer=opt, is_correct=check_true(IsTrue),
                             question=id_)
            answer.save()
            i = i + 1
        x = {
            'data': '1'
        }
        return JsonResponse(x)
    else:
        form = AddingNewQuestions()
    context = {
        'form': form
    }
    return render(request, "MasterDetailQuiz_Questions.html", context)


def check_true(IsTrue):
    if IsTrue == "true":
        return True
    else:
        return False


#

@staff_member_required
def StartQuiz(request, slug):
    users = User.objects.all()
    access = canAccess()
    permission = Permission.objects.get(codename='change_quiz')
    print(permission)
    for user in users:
        if user.is_active and not user.is_staff:
            if not user.has_perm('InterviewPanel.change_quiz'):
                user.user_permissions.add(permission)
                access.user = user
                access.QuizName = slug
                try:
                    access.save()
                except IntegrityError as e:
                    # print(e)
                    messages.success(request, "Alredy Granted Access To Users!! to Quiz:>>" + slug, extra_tags="danger")
            else:
                if canAccess.objects.filter(user=user):
                    ob = canAccess.objects.get(user=user)
                    if ob.QuizName != slug:
                        canAccess.objects.filter(user=user).update(QuizName=slug)
                else:
                    messages.error(request, "User is not there!!!!!", )

    # print(user.has_perm('InterviewPanel.change_quiz'))

    context = {
        'users': users
    }
    return render(request, 'QuizSiting.html', context)


def InterViewConducting(request):
    all_users = list(User.objects.all().values())
    context = {
        'All': all_users
    }
    return render(request, "Interview.html", context)


def GetDetailsForInterview(request, slug):
    grades = User.objects.get(username=slug).grades_set.all().values()
    all_users = list(User.objects.all().values())
    if grades:
        context = {
            'All': all_users,
            'gra': grades
        }
    else:
        context = {
            'All': all_users,
            'gra': '0'
        }
        messages.error(request, "No Grades For This User Means Not Attempted any Quiz!!", extra_tags="danger")

    return render(request, "Interview.html", context)


def GetApplicationForInterview(request, slug):
    application = list(Application.objects.filter(user=slug).all().values())
    context = {
        'app': application,
    }
    return render(request, "ApplicationInterviewpannel.html", context)


def StartInterview(request, slug):
    questions_set = list(InterviewQuestions.objects.all().values())
    if request.method == 'POST':
        form1 = InterviewForm(request.POST)
        if form1.is_valid():
            print("hsdjasgh")
            s = form1.save(commit=False)
            s.user = User.objects.get(username=slug)
            s.total_marks_for_interview = (s.Personality + s.Dressing_Sense + s.Communication_Skills +
                                           s.InterView_Questions) / 40 * 10
            s.save()
            print(s.total_marks_for_interview)
            messages.success(request, "Interview Results are Saved")
            return redirect('/inter/interview/')
        else:
            print(form1.errors)

    else:
        form1 = InterviewForm()
    context = {
        'InterviewForm': form1,
        'Questions': questions_set,
        'name': slug
    }
    return render(request, "StartInterview.html", context)


def SaveInterviewQuestions(request):
    if request.method == 'POST':
        form = InterQuestion(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully!!", extra_tags="success")
    else:
        form = InterQuestion()
    context = {
        "InterviewQuestions": form
    }
    return render(request, "QuestionForInterview.html", context)


def InterviewQuestionDetailView(request):
    model = list(InterviewQuestions.objects.all().values())
    if model:
        context = {
            'question': model
        }
        return render(request, "InterQuestionDetail.html", context)
    else:
        context = {
            'question': 0
        }
        return render(request, "InterQuestionDetail.html", context)


def RecommenderSystem(request):
    # loading the dataset
    pf = (pd.read_csv("C:/Users/zain ul hassan/Desktop/DataSetForFYPfinal.csv"))
    df = pd.DataFrame(pf.iloc[1:250, :(23)])  # selecting 250 rows and 23 columns from the csv file
    print(df)
    # -----------------------

    '''
    This portion of the code encodes the dataset and we construct training and testing colummns

    '''
    le = LabelEncoder()  # creating a object for encoding
    # in ML we cant classify english sentences hence we need to turn them into some numeric representation for the computer to understand
    X = df.drop('Column22', axis='columns')
    Y = df['Column22']
    X = X.apply(LabelEncoder().fit_transform)

    print(X)
    print(Y)  # without encoding
    Y = le.fit_transform(Y)
    print(Y)  # with encoding

    '''
    ---------------------------------------------------------------------------------
    '''

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.40)
    # dividing the dataset so that 60 percent is training data and 40 percent in testing data

    # for logistic regression
    # -------------------------
    logreg = LogisticRegression(C=1e5)  # model object created
    logreg.fit(X, Y)  # model learns
    y_predic_check = logreg.predict(X_test)  # model tested on training set
    # -------------------------
    # logistic regression end

    # for naivebyes(another different algorithm) with worse accuracy and f1 scores
    # --------------------------

    '''
    classifier=GaussianNB()
    classifier.fit(X_train,Y_train)

    y_predic_check=classifier.predict(X_test)
    '''
    # ----------------
    # naive_byes_end

    # inverse transform inverses encoding and shows it in a more understandable way
    print("Predicted Lables : ", le.inverse_transform((y_predic_check)))
    print("Actual Labels :    ", le.inverse_transform(list(Y_test)))

    # used to identify indivisual training examples or new examples
    # assume you have to identify a new teacher
    # You will have to encode the teachers data as encoded above
    pre = logreg.predict(X_train[:1])
    print(list(le.inverse_transform(pre)))
    # ---------------------------------------

    # used for performance evaluation and visual representation of the model
    conf_mat = confusion_matrix(y_predic_check, Y_test)
    names = np.unique(y_predic_check)
    # sns.heatmap(conf_mat, square=True, annot=True, cbar=False, xticklabels=names, yticklabels=names)
    # plt.xlabel('Truth')
    # plt.ylabel('Prediction')
    # b, t = plt.ylim()  # discover the values for bottom and top
    # b += 0.5  # Add 0.5 to the bottom
    # t -= 0.5  # Subtract 0.5 from the top
    # plt.ylim(b, t)  # update the ylim(bottom, top) values
    # plt.show()

    print("Classification Report : ")
    print(classification_report(Y_test, y_predic_check))







# @csrf_exempt
# @staff_member_required
# def GetQuizData(request):  # ajax validation
#     global quizlist, quiz
#     if request.is_ajax():
#         data = json.loads(request.body)
#         id_ = data['quiz']
#         quiz = Quiz.objects.filter(id=id_)
#     if quiz is not None:
#         quizlist = list(quiz.values())
#     return JsonResponse(quizlist, safe=False)

# @staff_member_required
# def Add_Questions(request):
#     if request.method == 'POST':
#         form = Add_Questions_to_Quiz(request.POST)
#         if form.is_valid():
#             data = form.save(commit=False)
#             data.save()
#             form.save_m2m()
#             # data.question.add(bc)
#             messages.error(request, "Quiz Added Successfully!!!", extra_tags="success")
#             return redirect('../')
#
#     else:
#         form = Add_Questions_to_Quiz()
#     context1 = {
#         'add': form,
#     }
#     return render(request, 'QuizAdding.html', context1)


# def QuestionAdd(request):
#     if request.method == 'POST':
#         form1 = questions(request.POST)
#         form = answers(request.POST)
#         if form1.is_valid():
#             dd = form1.save(commit=False)
#             dd.save()
#             print(dd)
#             messages.success(request, "Question Added", extra_tags="success")
#             return redirect('../')
#         if form.is_valid():
#             x = form.save(commit=False)
#             x.question = form1.question
#             x.save()
#     else:
#         form1 = questions()
#         form = answers()
#     context = {
#         'form1': form1,
#         'form2': form
#     }
#     return render(request, "QuizCreation.html", context)
# def Questions_Detail_view(request):
# #     #  Questions Details views
# #     global ques, QuestionAndAnswers, z, xx, lis, context, quest
# #     obj = Questions.objects.all()
# #     lis = []
# # 
# #     for x in obj.iterator():
# #         quest = x
# #         QuestionAndAnswers = Answers.objects.filter(question=x)
# #         xx = list((QuestionAndAnswers.values('answer', 'is_correct', 'question_id')))
# #         lis.append(quest)
# #         z = 0
# #         for v in xx:
# #             q = xx[z]
# #             lis.append(q)
# #             # print(lis)
# #             z += 1
# # 
# #     return render(request, "home.html", {'ans': lis})
# global z
#     # x = []
#     # Quiz1 = Quiz.objects.all().values()
#     # q = Quiz.objects.get(id__in=Quiz1).questions_set.all().values()
#     # for qu in q:
#     #     z = (Questions.objects.get(id__exact=qu['id']).answers_set.all().values())
#     #     x.append(z)
#     #
#     # print(Quiz1,'\n\n', q,'\n\n', x,'\n\n')
#
#     # context = {
#     #     'Quiz': Quiz1
#     # }
#     # return render(request, 'testingquiz.html')
