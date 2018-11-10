import { Component, OnInit } from '@angular/core';
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

  private items: ClubDetail;

  private club: Club;

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
  };

}
