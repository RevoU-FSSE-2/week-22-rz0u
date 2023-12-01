# Milestone 5 (Week 22)

### This App is designed to manage and track Todos, providing a digital solution for various industries that struggle with task management. Below, you will find short details about the available function.

## [API Documentation](https://documenter.getpostman.com/view/29347896/2s9YeK2peD) |  [Deployed API // BELUM](https://us-central1-revou-fullstack-2.cloudfunctions.net/milestone_3_rzou)
### Features
### User Registration

- **Endpoint:** `/api/users/register`
- **Method:** POST
- **Description:** Register a new user.

### User Login

- **Endpoint:** `/api/users/login`
- **Method:** POST
- **Description:** Authenticate and log in as a registered user.

### Get All Todos

- **Endpoint:** `/api/todos`
- **Method:** GET
- **Description:** Retrieve all Todos.

### Create new Todo

- **Endpoint:** `/api/todos`
- **Method:** POST
- **Description:** Create new Todo. (Only Manager have access)

### Update Todo

- **Endpoint:** `/api/todos/:id`
- **Method:** PUT
- **Description:** Update Todo progression.

### Delete Todo

- **Endpoint:** `/api/todos/:id`
- **Method:** Delete
- **Description:** Delete Todo. (Only the Assignor that can delete its own Todos)

## Deployment (With Firebase)

1. Create a Firebase project on the Firebase Console (https://console.firebase.google.com/).

2. Install the Firebase CLI tools if you haven't already: `npm install -g firebase-tools`.

3. Authenticate with Firebase using `firebase login`.

4. Initialize Firebase in your project directory using `firebase init`. Select the options for Hosting, and choose your Firebase project.

5. Build your React app for production using `npm run build`.

6. Deploy your app to Firebase Hosting using `firebase deploy`.

7. Your Todo List app is now deployed and accessible via a Firebase Hosting URL.
   
## [Deployed Fullstack App](https://milestone-3-rzou.web.app/register)
