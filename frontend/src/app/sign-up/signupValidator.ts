import { AbstractControl } from '@angular/forms';

export class SignupValidator {
  static matchForm(control: AbstractControl) {
    const email: string = control.get('email').value;
    const username: string = control.get('username').value;
    const password: string = control.get('password').value;
    const password_confirmation: string = control.get('password_confirmation').value;
    const year_of_admission: number = control.get('year_of_admission').value;
    const department: string = control.get('department').value;

    // TODO: Match RegExp to backend
    const emailReg: RegExp = new RegExp('^[^@\\s]+[@][^@\\s]+[.][a-z]{2,3}$');
    if (!emailReg.test(email)) {
      control.get('email').setErrors({ invalidEmail : true });
    }

    const usernameReg: RegExp = new RegExp('^$');
    if (usernameReg.test(username)) {
      control.get('username').setErrors({ invalidUsername : true });
    }

    // TODO: delete regexp on front or back.
    const passwordReg: RegExp = new RegExp(''); // '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'); // ^(?=.*\d)(?=.*[a-zA-Z])
    if (!passwordReg.test(password)) {
      control.get('password').setErrors({ invalidPassword : true });
    }

    if (password !== password_confirmation) {
      control.get('password_confirmation').setErrors({ invalidPasswordConfirmation : true });
    }

    if (year_of_admission > 2500 || year_of_admission < 1800) {
        control.get('year_of_admission').setErrors({ invalidYearOfAdmission : true });
    }

    const departmentReg: RegExp = new RegExp('^$');
    if (departmentReg.test(department)) {
      control.get('department').setErrors({ invalidDepartment : true });
    }
  }
}
