from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message":"Hi there, this is you Django API respone!!"})

