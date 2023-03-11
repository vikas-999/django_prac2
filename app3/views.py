from django.shortcuts import render

# Create your views here.
def again(request):
    return render(request, "again.html")