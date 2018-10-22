import { Component, OnInit } from '@angular/core';
import { AbstractControl, FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { AuthenticationService } from '../service/authentication.service';

import { SignupValidator } from './signupValidator';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent implements OnInit {

  signUpForm: FormGroup;
  email: AbstractControl;
  username: AbstractControl;
  password: AbstractControl;
  password_confirmation: AbstractControl;
  year_of_admission: AbstractControl;
  department: AbstractControl;

  constructor(private authenticationService: AuthenticationService,
    private router: Router,
    private formBuilder: FormBuilder
  ) {

  this.signUpForm = formBuilder.group({
    'email' : [ '', Validators.required ],
    'username' : [ '', Validators.required ],
    'password' : [ '', Validators.required ],
    'password_confirmation' : [ '', Validators.required ],
    'year_of_admission' : [ '', Validators.required ],
    'department' : [ '', Validators.required ],
    }, {
      validator : SignupValidator.matchForm
  });

    this.email = this.signUpForm.controls[ 'email' ];
    this.username = this.signUpForm.controls[ 'username' ];
    this.password = this.signUpForm.controls[ 'password' ];
    this.password_confirmation = this.signUpForm.controls[ 'password_confirmation' ];
    this.year_of_admission = this.signUpForm.controls[ 'year_of_admission' ];
    this.department = this.signUpForm.controls[ 'department' ];
  }

  ngOnInit() {
  }

  async signUp(): Promise<void> {
    try {
      const res_signup = await this.authenticationService.signUp(
        this.email.value,
        this.password.value,
        this.password_confirmation.value,
        this.username.value,
        this.year_of_admission.value,
        this.department.value,
      );
      if (res_signup) {
        // TODO: Add task after signed up
        this.router.navigate(['sign_in']);
      }
    } catch {
      alert('SignUp Failed');
    }
  }

}
