# workflow.py is the file where the workflow is defined.
from temporalio import workflow
from datetime import timedelta
from temporalio.common import RetryPolicy
with workflow.unsafe.imports_passed_through():
    import rootapp.projectactivities as projectactivities
@workflow.defn
class LoanExecutingProcess():
    @workflow.run
    async def run(self) -> str:
         # Configure retry policy
        retry_policy = RetryPolicy(
            initial_interval=timedelta(seconds=5),  # Initial retry interval
            maximum_attempts=60,  # Maximum number of retry attempts
            maximum_interval=timedelta(seconds=60),  # Maximum interval between retries
            backoff_coefficient=2.0,  # Backoff coefficient for exponential backoff
            
        )
        
        steps1_res =  await workflow.execute_activity(projectactivities.loanApplication, schedule_to_close_timeout=timedelta(seconds=180), retry_policy= retry_policy)
        steps2_res = await workflow.execute_activity(projectactivities.documentSubmissions, schedule_to_close_timeout=timedelta(seconds=180), retry_policy= retry_policy)
        steps3_res = await workflow.execute_activity(projectactivities.screenProcessing, schedule_to_close_timeout=timedelta(seconds=180), retry_policy= retry_policy)
        steps4_res = await workflow.execute_activity(projectactivities.negotitation, schedule_to_close_timeout=timedelta(seconds=180), retry_policy= retry_policy)
        steps5_res = await workflow.execute_activity(projectactivities.loanApplicationFinalization, schedule_to_close_timeout=timedelta(seconds=180), retry_policy= retry_policy)
        steps6_res = await workflow.execute_activity(projectactivities.approvalOfLoan, schedule_to_close_timeout=timedelta(seconds=180), retry_policy= retry_policy)
        return f"{steps1_res}+{steps2_res}+{steps3_res}+{steps4_res}+{steps5_res}+{steps6_res}"


