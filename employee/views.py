
from employee.models import Employee
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.viewsets import GenericViewSet
from employee.serializers import EmployeeSerializer
from rest_framework.mixins import RetrieveModelMixin,DestroyModelMixin


class MyOwnViewSet(GenericViewSet,RetrieveModelMixin,DestroyModelMixin):
    pass


from django.http.response import HttpResponse
from rest_framework.permissions import IsAuthenticated, AllowAny

class EmployeeOperations(ModelViewSet):          #EmployeeOperations -->`create()`, `retrieve()`, `update()`,`partial_update()`, `destroy()` and `list()`
    permission_classes = (AllowAny,)  # all 6 methods are open
    queryset = Employee.objects.all() # to retrive all the records
    serializer_class = EmployeeSerializer

    def get_permissions(self):
        if self.action in ["list"]:        # out of which --> list,create --> requires --> token  --> only list-->
            self.permission_classes = (IsAuthenticated,)
        #else:
        #    return super().get_permissions()
        return super().get_permissions()

'''
class EmployeeOperations(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        print('......', request.data,'.......')
        if type(request.data)== list:
            for empdata in request.data:
                return super().create(request, *args, **kwargs )
            serializer= self.get_serializer(data= request.data)'''


