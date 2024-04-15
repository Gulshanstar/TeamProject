from django.db import models


# Create your models here.
class IterationModels(models.Model):
    number = models.PositiveIntegerField()


# Create models for the activities
class ControllerModels(models.Model):
    is_loan_application_accepted = models.BooleanField(default=False)
    is_document_submitted = models.BooleanField(default=False)
    is_screening_done = models.BooleanField(default=False)
    is_negotiation_done = models.BooleanField(default=False)
    is_loan_finalized = models.BooleanField(default=False)
    is_loan_approved = models.BooleanField(default=False)

    # write the json for postman testing for loan application
    # {
    #     "is_loan_application_accepted": true,
    #     "is_document_submitted": true,
    #     "is_screening_done": true,
    #     "is_negotiation_done": true,
    #     "is_loan_finalized": true,
    #     "is_loan_approved": true
    # }