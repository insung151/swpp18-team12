import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ClubComponent } from './club.component';
import { FormsModule } from '@angular/forms';
import { DetailComponent } from './detail/detail.component';
import { RatingComponent } from './rating/rating.component';

describe('ClubComponent', () => {
  let component: ClubComponent;
  let fixture: ComponentFixture<ClubComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [
        ClubComponent,
        DetailComponent,
        RatingComponent,
      ],
      imports: [ FormsModule ],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ClubComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
