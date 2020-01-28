from django.http import HttpResponse
from django.template import loader
from .models import user
# Create your views here.

def login_access(request):
    all_users = user.objects.all()
    template = loader.get_template('Login.html')
    context = {
        'all_users': all_users
    }
    return HttpResponse(template.render(context, request))