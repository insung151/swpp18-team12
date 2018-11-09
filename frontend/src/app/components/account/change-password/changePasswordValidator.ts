import { AbstractControl } from '@angular/forms';

export class ChangePasswordValidator {
  static matchForm(control: AbstractControl) {
    const old_password: string = control.get('old_password').value;
    const new_password: string = control.get('new_password').value;
 
    const passwordReg: RegExp = /(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    if (!passwordReg.test(old_password)) {
      control.get('old_password').setErrors({ invalidPassword : true });
    }

    if (!passwordReg.test(new_password)) {
      control.get('new_password').setErrors({ invalidPassword : true });
    }

    if (old_password === new_password) {
      control.get('new_password').setErrors({ invalidPassword : true });
    }
  }
}
