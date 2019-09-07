import React from 'react';

class TextChanger extends React.Component {
    state = {
        'currentText': 'Smart switcher option 1',
        'o1': 'Smart switcher option 1',
        'o2': 'This is option 2'
    }
    switchText = () => {

        if (this.state.currentText === this.state.o1) {
            this.setState({currentText: this.state.o2})
        } else {
            this.setState({currentText: this.state.o1})
        }

    }

    render() {
        return (
            <div>
                <p>{this.state.currentText}</p>
                <button onClick={this.switchText}>Switch Text</button>
            </div>
        )
    }
}

export default TextChanger;