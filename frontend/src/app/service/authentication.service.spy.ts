export class AuthenticationServiceSpy {

  logIn = jasmine.createSpy('logIn').and.callFake((email: string, password: string) => {
      if (email === 'swpp@snu.ac.kr' && password === 'iluvswpp') {
        return Promise.resolve(true);
      } else {
        return Promise.resolve(false);
      }
  });

  logOut = jasmine.createSpy('signOut').and.callFake(() => {
      return Promise.resolve(true);
  });

  changePassword = jasmine.createSpy('changePassword').and.callFake((old_password: string, new_password: string) => {
      if (old_password !== new_password) {
        return Promise.resolve(true);
      } else {
        return Promise.resolve(false);
      }
  });

  forgotPassword = jasmine.createSpy('forgotPassword').and.callFake((email: string, ) => {
      if (email) {
        return Promise.resolve(true);
      } else {
        return Promise.resolve(false);
      }
    });

  signUp = jasmine.createSpy('signUp').and.callFake((
    email: string,
    password: string,
    password_confirmation: string,
    username: string,
    year_of_admission: string,
    department: string,
  ) => {
    if (password === password_confirmation) {
      return Promise.resolve(true);
    } else {
      return Promise.resolve(false);
    }
  });

  loggedIn = jasmine.createSpy('loggedIn').and.callFake(() => {
    return Promise.resolve(true);
  });

  getUserName = jasmine.createSpy('getUserName').and.callFake(() => {
    return Promise.resolve('username');
  });

}
