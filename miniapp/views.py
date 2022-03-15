from django.shortcuts import render


def cover_page(request):
    return render(request, "cover_image.html")
