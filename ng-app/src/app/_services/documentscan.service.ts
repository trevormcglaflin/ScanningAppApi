import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import * as jwtDecode from 'jwt-decode';
import { User } from '@/_models/user';
import { environment } from 'environments/environment';

@Injectable({ providedIn: 'root' })
export class DocumentScanService {
    constructor(private http: HttpClient) { }

    getCompanyList():Observable<any[]>{
        return this.http.get<any[]>(`${environment.apiUrl}/documentscan/companies`);
    }

    deleteCompany(val:any){
        return this.http.delete(environment.apiUrl + '/documentscan/companies/'+ val);
    }

    addCompany(val:any){
        return this.http.post(environment.apiUrl + '/documentscan/companies/', val);
    }

    updateCompany(val:any){
        return this.http.patch(environment.apiUrl + '/documentscan/companies/' + val.id + "/", val);
    }

    addDocument(val:any, companyId:any){
        return this.http.post(environment.apiUrl + '/documentscan/companies/' + companyId + "/documents/", val);
    }

    scanDocument(companyId:any, docId:any){
        return this.http.get(environment.apiUrl + '/documentscan/companies/' + companyId + "/documents/" + docId + '/savedocinfo/');
    }

    getIncomeStatementTemplate(companyId:any, docId:any){
        return this.http.get(environment.apiUrl + '/documentscan/companies/' + companyId + "/documents/" + docId + '/getincomestatementtemplate/');
    }

    addIncomeStatement(val:any, companyId:any){
        return this.http.post(environment.apiUrl + '/documentscan/companies/' + companyId + "/incomestatements/", val);
    }
}