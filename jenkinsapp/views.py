from django.http import JsonResponse
from django.shortcuts import render
from jenkinsapp.forms import StudentRegistrationForm


def create_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration_success.html')
    else:
        form = StudentRegistrationForm()
    return render(request, 'register_student.html', {'form': form})