from django.shortcuts import redirect, Http404, get_object_or_404
from Url.models import ShortUrl

# Create your views here.

def url_hit(request, *args, **kwargs):

    url = kwargs.get('short_url', '')
    if not url:
        raise Http404

    url_obj = get_object_or_404(ShortUrl, short_url=url)
    url_obj.increment_hit

    return redirect(url_obj.actual_url)
