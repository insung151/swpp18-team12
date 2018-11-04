import { TestBed, async, inject } from '@angular/core/testing';

import { AuthGuard } from './auth.guard';
import { Router } from '@angular/router';
import { AuthenticationService } from './service/authentication.service';
import { AuthenticationServiceSpy } from './service/authentication.service.spy';

describe('AuthGuard', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        AuthGuard, 
        { provide: Router, useClass: class { navigate = jasmine.createSpy('navigate'); }, },
        { provide: AuthenticationService, useClass: AuthenticationServiceSpy },
      ]
    });
  });

  it('should be created', inject([AuthGuard], (guard: AuthGuard) => {
    expect(guard).toBeTruthy();
  }));
});
