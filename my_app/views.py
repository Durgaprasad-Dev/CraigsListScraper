from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base.html')

def  new_search(request):
     # What we are typing in the search box we are retreiving
     search=request.POST.get('search')
     stuff_front_end={
         'search':search
     }
     print(search)
     #Context Dictionary
     return render(request,'my_app/new_search.html',stuff_front_end)

