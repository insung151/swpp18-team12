import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { ChangePasswordComponent } from './change-password.component';
import { NO_ERRORS_SCHEMA, Component } from '@angular/core';
import { AuthenticationService } from '../service/authentication.service';
import { AuthenticationServiceSpy } from '../service/authentication.service.spy';
import { FormsModule, ReactiveFormsModule, FormBuilder } from '@angular/forms';
import { RouterTestingModule } from '@angular/router/testing';

@Component({
  template: ``
})
class MockSignUpComponent { }

describe('ChangePasswordComponent', () => {
  let component: ChangePasswordComponent;
  let fixture: ComponentFixture<ChangePasswordComponent>;
  let authenticationServiceSpy: AuthenticationServiceSpy;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [
        ChangePasswordComponent,
        MockSignUpComponent,
      ],
      schemas: [ NO_ERRORS_SCHEMA ],
      imports: [
        RouterTestingModule.withRoutes([
          { path: 'signup', component: MockSignUpComponent },
        ]),
        FormsModule,
        ReactiveFormsModule,
      ],
      providers: [
        { provide: AuthenticationService, useClass: AuthenticationServiceSpy },
      ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ChangePasswordComponent);
    component = fixture.componentInstance;
    authenticationServiceSpy = fixture.debugElement.injector.get(AuthenticationService) as any;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  describe('change Password', () => {
    it('should change password', async(() => {
      const old_password = component.old_password.value;
      const new_password = component.new_password.value;
      component.changePassword().then(() => {
        fixture.detectChanges();
        expect(authenticationServiceSpy.changePassword).toHaveBeenCalledWith(old_password, new_password);
      });
    }));
  });
});
