import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { SignUpComponent } from './sign-up.component';
import { NO_ERRORS_SCHEMA, Component } from '@angular/core';
import { AuthenticationService } from '../service/authentication.service';
import { AuthenticationServiceSpy } from '../service/authentication.service.spy';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterTestingModule } from '@angular/router/testing';
import { AlertService } from '../service/alert.service';
import { AlertServiceSpy } from '../service/alert.service.spy';

@Component({
  template: ``
})
class MockSignInComponent {}

describe('SignUpComponent', () => {
  let component: SignUpComponent;
  let fixture: ComponentFixture<SignUpComponent>;
  let authenticationServiceSpy: AuthenticationServiceSpy;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [
        SignUpComponent,
        MockSignInComponent,
      ],
      schemas: [ NO_ERRORS_SCHEMA ],
      imports: [
        RouterTestingModule.withRoutes([
          { path: 'login', component: MockSignInComponent },
        ]),
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
    fixture = TestBed.createComponent(SignUpComponent);
    component = fixture.componentInstance;
    authenticationServiceSpy = fixture.debugElement.injector.get(AuthenticationService) as any;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  // @TODO: ngZone.run()?
  describe('signUp', () => {
    it('should try login the user', async(() => {
      const email = component.email.value;
      const username = component.username.value;
      const password = component.password.value;
      const password_confirmation = component.password_confirmation.value;
      const year_of_admission = component.year_of_admission.value;
      const department = component.department.value;

      component.signUp();
      fixture.detectChanges();
      expect(authenticationServiceSpy.signUp).toHaveBeenCalledWith(
        email,
        username,
        password,
        password_confirmation,
        year_of_admission,
        department,
      );
    }));
  });
});
