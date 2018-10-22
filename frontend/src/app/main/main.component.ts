import { Component, OnInit } from '@angular/core';

import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

import { AuthenticationService } from '../service/authentication.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  private loggedIn: boolean;

  constructor(private authenticationService: AuthenticationService,
              private router: Router) { }

  ngOnInit() {
    this.loggedIn = this.authenticationService.loggedIn();
  }

  logout(): void {
    if (this.authenticationService.logOut()) {
      this.loggedIn = false;
    }
  }

}
