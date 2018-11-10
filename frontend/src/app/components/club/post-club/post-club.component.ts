import { Component, OnInit } from '@angular/core';
import { AbstractControl, FormGroup, FormBuilder, Validators } from '@angular/forms';
import { AlertService } from 'src/app/service/alert.service';
import { ClubService } from 'src/app/service/club.service';
import { Router } from '@angular/router';
import { Club } from 'src/app/model/club';

@Component({
  selector: 'app-post-club',
  templateUrl: './post-club.component.html',
  styleUrls: ['./post-club.component.css']
})
export class PostClubComponent implements OnInit {

  private url: string;
  private selectedFile: File;

  createClubForm: FormGroup;

  /*
  name: string;
  profile_image: File;
  activity_type: number;
  short_description: string;
  category: number;
  subcategory: number;
  tags: string[];
  */

  name: AbstractControl;
  profile_image: AbstractControl;
  activity_type: AbstractControl;
  short_description: AbstractControl;
  category: AbstractControl;
  subcategory: AbstractControl ;
  tags:AbstractControl; 

  constructor(
    private formBuilder: FormBuilder,
    private alertService: AlertService,
    private clubService: ClubService,
    private router: Router,
  ) {

    this.createClubForm = formBuilder.group({
      'name': ['', ],
      'profile_image': ['', ],
      'activity_type': ['', ],
      'short_description': ['', ],
      'category': ['', ],
      'subcategory': ['1', ],
      'tags': ['', ],
    })

    this.name = this.createClubForm.controls['name'];
    // this.profile_image = this.createClubForm.controls['profile_image'];
    this.activity_type = this.createClubForm.controls['activity_type'];
    this.short_description = this.createClubForm.controls['short_description'];
    this.category = this.createClubForm.controls['category'];
    this.subcategory = this.createClubForm.controls['subcategory'];
    this.tags = this.createClubForm.controls['tags'];
  }

  ngOnInit() {
  }

  onSelectFile(event) {
    if (event.target.files && event.target.files[0]) {
      const reader: FileReader = new FileReader();

      reader.readAsDataURL(event.target.files[0]); // read file as data url
      this.selectedFile = event.target.files[0];
      console.log(this.selectedFile);

      reader.onload = (event) => { // called once readAsDataURL is completed

        this.url = reader.result as string;
        console.log(this.url);
      };
    }
  }

  // TODO: Fix 400 Error (image data form)
  async createClub(): Promise<void> {
    try {
      const club: Club = {
        name: this.name.value,
        // profile_image: this.profile_image.value,
        // profile_image: this.url,
        profile_image: this.selectedFile,
        activity_type: this.activity_type.value,
        short_description: this.short_description.value,
        category: this.category.value,
        subcategory: this.subcategory.value,
        tags: ["Test"],
        // tags: this.tags.value
      };
      console.dir(club);
      const res_postclub = await this.clubService.newClub(club);
      if (res_postclub) {
        this.alertService.success('create Suceess!', true);
        this.router.navigate([]);
      } else {
        this.alertService.error('Failed to create', false);
      }
    } catch {
      this.alertService.error('Unexpected Error', false);
    }
  }

}
