from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
import json
from .models import Follow
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.


class HomeView(generic.TemplateView):
    template_name = "index.html"

    def post(self, request):
        user_id = request.POST.get("user_id")
        follow = Follow.objects.filter(
            from_user=request.user,
            to_user_id=user_id
        ).last()
        if not follow:  # follow
            Follow.objects.create(
                from_user=request.user,
                to_user_id=user_id
            )
            return JsonResponse({
                "status": True
            })
        else:
            follow.delete()
            return JsonResponse({
                "status": False
            })

    def get_context_data(self, **kwargs):
        context = {}
        context["following"] = [follow.to_user for follow in self.request.user.following.all()]
        context["user_list"] = User.objects.all().exclude(id=self.request.user.id)
        return context


class Follower(generic.TemplateView):
    template_name = "followers.html"

    def get_context_data(self, **kwargs):
        context = {}
        context["followers"] = [follow.from_user for follow in self.request.user.followers.all()]
        return context


class Following(generic.TemplateView):
    template_name = "following.html"

    def get_context_data(self, **kwargs):
        context = {}
        context["following"] = [follow.to_user for follow in self.request.user.following.all()]
        return context