from django.views.generic import TemplateView, UpdateView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.http import HttpResponseRedirect
from django.urls import reverse


from .models import Profile
from .forms import ProfileForm


class Profiles(TemplateView):
    """User Profile View"""

    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        # Use get_object_or_404 instead of get to avoid raising an exception
        profile = get_object_or_404(Profile, user=self.kwargs["pk"])
        context = {"profile": profile, "form": ProfileForm(instance=profile)}

        return context


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a profile"""

    form_class = ProfileForm
    model = Profile

    def get_object(self, queryset=None):
        """Get the object this view is displaying."""
        # Use get_object_or_404 to avoid raising an exception
        return get_object_or_404(Profile, user=self.kwargs["pk"])

    def form_valid(self, form):
        self.success_url = f'/profiles/user/{self.kwargs["pk"]}/'
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user

    def test_func(self):
        profile = self.get_object()
        if profile:
            return self.request.user == profile.user
        return False

    def handle_no_permission(self):
        # Redirect to login page or show a message
        return redirect("login")
