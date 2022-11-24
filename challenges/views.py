from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotAllowed , HttpResponseNotFound ,HttpResponseRedirect , Http404
from django.urls import reverse
# from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    "january" : "in jan",
    "februray" : "in feb",
    "march" : "in mar",
    "april" : "in apr",
    "may" : "in may",
    "june" : "in june",
    "july" : "in july",
    "august" : "in aug",
    "september" : "in sept",
    "october" : "in oct",
    "november" : "in nov",
    "december" : None
}

def index(request):
    months = list(monthly_challenges.keys())
    return render(request , "challenges/index.html", {
        "months" : months
    })

def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("invalid month")

    # redirect_url = months[month-1]
    redirect_month = months[month-1]
    redirect_url = reverse("monthly_challenge" , args=[redirect_month])  
    return HttpResponseRedirect(redirect_url)
    # return redirect('/challenges/'+redirect_url)


def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request , "challenges/challenge.html",{
            "text" : challenge_text,
            "title" : month
        })
    except:
        raise Http404() # it automatically look for 404 file in template folder

        