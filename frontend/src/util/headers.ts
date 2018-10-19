import { HttpHeaders } from '@angular/common/http';


export function getCSRFHeaders(): HttpHeaders {
  let token = '';
  if (document.cookie) {
    token = document.cookie.split('csrftoken=')[1].split(';')[0];
  }
  return new HttpHeaders({
    'Content-Type': 'application/json',
    'X-CSRFToken': token
  });
}
