import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-fibonacci',
  templateUrl: './fibonacci.component.html',
  styleUrls: ['./fibonacci.component.css'],
})
export class FibonacciComponent {
  number: number = 0;
  sequence: number[] = [];

  constructor(private http: HttpClient) {}

  onInputChange() {
    if (this.number < 1) {
      this.sequence = [];
    }
  }

  getFibonacci() {
    if (this.number < 1) {
      return;
    }
    this.http
      .get<any>(`http://127.0.0.1:5000/fibonacci?n=${this.number}`)
      .subscribe((response) => {
        this.sequence = response.sequence;
      });
  }
}
