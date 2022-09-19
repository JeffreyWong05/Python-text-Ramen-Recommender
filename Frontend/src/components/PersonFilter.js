import React from 'react';
import axios from 'axios';

export default class PersonFilter extends React.Component {
  state = {
    name: '',
    brands:[]
  }

  handleChange = event => {
    this.setState({ name: event.target.value });
  }

  handleSubmit = async (event) => {
    event.preventDefault();

    const user = {
      name: this.state.name
    };

    console.log(user);

    const brand = user["name"];

    await axios.get(`http://127.0.0.1:5000/get/setlist/` + brand)
      .then(res => {
        console.log(res);
        console.log(res.data);

        const brands = res.data;
        
        this.setState({brands: brands})
      })
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>
            Brand Name:
            <input type="text" name="name" onChange={this.handleChange} />
          </label>
          <button type="submit">Find based on brand</button>
          <p>Your search results will appear just below:</p>
        </form>

        <ol>
        {
          this.state.brands
            .map(brand =>
              <li>
                <ul> 
                  <li>Result</li>
                  <li> Brand: {brand.Brand} </li> 
                  <li>Variety: {brand.Variety}</li> 
                  <li>Style: {brand.Style}</li> 
                  <li>Country: {brand.Country}</li> 
                  <li>Stars: {brand.Stars}</li> 
                </ul>
              </li>
            )
        }
      </ol>
      </div>
    )
  }
}