import React from 'react';
import './css/App.css';
import MagicText from './components/MagicText';

function App() {
  return (
    <div>
      <MagicText heading="1st child Heading from parent"/>
      <MagicText heading="2nd child"/>
      <MagicText heading="3rd child"/>
    </div>
  );
}

export default App;
