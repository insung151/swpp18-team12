import { Component, OnInit } from '@angular/core';

// import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

import { AuthenticationService } from '../service/authentication.service';

@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.css']
})
export class SignInComponent implements OnInit {

  private previousUrl: string;


  constructor(private authenticationService: AuthenticationService,
              private router: Router) { }

  async logIn(email: string, password: string): Promise<void> {
    const res: boolean = await this.authenticationService.logIn(email, password);
    if (res) {
      this.router.navigateByUrl(this.previousUrl); // login success
    } else {
      alert('login failed'); // TODO: login failed
    }
  }

  click(): void {
    this.router.navigateByUrl('/signup');
  }

  ngOnInit() {
  }

}
