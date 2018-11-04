import { Component, OnInit } from '@angular/core';
import { AbstractControl, FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { AuthenticationService } from '../service/authentication.service';
import { AlertService } from '../service/alert.service';

// @TODO: Change component name from reset -> forgot.

@Component({
  selector: 'app-reset-password',
  templateUrl: './reset-password.component.html',
  styleUrls: ['./reset-password.component.css']
})
export class ResetPasswordComponent implements OnInit {

  private resetPasswordForm: FormGroup;
  private previousUrl: string;

  email: AbstractControl;


  constructor(private authenticationService: AuthenticationService,
              private alertService: AlertService,
              private router: Router,
              private formBuilder: FormBuilder) {
    this.resetPasswordForm = formBuilder.group({
      'email': ['', ],
    });
    this.email = this.resetPasswordForm.controls['email'];
  }

  async forgotPassword() {
    const res: boolean = await this.authenticationService.forgotPassword(this.email.value);
    if (res) {
      this.router.navigateByUrl(this.previousUrl);
      this.alertService.success('Please check your mailbox!', false);
    } else {
      this.alertService.error('Invlide User', false);
    }
  }


  ngOnInit() {
  }

}
