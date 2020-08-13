from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """ View to return bag content """

    return render(request, 'bag/bag.html')
