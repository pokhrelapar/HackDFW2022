import React, { Component} from 'react'
import jakeStateFarm from './images/jake.png';
import './Home.css'


class Home extends Component {
  render() {
    return (
      <div class="grid-container">

        <div class="grid-child-1">
            <h1>
                       Hi! <br />
                  <strong> I am  Jake <br/> </strong>
                  <strong > <strong className ='from'>from </strong><br/>
                        State Farm. </strong>
            </h1>

            <h2>
                Welcome to Ten Years with Jake! This game simulates a State Farm home insurance plan over a 10 year period.
                Pick a place to live, an insurance plan, and you're off!
            </h2>
        </div>

        <div class="grid-child-2">
             <div className= 'jake-img'>
                <img src = {jakeStateFarm} alt =''/>
             </div>
        </div>

      </div>


    );
  }
}
export default Home;