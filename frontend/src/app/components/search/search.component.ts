import { Component, OnInit } from '@angular/core';
import { CategoryOption, ActivityOption } from '../../model/club-option';

import { SearchService } from '../../service/search.service';
import { InfiniteScrollerDirective } from '../../directive/infinite-scroller.directive';

import { tap, catchError } from 'rxjs/operators';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  private searchTerm: string;

  private activityOption: {value: number, label: string}[];
  private categoryOption: {value: number, label: string}[];
  private subcategoryOption: {value: number, label: string}[] = [];
  private tagOption: string[];

  private activity: number[] = [];
  private category: number[] = [];
  private subcategory: number[] = [];
  private tag: string[] = [];

  private currentPage = 1;
  private scrollCallback;
  private club: Array<any> = [];

  constructor(private searchService: SearchService) {
    this.scrollCallback = this.search.bind(this);
  }

  ngOnInit() {
    const adapter = option => option.map((value, index) => {
      return {value: index, label: value};
    });

    this.activityOption = adapter(ActivityOption);
    this.categoryOption = adapter(CategoryOption);

    this.tagOption = [
      'tag1', 'tag2', 'tag3', 'ttag', 'asdf', 'asas', '4sasd', '4dfa', 'ffds',
    ];
  }

  searchButton() {
    this.currentPage = 1;
    this.scrollCallback();
  }

  search() {
    return this.searchService.clubSearch(
      this.searchTerm,
      this.category,
      this.subcategory,
      this.activity,
      this.currentPage)
      .pipe(tap(this.processData));
  }

  private processData = (club) => {
    this.currentPage++;
    this.club = this.club.concat(club.json());
  }

}
