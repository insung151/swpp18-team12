import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

// External Module
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

// My Module
import { AppRoutingModule } from './app-routing.module';
import { AuthGuard } from './auth.guard';

// node_modules Module
import { SuiModule } from 'ng2-semantic-ui';

// Services
import { AuthenticationService } from './service/authentication.service';

// Components
import { AppComponent } from './app.component';

import { MainComponent } from './components/main/main.component';
import { HeaderComponent } from './components/header/header.component';
import { AlertComponent } from './components/alert/alert.component';

import { SignInComponent } from './components/account/sign-in/sign-in.component';
import { SignUpComponent } from './components/account/sign-up/sign-up.component';
import { ResetPasswordComponent } from './components/account/reset-password/reset-password.component';
import { ChangePasswordComponent } from './components/account/change-password/change-password.component';

import { ClubComponent } from './components/club/club.component';
import { DetailComponent } from './components/club/detail/detail.component';
import { RatingComponent } from './components/club/rating/rating.component';
import { PostRatingComponent } from './components/club/post-rating/post-rating.component';

import { AlertService } from './service/alert.service';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { PostClubComponent } from './components/club/post-club/post-club.component';
import { SearchComponent } from './components/search/search.component';

@NgModule({
  declarations: [
    AppComponent,
    SignInComponent,
    MainComponent,
    SignUpComponent,
    ResetPasswordComponent,
    ChangePasswordComponent,
    HeaderComponent,
    AlertComponent,
    ClubComponent,
    DetailComponent,
    RatingComponent,
    PostRatingComponent,
    PostClubComponent,
    SearchComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    FontAwesomeModule,
    SuiModule,
  ],
  providers: [
    AuthenticationService,
    AlertService,
    AuthGuard,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
