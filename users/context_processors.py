from store.models import Restaurant

from django.contrib.auth.decorators import login_required


def GetRest(request):
    if request.user.is_authenticated and (request.user.is_restaurant or request.user.is_user):
        try:
            restaurant = Restaurant.objects.get(user=request.user)
        except Exception as e:
            return {'rest_status': ''}
        else:
            return {'rest_status': restaurant}
    return {}
