from django.shortcuts import render
from django.http import HttpResponse
from .forms import PassForm
from generator_app.utils import pass_gen

# Create your views here.
def home(request):
    form = PassForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            choice, length = form.cleaned_data['social_choice'], form.cleaned_data['pass_length']
            result = pass_gen(length, choice)
            context['result'] = result
    return render(request, "home.html", context)
