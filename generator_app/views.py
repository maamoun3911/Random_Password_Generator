from django.shortcuts import render
from django.http import HttpResponse
from .forms import PassForm
from generator_app.utils import pass_gen

# Create your views here.
def home(request):
    form = PassForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        form.to = ""
        if form.is_valid():
            length = form.cleaned_data['length']
            result = pass_gen(length)
            context['result'] = result
    return render(request, "home.html", context)
