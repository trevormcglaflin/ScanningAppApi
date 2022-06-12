import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LoaddocComponent } from './loaddoc.component';

describe('LoaddocComponent', () => {
  let component: LoaddocComponent;
  let fixture: ComponentFixture<LoaddocComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LoaddocComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LoaddocComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
