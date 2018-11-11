import { Component, OnInit, Input } from '@angular/core';
import { ClubDetail } from '../../../model/club-detail';
import { ClubService } from 'src/app/service/club.service';
import { Router, ActivatedRoute } from '@angular/router';
import { AlertService } from 'src/app/service/alert.service';
import { Club } from 'src/app/model/club';

@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.css']
})
export class DetailComponent implements OnInit {
  @Input() clubId: number;

  /*
  TODO: Important note
  Change this area from club_short to club_detail.
  */
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
    this.club = await this.clubService.getClub(this.clubId);
    this.imgSrc = this.club.profile_image;
  };

}
