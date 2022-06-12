import { Component, OnInit, Input, EventEmitter, Output } from '@angular/core';
import { DocumentScanService } from '@/_services';

@Component({
  selector: 'app-scanthedoc',
  templateUrl: './scanthedoc.component.html',
  styleUrls: ['./scanthedoc.component.scss']
})
export class ScanthedocComponent implements OnInit {
  @Input() companyId:any;
  @Input() documentId:any;
  @Output() docScannedEvent = new EventEmitter<boolean>()

  constructor(private documentScanService: DocumentScanService) { }

  ngOnInit() {

  }
  
  scanDoc() {
    this.documentScanService.scanDocument(this.companyId, this.documentId).subscribe(
      (res) => this.docScannedEvent.emit(true),
      (err) => console.log()
    );
  }
}
