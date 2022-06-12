import { Component, OnInit, Input, EventEmitter, Output } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { DocumentScanService } from '@/_services';

@Component({
  selector: 'app-loaddoc',
  templateUrl: './loaddoc.component.html',
  styleUrls: ['./loaddoc.component.scss']
})
export class LoaddocComponent implements OnInit {
  @Input() companyId:any;
  @Output() docUploadedEvent = new EventEmitter<number>()
  title:any = "";
  document:any;
  uploadForm: FormGroup; 


  constructor(private documentScanService: DocumentScanService, 
              private formBuilder: FormBuilder, 
              private httpClient: HttpClient) { }

  ngOnInit() {
    this.uploadForm = this.formBuilder.group({
      document: [''],
      title: [''],
    });
  }

  onFileSelect(event) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.uploadForm.get('document').setValue(file);
    }
  }

  onNameSelect(event) {
    this.uploadForm.get('title').setValue(event.target.value);
  }

  onSubmit() {
    const formData = new FormData();
    formData.append('document', this.uploadForm.get('document').value);
    formData.append('title', this.uploadForm.get('title').value);
    this.documentScanService.addDocument(formData, this.companyId).subscribe(
      (res) => this.docUploadedEvent.emit(res['id']),
      (err) => console.log()
    );
  }
}
