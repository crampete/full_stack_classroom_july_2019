import React from 'react';
import PikachuImage from "../img/pikachu.jpg";
import BulbasaurImage from "../img/bulbasaur.jpg";
import SquirtleImage from "../img/squirtle.jpg";
import CharmanderImage from "../img/charmander.jpg";

class IChooseYou extends React.Component {
    state = {
        'chosenPokemon': 'Pikachu',
    }


    // These 3 functions can be re-written as one function
    choosePikachu = () => {
        this.setState({chosenPokemon: 'Pikachu'})
    }
    chooseBulba = () => {
        this.setState({chosenPokemon: 'Bulbasaur'})
    }
    chooseCharmander = () => {
        this.setState({chosenPokemon: 'Charmander'})
    }
    chooseSquirtle = () => {
        this.setState({chosenPokemon: 'Squirtle'})
    }

    render() {
        return (
            <div>
            {/* There are better ways to choose images rather than using four logic blocks */}
            {this.state.chosenPokemon.toLowerCase() === 'pikachu' && <img src={PikachuImage} className="pokemon-image"/>}
            {this.state.chosenPokemon.toLowerCase() === 'bulbasaur' && <img src={BulbasaurImage} className="pokemon-image"/>}
            {this.state.chosenPokemon.toLowerCase() === 'charmander' && <img src={CharmanderImage} className="pokemon-image"/>}
            {this.state.chosenPokemon.toLowerCase() === 'squirtle' && <img src={SquirtleImage} className="pokemon-image"/>}
                
                <h2>You chose {this.state.chosenPokemon}</h2>
                <div>
                    <button onClick={this.choosePikachu}>Pikachu</button>
                    <button onClick={this.chooseBulba}>Bulbasaur</button>
                    <button onClick={this.chooseCharmander}>Charmander</button>
                    <button onClick={this.chooseSquirtle}>Squirtle</button>
                </div>
            </div>
        )
    }
}

export default IChooseYou;