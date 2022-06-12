import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ManualeditComponent } from './manualedit.component';

describe('ManualeditComponent', () => {
  let component: ManualeditComponent;
  let fixture: ComponentFixture<ManualeditComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ManualeditComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ManualeditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
