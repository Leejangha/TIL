from django.shortcuts import render

# Create your views here.
def calculation(request):
    return render(request, 'calculators/calculation.html')

def result(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    mul = num1 * num2
    diff = num1 - num2
    if num2 != 0:
        div = num1 / num2
    else:
        False
    context = {
        'num1' : num1,
        'num2' : num2,
        'mul' : mul,
        'diff' : diff,
        'div' : div,
    }
    return render(request,'calculators/result.html', context)