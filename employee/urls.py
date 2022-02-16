from rest_framework.routers import SimpleRouter
from employee.views import EmployeeOperations
router = SimpleRouter()
router.register('apis',EmployeeOperations)
urlpatterns = router.urls