from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.http import Http404
from authentication.decorators import user_is_instructor, user_is_student
from core.forms import FeedbackForm

from .forms import AssignmentCreateForm, AssignmentSubmissionForm
from .models import Assignment, AssignmentSubmission

from .decorators import user_is_student, user_is_instructor
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


'''class HomeView(ListView):
    template_name = 'home.html'
    def get_queryset(self):
        return self.model.objects.all()
'''

# ASSIGNMENT CREATE VIEW
class AssignmentCreateView(CreateView):
    template_name = 'core/instructor/assignment_create.html'
    form_class = AssignmentCreateForm
    extra_context = {
        'title': 'New Course'
    }
    success_url = reverse_lazy('core:assignment-list')

    @method_decorator(login_required(login_url=reverse_lazy('authentication:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('authentication:login')
        if self.request.user.is_authenticated and self.request.user.role != 'instructor':
            return reverse_lazy('authentication:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AssignmentCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# VIEW FOR ASSIGNMENT LIST
class AssignmentView(ListView):
    model = Assignment
    template_name = 'core/instructor/assignments.html'
    context_object_name = 'assignment'

    @method_decorator(login_required(login_url=reverse_lazy('authentication:login')))
    # @method_decorator(user_is_student, user_is_instructor)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.all()  # filter(user_id=self.request.user.id).order_by('-id')


# DELETE ASSIGNMENT VIEW
class AssignmentDeleteView(DeleteView):
    model = Assignment
    success_url = reverse_lazy('core:assignment-list')


# ASSIGNMENT SUBMISSION VIEW
class AssignmentSubmissionView(CreateView):
    template_name = 'core/instructor/assignment_submission.html'
    form_class = AssignmentSubmissionForm
    extra_context = {
        'title': 'New Exam'
    }
    success_url = reverse_lazy('core:home')

    @method_decorator(login_required(login_url=reverse_lazy('authentication:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('authentication:login')
        if self.request.user.is_authenticated and self.request.user.role != 'student':
            return reverse_lazy('authentication:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AssignmentSubmissionView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# VIEW FOR Assignment Submission List
class AssignmentSubmissionListView(ListView):
    model = AssignmentSubmission
    template_name = 'core/instructor/assignment_submission_list.html'
    context_object_name = 'assignment_submission'



    @method_decorator(login_required(login_url=reverse_lazy('authentication:login')))
    # @method_decorator(user_is_instructor, user_is_student)
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('authentication:login')
        
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')  # filter(user_id=self.request.user.id).order_by('-id')




# EXAM DELETE VIEW
class AssignmentSubmissionDelete(DeleteView):
    model = AssignmentSubmission
    success_url = reverse_lazy('core:assignment-submission-list')



# class FeedbackSubmission(UpdateView):
#     template_name = 'core/instructor/assignment_feedback.html'
#     form_class = AssignmentSubmissionForm
#     extra_context = {
#         'title': 'New Exam'
#     }
#     success_url = reverse_lazy('core:home')

#     @method_decorator(login_required(login_url=reverse_lazy('authentication:login')))
#     def dispatch(self, request, *args, **kwargs):
#         if not self.request.user.is_authenticated:
#             return reverse_lazy('authentication:login')
#         # if self.request.user.is_authenticated and self.request.user.role != 'instructor':
#         #     return reverse_lazy('authentication:login')
#         return super().dispatch(self.request, *args, **kwargs)

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(FeedbackSubmission, self).form_valid(form)

#     def post(self, request, *args, **kwargs):
#         self.object = None
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

class FeedbackSubmission(UpdateView):
    model = AssignmentSubmission
    form_class = FeedbackForm
    context_object_name = 'assignment_feedback'
    template_name = 'core/instructor/assignment_feedback.html'
    success_url = reverse_lazy('core:assignment-feedback')

    @method_decorator(login_required(login_url=reverse_lazy('authentication:login')))
    #@method_decorator(user_is_instructor)
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('authentication:login')
        if self.request.user.is_authenticated and self.request.user.role != 'instructor':
            return reverse_lazy('authentication:login')
        return super().dispatch(self.request, *args, **kwargs)

    

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = self.request.user
        print(obj)
        if obj is None:
            raise Http404("Patient doesn't exists")
        return obj

# def profile(request):
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect(to='users-profile')
#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         profile_form = UpdateProfileForm(instance=request.user.profile)

#     return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})
