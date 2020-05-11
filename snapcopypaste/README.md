University of Dayton

Department of Computer Science

CPS 491 - Capstone II - Spring 2020

Team 1

## Capstone II Project

# Progressive Web App (PWA)

Goal: Develop a full blown Progressive Web Application (PWA) that includes features like connectivity independence, app like interface, push notifications, self updates etc.

# Team 1: Team members

1.  Bekah Greczanik, greczanikr1@udayton.edu
2.  Carl Schultz, schultzc3@udayton.edu
3.  Ajay Patnaik, patnaika2@udayton.edu
4.  Alex Zoumaya, zoumayaa1@udayton.edu

# Company Mentors

Joydeep Mukherjee, Ph.D., VP Merchant-Provider Digital Solutions; Vish Dadireddy, Senior Leader; Ravish Kumar, Senior Leader; Sarath Vadakapurapu, Senior Leader

Synchrony Financial

950 Forrer Blvd, Kettering, OH 45420

## Project homepage

https://cps491s20-team1.bitbucket.io/

# Overview

![Overview Architecture](proposal/diagrams/architecture.png)

Figure 1. - Proposed Architecture

# Use Cases

### User can access the PWA through a mobile web app

- Actors: Any User
- User Stories: I am any user accessing the pwa
- Use Case Description: Any user can access the pwa, no login required

### User can take a picture and see it displayed in the app interface

- Actors: Any User
- User Stories: I am any user and I can take a photo with my mobile device while on the app and can see it displayed within the app interface
- Use Case Description: Any user can access the pwa with a mobile device and take a photo that will be displayed on screen

### User can have the option to upload a photo instead of using the camera

- Actors: Any User
- User Stories: I am any user and I want to upload instead of take a photo
- Use Case Description: Any user can access the pwa and choose a photo from their camera roll to upload

### User can obtain text from an image of text

- Actors: Any User
- User Stories: I am any user who wants to turn a photo of text into text
- Use Case Description: Any user can take or upload a photo and obtain the text of that photo. This text will be copied to their clipboard.

### User can edit text obtained from the image

- Actors: Any User
- User Stories: I am any user who has uploaded an image and extracted the text from the image
- Use Case Description: Any user can take or upload a photo and obtain the text of that photo. This text can then be edited and saved on screen.

# Design

## Use Case Diagram

![Use Case Diagram](proposal/diagrams/UseCaseDiagram3.png =90x150)

Figure 2. - Use Case Diagram

## Database Design

No database implemented

## User Interface

![User Interface](proposal/diagrams/UI2.png =90x150)

Figure 3. - User Interface

# Project Context and Scope

Technically this project is completely independent of anything Synchrony is doing, this was developed in order to give us an opportunity to develop a PWA using agile methodologies. We will be developing the web application in full.

# High-level Requirements

1. Gaining camera access
2. Gaining access to camera roll
3. Gaining read access
4. Gaining write access
5. Obtaining text from photo
6. Editing text
7. Copying text to clipboard

# Technology

Based on early research we plan on using JavaScript, Angular.js, Workbox, Tesseract and Heroku.

# Implementation

To Implement our PWA we are using Angular and Node.js. We are incorporating the Tesseract library for the OCR. We are deploying to our bitbucket site for testing.

## Code Snippets

### Sprint 1

Gaining access to the camera of the device

![Code Snip](proposal/diagrams/camaccess.png =90x150)

### Sprint 2

Gained access to the camera roll by using the html input tag

![Code Snip](proposal/diagrams/camroll.png =90x150)

Implemented ability to process image file and show a preview of it on the webpage

![Code Snip](proposal/diagrams/process.png =90x150)

![Code Snip](proposal/diagrams/preview.png =90x150)

Implemented basic OCR recognition of image

![Code Snip](proposal/diagrams/ocr.png =90x150)

### Sprint 3

Created a progress bar using a node package for javascript components

![Code Snip](proposal/diagrams/progress.png =90x150)

![Code Snip](proposal/diagrams/bar.png =90x150)

Implemented copying text extracted from the image to your clipboard to be used elsewhere on your device by executing the copy command.

![Code Snip](proposal/diagrams/copy.png =90x150)

# Project Management

Length of Sprint Cycles:
Sprint 0: 01/14/2020 - 01/22/2020

      Brainstorm, plan, create diagrams

Sprint 1: 01/22/2020 - 02/12/2020

      Research, build angular shell, create basic site that is accessible, find focus for pwa

Sprint 2: 02/12/2020 - 03/04/2020

      Deploy on mobile, gain access to the camera and camera roll on phone, update landing page, research uploading a photo

Sprint 3: 03/04/2020 - 04/23/2020

      Improve OCR, finish progress bar, implement service workers (enable offline capability), improve UI design, make it installable, make text field editable, copy text to clipboard

#### Team Meeting Schedule:

Spring 2020: M-F 8:00PM - 9:00PM

#### Project Homepage/Website pwa is deployed on:

      https://cps491s20-team1.bitbucket.io/

#### Bitbucket Repository:

      https://bitbucket.org/cps491s20-team1/capstoneii/src

#### Trello Board:

      https://trello.com/b/TRo4zRxG/capstone-ii

# Company Support

Based on our discussion with the company, they will support our team by maintaining contact via email whilst we carry on with our project.

# Software Process Management

We are using Scrum as our software management process.

## Scrum Process

## Sprint 0

Duration: 11/1/2019-1/22/2020

### Completed Tasks:

1.  Brainstorming project ideas
2.  Choosing project focus
3.  Updated team homepage
4.  Created diagrams

### Contributions:

1.  Ajay Patnaik: project brainstorming and overall planning, 2 hours
2.  Bekah Greczanik: updated team webpage, worked on readme and updated trello, 2 hours
3.  Carl Schultz: use cases and diagram, technology brainstorming, architecture diagram, 2 hours
4.  Alex Zoumaya: project brainstorming and readme, 2 hours

### Sprint Retrospective

The focus of this sprint was on planning and brainstorming for our project with Synchrony Financial. We all brainstormed on our own and brought our ideas together. We are leaving our project very open ended to incorporate new ideas and functionalities as they develop.

## Sprint 1

Duration: 1/22/2020-2/12/2020

### Completed Tasks:

1.  Implement angular framework
2.  Create landing page
3.  Research pwa basics
4.  Research camera access
5.  Implement file system access

### Contributions:

1.  Ajay Patnaik: research and planning, presentation and readme 9 hours
2.  Bekah Greczanik: implemented angular framework and created landing page, readme, research 10 hours
3.  Carl Schultz: implemented angular framework and created landing page, research, 10 hours
4.  Alex Zoumaya: research, implement file system access, 9 hours

### Sprint Retrospective

The focus of this sprint was on researching progressive application and what they can do. Synchrony Financial left this application up to us to figure out what we want to do. This sprint was spent better solidifying our application and starting development. This sprint, we could have better spent our time with development and meeting as a group. We could have also better kept in contact with the sponsor.

## Sprint 2

Duration: 2/13/2020-3/04/2020

### Completed Tasks:

1.  Deployed app to bitbucket site for testing
2.  Implemented displaying photo after user upload
3.  Implemented gaining access to camera and camera roll on mobile
4.  Started implementation of optical character recognition from and image
5.  Started implementing progress bar for OCR

### Contributions:

1.  Ajay Patnaik: added tesseract into app, implemented getting image from text, deployed the app to bitbucket site, researched progress bar and online service workers for pwa 10 hours
2.  Bekah Greczanik: added tesseract into app, implemented getting image from test, fixed node problem, researched progress bar/how to get tesseract progress, brainstorming/planning for sprint 3 10 hours
3.  Carl Schultz: added functionality to preview photo after upload, worked on stylizing the choose file button 10 hours
4.  Alex Zoumaya: brain-storming, researched more of the tesseract documentation to upgrade capabilities, aided in debugging 10 hours

### Sprint Retrospective

The focus of this sprint was getting the app working on mobile, implementing retrieving a photo and also adding in tesseract. We did a good job meeting up and working together this sprint and developed the overall idea for our app a little better. We saw great improvement as a team this sprint.

## Sprint 3

Duration: 03/04/2020-4/23/2020

### Completed Tasks:

1.  Update landing page UI
2.  Implemented progress bar
3.  Implemented copying text to the clipboard
4.  Fixing past README
5.  Implementing service workers
6.  Created icon for installable
7.  Made text result editable
8.  Made it installable

### Contributions:

1.  Ajay Patnaik: updated landing page UI, readme, deployed site, icon brainstorming
2.  Bekah Greczanik: implemented progress bar, copy to clipboard, readme, created icon, and implemented service workers for installable 20 hours 
3.  Carl Schultz:
4.  Alex Zoumaya:

### Sprint Retrospective

The focus of this sprint was on finalizing the user interface and finishing the quality-of-life features. Another important part was implementing the service workers to make our application an actual progressive web app. We did a good job talking through bugs and issues we were having this sprint.

# User guide

To use our application first go to https://cps491s20-team1.bitbucket.io/ on a mobile device. From there click "Snap a Photo" and then click "Choose File". This will give you the option to select an image from your camera roll or take a photo. Once you have uploaded an image, the image is displayed on the page and the optical character recognition begins working. The progress will be shown on the progress bar below the result title. Once completed, the text from the image is displayed below the image. The text result can be edited if needed and the save button must be clicked to save the edits. Then the text can be copied to the clipboard by clicking copy below the result. This text can be pasted anywhere using ctrl + v or by right clicking and clicking paste.
