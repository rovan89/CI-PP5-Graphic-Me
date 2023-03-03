from django.shortcuts import render


def about_page(request):
    """ A view to return the about page """

    return render(request, 'about/about.html')
