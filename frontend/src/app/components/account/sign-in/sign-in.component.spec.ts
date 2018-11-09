import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { SignInComponent } from './sign-in.component';
import { NO_ERRORS_SCHEMA, Component } from '@angular/core';
import { AuthenticationService } from '../../../service/authentication.service';
import { AuthenticationServiceSpy } from '../../../service/authentication.service.spy';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterTestingModule } from '@angular/router/testing';
import { AlertService } from '../../../service/alert.service';
import { AlertServiceSpy } from '../../../service/alert.service.spy';

@Component({
  template: ``
})
class MockSignUpComponent { }

describe('SignInComponent', () => {
  let component: SignInComponent;
  let fixture: ComponentFixture<SignInComponent>;
  let authenticationServiceSpy: AuthenticationServiceSpy;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [
        SignInComponent,
        MockSignUpComponent,
      ],
      schemas: [ NO_ERRORS_SCHEMA ],
      imports: [
        RouterTestingModule.withRoutes([{ path: 'signup', component: MockSignUpComponent }]),
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
    fixture = TestBed.createComponent(SignInComponent);
    component = fixture.componentInstance;
    authenticationServiceSpy = fixture.debugElement.injector.get(AuthenticationService) as any;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  describe('tryLogin', () => {
    it('should try login the user', async(() => {
      const email = component.email.value;
      const password = component.password.value;
      component.logIn();
      fixture.detectChanges();
      expect(authenticationServiceSpy.logIn).toHaveBeenCalledWith(email, password);
    }));
  });
});
