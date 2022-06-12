import { Component, OnInit, Input } from '@angular/core';

import { Company } from '@/_models';
import { DocumentScanService } from '@/_services';

@Component({
  selector: 'app-add-edit-company',
  templateUrl: './add-edit-company.component.html',
  styleUrls: ['./add-edit-company.component.scss']
})
export class AddEditCompanyComponent implements OnInit {

  constructor(private documentScanService: DocumentScanService) { }

  @Input() company:any;
  companyId:string = '';
  companyName:string = '';

  ngOnInit() {
    this.companyId=this.company.id;
    this.companyName=this.company.title;
  }

  addCompany(){
    var val = {id:this.companyId,
                title:this.companyName};
    this.documentScanService.addCompany(val).subscribe(res=>{
      alert("Are you sure?");
    });
  }

  updateCompany(){
    var val = {document:this.companyId,
              title:this.companyName};
    this.documentScanService.updateCompany(val).subscribe(res=>{
      alert("Are you sure?");
    });
  }
}
