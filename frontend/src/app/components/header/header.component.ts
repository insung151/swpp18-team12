import { Component, OnInit } from '@angular/core';

import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

import { AuthenticationService } from '../../service/authentication.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  private loggedIn: boolean;
  private username: string;

  constructor(private authenticationService: AuthenticationService,
              private router: Router) { }

  ngOnInit() {
    this.loggedIn = this.authenticationService.loggedIn();
    this.username = this.authenticationService.getUserName();
  }

  logout(): void {
    if (this.authenticationService.logOut()) {
      this.loggedIn = false;
    }
  }

}
