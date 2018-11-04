import { TestBed, inject, async, fakeAsync, tick } from '@angular/core/testing';

import { HttpClient, HttpErrorResponse, HttpResponse } from '@angular/common/http';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';

import { AuthenticationService } from './authentication.service';
import { User } from '../model/user';

const mockUsers = [
  {
    id: 1,
    email: 'swpp@snu.ac.kr',
    password: 'iluvswpp1',
    username: 'swpp',
    year_of_admission: 2018,
    department: 'cse',
  },
  {
    id: 2,
    email: 'yj8902@naver.com',
    password: 'testpassword123',
    username: 'snumath',
    year_of_admission: 2016,
    department: 'math',
  },
] as User[];

const mockUser = {
  id: 1,
  email: 'swpp@snu.ac.kr',
  password: 'iluvswpp1',
  username: 'swpp',
  year_of_admission: 2018,
  department: 'cse',
} as User;

describe('AuthenticationService', () => {

  let httpClient: HttpClient;
  let httpMock: HttpTestingController;
  let authenticationService: AuthenticationService;
  const apiUrl = 'api/accounts';

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [ HttpClientTestingModule ],
      providers: [ AuthenticationService ],
    });
    httpClient = TestBed.get(HttpClient);
    httpMock = TestBed.get(HttpTestingController);
    authenticationService = TestBed.get(AuthenticationService);
  });



  it('should be created', inject([AuthenticationService], (service: AuthenticationService) => {
    expect(service).toBeTruthy();
  }));

  it('should have no httpRequest at the beginning', async() => {
    httpMock.verify();
  });

  it('login(email, password)', async () => {
    authenticationService.logIn(mockUser['email'], mockUser['password']).then( res => {
      alert(localStorage.getItem['currentUser']);
      expect(res).toEqual(true);
    });

    const req = httpMock.expectOne(`${apiUrl}/login/`);
    expect(req.request.method).toEqual('POST');
    req.flush({});
  });

  it('logOut()', async () => {
    authenticationService.logOut().then( res => {
      expect(res).toEqual(true);
    });

    const req = httpMock.expectOne(`${apiUrl}/logout/`);
    expect(req.request.method).toEqual('GET');
    req.flush({});
  });

  it('changePassword(old_password, new_password)', async () => {
    authenticationService.changePassword(mockUser['password'], 'iluvswpp123').then( res => {
      expect(res).toEqual(true);
    });

    const req = httpMock.expectOne(`${apiUrl}/change_password/`);
    expect(req.request.method).toEqual('PUT');
    req.flush({});
  });

  it('signUp(too many...)', async () => {
    authenticationService.signUp(
      'test@snu.ac.kr',
      'newidpw1',
      'newidpw1',
      'newidpw1',
      2016,
      'newidpw1'
    ).then( res => {
      console.log(res);
      expect(res).not.toBeTruthy();
    });

    const req = httpMock.expectOne(`${apiUrl}/signup/`);
    expect(req.request.method).toEqual('POST');
    req.flush({});
  });

  afterEach(() => {
    httpMock.verify();
  });

});

