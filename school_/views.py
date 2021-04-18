from django.shortcuts import render, redirect
from .forms import SchoolForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def create(request):
    if request.method == "POST":
        form = SchoolForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user_id = request.user.id
            f.save()
            # return redirect()

    return render(request, 'school.create.html')

def read(request):
    schools = school_.objects.all()
    return render(request, 'school.read.html', {'schools': schools})
@login_required()
def update(request, school_id):
    school_ = .objects.get(id=id)
    if request.method == "POST":
        form = SchoolForm(request.POST, request.FILES, instance=school_)
        if form.is_valid():
            form.save()
            return redirect('read.sc')
    return render(request, 'school.update.html', {'school_': school_})

def delete(request, school_id):
    school = school_.objects.get(id=id)
    school_.delete()
    return redirect('read.sch')