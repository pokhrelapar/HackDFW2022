import './App.css';
import { state, setState, useState } from 'react';
import Card from './components/Card';
import ExpandedCard from './components/ExpandedCard';
import useLocationStore from './store/locationStore';
import useScenarioStore from './store/scenarioStore';
import usePlanStore from './store/planStore';


function App() {
  const locations = useLocationStore(state => state.locations);
  const scenarios = useScenarioStore(state => state.scenarios);
  const plans = usePlanStore(state => state.plans);
  const [selected, setSelected] = useState();
  const [stage, setStage] = useState("location");
  const [year, setYear] = useState(0);

  const handleSelect = e => {
    setSelected(e.currentTarget.id);
  }
  const handleStage = e => {
    if (stage === "location") {
      setStage("plan");
    } else if (stage === "plan") {
      setStage("outcome");
    } else if (year !== 9) {
      setStage("outcome");
      setYear(year + 1);
    }
    else {
      setStage("end");
    }
  }

  if (stage === "location") {
    return (
      <div className="App">
        <header className="App-header">
          <div class="container">
            <div class="row row-cols-4 row-cols-md-4 gx-5 d-flex align-items-stretch mb-3">
              {locations.map(item => (
                <div class="col" onClick={(e) => handleSelect(e)} id={item.id}>
                  <Card name={item.name} id={item.id} desc={item.desc} ></Card>
                </div>
              ))}
            </div>
            <button type="button" class="btn btn-primary" onClick={() => handleStage()}>Next</button>
          </div>
        </header >
      </div >
    );
  }
  else if (stage === "plan") {
    return (
      <div className="App">
        <header className="App-header">
          <div class="container">
            <div class="row row-cols-4 row-cols-md-4 gx-5 d-flex align-items-stretch mb-3">
              {plans.map(item => (
                <div class="col" onClick={(e) => handleSelect(e)} id={item.id}>
                  <Card name={item.header} id={item.id} desc={item.desc} ></Card>
                </div>
              ))}
            </div>
            <button type="button" class="btn btn-primary" onClick={() => handleStage()}>Next</button>
          </div>
        </header >
      </div >
    );
  }
  else if (stage === "outcome") {
    return (
      <div className="App">
        <header className="App-header">
          <div class="container mb-3">
            <ExpandedCard header={scenarios[0].header} desc={scenarios[0].desc}></ExpandedCard>
          </div>
            <button type="button" class="btn btn-primary" onClick={() => handleStage()}>Next</button>
        </header>
      </div>
    )
  }
  else if (stage === "end") {
    return (
      <div className="App">
        <header className="App-header">
          <div class="container mb-3">
            <ExpandedCard header={scenarios[0].header} desc={scenarios[0].desc}></ExpandedCard>
          </div>
            <button type="button" class="btn btn-primary" onClick={() => handleStage()}>Next</button>
        </header>
      </div>
    )
  }
}

export default App;
