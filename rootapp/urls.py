from django.urls import path
from .views import start_workflow, worker

urlpatterns = [
    path('start/', start_workflow, name='start_workflow'),
    path('worker/', worker, name='worker')
    

    
]

# print("else part")
#             print("looping")
#             value = IterationModels.objects.first()
#             while no < value.number:
#                     print(f"looping: {no}")
#                     DOCUMENT_SUBMISSIONS_GAUGE_FAIL.inc()
#                     no += 1
                
#             flag = 0
#             else_executed = True
#             number = 5/0 