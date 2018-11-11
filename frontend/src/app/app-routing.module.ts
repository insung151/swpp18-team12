import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AuthGuard } from './auth.guard';

import { MainComponent } from './components/main/main.component';
import { SignInComponent } from './components/account/sign-in/sign-in.component';
import { SignUpComponent } from './components/account/sign-up/sign-up.component';
import { ResetPasswordComponent } from './components/account/reset-password/reset-password.component';
import { ChangePasswordComponent } from './components/account/change-password/change-password.component';
import { ClubComponent } from './components/club/club.component';
import { PostClubComponent } from './components/club/post-club/post-club.component';
import { SearchComponent } from './components/search/search.component';

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
  { path: 'club',
    children: [
      { path: 'new', component: PostClubComponent },
      { path: ':id', component: ClubComponent },
    ],
  },
  { path: 'search', component: SearchComponent },
  { path: '**', component: MainComponent },
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
