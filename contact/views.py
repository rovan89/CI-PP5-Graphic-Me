from django.shortcuts import render

def contact_page(request):
    """ A view to return the contact page """

    return render(request, 'contact/contact.html')
