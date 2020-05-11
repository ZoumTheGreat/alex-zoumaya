import { BrowserModule } from "@angular/platform-browser";
import { MatProgressBarModule } from "@angular/material";
import { NgModule } from "@angular/core";
import { NgbModule } from "@ng-bootstrap/ng-bootstrap";

import { AppRoutingModule } from "./app-routing.module";
import { AppComponent } from "./app.component";
import { CameraComponent } from "./camera/camera.component";
import { NoopAnimationsModule } from "@angular/platform-browser/animations";
import { ServiceWorkerModule } from '@angular/service-worker';
import { environment } from '../environments/environment';

@NgModule({
  declarations: [AppComponent, CameraComponent],
  imports: [
    NgbModule,
    BrowserModule,
    AppRoutingModule,
    MatProgressBarModule,
    NoopAnimationsModule,
    ServiceWorkerModule.register('ngsw-worker.js', { enabled: environment.production })
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
