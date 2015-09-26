import base64
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render_to_response
from .models import Page


def page_index(request):
    pages = Page.objects.all()
    return render_to_response('pages/index.html', {"pages": pages})

def page_view(request, slug, **kwargs):
    try:
        page = Page.objects.get(page_slug=slug)
    except ObjectDoesNotExist:
        return render_to_response('pages/404.html')

    # If private page do basic auth
    if page.is_private:
        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                if auth[0].lower() == "basic":
                    uname, passwd = base64.b64decode(auth[1]).split(':')
                    user = authenticate(username=uname, password=passwd)
                    if user is not None and user.is_active:
                        request.user = user

                        return render_to_response('pages/page.html', {"page": page})

        response = HttpResponse()
        response.status_code = 401
        response['WWW-Authenticate'] = 'Basic realm="%s"' % "Basci Auth Protected"
        return response
    else:
        return render_to_response('pages/page.html', {"page": page})