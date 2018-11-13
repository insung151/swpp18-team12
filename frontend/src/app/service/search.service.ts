import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { getCSRFHeaders } from '../../util/headers';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  clubSearch(keyword: string, cat: number[] = null, sub: number[] = null, type: number[] = null, page: number = 1) {
    const url = 'api/club/search';
    return this.http.get(
      `${url}/?keyword=${keyword}&cat=${cat.join()}&sub=${sub.join()}&type=${type.join()}&page=${page}`,
      { headers: getCSRFHeaders(), withCredentials: true });
  }

  constructor(private http: HttpClient) { }
}
