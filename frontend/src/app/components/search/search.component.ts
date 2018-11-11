import { Component, OnInit } from '@angular/core';
import { CategoryOption, ActivityOption } from '../../model/club-option';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  private activityOption: string[] = ActivityOption;
  private activity: string[];

  private categoryOption: string[] = CategoryOption;
  private category: string[];

  private subcategoryOption: string[] = [];
  private subcategory: string[];

  constructor() { }

  ngOnInit() {
  }

 
  toggle() {
    /*
    const x = document.getElementById("detail");
    if (x.style.display === "none") {
      x.style.display = "block"
    } else {
      x.style.display = "none";
    }
    */
    console.dir(this.category);
  }


}
