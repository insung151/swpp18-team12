import { Component, OnInit } from '@angular/core';
import { AbstractControl, FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { AuthenticationService } from '../service/authentication.service';


@Component({
  selector: 'app-reset-password',
  templateUrl: './reset-password.component.html',
  styleUrls: ['./reset-password.component.css']
})
export class ResetPasswordComponent implements OnInit {

  private resetPasswordForm: FormGroup;
  private previousUrl: string;

  private old_password: AbstractControl;
  private new_password: AbstractControl;


  constructor(private authenticationService: AuthenticationService,
              private router: Router,
              private formBuilder: FormBuilder) {
    this.resetPasswordForm = formBuilder.group({
      'old_password': ['', ],
      'new_password': ['', ],
    });
    this.old_password = this.resetPasswordForm.controls['old_password'];
    this.new_password = this.resetPasswordForm.controls['new_password'];
  }

  async resetPassword() {
    alert('Not implemented yet!');
  }


  ngOnInit() {
  }

}
