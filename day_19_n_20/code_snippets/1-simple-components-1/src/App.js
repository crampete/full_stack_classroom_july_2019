import React from 'react';
import Header from "./components/Header"
import StudentInfoArvind from "./components/StudentInfoArvind";
import StudentInfo from "./components/StudentInfo";
import "./App.css";

function App() {
  return (
    <div id="main-app-wrapper">
      <Header/>
      <StudentInfoArvind/>
      <StudentInfo name="Bradley" college="MCC" dob="2-2-1997"/>
      <StudentInfo name="Arijith" college="SSN" dob="3-3-1998"/>
      <StudentInfo name="Sasuke" college="Ninja Academy" dob="4-7-1998"/>
      <StudentInfo name="Sakura" college="Ninja Academy" dob="4-7-1999"/>
    </div>
  );

  

}

export default App;
