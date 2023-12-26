import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import axios from 'axios';

import CodeGeneration from './components/CodeGeneration';
import DebuggingAssistant from './components/DebuggingAssistant';
import CodeExplanation from './components/CodeExplanation';
import DocumentationGenerator from './components/DocumentationGenerator';
import LearningSupport from './components/LearningSupport';
import CodeOptimizer from './components/CodeOptimizer';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      apiResponse: "",
    };
  }

  callAPI() {
    axios.get("http://localhost:9000/testAPI")
      .then(res => this.setState({ apiResponse: res.data }))
      .catch(err => console.log(err));
  }

  componentDidMount() {
    this.callAPI();
  }

  render() {
    return (
      <Router>
        <div className="App">
          <Switch>
            <Route path="/code-generation" component={CodeGeneration} />
            <Route path="/debugging-assistant" component={DebuggingAssistant} />
            <Route path="/code-explanation" component={CodeExplanation} />
            <Route path="/documentation-generator" component={DocumentationGenerator} />
            <Route path="/learning-support" component={LearningSupport} />
            <Route path="/code-optimizer" component={CodeOptimizer} />
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;
