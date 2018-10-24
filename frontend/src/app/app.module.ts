import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

// External Module
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

// My Module
import { AppRoutingModule } from './app-routing.module';

// Services
import { AuthenticationService } from './service/authentication.service';

// Components
import { AppComponent } from './app.component';
import { SignInComponent } from './sign-in/sign-in.component';
import { MainComponent } from './main/main.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { ResetPasswordComponent } from './reset-password/reset-password.component';

@NgModule({
  declarations: [
    AppComponent,
    SignInComponent,
    MainComponent,
    SignUpComponent,
    ResetPasswordComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [
    AuthenticationService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
