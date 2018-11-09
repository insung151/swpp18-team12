import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AuthGuard } from './auth.guard';

import { MainComponent } from './main/main.component';
import { SignInComponent } from './sign-in/sign-in.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { ResetPasswordComponent } from './reset-password/reset-password.component';
import { ChangePasswordComponent } from './change-password/change-password.component';
import { ClubComponent } from './club/club.component';

const routes: Routes = [
  { path: '', component: MainComponent },
  { path: 'login', component: SignInComponent },
  { path: 'signup', component: SignUpComponent },
  { path: 'account', 
    children: [
      { path: 'change_password', component: ChangePasswordComponent, canActivate: [AuthGuard], },
      { path: 'forgot_password', component: ResetPasswordComponent },
    ]
  },
  { path: 'club', component: ClubComponent },
  { path: '**', component: MainComponent },
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
