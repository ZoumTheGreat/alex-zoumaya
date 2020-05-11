import { Component } from "@angular/core";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.css"]
})
export class AppComponent {
  title = "pwa";
  showCamera: boolean = true;

  choosePhoto() {
    alert("worked!");
  }

  toggleCamera() {
    
    document.getElementById('selectedFile').click();
  }
}
