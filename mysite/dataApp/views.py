# from .serializers import YourModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import logging
from .models import tableLine
from django.db import connection

logger = logging.getLogger(__name__)
# import encryption as encrypt
# import windowMain as windowMain
class MyAPIView(APIView):

    # def post(self, request):
    #     if request.method == 'POST':
    #         print("s a intrat aici in post")
    #         # data = request.POST
    #         data = request.data
    #         print("Recieved data: %s", data)
    #         logger.info("Received data: %s", data)
    #         keys = data.keys()
    #         if 'saveData' in keys:
    #             # de gandit logica de trasnfer intre server si aplicatie desktop
    #
    #             values = data["saveData"]
    #             newData = []
    #             for l in values:
    #                 l.pop(0)
    #                 newData.append(l)
    #             print("newData = ",newData)
    #             response = JsonResponse({'success': True, 'message': 'Data saved successfully'})
    #             response["Access-Control-Allow-Origin"] = "*"
    #             response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    #             response["Access-Control-Allow-Headers"] = "Content-Type"
    #             return response
    #         else:
    #             try:
    #                 self.clear_and_save_data(data)
    #                 print("list:", list)
    #                 for key, values in data.items():
    #                     if values:
    #                         title, username, password, url, notes = values
    #                         table_line = tableLine.objects.create(
    #                             title=title,
    #                             username=username,
    #                             password=password,
    #                             url=url,
    #                             notes=notes
    #                         )
    #                         table_line.save()
    #                 self.clear_and_save_data(data)
    #                 logger.info("Data saved successfully")
    #                 response = JsonResponse({'success': True, 'message': 'Data saved successfully'})
    #                 response["Access-Control-Allow-Origin"] = "*"
    #                 response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    #                 response["Access-Control-Allow-Headers"] = "Content-Type"
    #                 return response
    #                 # return JsonResponse({'success': True, 'message': 'Data saved successfully'})
    #             except Exception as e:
    #                 logger.error("Error saving data: %s", str(e))
    #                 return JsonResponse({'error': 'Error saving data'}, status=500)
    #     else:
    #         return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

    def post(self, request):
        if request.method == 'POST':
            data = request.data
            try:
                tableLine.objects.all().delete()
                keys = data.keys()
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
                logger.info("Data saved successfully")
                response = JsonResponse({'success': True, 'message': 'Data saved successfully'})
                response["Access-Control-Allow-Origin"] = "*"
                response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
                response["Access-Control-Allow-Headers"] = "Content-Type"
                return response
            except Exception as e:
                logger.error("Error saving data: %s", str(e))
                return JsonResponse({'error': 'Error saving data'}, status=500)
        else:
            return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

    def add_data(self, request):
        if request.method == 'POST':
            received_data = request.POST.get('data', ' ')
            print("s a facut add_data")
            print(received_data)
            return JsonResponse({'success': True, 'message': 'Data saved successfully'})
        elif request.method == 'GET':
            return JsonResponse({'error': 'GET method not allowed for add_data'}, status=405)

    def get(self, request):
        t = tableLine.objects.all().values()
        data = {}
        index = 0
        for dict in t:
            l = list(dict.values())
            data[index] = l
            index += 1

        if data is not None:
            response = JsonResponse(data, safe=False)
        else:
            response = JsonResponse({}, safe=False)
        logger.info("Response: %s", data)
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
        print("response: ", response)
        return response

    def get_data(self):
        data = tableLine.objects.all().values()
        return JsonResponse(list(data), safe=False)




