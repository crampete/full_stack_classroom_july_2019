import React from 'react';


class StudentInfo extends React.Component {
    render() {
       return (  
        <div className="student-info">
            <p className="student-field">Name</p>
            <p>{this.props.name}</p>
            <p className="student-field">College</p>
            <p>{this.props.college}</p>
            <p className="student-field">Date of Birth</p>
            <p>{this.props.dob}</p>
        </div>
        );
    }
}


export default StudentInfo;