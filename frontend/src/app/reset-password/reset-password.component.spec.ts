import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ResetPasswordComponent } from './reset-password.component';
import { NO_ERRORS_SCHEMA, Component } from '@angular/core';
import { AuthenticationService } from '../service/authentication.service';
import { AuthenticationServiceSpy } from '../service/authentication.service.spy';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterTestingModule } from '@angular/router/testing';
import { AlertService } from '../service/alert.service';
import { AlertServiceSpy } from '../service/alert.service.spy';

describe('ResetPasswordComponent', () => {
  let component: ResetPasswordComponent;
  let fixture: ComponentFixture<ResetPasswordComponent>;
  let authenticationServiceSpy: AuthenticationService;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ResetPasswordComponent ],
      schemas: [ NO_ERRORS_SCHEMA ],
      imports: [
        RouterTestingModule,
        FormsModule,
        ReactiveFormsModule,
      ],
      providers: [
        { provide: AuthenticationService, useClass: AuthenticationServiceSpy },
        { provide: AlertService, useClass: AlertServiceSpy },
      ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ResetPasswordComponent);
    component = fixture.componentInstance;
    authenticationServiceSpy = fixture.debugElement.injector.get(AuthenticationService) as any;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  describe('Forgot password', () => {
    it('get email', async(() => {
      const email = component.email.value;
      component.forgotPassword().then(() => {
        fixture.detectChanges();
        expect(authenticationServiceSpy.forgotPassword).toHaveBeenCalledWith(email);
      });
    }));
  });
});
