import { TestBed, inject, async, fakeAsync, tick } from '@angular/core/testing';

import { HttpClient, HttpClientModule } from '@angular/common/http';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { AuthenticationService } from './authentication.service';

describe('AuthenticationService', () => {

  let httpClient: HttpClient;
  let httpMock: HttpTestingController;
  let authenticationService: AuthenticationService;
  const api = 'api/';

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [ HttpClientTestingModule ],
      providers: [AuthenticationService]
    });
  });

  beforeEach(() => {
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

});
