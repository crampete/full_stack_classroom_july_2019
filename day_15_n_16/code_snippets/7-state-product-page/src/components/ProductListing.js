import React from 'react';


class ProductListing extends React.Component {
    state = {
        "qty": 1        
    }

    increaseQty = () => {
        // var can also be used
        let newQty = this.state.qty + 1;
        this.setState({
        "qty": newQty 
        })
    }

    decreaseQty = () => {
        if (this.state.qty > 0) {
            let newQty = this.state.qty - 1;
            this.setState({
                "qty": newQty
            })
        }
    }
    render() {
       return (  
           <div>
           <h2>{this.props.title}</h2>
           <p>Rate:- {this.props.price}</p>
           <p>Qty:- {this.state.qty}</p>
           <p>Total:- {this.props.price * this.state.qty}</p>
           <button onClick={this.decreaseQty}>-</button>
           <button onClick={this.increaseQty}>+</button>
           </div>
        );
    }
}


export default ProductListing;