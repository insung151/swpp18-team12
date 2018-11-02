import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AuthenticationService } from '../service/authentication.service';
import { AuthenticationServiceSpy } from '../service/authentication.service.spy';
import { HeaderComponent } from './header.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterTestingModule } from '@angular/router/testing';

describe('HeaderComponent', () => {
  let component: HeaderComponent;
  let fixture: ComponentFixture<HeaderComponent>;
  let authenticationServiceSpy: AuthenticationServiceSpy;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HeaderComponent ],
      imports: [
        RouterTestingModule,
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
    fixture = TestBed.createComponent(HeaderComponent);
    component = fixture.componentInstance;
    authenticationServiceSpy = fixture.debugElement.injector.get(AuthenticationService) as any;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
