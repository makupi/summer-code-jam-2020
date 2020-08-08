
from .forms import UserRegisterForm, ProfileForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterUserView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'

    def get_second_form(self):
        if self.request.method == 'POST':
            return ProfileForm(self.request.POST)
        else:
            return ProfileForm()

    def form_valid(self, form):
        self.second_form = self.get_second_form()
        if self.second_form.is_valid():
            print(self.second_form)  # debug purpose
            user = self.request.user
            print(user)  # debug purpose
            self.second_form.save(commit=True)
            print(user.profile.news_source)  # debug purpose
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['second_form'] = getattr(
            self, 'second_form', self.get_second_form()
            )
        return context
