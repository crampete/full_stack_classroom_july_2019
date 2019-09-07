import React from 'react';

class MagicText extends React.Component {
    state = {
        heading: 'Heading from state'
    }



    render() {
        return (
            <div>
                <p>{this.props.heading}</p>
                <p>{this.state.heading}</p>
            </div>
        )
    }
}


export default MagicText;