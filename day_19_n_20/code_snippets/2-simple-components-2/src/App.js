import React from 'react';
import Header from "./components/Header"
import StudentInfoArvind from "./components/StudentInfoArvind";
import StudentInfo from "./components/StudentInfo";
import "./css/App.css";

function App() {

  // let data = []
  var data = [
    {'name': 'Bradley', 'college': 'MCC', 'dob': '2-2-1997'},
    {'name': 'Arijith', 'college': 'SSN', 'dob': '3-3-1998'},
    {'name': 'Sakura', 'college': 'Ninja Academy', 'dob': '4-7-1999'},
  ]

  return (
    <div id="main-app-wrapper">
      <Header/>
      <StudentInfoArvind/>
      {
        data.map((studentInfoDict) => {
          return <StudentInfo college={studentInfoDict.college} name={studentInfoDict.name} dob={studentInfoDict.dob}/>
        })
      }
    </div>
  );

  

}

export default App;
