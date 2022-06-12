from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.decorators import action, permission_classes
from django.shortcuts import render, get_object_or_404
from django.db.models.aggregates import Count
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
import json
from .models import Document, Company, User, IncomeStatement
from .serializers import DocumentSerializer, CompanySerializer, AddCompanySerializer, UpdateCompanySerializer, UserSerializer, DocumentISSerializer, ListIncomeStatementSerializer, IncomeStatementSerializer
from .doc_analysis import save_doc_type_and_doc_string, save_tax_form_data, make_income_statement
from .permissions import CompanyBelongsToUser

class CompanyViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCompanySerializer
        elif self.request.method == 'PATCH':
            return UpdateCompanySerializer
        return CompanySerializer
    
    def get_queryset(self):
        user = self.request.user
        return Company.objects.prefetch_related('documents').filter(user_id=user.id)

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}
    
    def get_permissions(self):
        return [IsAuthenticated()]
    
class DocumentViewSet(ModelViewSet):
    serializer_class = DocumentSerializer 
    #permission_classes = [IsAuthenticated,CompanyBelongsToUser]

    def get_serializer_context(self):
        return {'company_id': self.kwargs['company_pk'], 'user_id': self.request.user.id, }
    
    def get_queryset(self):
        return Document.objects.filter(company_id=self.kwargs['company_pk'])
    
    #TODO: make it so that it also gets document year
    @action(detail=True, methods=['GET'], permission_classes=[IsAuthenticated])
    def savedocinfo(self, request, *args, **kwargs):
        document = get_object_or_404(Document, pk=self.kwargs['pk'])
        doc_path_string = str(document.document)
        if doc_path_string[doc_path_string.index(".")+1:] != "pdf":
            return Response("Unknown")
        doc = save_doc_type_and_doc_string(doc_path_string)
        document.doc_type = doc[0]
        document.raw_ocr_string = doc[1]
        document = save_tax_form_data(document, doc[1])
        document.save()
        return Response(DocumentISSerializer(document).data)

    @action(detail=True, methods=['GET'], permission_classes=[IsAuthenticated])
    def getincomestatementtemplate(self, request, *args, **kwargs):
        document = get_object_or_404(Document, pk=self.kwargs['pk'])
        income_statement = make_income_statement(document)
        return Response(ListIncomeStatementSerializer(income_statement).data)

class IncomeStatementViewSet(ModelViewSet):
    serializer_class = IncomeStatementSerializer
    permission_classes = [IsAuthenticated, CompanyBelongsToUser]
    
    def get_queryset(self):
        return IncomeStatement.objects.filter(company_id=self.kwargs['company_pk'])

    def get_serializer_context(self):
        return {'company_id': self.kwargs['company_pk'], }


    
    
