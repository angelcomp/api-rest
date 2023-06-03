import logo from './logo.svg';
import './App.css';
import Cronometro from './components/cronometro';
import Node from './components/Node';
import Py from './components/Py';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Cronometro/>
        <div className="component">
          <Node/>
          <Py/>
        </div>
      </header>
    </div>
  );
}

export default App;
