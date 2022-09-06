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
        console.log("help");
        const persons = res.data;
        console.log("help");
        this.setState({persons: persons})
        console.log(persons);
      })
  }

  render() {
    
    return (
      <ul>
        {
          this.state.persons
            .map(person =>
              <li> {person.Brand} </li>
            )
        }
      </ul>
    )
  }
}