import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

// External Module
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

// My Module
import { AppRoutingModule } from './app-routing.module';
import { AuthGuard } from './auth.guard';

// Services
import { AuthenticationService } from './service/authentication.service';

// Components
import { AppComponent } from './app.component';
import { SignInComponent } from './sign-in/sign-in.component';
import { MainComponent } from './main/main.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { ResetPasswordComponent } from './reset-password/reset-password.component';
import { ChangePasswordComponent } from './change-password/change-password.component';
import { HeaderComponent } from './header/header.component';
import { AlertComponent } from './alert/alert.component';
import { AlertService } from './service/alert.service';
import { ClubComponent } from './club/club.component';
import { DetailComponent } from './club/detail/detail.component';
import { RatingComponent } from './club/rating/rating.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { PostRatingComponent } from './post-rating/post-rating.component';

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
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    FontAwesomeModule,
  ],
  providers: [
    AuthenticationService,
    AlertService,
    AuthGuard,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
