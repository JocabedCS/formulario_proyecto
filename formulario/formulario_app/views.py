from django.shortcuts import render
from .forms import RegistroForm

def registro_view(request):
    if request.method == "POST":
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            return render(request, "exito.html", {"datos": form.cleaned_data})
    else:
        form = RegistroForm()
    return render(request, "registro.html", {"form": form})
