from django.db import models

# Create your models here.
from prometheus_client import Gauge

# Create custom gauge metrics
LOAN_APPLICATION_GAUGE_SUCCESS = Gauge('k_loan_application_count_success', 'Count of Loan Application')
LOAN_APPLICATION_GAUGE_FAIL = Gauge('k_loan_application_count_fail', 'Count of Loan Application')
DOCUMENT_SUBMISSIONS_GAUGE_SUCCESS = Gauge('k_document_submissions_count_success', 'Count of Document Submissions')
DOCUMENT_SUBMISSIONS_GAUGE_FAIL = Gauge('k_document_submissions_count_fail', 'Count of Document Submissions')
SCREEN_PROCESSING_GAUGE_SUCCESS = Gauge('k_screen_processing_count_success', 'Count of Screen Processing')
SCREEN_PROCESSING_GAUGE_FAIL = Gauge('k_screen_processing_count_fail', 'Count of Screen Processing')
NEGOTIATION_GAUGE_SUCCESS = Gauge('k_negotiation_count_success', 'Count of Negotiation')
NEGOTIATION_GAUGE_FAIL = Gauge('k_negotiation_count_fail', 'Count of Negotiation')
LOAN_APPLICATION_FINALIZATION_GAUGE_SUCCESS = Gauge('k_loan_application_finalization_count_success', 'Count of Loan Application Finalization')
LOAN_APPLICATION_FINALIZATION_GAUGE_FAIL = Gauge('k_loan_application_finalization_count_fail', 'Count of Loan Application Finalization')
APPROVAL_OF_LOAN_GAUGE_SUCCESS = Gauge('k_approval_of_loan_count_success', 'Count of Approval of Loan')
APPROVAL_OF_LOAN_GAUGE_FAIL = Gauge('k_approval_of_loan_count_fail', 'Count of Approval of Loan')

