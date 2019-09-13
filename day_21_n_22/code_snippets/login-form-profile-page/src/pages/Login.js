import React from "react"
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'



class LoginPage extends React.Component {

    state = {
        'username': '',
        'password': ''
    }

    submitForm = () => {
        if (this.state.username === 'james' && this.state.password === 'bond') {
            this.props.history.push('/profile');
        } else {
            alert("Wrong username and password.")
        }
    }

    handleInputChange = (e) => {
        let name = e.target.name;
        let value = e.target.value;
        this.setState({[name]: value})
    }

    resetFields = () => {
        this.setState({username: '', password: ''})
    }

    render() {
        return(
            <div id="login-box">
                <div id="login-inner" className="mx-auto pt-3 pb-3 pl-3 pr-3">

                <h1 className="h2 text-center text-lowercase">Login</h1>
                {/* It's advisable to use a <form> for such things</form> */}
                {/* You can also use Bootstrap Form components */}
                <div className="form-group">
                    <label>Username</label>
                    <input value={this.state.username} name="username" onChange={this.handleInputChange} className="form-control"/>
                </div>


                {/* We can use Bootstrap classes directly as well */}
                <div className="form-group">
                    <label>Password</label>
                    <input value={this.state.password} name="password" onChange={this.handleInputChange} type="password" className="form-control"/>
                </div>

                {/* using plain HTML buttons and bootstrap components */}
                <div className="form-group text-center">
                    <button onClick={this.resetFields} className="btn mr-3" style={{
                        backgroundColor: "#de8b8b"
                    }}>Reset</button>
                    <button className="btn"
                    onClick={this.submitForm} style={{
                        backgroundColor: '#a4a4e6'
                    }}>Submit</button>
                </div>
                </div>

            </div>
        )
    }
}


export default LoginPage;