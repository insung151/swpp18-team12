import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Club } from '../model/club';
import { getCSRFHeaders } from 'src/util/headers';

@Injectable({
  providedIn: 'root'
})
export class ClubService {

  // TODO: Fix 400 Error (image data form)
  async newClub(club: Club): Promise<boolean> {
    const url = 'api/club/new/';
    try {
      const res: any = await this.http.post(url,
        JSON.stringify(club), { headers: getCSRFHeaders(), withCredentials: true, observe: 'response'})
      .toPromise();
      if (res.status === 201) { // Successful login
        return true;
      } else {
        alert('Unexpected in club post'); // Should not be called
        return false;
      }
    } catch (e) {
      return false;
    }
  }

  async getClub(id: number): Promise<Club> {
    const url = `api/club/${id}/club_short`;
    try {
      const res: any = await this.http.get(url,
        { headers: getCSRFHeaders(), withCredentials: true, })
        .toPromise();
      return res;
    } catch (e) {
      return null;
    }
  }

  async getRating(id: number): Promise<string[]> {
    const url = `api/club/${id}/rating`;
    try {
      const res: any = await this.http.get(url,
        { headers: getCSRFHeaders(), withCredentials: true, })
        .toPromise();
      const comments: string[] = res.map(x => x['comments']);
      return comments;
    } catch (e) {
      return null;
    }
  }

  constructor(private http: HttpClient) { }
}
