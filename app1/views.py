from django.shortcuts import render

# Create your views here.
def operations(request):
    data=('10', '10000')
    d={'a':data , 'b':10000}
    return render(request, 'operations.html', context=d)