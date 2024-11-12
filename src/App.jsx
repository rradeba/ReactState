

import React from 'react';
import MoviesList from './components/MoviesList';
import UserProfile from './components/UserProfile';

const App = () => {
    return (
        <div style={{ padding: '20px' }}>
            <h1>My React App</h1>
            
            <section style={{ marginBottom: '40px' }}>
                <UserProfile />
            </section>

            <section>
                <MoviesList />
            </section>
        </div>
    );
};

export default App;
