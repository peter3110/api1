
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from restapi1.script1 import *

# =====================================================================
# Data for charts
# =====================================================================
@csrf_exempt
def twitterdata(request):
    response = {
    	"following": query1("pedror3110")
    }
    return JsonResponse(response, status=200)