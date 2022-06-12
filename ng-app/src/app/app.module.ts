import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { routing } from './app.routing';

import { JwtInterceptor } from './_helpers';
import { HomeComponent } from './home';
import { LoginComponent } from './login';
import { CompanyComponent } from './company/company.component';
import { AddEditCompanyComponent } from './company/add-edit-company/add-edit-company.component';
import { ScanDocsComponent } from './company/scan-docs/scan-docs.component';
import { LoaddocComponent } from './company/scan-docs/loaddoc/loaddoc.component';
import { ScanthedocComponent } from './company/scan-docs/scanthedoc/scanthedoc.component';
import { ManualeditComponent } from './company/scan-docs/manualedit/manualedit.component';

@NgModule({
    imports: [
        BrowserModule,
        ReactiveFormsModule,
        HttpClientModule,
        FormsModule,
        routing
    ],
    declarations: [
        AppComponent,
        HomeComponent,
        LoginComponent,
        CompanyComponent,
        AddEditCompanyComponent,
        ScanDocsComponent,
        LoaddocComponent,
        ScanthedocComponent ,
        ManualeditComponent,   
    ],
    providers: [
        { provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true },
    ],
    bootstrap: [AppComponent]
})

export class AppModule { }