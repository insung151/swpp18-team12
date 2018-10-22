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

@NgModule({
  declarations: [
    AppComponent,
    SignInComponent,
    MainComponent,
    SignUpComponent,
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
    // TODO: Fix Dependency Inejction Error. I think I have to ask TA about it.
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
