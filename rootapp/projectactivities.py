# #activities.py
# from temporalio import activity
# from .models import LOAN_APPLICATION_GAUGE_SUCCESS, LOAN_APPLICATION_GAUGE_FAIL, DOCUMENT_SUBMISSIONS_GAUGE_SUCCESS, DOCUMENT_SUBMISSIONS_GAUGE_FAIL, SCREEN_PROCESSING_GAUGE_SUCCESS, SCREEN_PROCESSING_GAUGE_FAIL, NEGOTIATION_GAUGE_SUCCESS, NEGOTIATION_GAUGE_FAIL, LOAN_APPLICATION_FINALIZATION_GAUGE_SUCCESS, LOAN_APPLICATION_FINALIZATION_GAUGE_FAIL, APPROVAL_OF_LOAN_GAUGE_SUCCESS, APPROVAL_OF_LOAN_GAUGE_FAIL
# @activity.defn
# def loanApplication() -> str:
#      LOAN_APPLICATION_GAUGE_SUCCESS.inc()
#      print( "Loan Application")

# @activity.defn
# def documentSubmissions() -> str:
#     print( "Document Submissions")

# @activity.defn
# def screenProcessing() -> str:
#      print( "Document Submissions")

# @activity.defn
# def negotitation() -> str:
#      print( "Document Submissions")

# @activity.defn
# def loanApplicationFinalization() -> str:
#      print( "Document Submissions")

# @activity.defn
# def approvalOfLoan() -> str:
#      print( "Document Submissions")

from django.db import close_old_connections
from django.db.utils import DatabaseError
from django.core.exceptions import SynchronousOnlyOperation
from api.models import IterationModels, ControllerModels
from temporalio import activity
from .models import (
    LOAN_APPLICATION_GAUGE_SUCCESS, 
    LOAN_APPLICATION_GAUGE_FAIL, 
    DOCUMENT_SUBMISSIONS_GAUGE_SUCCESS, 
    DOCUMENT_SUBMISSIONS_GAUGE_FAIL, 
    SCREEN_PROCESSING_GAUGE_SUCCESS, 
    SCREEN_PROCESSING_GAUGE_FAIL, 
    NEGOTIATION_GAUGE_SUCCESS,
     NEGOTIATION_GAUGE_FAIL,
     LOAN_APPLICATION_FINALIZATION_GAUGE_SUCCESS,
     LOAN_APPLICATION_FINALIZATION_GAUGE_FAIL, 
     APPROVAL_OF_LOAN_GAUGE_SUCCESS, 
     APPROVAL_OF_LOAN_GAUGE_FAIL
)
from asgiref.sync import sync_to_async
flag = None
no = 0
else_executed = False
@sync_to_async
def update_loan_application_count():
    try:
        controller = ControllerModels.objects.first()
        if controller.is_loan_application_accepted:
            LOAN_APPLICATION_GAUGE_SUCCESS.inc()
        else:
            LOAN_APPLICATION_GAUGE_FAIL.inc()
    except (DatabaseError, SynchronousOnlyOperation):
        close_old_connections()
        controller = ControllerModels.objects.first()
        if controller.is_loan_application_accepted:
            LOAN_APPLICATION_GAUGE_SUCCESS.inc()
        else:
          LOAN_APPLICATION_GAUGE_FAIL.inc()


@sync_to_async
def update_document_submissions_count():
     print("enter inside  documentSubmissions")
     global flag, no, else_executed
     
     flag = 1
     no = 0
     
     try:
        controller = ControllerModels.objects.first()
        if flag == 1 and controller.is_document_submitted:
            print("if part")
            DOCUMENT_SUBMISSIONS_GAUGE_SUCCESS.inc()
           

        else:
            value = IterationModels.objects.first()
            try:
                while no < value.number:
                    print(f"looping: {no}")
                    DOCUMENT_SUBMISSIONS_GAUGE_FAIL.inc()
                    no += 1
                flag = 0
                print(5/0) 
            except Exception as e:
                if flag == 0 and controller.is_document_submitted:
                    print("after failed passed")
                    DOCUMENT_SUBMISSIONS_GAUGE_FAIL.dec()
                    DOCUMENT_SUBMISSIONS_GAUGE_SUCCESS.inc()
            
                
                
          
                

               
                
                
            
     except (DatabaseError, SynchronousOnlyOperation):
        close_old_connections()
        controller = ControllerModels.objects.first()
        
        if flag == 0 and controller.is_document_submitted:
            print("after failed passed")
            DOCUMENT_SUBMISSIONS_GAUGE_FAIL.dec()
            DOCUMENT_SUBMISSIONS_GAUGE_SUCCESS.inc()

        else:
          print("Document Submissions failed again")

@sync_to_async
def update_screen_processing_count():
    
    try:
        controller = ControllerModels.objects.first()
        if controller.is_screening_done:
               SCREEN_PROCESSING_GAUGE_SUCCESS.inc()
          
        else:
          SCREEN_PROCESSING_GAUGE_FAIL.inc()
            
    except (DatabaseError, SynchronousOnlyOperation):
        close_old_connections()
        controller = ControllerModels.objects.first()
        if controller.is_screening_done:
               SCREEN_PROCESSING_GAUGE_SUCCESS.inc()
            
        else:
          SCREEN_PROCESSING_GAUGE_FAIL.inc()
            

@sync_to_async
def update_negotiation_count():
    try:
        controller = ControllerModels.objects.first()
        if controller.is_negotiation_done:
             NEGOTIATION_GAUGE_SUCCESS.inc()
            
        else:
          NEGOTIATION_GAUGE_FAIL.inc()
          
    except (DatabaseError, SynchronousOnlyOperation):
        close_old_connections()
        controller = ControllerModels.objects.first()
        if controller.is_negotiation_done:
                NEGOTIATION_GAUGE_SUCCESS.inc()
         
        else:

          NEGOTIATION_GAUGE_FAIL.inc()
            

@sync_to_async
def update_loan_application_finalization_count():
    try:
        controller = ControllerModels.objects.first()
        if controller.is_loan_finalized:
            LOAN_APPLICATION_FINALIZATION_GAUGE_SUCCESS.inc()
            
        else:
          LOAN_APPLICATION_FINALIZATION_GAUGE_FAIL.inc()
           
    except (DatabaseError, SynchronousOnlyOperation):
        close_old_connections()
        controller = ControllerModels.objects.first()
        if controller.is_loan_finalized:
               LOAN_APPLICATION_FINALIZATION_GAUGE_SUCCESS.inc()
        
        else:
          LOAN_APPLICATION_FINALIZATION_GAUGE_FAIL.inc()
           

@sync_to_async
def update_approval_of_loan_count():
    try:
        controller = ControllerModels.objects.first()
        if controller.is_loan_approved:
            APPROVAL_OF_LOAN_GAUGE_SUCCESS.inc()
        else:
            APPROVAL_OF_LOAN_GAUGE_FAIL.inc()
    except (DatabaseError, SynchronousOnlyOperation):
        close_old_connections()
        controller = ControllerModels.objects.first()
        if controller.is_loan_approved:
            APPROVAL_OF_LOAN_GAUGE_SUCCESS.inc()
        else:
          APPROVAL_OF_LOAN_GAUGE_FAIL.inc()
            

@activity.defn
async def loanApplication() -> str:
    await update_loan_application_count()
    print("Loan Application")
    return "Loan Application"

@activity.defn
async def documentSubmissions() -> str:
    await update_document_submissions_count()
    print("Document Submissions")
    return "Document Submissions"

@activity.defn
async def screenProcessing() -> str:
    await update_screen_processing_count()
    print("Screen Processing")
    return "Screen Processing"

@activity.defn
async def negotitation() -> str:
    await update_negotiation_count()
    print("Negotiation")
    return "Negotiation"

@activity.defn
async def loanApplicationFinalization() -> str:
    await update_loan_application_finalization_count()
    print("Loan Application Finalization")
    return "Loan Application Finalization"

@activity.defn
async def approvalOfLoan() -> str:
    await update_approval_of_loan_count()
    print("Approval of Loan")
    return "Approval of Loan"


    


