import { Component, OnInit } from '@angular/core';
import { CategoryOption } from '../../model/club-option';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  private category: string[] = CategoryOption;

  constructor() { }

  ngOnInit() {
  }

 
  toggle() {
    const x = document.getElementById("detail");
    if (x.style.display === "none") {
      x.style.display = "block"
    } else {
      x.style.display = "none";
    }
  }
 

}
