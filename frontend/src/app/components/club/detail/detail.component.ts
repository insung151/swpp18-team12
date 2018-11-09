import { Component, OnInit } from '@angular/core';
import { ClubDetail } from '../../../model/club-detail';

@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.css']
})
export class DetailComponent implements OnInit {

  private items: ClubDetail;

  constructor() { }

  ngOnInit() {
    this.items = {
      join_due_datetime: '12/24',
      join_link: 'goo.gl/asdf',
        site_link: 'http://scsc.snu.ac.kr',
        long_description: 'Blah Blah',
        history: 'Blah Blah',
        hits: 123,
    };
  }

}
