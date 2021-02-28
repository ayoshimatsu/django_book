import logging
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import InquiryForm

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "diary/index.html"  # mysite/templates/diary/

class InquiryView(generic.FormView):
    """
    Inquiry box.
    """
    template_name = "diary/inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy("diary:inquiry")

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, "Message was sent.")
        logger.info("Inquiry sent by {}".format(form.cleaned_data["name"]))
        return super().form_valid(form)

