import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PostClubComponent } from './post-club.component';

describe('PostClubComponent', () => {
  let component: PostClubComponent;
  let fixture: ComponentFixture<PostClubComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PostClubComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PostClubComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
