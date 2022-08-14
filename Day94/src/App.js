import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
import Example from './Example';
let value_n = 0;


function App()
{
  return (
    <div className="App">
      <header className="App-header">
        <h1>Counter App</h1>
      </header>

      <Example></Example>
    </div>
  );
}

export default App;
