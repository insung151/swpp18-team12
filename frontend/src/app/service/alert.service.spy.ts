import { Subject } from 'rxjs';

export class AlertServiceSpy {

    private subject = new Subject<any>();

    success = jasmine.createSpy('success').and.callFake((message: string, keepAfter = false) => {
        this.subject.next({ type: 'success', text: message });
    });

    error = jasmine.createSpy('error').and.callFake((message: string, keepAfter = false) => {
        this.subject.next({ type: 'error', text: message });
    });

    getMessage = jasmine.createSpy('getMessage').and.callFake(() => {
        return this.subject.asObservable();
    });

}
