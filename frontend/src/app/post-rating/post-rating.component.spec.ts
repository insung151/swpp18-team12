import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PostRatingComponent } from './post-rating.component';

describe('PostRatingComponent', () => {
  let component: PostRatingComponent;
  let fixture: ComponentFixture<PostRatingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PostRatingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PostRatingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
