import { Component, OnInit } from '@angular/core';
import { CategoryOption, ActivityOption } from '../../model/club-option';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  private activityOption: string[] = ActivityOption;
  private activity: any[];

  private categoryOption: string[] = CategoryOption;
  private category: string[];

  private subcategoryOption: string[] = [];
  private subcategory: string[];

  constructor() { }

  ngOnInit() {
  }

  search(): void {
    alert("I've not implemented yet!");
  }

}
