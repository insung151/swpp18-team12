import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { getCSRFHeaders } from '../../util/headers';

@Injectable()
export class AuthenticationService {

  private headers: HttpHeaders = new HttpHeaders({ 'Content-Type': 'application/json' });
  // const url = '/api/account';

  // login function
  // TODO: connect backend and frontend (solve CRSF problem)
  async logIn(email: string, password: string): Promise<boolean> {
    const url = 'api/account/login';
    const res = await this.http.post(url,
      {'email': email, 'password': password }, { headers: getCSRFHeaders(), withCredentials: true})
      .toPromise();
    try {
      // Successful login
      if (res.status === 200) {
        let token = '';
        if (document.cookie) {
          token = document.cookie.split('csrftoken=')[ 1 ].split(';')[ 0 ];
        }
        localStorage.setItem('currentUser', JSON.stringify({ 'token' : token }));
        return true;
      } else if (res.status === 401) {
        // 'Email verification is incomplete or your account information is incorrect.'
        alert(res.message);
      }
    } catch {
      // TODO: Error Handler
    }
  }

  async logOut(): Promise<boolean> {
    const url = `/api/account/signout`;
    const res = await this.http.get(url).toPromise();
    try {
      localStorage.removeItem('currentUser');
      return true;
    } catch {
      // TODO: Error Handler
      localStorage.removeItem('currentUser');
      return true;
    }
  }

  // TODO: Match variable name as DB in backend.
  // TODO: Error handling
  async signUp(
    email: string,
    username: string,
    password: string,
    password_confirmation: string,
    admission: string,
    department): Promise<boolean> {
    const url = 'api/account/signup';
    const res = await this.http.post(url,
      {email: email, username: username, password: password, admission: admission, department: department},
      { headers: getCSRFHeaders() })
      .toPromise();
    try {
      if (this.status === 201) {

      }
    } catch {

    }
  }

  /*
  TODO: Finish changePassword. 1) check valid user 2) check pw change 3) put api
  async changePassword(password: string, password_confirmation: string): Promise<boolean> {
    const url = 'api/account/change_password';
    const res = await this.http.post(url, {'password': password }, { headers: getCSRFHeaders(), withCredentials: true})
      .toPromise();
    try {
      // Successful login
      if (res.status === 200) {
        let token = '';
        if (document.cookie) {
          token = document.cookie.split('csrftoken=')[ 1 ].split(';')[ 0 ];
        }
        localStorage.setItem('currentUser', JSON.stringify({ 'token' : token }));
        return true;
      } else if (res.status === 401) {
        // 'Email verification is incomplete or your account information is incorrect.'
        alert(res.message);
      }
    } catch {
      // TODO: Error Handler
    }
  }
  */

  constructor(private http: HttpClient) { }
}

