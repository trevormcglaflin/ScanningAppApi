import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ScanthedocComponent } from './scanthedoc.component';

describe('ScanthedocComponent', () => {
  let component: ScanthedocComponent;
  let fixture: ComponentFixture<ScanthedocComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ScanthedocComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ScanthedocComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
