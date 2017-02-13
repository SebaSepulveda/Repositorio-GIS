from django.shortcuts import render
from .models import DocumentForm
from .forms import model_form_upload

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, './../../repocit/templates/upload.html', {
        'form': form
    })