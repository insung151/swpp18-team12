import { Component, OnInit } from '@angular/core';
import { AbstractControl, FormGroup, FormBuilder, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';

import { AuthenticationService } from '../service/authentication.service';
import { AlertService } from '../service/alert.service';

import { ChangePasswordValidator } from './changePasswordValidator';

@Component({
  selector: 'app-change-password',
  templateUrl: './change-password.component.html',
  styleUrls: ['./change-password.component.css']
})
export class ChangePasswordComponent implements OnInit {

  private changePasswordForm: FormGroup;
  private previousUrl: string;

  old_password: AbstractControl;
  new_password: AbstractControl;


  constructor(private authenticationService: AuthenticationService,
              private alertService: AlertService,
              private router: Router,
              private formBuilder: FormBuilder) {
    this.changePasswordForm = formBuilder.group({
      'old_password': ['', Validators.required],
      'new_password': ['', Validators.required],
    }, {
      validator: ChangePasswordValidator.matchForm
    });
    this.old_password = this.changePasswordForm.controls['old_password'];
    this.new_password = this.changePasswordForm.controls['new_password'];
  }

  async changePassword(): Promise<void> {
    const res: boolean = await this.authenticationService.changePassword(this.old_password.value, this.new_password.value);
    if (res) {
      this.router.navigateByUrl(this.previousUrl);
      this.alertService.success('Password changed', false);
    } else {
      this.alertService.error('Password change failed', false);
    }
  }

  ngOnInit() {
  }

}
