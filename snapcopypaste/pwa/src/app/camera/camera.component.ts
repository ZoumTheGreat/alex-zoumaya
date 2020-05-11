import { Component, OnInit, Input } from "@angular/core";
import * as Tesseract from "tesseract.js";
import { ThemePalette } from "@angular/material";

@Component({
  selector: "app-camera",
  templateUrl: "./camera.component.html",
  styleUrls: ["./camera.component.css"]
})
export class CameraComponent implements OnInit {
  fileData: File = null;
  previewUrl: any = null;
  seeResult: boolean = false;
  textResult: string = "";
  status: string = "";
  progressValue: number = 0;
  seeProgress: boolean = true;

  getIt() {
    Tesseract.recognize(this.fileData, "eng", {
      logger: m => {
        console.log(m);
        if (m.status == "recognizing text") {
          this.updateStatus(m.status);
          this.progressValue = m.progress * 100;
        } else {
          this.updateStatus(m.status);
        }
      }
    }).then(({ data: { text } }) => {
      this.status = "";
      this.seeProgress = false;
      console.log(text);
      this.textResult = text;
    });
  }

  updateStatus(status) {
    this.status = status + "...";
  }

  ngOnInit() {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      console.log("working");
    } else {
      console.log("not working");
    }
  }

  processFile(fileInput: any) {
    this.fileData = <File>fileInput.target.files[0];
    this.reset();
    this.preview();
    this.getIt();
    this.seeResult = true;
  }

  reset() {
    this.textResult = "";
    this.progressValue = 0;
    this.seeProgress = true;
    this.status = "";
  }

  preview() {
    var mimeType = this.fileData.type;
    if (mimeType.match(/image\/*/) == null) {
      return;
    }

    var reader = new FileReader();
    reader.readAsDataURL(this.fileData);
    reader.onload = _event => {
      this.previewUrl = reader.result;
    };
  }

  copyToClipboard() {
    var textArea = document.createElement("textarea");
    document.body.appendChild(textArea);
    textArea.value = this.textResult;
    textArea.select();
    document.execCommand("copy");
    document.body.removeChild(textArea);
  }

  editText() {
    var text = document.getElementById("textResult");
    var b = document.getElementById("editButton");
    if (text.contentEditable == "true") {
      text.contentEditable = "false";
      b.innerHTML = "Edit";
    } else {
      text.contentEditable = "true";
      b.innerHTML = "Save";
    }
    this.textResult = text.innerHTML.replace("&nbsp;", " ");
  }
}
