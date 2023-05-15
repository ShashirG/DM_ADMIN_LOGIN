from django.shortcuts import render
# Create your views here.

from django.http.response import Http404
from login_app.models import connection_detail
from rest_framework.views import APIView
from connection_details_app.serializers import Connection_Details_Serializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,SessionAuthentication,BasicAuthentication


# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view, authentication_classes, permission_classes

# @api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated,])
# def secure_view(request):
#     return Response({'message': 'Secure view!'})
# @login_required
class Connectiton_Detail_View(APIView):
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    # queryset = connection_detail.objects.all()
    # serializer_class = Connection_Details_Serializer
    def get_object(self, pk):
            try:
                return connection_detail.objects.get(pk=pk)
            except connection_detail.DoesNotExist:
                raise Http404
    def get(self, request, pk=None, format=None):
        var_pipeline_det_id= connection_detail.objects.filter(id=3).values('con_str')
        print(var_pipeline_det_id)
        # temp_pd_id=pipeline_det_id[0]
        if pk:
                data = self.get_object(pk)
                var_serializer = Connection_Details_Serializer(data)
                return Response([var_serializer.data])

        else:
                data = connection_detail.objects.all()
                var_serializer = Connection_Details_Serializer(data, many=True)

                return Response(var_serializer.data)

    def post(self, request, format=None):
        data = request.data
        var_serializer = Connection_Details_Serializer(data=data)

        var_serializer.is_valid(raise_exception=True)

        var_serializer.save()

        response = Response()

        response.data = {
            'message': 'connect_detail Created Successfully',
            'data': var_serializer.data
        }
        return response

    def put(self, request, pk=None, format=None):
        var_update_conn_details = connection_detail.objects.get(pk=pk)
        var_serializer = Connection_Details_Serializer(instance=var_update_conn_details,data=request.data, partial=True)
        var_serializer.is_valid(raise_exception=True)
        var_serializer.save()
        response = Response()
        response.data = {
            'message': 'conect_detail Updated Successfully',
            'data': var_serializer.data
        }
        return response

    def delete(self, request, pk, format=None):
        var_delete_conn_details =  connection_detail.objects.get(pk=pk)
        var_delete_conn_details.delete()
        return Response({
            'message': 'connect_detail Deleted Successfully'
        })

