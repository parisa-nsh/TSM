from django.shortcuts import render

# Create your views here.
def home(request):
    """
    This function handles request for the home page.
    Grouped all transaction based on SKU number and sum up quantity left & reserved quantity.

    :param request: httpresponse
    :return:
    """

    context = {

    }

    return render(request, "teachers/home.html", context)
