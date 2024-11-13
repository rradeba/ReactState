Module 11 Lesson 2: Assignments | React State and Props
Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!

Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!

1. Exploring State and Props in Class Components
Objective: The aim of this assignment is to strengthen your understanding of state and props management in React class components. You'll also practice conditional rendering and displaying lists, crucial aspects of dynamic React applications.

Problem Statement: You are working on a React project that involves a user profile component. The component is supposed to display user information, a list of hobbies, and allow toggling between 'Edit' and 'View' modes. However, the current implementation has several bugs and lacks some functionalities. Your task is to correct the code, implement missing features, and ensure the component works as expected.

Task 1: Code Correction

The current implementation of the user profile component has a bug in state management. Analyze and correct the code to ensure the user's name is displayed correctly.
Code Example:

class UserProfile extends Component {
    constructor(props) {
        super(props);
        this.state = { name: 'Alex' };
    }

    // Incorrect function
    changeName() {
        this.state.name = 'Charlie';
    }

    render() {
        return (
            <div>
                <h1>User Profile</h1>
                <p>Name: {this.state.name}</p>
                <button onClick={this.changeName}>Change Name</button>
            </div>
        );
    }
}
Expected Outcome:

The changeName method should correctly update the state using this.setState.
Ensure the method is properly bound to the component.

2. Enhancing Functional Components with React Hooks
Objective: This assignment aims to deepen your skills in using React Hooks for state management, props handling, conditional rendering, and list operations in functional components. You'll be building a dynamic component that responds to user interactions.

Problem Statement: You are tasked with developing an interactive 'Favorite Movies' list component in React. This component should allow users to add movies to a list, remove them, and toggle between different views. The list of movies will be hardcoded for simplicity. Your challenge is to implement this functionality using functional components and React Hooks.

Task 1: Initializing and Displaying a List

Start by creating a MoviesList functional component.
Initialize a state with a hardcoded list of movie titles using the useState hook.
Expected Outcome:

The component should render an unordered list (<ul>) of movie titles.


Task 2: Conditional Rendering of Movie Details

For each movie, implement a feature that toggles additional details (like a brief description) when the movie title is clicked.
Use conditional rendering to show or hide these details.
Expected Outcome:

Clicking on a movie title toggles the display of its details.
Each movie should maintain its own toggle state.


Task 3: Implementing Movie Removal

Add a 'Remove' button next to each movie title.
Implement a function to remove a movie from the list when this button is clicked.
Expected Outcome:

Clicking the 'Remove' button should instantly remove the movie from the list.


Task 4: Toggling List View

Implement a button outside the list to toggle between showing all movies and only showing a specific genre (e.g., 'Action').
Use conditional rendering and state management to control the list's display based on this toggle.
Expected Outcome:

The toggle button should switch the view between all movies and movies of a specified genre.
The state should correctly reflect the current view.


Code Structure Guidance:

// src/components/MoviesList.jsx

import React, { useState } from 'react';

const MoviesList = () => {
    // Initialize state with a list of movies
    // Implement required functionalities here

    return (
        <div>
            {/* Toggle view button */}
            <ul>
                {/* Map through the movies and display them */}
            </ul>
        </div>
    );
};
export default MoviesList;
NOTE: Ensure that all code in your file is ready to run. This means that when your code is cloned down, we should be able to install the dependencies and run the react app. Your components should be implemented and all code should run as expected and asked for in the assignment.

The goal of this note is to ensure that all code in your React project runs smoothly and that is has been tested.

