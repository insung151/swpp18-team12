import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ClubService } from 'src/app/service/club.service';
import { AlertService } from 'src/app/service/alert.service';

@Component({
  selector: 'app-club',
  templateUrl: './club.component.html',
  styleUrls: ['./club.component.css']
})


export class ClubComponent implements OnInit {

  private club: Club;
  private imgSrc: string;


  constructor(
    private activatedRoute: ActivatedRoute,
    private clubService: ClubService,
    private alertService: AlertService,
    private router: Router,
  ) { }


  ngOnInit() {
    this.getClub();
  }

  async getClub(): Promise<void> {
    const id = +this.activatedRoute.snapshot.paramMap.get('id');
    this.club = await this.clubService.getClub(id);
    this.imgSrc = this.club.profile_image;
  };
}
