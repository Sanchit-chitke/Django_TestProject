from django.shortcuts import render, redirect
from .forms import FirstModelForm, SecondModelForm, ThirdModelForm
from .models import ThirdModel

def create_first_entry(request):
    if request.method == 'POST':
        form = FirstModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_second_entry')
    else:
        form = FirstModelForm()
    return render(request, 'create_first_entry.html', {'form': form})

def create_second_entry(request):
    if request.method == 'POST':
        form = SecondModelForm(request.POST)
        if form.is_valid():
            first_model_instance = form.cleaned_data['first_model']  # Get the associated FirstModel instance
            second_model_instance = form.save(commit=False)
            second_model_instance.first_model = first_model_instance  # Set the first_model foreign key
            second_model_instance.save()
            return redirect('create_third_entry')  # Redirect to create_third_entry view
    else:
        form = SecondModelForm()
    return render(request, 'create_second_entry.html', {'form': form})

def create_third_entry(request):
    if request.method == 'POST':
        form = ThirdModelForm(request.POST)
        if form.is_valid():
            second_model_instance = form.cleaned_data['second_model']  # Get the associated SecondModel instance
            third_model_instance = form.save(commit=False)
            third_model_instance.second_model = second_model_instance  # Set the second_model foreign key
            third_model_instance.save()
            return redirect('show_third_entry')  # Redirect to show_third_entry view
    else:
        form = ThirdModelForm()
    return render(request, 'create_third_entry.html', {'form': form})

def show_third_entry(request):
    third_entry = ThirdModel.objects.last()
    return render(request, 'show_third_entry.html', {'third_entry': third_entry})

def go_to_first_entry(request):
    return redirect('create_first_entry')
