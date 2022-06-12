from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)

class Company(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="companies")
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']

class Document(models.Model):
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to="documentscan/images")
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='documents')
    doc_type = models.CharField(max_length=255, null=True)
    raw_ocr_string = models.TextField(null=True)

    # doc data
    sales = models.FloatField(null=True, default=0)
    returns_and_allowances = models.FloatField(null=True, default=0)
    net_sales = models.FloatField(null=True, default=0)
    cogs = models.FloatField(null=True, default=0)
    gross_profit = models.FloatField(null=True, default=0)

    # operating expenses
    total_operating_expense = models.FloatField(null=True, default=0)
    officer_compensation_expense = models.FloatField(null=True, default=0)
    salaries_and_wages_expense = models.FloatField(null=True, default=0)
    repairs_and_maintenence_expense = models.FloatField(null=True, default=0)
    bad_debt_expense = models.FloatField(null=True, default=0)
    rent_expense = models.FloatField(null=True, default=0)
    taxes_and_licenses_expense = models.FloatField(null=True, default=0)
    interest_expense = models.FloatField(null=True, default=0)
    charitable_contributions_expense = models.FloatField(null=True, default=0)
    depreciation_expense = models.FloatField(null=True, default=0)
    depletion_expense = models.FloatField(null=True, default=0)
    advertising_expense = models.FloatField(null=True, default=0)
    pension_expense = models.FloatField(null=True, default=0)
    employee_benefits_expense = models.FloatField(null=True, default=0)
    reserved_for_future_use_expense = models.FloatField(null=True, default=0)
    other_deductions_expense = models.FloatField(null=True, default=0)
    taxable_income = models.FloatField(null=True, default=0)
    
    # other income
    dividend_revenue = models.FloatField(null=True, default=0)
    interest_revenue  = models.FloatField(null=True, default=0)
    rent_revenue = models.FloatField(null=True, default=0)
    royalty_revenue = models.FloatField(null=True, default=0)
    capital_gain_revenue = models.FloatField(null=True, default=0)
    net_gain_or_loss_revenue = models.FloatField(null=True, default=0)
    other_income_revenue = models.FloatField(null=True, default=0)
    
    # taxes
    income_tax_expense = models.FloatField(null=True, default=0)
    net_income = models.FloatField(null=True, default=0)


class IncomeStatement(models.Model):
    company = models.ForeignKey(Document, on_delete=models.PROTECT, related_name='incomestatements')
    year = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sales = models.FloatField(null=True, default=0)
    returns_and_allowances = models.FloatField(null=True, default=0)
    net_sales = models.FloatField(null=True, default=0)
    cogs = models.FloatField(null=True, default=0)
    gross_profit = models.FloatField(null=True, default=0)
    total_operating_expense = models.FloatField(null=True, default=0)
    salaries_and_wages_expense = models.FloatField(null=True, default=0)
    repairs_and_maintenence_expense = models.FloatField(null=True, default=0)
    bad_debt_expense = models.FloatField(null=True, default=0)
    rent_expense = models.FloatField(null=True, default=0)
    taxes_and_licenses_expense = models.FloatField(null=True, default=0)
    interest_expense = models.FloatField(null=True, default=0)
    charitable_contributions_expense = models.FloatField(null=True, default=0)
    depreciation_expense = models.FloatField(null=True, default=0)
    depletion_expense = models.FloatField(null=True, default=0)
    advertising_expense = models.FloatField(null=True, default=0)
    operating_profit = models.FloatField(null=True, default=0)
    other_income = models.FloatField(null=True, default=0)
    taxable_income = models.FloatField(null=True, default=0)
    income_tax_expense = models.FloatField(null=True, default=0)
    net_income = models.FloatField(null=True, default=0)
