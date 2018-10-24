import { Component, OnInit } from '@angular/core';

import { AbstractControl, FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { AuthenticationService } from '../service/authentication.service';


@Component({
  selector: 'app-change-password',
  templateUrl: './change-password.component.html',
  styleUrls: ['./change-password.component.css']
})
export class ChangePasswordComponent implements OnInit {

  private changePasswordForm: FormGroup;
  private previousUrl: string;

  private old_password: AbstractControl;
  private new_password: AbstractControl;


  constructor(private authenticationService: AuthenticationService,
              private router: Router,
              private formBuilder: FormBuilder) {
    this.changePasswordForm = formBuilder.group({
      'old_password': ['', ],
      'new_password': ['', ],
    });
    this.old_password = this.changePasswordForm.controls['old_password'];
    this.new_password = this.changePasswordForm.controls['new_password'];
  }

  async changePassword(): Promise<void> {
    const res: boolean = await this.authenticationService.changePassword(this.old_password.value, this.new_password.value);
    if (res) {
      this.router.navigateByUrl(this.previousUrl); // login success
    } else {
      alert('change password failed'); // TODO: login failed
    }
  }

  ngOnInit() {
  }

}
