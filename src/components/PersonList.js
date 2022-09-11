import React from 'react';
import axios from 'axios';

export default class PersonList extends React.Component {
  state = {
    persons: []
  }

  async componentDidMount() {
    await axios.get(`http://127.0.0.1:5000/get/listoften/`,{headers: {
      "Content-type": 'application/json',
    }})
      .then(res => {
        
        const persons = res.data;
        
        this.setState({persons: persons})
        //console.log(persons);
      })
  }

  render() {
    
    return (
      <ol>
        {
          this.state.persons
            .map(person =>
              <li>
                <ul> 
                  <li>Review</li>
                  <li> Brand: {person.Brand} </li> 
                  <li>Variety: {person.Variety}</li> 
                  <li>Style: {person.Style}</li> 
                  <li>Country: {person.Country}</li> 
                  <li>Stars: {person.Stars}</li> 
                </ul>
              </li>
            )
        }
      </ol>
    )
  }
}