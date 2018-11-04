import { TestBed, inject } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { Observable, Subject } from 'rxjs';

import { AlertService } from './alert.service';
import { Component } from '@angular/core';

@Component({
  template: ``
})
class MockComponent { }

describe('AlertService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [
        MockComponent,
      ],
      imports: [
        RouterTestingModule.withRoutes([{
          path: '**', component: MockComponent,
        }]),
      ],
      providers: [
        AlertService,
      ]
    });
  });

  it('should be created', inject([AlertService], (service: AlertService) => {
    expect(service).toBeTruthy();
  }));
});
