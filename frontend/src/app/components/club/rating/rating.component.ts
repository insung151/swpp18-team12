import { Component, OnInit, Input } from '@angular/core';
import { ClubService } from 'src/app/service/club.service';

@Component({
  selector: 'app-rating',
  templateUrl: './rating.component.html',
  styleUrls: ['./rating.component.css']
})
export class RatingComponent implements OnInit {
  @Input() clubId: number;

  ratings: string[];

  getRatings(): void {
    this.clubService.getRating(this.clubId).then(
      ratings => this.ratings = ratings 
    );
    console.log(this.clubId);
    console.log(this.ratings);
  }

  constructor(private clubService: ClubService) { }

  ngOnInit() {
    this.getRatings();
  }

}
