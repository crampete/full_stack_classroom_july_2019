import React from "react"
import NarutoPic from "../img/naruto.png"

class ProfilePage extends React.Component {
    render() {
        return(
            <div className="pt-3 pb-3 pl-3 pr-3">
                <h1 className="h2 text-center text-lowercase">profile</h1>
                <div id="profile" className="mt-5">
                <div className="mycard mr-auto ml-auto">
                    <img src={NarutoPic} />
                    <h2 className="h3 text-lowercase text-center mt-3">Naruto Uzumaki</h2>
                    <p className="lead text-center mt-3">Hokage, Sage of Six Paths</p>
                </div>
                </div>
            </div>
        )
    }
}


export default ProfilePage;