import React from 'react'
import './App.css';
import PersonList from './components/PersonList.js';
import PersonAdd from './components/PersonAdd';
import PersonRemove from './components/PersonRemove';
import PersonFilter from './components/PersonFilter';

function App() {
  return (
    <div ClassName="App">
      <PersonAdd/>
      <PersonFilter/>
      <h2>Top Reviews</h2>
      <PersonList/>
      <PersonRemove/>
    </div>
  )
}


export default App;
