# # views.py
from django.shortcuts import render
from .projectworkflow import LoanExecutingProcess
from .projectactivities import loanApplication, documentSubmissions, screenProcessing, negotitation, loanApplicationFinalization, approvalOfLoan
from django.http import JsonResponse
from temporalio.client import Client
from temporalio.worker import Worker
import concurrent.futures
import asyncio
from django.db import close_old_connections
from django.db.utils import DatabaseError
from django.core.exceptions import SynchronousOnlyOperation
from django.db import transaction
from asgiref.sync import sync_to_async
from api.models import IterationModels


@sync_to_async
def get_karan_models():
    try:
        karan_models = list(IterationModels.objects.all())
    except (DatabaseError, SynchronousOnlyOperation):
        close_old_connections()
        karan_models = list(IterationModels.objects.all())
    return karan_models

async def execute_workflow(client, workflow_id):
    result = await client.execute_workflow(
        LoanExecutingProcess.run, id=workflow_id, task_queue="default"
    )
    return result

# first views
# async def worker(request):
#     # Create client connected to server at the given address
#     client = await Client.connect("localhost:7233")

#     # Run the worker
#     with concurrent.futures.ThreadPoolExecutor(max_workers=100) as activity_executor:
#         worker = Worker(
#           client,
#           task_queue="default",
#           workflows=[LoanExecutingProcess],
#           activities=[loanApplication, documentSubmissions, screenProcessing, negotitation, loanApplicationFinalization, approvalOfLoan],
#           activity_executor=activity_executor,
#         )
        
#         await worker.run()
#     # return JsonResponse({"result": "Worker is running"})


async def worker(request):
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Run the worker with concurrent.futures.ThreadPoolExecutor(max_workers=100) as activity_executor:
    worker = Worker(
        client,
        task_queue="default",
        workflows=[LoanExecutingProcess],
        activities=[
            loanApplication,
            documentSubmissions,
            screenProcessing,
            negotitation,
            loanApplicationFinalization,
            approvalOfLoan,
        ],
        activity_executor=concurrent.futures.ThreadPoolExecutor(max_workers=100),
    )
    await worker.run()

    # return JsonResponse({"result": "Worker is running"})
# second views
async def start_workflow(request):
    
    client = await Client.connect("localhost:7233")
    tasks = []
    karan_models = await get_karan_models()
    if not karan_models:
        return JsonResponse({"error": "KaranModels objects not found"})

    for karan_model in karan_models:
        number = karan_model.number
        for i in range(number):
            workflow_name = f"gulshan mundri-{i}"
            workflow_id = f"loan_process-{i}"
            tasks.append(execute_workflow(client, workflow_id))

    results = await asyncio.gather(*tasks)
    return JsonResponse({"result": results})


