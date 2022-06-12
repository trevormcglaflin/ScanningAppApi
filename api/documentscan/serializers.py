import datetime
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from .models import Document, Company, IncomeStatement

class DocumentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        company_id = self.context['company_id']
        return Document.objects.create(company_id=company_id, **validated_data)

    class Meta:
        model = Document
        fields = ['id', 'title', 'document', 'company_id']

class DocumentISSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'document', 'company_id', 'doc_type',
        'sales', 'returns_and_allowances', 'net_sales', 'cogs', 'gross_profit',
        'total_operating_expense', 'officer_compensation_expense', 'salaries_and_wages_expense',
        'repairs_and_maintenence_expense', 'bad_debt_expense', 'rent_expense', 'taxes_and_licenses_expense',
        'interest_expense', 'charitable_contributions_expense', 'depreciation_expense',
        'depletion_expense', 'advertising_expense', 'pension_expense', 'employee_benefits_expense',
        'reserved_for_future_use_expense', 'other_deductions_expense', 'taxable_income',
        'dividend_revenue', 'interest_revenue', 'rent_revenue', 'royalty_revenue', 'capital_gain_revenue',
        'net_gain_or_loss_revenue', 'other_income_revenue', 'income_tax_expense', 'net_income']

class CompanySerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(many=True, read_only=True)
    class Meta:
        model = Company
        fields = ['id', 'title', 'user_id', 'documents']

    user_id = serializers.IntegerField(read_only=True)

class AddCompanySerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'title', 'user_id']

    def save(self, **kwargs):
        user_id = self.context['user_id']
        title = self.validated_data['title']

        try:
            company = Company.objects.get(
                title=title, user_id=user_id)
            company.save()
            self.instance = company
        except Company.DoesNotExist:
            self.instance = Company.objects.create(
                user_id=user_id, **self.validated_data)
        return self.instance

class UpdateCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['title']

class UserSerializer(BaseUserSerializer):
    companies = CompanySerializer(many=True, read_only=True)
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone', 'birth_date', 'companies']

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name', 'phone', 'birth_date']

class ListIncomeStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model =  IncomeStatement
        fields = ['sales', 'returns_and_allowances', 'net_sales', 'cogs', 'gross_profit',
        'total_operating_expense', 'salaries_and_wages_expense',
        'repairs_and_maintenence_expense', 'bad_debt_expense', 'rent_expense', 'taxes_and_licenses_expense',
        'interest_expense', 'charitable_contributions_expense', 'depreciation_expense',
        'depletion_expense', 'advertising_expense', 'other_income', 'taxable_income',
        'income_tax_expense', 'net_income']

class IncomeStatementSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        company_id = self.context['company_id']

        # validate income statement data
        """
        valid = True
        if validated_data['year'] < 2010 or validated_data['year'] > datetime.datetime.now().year:
            valid = False
        elif validated_data['sales'] - validated_data['returns_and_allowances'] != validated_data['net_sales']:
            valid = False
        elif validated_data['net_sales'] - validated_data['cogs'] != validated_data['gross_profit']:
            valid = False
        elif validated_data['gross_profit'] - validated_data['total_operating_expense'] + validated_data['other_income'] != validated_data['taxable_income']:
            valid = False
        elif validated_data['taxable_income'] - validated_data['income_tax_expense'] != validated_data['net_income']:
            valid = False
        elif validated_data['salaries_and_wages_expense'] + validated_data['repairs_and_maintenence_expense'] + validated_data['bad_debt_expense'] + validated_data['rent_expense'] + \
            validated_data['taxes_and_licenses_expense'] + validated_data['interest_expense'] + validated_data['charitable_contributions_expense'] + validated_data['depreciation_expense'] + \
            validated_data['depletion_expense'] + validated_data['advertising_expense'] != validated_data['total_operating_expense']:
            valid = False
        if not valid:
            raise serializers.ValidationError('Invalid Income Statement Data.')
        """
        return IncomeStatement.objects.create(company_id=company_id, **validated_data)
    
    class Meta:
        model =  IncomeStatement
        fields = ['id', 'company_id', 'year', 'sales', 'returns_and_allowances', 'net_sales', 'cogs', 'gross_profit',
        'total_operating_expense', 'salaries_and_wages_expense',
        'repairs_and_maintenence_expense', 'bad_debt_expense', 'rent_expense', 'taxes_and_licenses_expense',
        'interest_expense', 'charitable_contributions_expense', 'depreciation_expense',
        'depletion_expense', 'advertising_expense', 'other_income', 'taxable_income',
        'income_tax_expense', 'net_income']