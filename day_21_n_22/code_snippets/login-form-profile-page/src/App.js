import React from 'react';
import logo from './logo.svg';
import {Switch, Route, BrowserRouter} from "react-router-dom";
import LoginPage from "./pages/Login"
import ProfilePage from "./pages/Profile"
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container'
import "./style.css"



function App() {
  return (
    <BrowserRouter>
    <Switch>
    <Container> {/*Bootstrap container */}
      {/* <div className="container"> can also be done */}
      <Route path="/login" component={LoginPage}/>
      <Route path="/profile" component={ProfilePage}/>
    </Container>
    </Switch>
    </BrowserRouter>
  );
}

export default App;
