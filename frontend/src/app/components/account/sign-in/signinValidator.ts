import { AbstractControl } from '@angular/forms';

export class SigninValidator {
  static matchForm(control: AbstractControl) {
    const email: string = control.get('email').value;
    const password: string = control.get('password').value;

    const emailReg: RegExp = new RegExp('^[^@\\s]+[@][^@\\s]+[.][a-z]{2,3}$');
    if (!emailReg.test(email)) {
      control.get('email').setErrors({ invalidEmail : true });
    }

    const passwordReg: RegExp = /(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    if (!passwordReg.test(password)) {
      control.get('password').setErrors({ invalidPassword : true });
    }
  }
}
