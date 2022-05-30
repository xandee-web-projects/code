from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import UserSerializer
from base.models import AreaCode, Location, User

@api_view(['GET'])
def get_numbers(request, area_code):
    area = AreaCode.objects.filter(code=area_code).first()
    if area:
        loc = area.location
        user = User.objects.filter(location=loc).first()
        print(User.objects.filter(location=loc).all())
        serializer = UserSerializer(user)
        # Delete the user from the database
        return Response(serializer.data)
    else:
        return Response("Area code is invalid")
