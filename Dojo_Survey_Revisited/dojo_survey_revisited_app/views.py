from django.shortcuts import render, redirect

# your code here
def index(request):
    return render(request,'my_home_page.html')

def process(request):
    # request.session['name'] = request.post['name']
    if request.method == 'POST':
        print(request.POST)
        request.session['name'] = request.POST['name']
        request.session['color'] = request.POST.getlist('color')
        request.session['plant'] = request.POST['plant']
        return redirect('/result')
    return redirect('/')
    
def result(request):
    return render(request, 'result.html')
