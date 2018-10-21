import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { SignInComponent } from './sign-in/sign-in.component';
import { MainComponent } from './main/main.component';

import { AppRoutingModule } from './app-routing.module';

import { AuthenticationService } from './service/authentication.service';

@NgModule({
  declarations: [
    AppComponent,
    SignInComponent,
    MainComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [
    AuthenticationService
    // TODO: Fix Dependency Inejction Error. I think I have to ask TA about it.
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
