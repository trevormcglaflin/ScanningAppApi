import { Component, OnInit } from '@angular/core';
import { Company } from '@/_models';
import { DocumentScanService } from '@/_services';

@Component({
  selector: 'app-company',
  templateUrl: './company.component.html',
  styleUrls: ['./company.component.scss']
})
export class CompanyComponent implements OnInit {
  companyList: Company[] = [];
  modalTitle:string = '';
  activateAddEditCompany:boolean = false;
  company:any;
  constructor(private documentScanService: DocumentScanService) { }

  ngOnInit() {
    this.refreshCompanyList();
  }

  refreshCompanyList(){
    this.documentScanService.getCompanyList().subscribe(data=>{
      this.companyList=data;
    });
  }

  deleteCompany(company:any) {
    if(confirm('Are you sure??')){
      this.documentScanService.deleteCompany(company.id).subscribe(data=>{
        alert(data.toString());
        this.refreshCompanyList();
      })
    }
  }

  addClick() {
    this.activateAddEditCompany = true;
    this.company={
      id:0,
      title:""
    }
    this.modalTitle="Add Department";
  }

  updateClick(company:any) {
    this.company = company;
    this.modalTitle = "Edit Company";
    this.activateAddEditCompany = true;
  }

  closeClick(){
    this.activateAddEditCompany = false;
    this.refreshCompanyList();
  }
}