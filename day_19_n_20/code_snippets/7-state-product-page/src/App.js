import React from 'react';
import logo from './logo.svg';
import './App.css';
import ProductListing from "./components/ProductListing"

function App() {
  return (
    <div className="App">
      <ProductListing name="Parachute Oil" price={10}/>
      <ProductListing name="Head n Shoulders Shampoo" price={20}/>
    </div>
  );
}

export default App;
