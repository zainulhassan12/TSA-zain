# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem

from ...InterviewPannel.models import quizdata
from TeacherSelection.UserViews.models import Application


class QuizItem(DjangoItem):
    # define the fields for your item here like:
    django_model = quizdata
