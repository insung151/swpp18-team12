import { Component, OnInit } from '@angular/core';

import { AbstractControl, FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { AuthenticationService } from '../service/authentication.service';

@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.css']
})
export class SignInComponent implements OnInit {

  private signInForm: FormGroup;
  private previousUrl: string;

  private email: AbstractControl;
  private password: AbstractControl;


  constructor(private authenticationService: AuthenticationService,
              private router: Router,
              private formBuilder: FormBuilder) {
    this.signInForm = formBuilder.group({
      'email': ['', ],
      'password': ['', ],
    });
    this.email = this.signInForm.controls['email'];
    this.password = this.signInForm.controls['password'];
  }

  async logIn(): Promise<void> {
    const res: boolean = await this.authenticationService.logIn(this.email.value, this.password.value);
    if (res) {
      this.router.navigateByUrl(this.previousUrl); // login success
    } else {
      alert('login failed'); // TODO: login failed
    }
  }

  ngOnInit() {
  }

}
