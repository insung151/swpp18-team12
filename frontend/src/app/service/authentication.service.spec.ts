import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { getCSRFHeaders } from '../../util/headers';

@Injectable()
export class AuthenticationService {

  private headers: HttpHeaders = new HttpHeaders({ 'Content-Type': 'application/json' });

  async logIn(email: string, password: string): Promise<boolean> {
    const url = 'api/accounts/login/';
    try {
      const res: any = await this.http.post(url,
        JSON.stringify({'email': email, 'password': password }),
        { headers: getCSRFHeaders(), withCredentials: true, observe: 'response'})
      .toPromise();
      if (res.status === 200) { // Successful login
        let token = '';
        if (document.cookie) {
          token = document.cookie.split('csrftoken=')[ 1 ].split(';')[ 0 ];
        }
        localStorage.setItem('currentUser', JSON.stringify({ 'token' : token, 'username': res.body['username'] }));
        return true;
      } else {
        alert('Unexpected in logIn'); // Should not be called
        return false;
      }
    } catch (e) {
      alert(Object.values(e.error));
      return false;
    }
  }

  loggedIn(): boolean {
    if (localStorage.getItem('currentUser')) {
      return true;
    }
    return false;
  }

  getUserName(): string {
    const user = localStorage.getItem('currentUser');
    if (user) {
      return JSON.parse(user)['username'];
    }
    return '';
  }

  async logOut(): Promise<boolean> {
    const url = 'api/accounts/logout/';
    try {
      const res = await this.http.get(url,
        { headers: getCSRFHeaders(), withCredentials: true, observe: 'response'})
        .toPromise();
      localStorage.removeItem('currentUser');
      return true;
    } catch {
      // TODO: Error Handler
      localStorage.removeItem('currentUser');
      return true;
    }
  }

  async signUp(
    email: string,
    password: string,
    password_confirmation: string,
    username: string,
    year_of_admission: number,
    department: string): Promise<boolean> {
    const url = 'api/accounts/signup/';
    try {
      const res: any = await this.http.post(url,
        JSON.stringify({ 'email': email,
          'username': username,
          'password': password,
          'password_confirmation': password_confirmation,
          'year_of_admission': year_of_admission,
          'department': department}),
        { headers: getCSRFHeaders(), withCredentials: true, observe: 'response' })
        .toPromise();
      if (res.status === 201) {
        return true; // successfully logined
      } else {
        alert('Unexpected in signUp'); // should not be called
        return false;
      }
    } catch (e) {
      alert(Object.values(e.error));
      return false;
    }
  }


  async changePassword(old_password: string, new_password: string): Promise<boolean> {
    const url = 'api/accounts/change_password/';
    try {
      const res: any = await this.http.put(url,
        {'old_password': old_password, 'new_password': new_password },
        { headers: getCSRFHeaders(), withCredentials: true, observe: 'response'})
        .toPromise();
        // Successfully changed
      if (res.status === 200) {
        return true;
      } else {
        alert('Unexpeected in changePassword'); // Should not be called
      }
    } catch (e) {
      alert(Object.values(e.error));
      return false;
    }
  }


  constructor(private http: HttpClient) { }
}


