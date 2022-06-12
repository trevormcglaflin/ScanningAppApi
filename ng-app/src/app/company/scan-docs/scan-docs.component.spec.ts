import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ScanDocsComponent } from './scan-docs.component';

describe('ScanDocsComponent', () => {
  let component: ScanDocsComponent;
  let fixture: ComponentFixture<ScanDocsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ScanDocsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ScanDocsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
