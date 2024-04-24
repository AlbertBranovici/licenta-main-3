# from .serializers import YourModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import logging
from .models import tableLine
from django.db import connection
logger = logging.getLogger(__name__)

class MyAPIView(APIView):
    def post(self, request):
        if request.method == 'POST':
            data = request.POST
            logger.info("Received data: %s", data)
            try:
                self.clear_and_save_data(data)
                print("list:", list)
                for key, values in data.items():
                    if values:
                        title, username, password, url, notes = values
                        table_line = tableLine.objects.create(
                            title=title,
                            username=username,
                            password=password,
                            url=url,
                            notes=notes
                        )
                        table_line.save()
                self.clear_and_save_data(data)
                logger.info("Data saved successfully")
                return JsonResponse({'success': True, 'message': 'Data saved successfully'})
            except Exception as e:
                logger.error("Error saving data: %s", str(e))
                return JsonResponse({'error': 'Error saving data'}, status=500)
        else:
            return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)



    def clear_and_save_data(self,data):
        # Step 1: Clear existing data from the database
        tableLine.objects.all().delete()
        with connection.cursor() as cursor:
            cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='tableLine';")

        # Step 2: Parse the data received from the server and create new tableLine objects
        keys = data.keys()
        print("keys:", keys)

        for key in keys:
            list = data.getlist(key)
            title = list[0]
            username = list[1]
            password = list[2]
            url = list[3]
            notes = list[4]
            table_line = tableLine.objects.create(
                title=title,
                username=username,
                password=password,
                url=url,
                notes=notes
            )
            table_line.save()

    def get(self, request):
        # Process GET request
        t = tableLine.objects.all().values()
        data = {}
        index = 0
        for dict in t:
            l = list(dict.values())
            data[index] = l
            index += 1
        print("final state of data: ",data)

        if data is not None:
            response = JsonResponse(data, safe=False)
        else:
            response = JsonResponse({}, safe=False)
        logger.info("Response: %s", data)

        # Set CORS headers for GET request
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response


    def options(self, request, *args, **kwargs):
        # Handle OPTIONS request for CORS preflight
        response = Response()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response




# def post(request):  # Ensure that 'request' argument is included
#         if request.method == 'POST':
#             # Extract data from the request
#             data = request.POST  # Assuming data is sent as form data
#             logger.info("Received data: %s", data)
#             # Validate data if needed
#
#             print("date primite: %s",data)
#             print("s a facut post")
#             # Save the data to the session
#             request.session['data'] = data
#             table = tableLine()
#
#             # Optionally, serialize the data before returning a response
#             # serialized_data = YourModelSerializer(new_instance).data
#
#             return JsonResponse({'success': True, 'data': data})
#             # return JsonResponse({'success': True, 'data': serialized_data})
#         else:
#             return JsonResponse({'error': 'Only POST requests are allowed'})
# def get(self, request):
#     # Process GET request
#     data = request.session.get('data')
#     if data is not None:
#         response = JsonResponse(data, safe=False)
#     else:
#         response = JsonResponse({}, safe=False)
#     logger.info("Response: %s", data)
#
#     # Set CORS headers for GET request
#     response["Access-Control-Allow-Origin"] = "*"
#     response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
#     response["Access-Control-Allow-Headers"] = "Content-Type"
#     return response







# def index(request):
#     print("ddd")
#     return HttpResponse("Pagina dataApp")