from django.shortcuts import render

from . import translate


# Create your views here.
def translator_view(request):
    if request.method == "POST":
        origin_text = request.POST["origin_text"]
        translated_text = translate.translate(origin_text)
        return render(
            request,
            "translator.html",
            {"origin_text": origin_text, "translated_text": translated_text},
        )
    else:
        return render(request, "translator.html")
