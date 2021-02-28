from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from datetime import datetime

class Index(TemplateView):
    template_name = "practice/index2.html"

index = Index.as_view()

class exercise_class(TemplateView):
    template_name = "practice/exercise.html"
    def get(self, request, **kwargs):
        now = datetime.now()
        context = {
            "text": "TEST_EXERCISE_CLASS",
            "time": now,
        }
        return self.render_to_response(context)

def index_template(request):
    return render(request, "practice/index.html")

def exercise(request):
    if request.method == "GET":
        now = datetime.now()
        context = {
            "text": "TEST_EXERCISE",
            "time": now,
        }
        return render(request, "practice/exercise.html", context)

