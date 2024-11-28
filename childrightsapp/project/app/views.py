
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Child, Video
from .forms import ChildForm, VideoForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import HelpForm
from django.views.generic.edit import FormView
from django.contrib import messages

class ChildListView(ListView):
    model = Child
    template_name = 'child_list.html'
    context_object_name = 'children'

class ChildDetailView(DetailView):
    model = Child
    template_name = 'child_detail.html'
    context_object_name = 'child'

class ChildCreateView(CreateView):
    model = Child
    form_class = ChildForm
    template_name = 'child_form.html'
    success_url = reverse_lazy('child_list')

class ChildUpdateView(UpdateView):
    model = Child
    form_class = ChildForm
    template_name = 'child_form.html'
    success_url = reverse_lazy('child_list')


class ChildDeleteView(DeleteView):
    model = Child
    success_url = '/children/'  # Redirect to the child list after deletion
    template_name = 'child_confirm_delete.html'
    success_url = reverse_lazy('child_list')

class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'video_form.html'
    success_url = reverse_lazy('child_list')

class VideoUpdateView(UpdateView):
    model = Video
    form_class = VideoForm
    template_name = 'video_form.html'

class VideoDetailView(DetailView):
    model = Video
    template_name = 'video_detail.html'
    context_object_name = 'video'

class VideoDeleteView(DeleteView):
    model = Video
    success_url = reverse_lazy('child_list')
    template_name = 'video_confirm_delete.html'

# Similarly, you can create UpdateView, DeleteView, and other views for the Video model.
class HomePageView(TemplateView):
    template_name = 'home.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class HelpPageView(TemplateView):
    template_name = 'help.html'

# views.py
from django.views.generic import ListView
from .models import Video

class VideoListView(ListView):
    model = Video
    template_name = 'video_list.html'
    context_object_name = 'videos'

class HelpPageView(FormView):
    template_name = 'help.html'
    form_class = HelpForm

    def get_success_url(self):
        # Get the URL to redirect after form submission
        messages.success(self.request, 'Form submitted successfully!')
        return reverse_lazy('help')  # Replace 'help' with the correct pattern name

    def form_valid(self, form):
        # Process the form data (save to the database, send an email, etc.)
        # For simplicity, let's print the data to the console
        print(form.cleaned_data)

        # Redirect to the success URL
        return super().form_valid(form)
def success(request):
    return render(request,'successpage.html')
