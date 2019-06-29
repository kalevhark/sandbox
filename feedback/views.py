from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, CreateView

from .models import Feedback

class  FeedbackForm(forms.ModelForm):
    class  Meta:
        model = Feedback
        fields =  '__all__'

class  FeedbackList(View):
    def  get(self, request):
        feedbacks =  list(Feedback.objects.all().values())
        data =  dict()
        data['feedbacks'] = feedbacks
        return JsonResponse(data)

class  FeedbackDetail(View):
    def  get(self, request, pk):
        feedback = get_object_or_404(Feedback, pk=pk)
        data =  dict()
        data['feedback'] = model_to_dict(feedback)
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class  FeedbackCreate(CreateView):
    def  post(self, request):
        data =  dict()
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()
            data['feedback'] = model_to_dict(feedback)
        else:
            data['error'] =  "form not valid!"
        return JsonResponse(data)

class  FeedbackUpdate(View):
    def  post(self, request, pk):
        data =  dict()
        feedback = Feedback.objects.get(pk=pk)
        form = FeedbackForm(instance=feedback, data=request.POST)
        if form.is_valid():
            feedback = form.save()
            data['feedback'] = model_to_dict(feedback)
        else:
            data['error'] =  "form not valid!"
        return JsonResponse(data)

class  FeedbackDelete(LoginRequiredMixin, View):
    def  post(self, request, pk):
        data =  dict()
        feedback = Feedback.objects.get(pk=pk)
        if feedback:
            feedback.delete()
            data['message'] =  "Feedback deleted!"
        else:
            data['error'] =  "Error!"
        return JsonResponse(data)