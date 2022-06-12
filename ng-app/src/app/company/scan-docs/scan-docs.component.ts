import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';

@Component({
  selector: 'app-scan-docs',
  templateUrl: './scan-docs.component.html',
  styleUrls: ['./scan-docs.component.scss']
})
export class ScanDocsComponent implements OnInit {
  docLoaded:boolean = false;
  docScanned:boolean = false;
  companyName:string = "";
  companyId:number = 0;
  documentId:number = 0;

  constructor(private location:Location) { }

  ngOnInit() {
    this.companyName = history.state.title;
    this.companyId = history.state.id;
  }

  docIsUploaded(documentId:any){
    this.docLoaded = true;
    this.documentId = documentId;
  }

  docIsScanned(isScanned:any){
    this.docScanned = isScanned;
  }
}
