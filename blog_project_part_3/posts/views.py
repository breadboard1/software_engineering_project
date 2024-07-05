from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import forms, models
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


@method_decorator(login_required, name="dispatch")
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = "./posts/add_post.html"
    success_url = reverse_lazy("add_post")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = "./posts/add_post.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("profile")


@method_decorator(login_required, name="dispatch")
class DeletePostView(DeleteView):
    model = models.Post
    template_name = "./posts/delete.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("profile")


class DetailPostView(DetailView):
    model = models.Post
    pk_url_kwarg = "id"
    template_name = "./posts/post_details.html"

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
