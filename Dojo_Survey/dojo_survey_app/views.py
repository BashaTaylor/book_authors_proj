from django.shortcuts import render, redirect

# your code here
def index(request):
    return render(request,'my_home_page.html')

def process(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'plant': request.POST['plant'],
            'color': request.POST['color']
        }
        return render(request, 'result.html', context)
    return render(request, 'result.html')

